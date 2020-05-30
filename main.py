import pandas as pd
import pandas_datareader as pdr
import datetime

aapl = pdr.get_data_yahoo('AAPL',
                         start=datetime.datetime(2006, 10, 1),
                         end=datetime.datetime(2012,1,1))

aapl.head()
aapl.tail()
aapl.describe()
aapl.to_csv('data/aapl_ohlc.csv')