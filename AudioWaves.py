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

def gif_sound(sound_info, onesec_info):
    '''Function returning the animation of the sound wave'''
    fig, ax = plt.subplots()
    ylim = max(abs(sound_info)) * 1.1

    mod = 10 # from 1 to length

    def animate(i):
        ax.cla()
        ax.set_ylim(-ylim,ylim)
        ax.set_axis_off()

        current = (int(i * onesec_info/ mod),int((i + 1) * onesec_info / mod))
        ax.plot(sound_info[current[0]:current[1]],lw=0.2)
        
    frames = int(length) * mod
    ani = FuncAnimation(fig, animate, frames=frames, interval = 1000/mod, repeat=False)
    return ani

'''Now comes the actual plotting'''
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
    
    rc('animation', html='html5')
    
    if mode == 'audio':
        ani = gif_sound(sound_info, onesec_info)
        ani.save('testgif.gif', writer='imagemagick')
    else:
        import spectrum
        freq = spectrum.speriodogram(sound_info)
        plt.plot(freq, lw = 0.5)
    
