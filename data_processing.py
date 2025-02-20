import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Parent class
class Stock_Analyzer:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    # Get summary statistics of numerical columns
    def get_summary(self):
        return self.df.describe()
    
    # Returns a list of all columns and their data type
    def get_info(self):
        return self.df.dtypes

    # Checks for missing/null values
    def loc_missing_vals(self):
        return self.df.isnull().sum()
    
stock_analysis = Stock_Analyzer("SM_Analysis/stocks.csv")
    
