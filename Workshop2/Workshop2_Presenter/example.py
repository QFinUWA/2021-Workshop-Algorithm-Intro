import pandas as pd
from talib.abstract import *

# local imports
from gemini_modules import engine

# read in data preserving dates
df = pd.read_csv("LTC.csv", parse_dates=[0])

backtest = engine.backtest(df)

def logic(account, lookback):
    print(lookback)
    

backtest.start(100, logic)
backtest.results()
backtest.chart()


