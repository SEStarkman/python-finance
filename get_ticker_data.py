import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import argparse
from pandas.plotting import register_matplotlib_converters


def display_chart(ticker, small_window, large_window, time_window):
        yahoo = yf.Ticker(ticker)
        df = yahoo.history(period=time_window)
        print(df)

        rolling_small = df.rolling(window=small_window).mean()
        rolling_large = df.rolling(window=large_window).mean()

        fig, ax = plt.subplots(figsize=(12, 8))

        ax.plot(df.index, df['Close'], color='black', label=ticker)
        ax.plot(rolling_small.index, rolling_small['Close'], color='green', label=f'{small_window}-Day SMA')
        ax.plot(rolling_large.index, rolling_large['Close'], color='red', label=f'{large_window}-Day SMA')

        title = f"{ticker} SMA Comparison"
        ax.set_title(title)
        ax.set_xlabel('Date')
        ax.set_ylabel('Close Price ($)')

        ax.legend()
        plt.show()


if __name__ == '__main__':

    register_matplotlib_converters()

    parser = argparse.ArgumentParser()
    parser.add_argument('--filename')
    parser.add_argument('--ticker', nargs='+')
    args = parser.parse_args()

    small_window = 5
    large_window = 15
    time_window = '3mo'

if args.filename:
    with open(args.filename) as file:
        tickers = file.readlines()
        tickers = [ticker.strip() for ticker in tickers]

    for ticker in tickers:
        display_chart(ticker, small_window, large_window, time_window)

elif args.ticker:
    ticker_list = args.ticker
    for ticker in ticker_list:
        display_chart(ticker, small_window, large_window, time_window)