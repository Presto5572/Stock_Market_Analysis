# Stock Market Analysis Data Overview

## head()
 Ticker        Date        Open        High         Low       Close   Adj Close    Volume
0   AAPL  2023-02-07  150.639999  155.229996  150.639999  154.649994  154.414230  83322600
1   AAPL  2023-02-08  153.880005  154.580002  151.169998  151.919998  151.688400  64120100
2   AAPL  2023-02-09  153.779999  154.330002  150.419998  150.869995  150.639999  56007100
3   AAPL  2023-02-10  149.460007  151.339996  149.220001  151.009995  151.009995  57450700
4   AAPL  2023-02-13  150.949997  154.259995  150.919998  153.850006  153.850006  62199000

## columns
Index(['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close',
       'Volume'],
      dtype='object')

## info()
RangeIndex: 248 entries, 0 to 247
Data columns (total 8 columns):
 #   Column     Non-Null Count  Dtype
---  ------     --------------  -----
 0   Ticker     248 non-null    object
 1   Date       248 non-null    object
 2   Open       248 non-null    float64
 3   High       248 non-null    float64
 4   Low        248 non-null    float64
 5   Close      248 non-null    float64
 6   Adj Close  248 non-null    float64
 7   Volume     248 non-null    int64
dtypes: float64(5), int64(1), object(2)
memory usage: 15.6+ KB
