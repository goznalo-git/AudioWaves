#! /bin/python

'''
This script will provide a bridge from .wav files to animations, as tested with the Jupyter notebook.
It accepts user input: 
- Audio: required input file
- Mode (audio or spectrum graphs)
- Staticity (full wave static image or gif)
'''

import argparse

parser = argparse.ArgumentParser(description='Generate static or dynamical visualizations of audio waves and their spectrums')

parser.add_argument('file')
parser.add_argument('-s', '--static', action='store_true', default=False, help='Use this option to generate a png image of the full audio clip rather than a gif.') 
parser.add_argument('-c', '--chunk', default=10, type=int, help='Use this option to specify the length of each cut used for the animation.') 
parser.add_argument('-l', '--linewidth', default=0.3, type=float, help = 'Line width parameter for the plot.') 

subparsers = parser.add_subparsers(dest='mode', help='Available sub-commands')

subparser_a = subparsers.add_parser('audio', help='audio sub-command help')
subparser_s = subparsers.add_parser('spectrum', help='spectrum sub-command help')
#subparser.add_argument('-m', '--mode', choices=['audio','spectrum'], default='audio') # choose between audio and spectrum 

subparser_s.add_argument('-p', '--periodogram', choices=['simple','log','sqrt','Welch','Daniell','Corr'], default='simple', help="Choice of spectrum type")
subparser_s.add_argument('-L','--lag', default=100, type=int, help="Parameter for the Welch periodogram")
subparser_s.add_argument('-P','--points', default=8, type=int, help="Parameter for the Daniell periodogram")

args = vars(parser.parse_args())

inputfile = args['file']
mode = args['mode']
static = args['static']
mod = args['chunk']
lw = args['linewidth']
per = args['periodogram']
lag = args['lag']
P = args['points']

if static and mod != 10:
    print('Note: the "-c" or "--chunk" argument is only relevant in dynamic (gif) plots.')
elif per != 'Welch' and lag != 100: 
    print('Note: the "-L" or "--lag" argument is only relevant in the Welch periodogram.')
elif per != 'Daniell' and P != 8:
    print('Note: the "-P" or "--points" argument is only relevant in the Daniell periodogram.')

#TO-DO: remove defaults from add_argument, place them in function inputs and check if blank arguments don't override defaults.

import wave
import numpy as np
from plotfuncs import *

'''Open the audio file and retrieve its properties'''
with wave.open(inputfile,'r') as spf: 
    sound_info = np.frombuffer(spf.readframes(-1), int)
    
    nframes = spf.getnframes() # number of frames
    frate = spf.getframerate() # frames per second

# get the length of the clip, and the amount of info in a second.
length = nframes/float(frate)
onesec_info = round(len(sound_info)/length)


'''Now comes the actual plotting'''
if static:
    plt.axis('off')
    if mode == 'audio':
        plt.plot(sound_info, lw = lw)
    else:
        plot_spectrum(sound_info, per, lw, P, lag)
    
    plt.savefig('testplot.png')
    
else:    
    if mode == 'audio':
        ani = gif_audio(sound_info, onesec_info, length, mod, lw)
    else:
        ani = gif_spectrum(sound_info, per, onesec_info, length, mod, lw)
        
    ani.save('testgif.gif', writer='imagemagick')
    
