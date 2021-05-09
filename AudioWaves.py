#! /bin/python

'''
This script will provide a bridge from .wav files to animations, as tested with the Jupyter notebook.
It accepts user input: 
- Audio: required input file
- Mode (audio or spectrum graphs)
- Staticity (full wave static image or gif)
'''

import argparse

parser = argparse.ArgumentParser(description='Generate dynamical visualizations of audio waves and their spectrums')

parser.add_argument('audio') # compulsory argument, the .wav file
parser.add_argument('-m', '--mode', choices=['audio','spectrum'], default='audio') # choose between audio and spectrum 
parser.add_argument('-s', '--static', action='store_true', default=False) # generate gifs unless the option is provided
parser.add_argument('-c', '--chunk', default=10) #specify the divisions of a second in which the audio will be split.
parser.add_argument('-l', '--linewidth', default=0.3) #specify the plot's linewidth.

args = vars(parser.parse_args())

audio = args['audio']
mode = args['mode']
static = args['static']
mod = int(args['chunk'])
lw = args['linewidth']

#print(args)

import wave
import numpy as np
from plotfuncs import *

'''Open the audio file and retrieve its properties'''
with wave.open(audio,'r') as spf: 
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
        plot_spectrum(sound_info, lw)
    
    plt.savefig('testplot.png')
    
else:    
    if mode == 'audio':
        ani = gif_audio(sound_info, onesec_info, length, mod, lw)
    else:
        ani = gif_spectrum(sound_info, onesec_info, length, mod, lw)
        
    ani.save('testgif.gif', writer='imagemagick')
    
