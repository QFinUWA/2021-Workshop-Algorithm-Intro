import pandas as pd
from talib.abstract import *

# local imports
from gemini_modules import engine

# read in data preserving dates
df = pd.read_csv("LTC.csv", parse_dates=[0])

# globals
training_period = 20

#backtesting
backtest = engine.backtest(df)

def logic(account, lookback):
    today = len(lookback)-1
    todays_price = lookback['close'].loc[today]
    todays_volume = lookback['volume'].loc[today]

    if(today > training_period): 
        price_moving_average = lookback['close'].rolling(window=training_period).mean().loc[today]  # update PMA
        volumn_moving_average = lookback['volume'].rolling(window=training_period).mean().loc[today]  # update VMA

        if(todays_price < price_moving_average):
            if( todays_volume > volumn_moving_average):
                if(account.buying_power > 0):
                    account.enter_position('long', account.buying_power, lookback['close'].loc[today])
        else:
            if(todays_price > price_moving_average):
                if( todays_volume < volumn_moving_average):
                    for position in account.positions:
                            account.close_position(position, 1, lookback['close'].loc[today]) 


if __name__ == "__main__":
    backtest.start(100, logic)
    backtest.results()
    backtest.chart()
