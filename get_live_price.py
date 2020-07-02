# Writes rolling window live price to file, to be read by live_graph.py

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from yahoo_fin import stock_info as si
import time
import os
import argparse


def write_live_price(ticker, window_size, small_window, large_window, interval):
    filename = f'live-{ticker}.txt'

    while(True):
        with open(filename, 'r') as f_read:
            lines = f_read.readlines()
            if len(lines) > window_size:
                with open(filename, 'w') as f_write:
                    lines = lines[1:]
                    for line in lines:
                        f_write.write(line)

        with open(filename, 'a+') as f:
            now = datetime.now().strftime("%H:%M:%S")

            live_price = si.get_live_price(ticker)

            rolling_small = live_price
            rolling_large = live_price
            # print(lines)
            if len(lines) > small_window:
                values = [float(line.split(',')[1]) for line in lines]
                rolling_small = sum(values[-small_window:]) / small_window

            if len(lines) > large_window:
                values = [float(line.split(',')[1]) for line in lines]
                rolling_large = sum(values[-large_window:]) / large_window

            output = f"{now},{live_price},{rolling_small},{rolling_large}"
            f.write(output)
            f.write('\n')
            time.sleep(interval)
            print(output)
        

if __name__ == '__main__':
    window_size = 1800
    small_window = 15
    large_window = 60
    interval = 1
    parser = argparse.ArgumentParser()
    parser.add_argument('ticker')
    args = parser.parse_args()
    ticker = args.ticker
    write_live_price(ticker, window_size, small_window, large_window, interval)