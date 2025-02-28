import pandas as pd

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

# Filtering for just aapl's CLOSE results on the 19 & 21
aapl_stk = new_sm.loc[(new_sm['Ticker'] == 'AAPL'), 'Close']
print(aapl_stk.loc['2023-03-19':'2023-03-21'])

print(pd.Timestamp('2023-03-19') in aapl_stk.index)  # Will return True or False
