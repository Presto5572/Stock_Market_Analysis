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

    # ---| Cleaning Supplies |---
    # Find missing values
    def find_missing(self):
        return self.df.isnull().sum()

    # Drop missing values once found
    def drop_missing(self):
        self.df.dropna(inplace=True)
        return self.df

    # Fill in missing values
    def fill_missing(self, column_name, default_value):
        self.df.fillna({column_name: default_value}, inplace=True)
        return self.df

    # Handles duplicate values
    def find_duplicate(self):
        duplicate_count = self.df.duplicated().sum()
        return duplicate_count  # Returns the count of duplicate rows
        
    # Drop duplicate values
    def drop_duplicate(self):
        self.df.drop_duplicates(inplace=True)
        return self.df
    
    # Fix column name inconsistencies (i.e. spacing and capitalization errors)
    def fix_text(self, column_name):
        if column_name in self.df.columns:
            self.df["column_name"] = self.df["column_name"].str.strip().str.title()
        else:
            print(f"Column {column_name} does not exist in the DataFrame.")
        return self.df
    
    # Ensures any dates are converted into DATETIME objects
    def fix_date(self, column_name):
        self.df[column_name] = pd.to_datetime(self.df[column_name], dayfirst=True)
        return self.df
    
def main():
    stk_analyzer = Stock_Analyzer("SM_Analysis/stocks.csv")

    """ Cleaning actions (Text & Date)
    # Cleans a specific column (replace 'YourColumnName' with an actual column name)
    cleaned_df = stk_analyzer.fix_text("YourColumnName")
    print(cleaned_df.head())

    # Fixes the dates if needed
    cleaned_date = stk_analyzer.fix_date("Date")
    print(cleaned_date.head())
    """

    print(stk_analyzer.get_summary())

if __name__ == "__main__":
    main()
