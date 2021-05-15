#! /bin/python

'''
This script will provide a bridge from .wav files to animations, as tested with the Jupyter notebook.
It accepts user input: 
- Audio: required input file
- Mode (audio or spectrum graphs)
- Staticity (full wave static image or gif)
'''

from input_args import initiation

args = initiation()

#print(args)

inputfile = args['file']
mode = args['mode']
static = args['static']
mod = args['chunk']
lw = args['linewidth']
if mode == 'spectrum':
    per = args['periodogram']
    lag = args['lag']
    P = args['points']

if static and mod != 10:
    print('Note: the "-c" or "--chunk" argument is only relevant in dynamic (gif) plots.')
if mode == 'spectrum':
    if per != 'Welch' and lag != 100: 
        print('Note: the "-L" or "--lag" argument is only relevant in the Welch periodogram.')
    if per != 'Daniell' and P != 8:
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

#sound_info = sound_info[:int(round(length/2))]

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
        ani = gif_spectrum(sound_info, per, onesec_info, length, mod, lw, P, lag)
        
    ani.save('testgif.gif', writer='imagemagick')
    
