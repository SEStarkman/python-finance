import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

ticker = "XLK"
tsla = yf.Ticker(ticker)
df = tsla.history(period='5y')

rolling_20 = df.rolling(window=20).mean()
rolling_100 = df.rolling(window=100).mean()

fig, ax = plt.subplots(figsize=(16,9))

ax.plot(df.index, df['Close'], label='TSLA')
ax.plot(rolling_20.index, rolling_20['Close'], label='20-Day SMA')
ax.plot(rolling_100.index, rolling_100['Close'], label='100-Day SMA')

title = f"{ticker} SMA Comparison"
ax.set_title(title)
ax.set_xlabel('Date')
ax.set_ylabel('Close Price ($)')

ax.legend()
plt.show()

