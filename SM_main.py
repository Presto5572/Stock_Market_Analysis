import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------
# --Windows--
# stocks_data = pd.read_csv("_____")

# --Mac--
stocks_data = pd.read_csv("SM_Analysis/stocks.csv")
# -------------------------------------------------

print(stocks_data)

print(stocks_data.Ticker.value_counts())