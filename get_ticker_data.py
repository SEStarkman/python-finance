import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import argparse
from pandas.plotting import register_matplotlib_converters


def display_chart(ticker):
        yahoo = yf.Ticker(ticker)
        small_window = 5
        large_window = 15
        time_window = '3mo'
        df = yahoo.history(period=time_window)

        rolling_small = df.rolling(window=small_window).mean()
        rolling_large = df.rolling(window=large_window).mean()

        fig, ax = plt.subplots(figsize=(12, 8))

        ax.plot(df.index, df['Close'], label=ticker)
        ax.plot(rolling_small.index, rolling_small['Close'], label=f'{small_window}-Day SMA')
        ax.plot(rolling_large.index, rolling_large['Close'], label=f'{large_window}-Day SMA')

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
    parser.add_argument('--ticker')
    args = parser.parse_args()

if args.filename:
    with open(args.filename) as file:
        tickers = file.readlines()
        tickers = [ticker.strip() for ticker in tickers]
    print(tickers)

    num_tickers = len(tickers)

    for ticker in tickers:
        display_chart(ticker)
elif args.ticker:
    ticker = args.ticker
    display_chart(ticker)