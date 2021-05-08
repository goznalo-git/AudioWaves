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


args = vars(parser.parse_args())

audio = args['audio']
mode = args['mode']
static = args['static']

#print(args)

import wave
import numpy as np
import matplotlib.pyplot as plt


'''Open the audio file and retrieve its properties'''
with wave.open(audio,'r') as spf: 
    sound_info = np.frombuffer(spf.readframes(-1), int)
    
    nframes = spf.getnframes() # number of frames
    frate = spf.getframerate() # frames per second

    
length = nframes/float(frate)
onesec_info = round(len(sound_info)/length)

if static:
    plt.axis('off')
    if mode == 'audio':
        plt.plot(sound_info, lw = 0.5)
    else:
        import spectrum
        freq = spectrum.speriodogram(sound_info)
        plt.plot(freq, lw = 0.5)
    
    plt.savefig('testplot.png')
    
else:
    from matplotlib.animation import FuncAnimation
    from matplotlib import rc
    
    exit()
    if mode == 'audio':
        plt.plot(sound_info)
    else:
        import spectrum
        freq = spectrum.speriodogram(sound_info)
        plt.plot(freq, lw = 0.5)
    
