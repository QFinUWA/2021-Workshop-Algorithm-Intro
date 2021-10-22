import pandas as pd
from talib.abstract import *

# local imports
from gemini_modules import engine

# read in data preserving dates
df = pd.read_csv("LTC.csv", parse_dates=[0])

# globals

backtest = engine.backtest(df)

'''Algorithm function, lookback is a data frame parsed to function continuously until end of initial dataframe is reached.'''
def logic(account, lookback):
    today = len(lookback)-1
    todays_price = lookback['close'].loc[today]
    average = lookback['close'].mean() 
    
    if(todays_price < average):
            if(account.buying_power > 0):
                account.enter_position('long', account.buying_power, todays_price)
    else:
        if(todays_price > average):
                for position in account.positions:
                        account.close_position(position, 1, todays_price) 

backtest.start(100, logic)
backtest.results()
backtest.chart()