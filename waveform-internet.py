#!/usr/bin/env python

'''
https://web.archive.org/web/20161203074728/http://jaganadhg.freeflux.net:80/blog/archive/2009/09/09/plotting-wave-form-and-spectrogram-the-pure-python-way.html
'''
import sys
from pylab import *
import wave

def show_wave_n_spec(speech):
    spf = wave.open(speech,'r')
    sound_info = spf.readframes(-1)
    sound_info = frombuffer(sound_info, int)

    f = spf.getframerate()
   
    subplot(211)
    plot(sound_info)
    title('Wave from and spectrogram of %s' % sys.argv[1])

    subplot(212)
    spectrogram = specgram(sound_info, Fs = f, scale_by_freq=True,sides='default')
   
    show()
    spf.close()

fil = sys.argv[1]

show_wave_n_spec(fil)
