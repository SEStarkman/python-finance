from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from datetime import date
import pandas as pd

api_key = "PVBSBOZLVFHB2VHE"

ticker = 'TSLA'

ts = TimeSeries(api_key)
data = ts.get_intraday(symbol='TSLA',interval='1min')
df = pd.DataFrame.from_dict(data[0], orient='index')

last_minute_open = df['1. open'][-1]
last_minute_close = df['4. close'][-1]

print(last_minute_open, last_minute_close)