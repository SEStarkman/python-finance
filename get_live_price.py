# Writes rolling window live price to file, to be read by live_graph.py

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from yahoo_fin import stock_info as si
import time
import os

if __name__ == '__main__':
    ticker = 'TSLA'
    window_size = 20
    filename = f'live-{ticker}.txt'
    os.system(f"touch {filename}")

    while(True):
        count = 0
        with open(filename, 'r') as f:
            lines = f.readlines()
        if len(lines) > 20:
            with open(filename, 'w') as f:
                lines = lines[1:]
                for line in lines:
                    f.write(line)
        
        with open(filename, 'a+') as f:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            live_price = si.get_live_price(ticker)
            print(current_time, live_price)
            f.write(str(current_time))
            f.write(', ')
            f.write(str(live_price))
            f.write('\n')
            f.flush()
            time.sleep(1)