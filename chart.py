import time
import paramiko
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib import style
import warnings
warnings.filterwarnings(action='ignore')

style.use('dark_background')
font = {'family': 'monospace',
        'color':  'limegreen',
        'weight': 'bold',
        'size': 8,
        }
fig = plt.figure(figsize=(8,5))
plt.rc('grid', linestyle='dotted', color='limegreen', linewidth = 1)
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['xtick.color']  = 'limegreen'
plt.rcParams['ytick.color'] = 'limegreen'

ax1 = fig.add_subplot(1,1,1)

centre_freq = 3e3
freq_span = 3.5e3
frame_size = 512
frame_interval = 100
lower_freq_limit = centre_freq - (freq_span/2)
upper_freq_limit = centre_freq + (freq_span/2)

# Generate some test data in array d
a = np.zeros(253)
c = list(a)
b = np.ones(6)
b[0] = 0.5
b[1] = 0.7
b[4] = 0.7
b[5] = 0.5
a[33] = 0.01
a[81] = 0.005
c[22] = 0.02
d = a.tolist() + b.tolist() + c


def animate(i):
    xs = np.linspace(lower_freq_limit, upper_freq_limit, frame_size, endpoint=True)
    ys = []
    for j in range(frame_size):
        y_val =  (10.0 * d[j] + 0.001 + 0.01 * random.random())
        ys.append(np.log10(y_val))
    ax1.clear()
    ax1.plot(xs, ys, 'limegreen',  linewidth=0.9)

    plt.text(1300, 1.6, 'ATTEN: 10dB', fontdict=font)
    plt.text(2100, 1.6, '10dB / DIV', fontdict=font)
    plt.text(3000, 1.6, 'RBW: 3000Hz',fontdict=font)
    plt.ylabel('Amplitude (dB)', fontdict=font)
    plt.xlabel('Frequency kHz', fontdict=font)
    plt.xlim(lower_freq_limit, upper_freq_limit)
    plt.text(0.7 * upper_freq_limit, 1.1, "peak = " + str(max(ys)), fontdict=font)
    ax1.grid(True)

ani = animation.FuncAnimation(fig, animate, interval = frame_interval)

plt.show()
