# Plots the live data in a rolling window

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

ticker = 'TSLA'

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.tick_params(axis='x', rotation=90)
# ax1.get_xaxis().set_visible(False)



def animate(i):
    filename=f'live-{ticker}.txt'
    graph_data = open(filename, 'r').read()
    lines = graph_data.split('\n')
    xs = []
    # x2 = np.arange(0, 61)
    y_live = []
    y_small = []
    y_large = []
    for line in lines:
        if len(line) > 1:
            x, y1, y2, y3 = line.split(',')
            xs.append(x)
            y_live.append(float(y1))
            y_small.append(float(y2))
            y_large.append(float(y3))
    ax1.clear()
    ax1.plot(xs, y_live)


if __name__ == '__main__':
    # ani = animation.FuncAnimation(fig, animate, interval=1000)
    filename=f'live-{ticker}.txt'
    graph_data = open(filename, 'r').read()
    lines = graph_data.split('\n')
    xs = []
    # x2 = np.arange(0, 61)
    y_live = []
    y_small = []
    y_large = []
    for line in lines:
        if len(line) > 1:
            time = line.split(',')[0]
            live = line.split(',')[1]
            sma_small = line.split(',')[2]
            sma_large = line.split(',')[3]

            xs.append(time)
            y_live.append(float(live))
            y_small.append(float(sma_small))
            y_large.append(float(sma_large))
    ax1.clear()
    ax1.plot(xs, y_live)
    ax1.plot(xs, y_small)
    ax1.plot(xs, y_large)    
    plt.show()