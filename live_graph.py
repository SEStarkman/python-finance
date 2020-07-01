# Plots the live data in a rolling window

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

ticker = 'TSLA'

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.tick_params(axis='x', rotation=90)


def animate(i):
    filename=f'live-{ticker}.txt'
    graph_data = open(filename, 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)


if __name__ == '__main__':
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()