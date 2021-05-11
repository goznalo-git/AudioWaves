import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rc
import spectrum

rc('animation', html='html5')

def plot_spectrum(sound_info, per, lw, P, lag):
    '''Function plotting the spectrum of the whole audio clip'''
    freq = spectrum.speriodogram(sound_info)
    if per == 'log':
        freq = 10*np.log10(freq)
    elif per == 'sqrt':
        freq = np.sqrt(freq)
    elif per == 'Welch':
        freq = spectrum.WelchPeriodogram(sound_info) 
        plt.close()
        freq = 10*np.log10(freq[0][0])
    elif per == 'Daniell':
        freq = spectrum.DaniellPeriodogram(sound_info, P = P)[0]
    elif per == 'Corr':
        freq = spectrum.CORRELOGRAMPSD(sound_info, lag = lag) 
    
    plt.plot(freq, lw = lw)


def gif_audio(sound_info, onesec_info, length, mod, lw):
    '''Function returning the animation of the sound wave'''
    fig, ax = plt.subplots()
    ylim = max(abs(sound_info)) * 1.1

    def animate(i):
        ax.cla()
        ax.set_ylim(-ylim,ylim)
        ax.set_axis_off()

        current = (int(i * onesec_info/ mod),int((i + 1) * onesec_info / mod))
        ax.plot(sound_info[current[0]:current[1]],lw = lw)
        
    frames = int(length) * mod
    ani = FuncAnimation(fig, animate, frames=frames, interval = 1000/mod, repeat=False)
    return ani

def gif_spectrum(sound_info, per, onesec_info, length, mod, lw):
    '''Function returning the animation of the sound wave's spectrum'''
    fig, ax = plt.subplots()
    ylim = 1e+40
    
    def animate(i):
        ax.cla()
        #ax.set_xlim()
        ax.set_axis_off()

        current = (int(i * onesec_info/ mod),int((i + 1) * onesec_info / mod))
        
        freq = spectrum.speriodogram(sound_info[current[0]:current[1]])
        ax.set_ylim(-1e+39,ylim)
        ax.plot(freq, lw = lw)
    
    frames = int(length) * mod
    ani = FuncAnimation(fig, animate, frames=frames, interval = 1000/mod, repeat=False)
    return ani