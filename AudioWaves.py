#! /bin/python

'''
This script will provide a bridge from .wav files to animations, as tested with the Jupyter notebook.
It accepts user input
'''

import argparse

parser = argparse.ArgumentParser(description='Generate dynamical visualizations of audio waves and their spectrums')

parser.add_argument('audio') # compulsory argument, the .wav file
parser.add_argument('-m', '--mode', choices=['audio','spectrum'], default='audio') # choose between audio and spectrum 
parser.add_argument('-s', '--static', action='store_true', default=False) # generate gifs unless the option is provided


args = parser.parse_args()

print(args)

exit()

import wave
import numpy as np
import matplotlib.pyplot as plt

