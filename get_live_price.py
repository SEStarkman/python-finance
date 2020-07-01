# Writes rolling window live price to file, to be read by live_graph.py

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from yahoo_fin import stock_info as si
import time
import os


def write_live_price(ticker):
    window_size = 20
    filename = f'live-{ticker}.txt'
    os.system(f"touch {filename}")

    while(True):
        # Add next time step
        with open(filename, 'a+') as f:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            live_price = si.get_live_price(ticker)
            output_line = f"{current_time},{live_price},0,0"
            print(output_line)
            f.write(output_line)
            f.write('\n')
            f.flush()
            time.sleep(1)

        # Check if > window
        with open(filename, 'r') as f:
            lines = f.readlines()

        if len(lines) >= window_size:
            with open(filename, 'w') as f:

                lines = lines[1:]
                times = []
                live_values = []
                rolling_small = []
                rolling_large = []
                for line in lines:
                    line = line.rstrip()
                    line_list = line.split(',')
                    times.append(line_list[0])
                    live_values.append(float(line_list[1]))
                    rolling_small.append(line_list[2])
                    rolling_large.append(line_list[3])

                sma_small = sum(live_values[-5:])/5
                sma_large = sum(live_values[-15:])/15

                rolling_small[-1] = sma_small
                rolling_large[-1] = sma_large

                for i in range(len(times)):
                    output_line = f"{times[i]},{live_values[i]},{rolling_small[i]},{rolling_large[i]}"
                    print(f"output line: {output_line.rstrip()}")
                    f.write(output_line)
                    f.write('\n')
                    f.flush()
        

if __name__ == '__main__':
    ticker = 'TSLA'
    write_live_price(ticker)
    