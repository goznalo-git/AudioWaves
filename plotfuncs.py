import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rc
    
rc('animation', html='html5')

def gif_audio(sound_info, onesec_info, length, mod):
    '''Function returning the animation of the sound wave'''
    fig, ax = plt.subplots()
    ylim = max(abs(sound_info)) * 1.1

    def animate(i):
        ax.cla()
        ax.set_ylim(-ylim,ylim)
        ax.set_axis_off()

        current = (int(i * onesec_info/ mod),int((i + 1) * onesec_info / mod))
        ax.plot(sound_info[current[0]:current[1]],lw=0.2)
        
    frames = int(length) * mod
    ani = FuncAnimation(fig, animate, frames=frames, interval = 1000/mod, repeat=False)
    return ani

def gif_spectrum(sound_info, onesec_info, length, mod):
    '''Function returning the animation of the sound wave'''
    fig, ax = plt.subplots()
    ylim = max(abs(sound_info)) * 1.1

    def animate(i):
        ax.cla()
        ax.set_ylim(-ylim,ylim)
        ax.set_axis_off()

        current = (int(i * onesec_info/ mod),int((i + 1) * onesec_info / mod))
        ax.plot(sound_info[current[0]:current[1]],lw=0.2)
        
    frames = int(length) * mod
    ani = FuncAnimation(fig, animate, frames=frames, interval = 1000/mod, repeat=False)
    return ani