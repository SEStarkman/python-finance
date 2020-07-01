import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import argparse
# import Tkinter as tk

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

    fig, ax = plt.subplots(num_tickers)
    fig.tight_layout(pad=3.0)

    i = 0
    for ticker in tickers:
        yahoo = yf.Ticker(ticker)
        df = yahoo.history(period='5y')

        rolling_20 = df.rolling(window=20).mean()
        rolling_100 = df.rolling(window=100).mean()

        ax[i].plot(df.index, df['Close'], label=ticker)
        ax[i].plot(rolling_20.index, rolling_20['Close'], label='20-Day SMA')
        ax[i].plot(rolling_100.index, rolling_100['Close'], label='100-Day SMA')

        title = f"{ticker} SMA Comparison"
        ax[i].set_title(title)
        ax[i].set_xlabel('Date')
        ax[i].set_ylabel('Close Price ($)')

        ax[i].legend()
        i += 1


    plt.show()

elif args.ticker:
    ticker = args.ticker
    yahoo = yf.Ticker(ticker)
    df = yahoo.history(period='5y')

    rolling_20 = df.rolling(window=20).mean()
    rolling_100 = df.rolling(window=100).mean()

    fig, ax = plt.subplots()

    ax.plot(df.index, df['Close'], label=ticker)
    ax.plot(rolling_20.index, rolling_20['Close'], label='20-Day SMA')
    ax.plot(rolling_100.index, rolling_100['Close'], label='100-Day SMA')

    title = f"{ticker} SMA Comparison"
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Close Price ($)')

    ax.legend()
    plt.show()


