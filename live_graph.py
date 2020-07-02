# Plots the live data in a rolling window

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import argparse

def animate(i):
    filename=f'live-{ticker}.txt'
    graph_data = open(filename, 'r').read()
    lines = graph_data.split('\n')
    xs = []
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
    ax1.plot(xs, y_live, color= 'black', label='Live Price')
    ax1.plot(xs, y_small, color='green', label='SMA Short Term')
    ax1.plot(xs, y_large, color='red', label='SMA Long Term') 
    ax1.legend(loc='lower left')


if __name__ == '__main__':
    
    # ticker = 'NKLA'
    parser = argparse.ArgumentParser()
    parser.add_argument('ticker')
    args = parser.parse_args()
    ticker = args.ticker

    # style.use('fivethirtyeight')

    fig = plt.figure(figsize=(12, 8))
    fig.suptitle(f"{ticker}")
    ax1 = fig.add_subplot(1,1,1)
    ax1.tick_params(axis='x', rotation=90)
    ax1.get_xaxis().set_visible(False)

    ani = animation.FuncAnimation(fig, animate, interval=1000)  
    plt.show()