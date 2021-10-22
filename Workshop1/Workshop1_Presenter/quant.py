import pandas as pd
df = pd.read_csv("BTC.csv")
# # print(df)

# # DATA SELECTION----------------------------------------------------

# # Select and print just the “close” column of the data frame.
# print(df["close"])

# # Select and print the 18th row of the data frame.
# print(df.loc[18])

# # Select and print just the 17th,18th and 19th rows of just the “open” column. 
# print(df["open"].loc[17:19])


















# DATA MANIPULATION----------------------------------------------------

# Find the maximum and minimum “close” price in the first 100 rows.
# print(df["close"].loc[0:100].min())
# print(df["close"].loc[0:100].max())

# What is the average volume moved of BTC moved per day? (remember each line of the data is a 30-minute interval). 
# print(df["volume"].mean()*24*2)

# # Create a column that is the total $ amount of BTC sold for that time period called “dollar_amount” (assume every coin was traded at “close” price).
# # df["dollar_amount"] = df["close"]*df["volume"]
# # print(df)

# # What is the largest increase between the open and close prices in a single row?
# df["change"] = df["close"] - df["open"]
# print(df["change"].max())













# GRAPHING ROLLING AVERAGES-------------------------------------------
import matplotlib.pyplot as plt
# Plot the “close” price against a 100-interval rolling average.
# data = df["close"]
# data2 = df["close"].rolling(window=100).mean()

# plt.plot(data,color='green')
# plt.plot(data2,color='blue')
# plt.show()

# Plot the “close” price against a 100-interval rolling average and a 10-interval rolling average (select timeframe .loc[100:150]). 
data = df["close"].loc[100:150]
data2 = df["close"].rolling(window=100).mean().loc[100:150]
data3 = df["close"].rolling(window=10).mean().loc[100:150]
plt.plot(data,color='green')
plt.plot(data2,color='blue')
plt.plot(data3,color='red')
plt.show()