import pandas as pd
import matplotlib.pyplot as plt

# Read CSV with Date already parsed
sm = pd.read_csv("Stocket_Market_Analysis/SM_Datasets/stocks.csv", parse_dates=['Date'])

""" Cleaning the data """
new_sm = sm.copy()  # Creates a copy of the data

new_sm['Date'] = pd.to_datetime(new_sm['Date'])
new_sm = new_sm.set_index('Date')
new_sm = new_sm.sort_index()

# Check data types
#print(new_sm.index.is_monotonic_increasing)
#print(new_sm.index.min(), new_sm.index.max())

'''
# Filtering for just aapl's CLOSE results on the 19 & 21
aapl_stk = new_sm.loc[(new_sm['Ticker'] == 'AAPL'), 'Close']
print(aapl_stk.loc['2023-03-19':'2023-03-21'])

print(pd.Timestamp('2023-03-19') in aapl_stk.index)  # Will return True or False
'''

# Basic Data Vis -----------------------

"""# Barchart of each company's number of stocks
ticker_counts = new_sm['Ticker'].value_counts()

plt.bar(ticker_counts.index, ticker_counts.values, color='blue', edgecolor='black')

plt.xlabel('Ticker')
plt.ylabel('Number of Stocks')
plt.title('Company Stock Count')

plt.xticks(rotation=45)

plt.show()
"""

"""# Lineplot of AAPL's stock volume in February

# Selecting only AAPL's Closing stock prices in February
aapl_close = new_sm.loc[(new_sm['Ticker'] == 'AAPL') & (new_sm.index.month == 2), 'Close']

# Initiating a line plot, cyan
plt.plot(aapl_close.index, aapl_close.values, color='c', linestyle='-')

# Graph labels
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('AAPL Stock Closings')
plt.xticks(rotation=45)

# Shows the plot
plt.show()
"""

"""# Lineplot of all company's stock volume

# Selection
aapl_vol = new_sm.loc[new_sm['Ticker'] == 'AAPL', 'Volume']
goog_vol = new_sm.loc[new_sm['Ticker'] == 'GOOG', 'Volume']
msft_vol = new_sm.loc[new_sm['Ticker'] == 'MSFT', 'Volume']
nflx_vol = new_sm.loc[new_sm['Ticker'] == 'NFLX', 'Volume']

plt.plot(aapl_vol.index, aapl_vol.values, color='blue', linestyle='-', label='AAPL')
plt.plot(goog_vol.index, goog_vol.values, color='orange', linestyle='-', label='GOOG')
plt.plot(msft_vol.index, msft_vol.values, color='green', linestyle='-', label='MSFT')
plt.plot(nflx_vol.index, nflx_vol.values, color='red', linestyle='-', label='NFLX')

# Graph labels
plt.xlabel('Date')
plt.ylabel('Stock Volume')
plt.title('Company Stock Volume')
plt.xticks(rotation=45)
plt.legend()

# Show graph
plt.show()
"""

"""# Lineplot of all company's stock volume (LOOP VERSION)

companies = {
    'AAPL': 'blue',
    'GOOG': 'orange',
    'MSFT': 'green',
    'NFLX': 'red'
}

plt.figure(figsize=(10.5,5))

# plot each company's stock volume in the loop
for ticker, color in companies.items():
    stock_vol = new_sm.loc[new_sm['Ticker'] == ticker, 'Volume']
    plt.plot(stock_vol.index, stock_vol.values, color=color, linestyle='-', label=ticker, alpha=0.7)

# Graph labels
plt.xlabel('Date')
plt.ylabel('Stock Volume')
plt.title('Company Stock Volume')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# Show graph
plt.show()
"""

