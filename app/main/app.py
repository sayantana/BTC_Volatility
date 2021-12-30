from db import initialize
import math
import os
import time
import pandas as pd
from datetime import date, timedelta


date_columns = ['time_period_start','time_period_end','time_open','time_close']


def convertToDate(df):
    for col in date_columns:
        df[col] = pd.to_datetime(df[col])
    return df

        
def calculateVolatility(df):
    df['day'] = df['time_period_start'].dt.date
    df['price_diff_per_day'] = df['price_high']-df['price_low']
    return df.groupby('day', as_index = False).agg(
        price_close_std = ('price_close','std'),
        price_open_std = ('price_open','std'),
        price_low_std = ('price_low','std'),
        price_high_std = ('price_high', 'std'),
        price_diff_per_day_std = ('price_diff_per_day', 'std')
    )

def etl():
    df = pd.read_json('http://cf-code-challenge-40ziu6ep60m9.s3-website.eu-central-1.amazonaws.com/ohlcv-btc-usd-history-6min-2020.json')
    df = convertToDate(df)
    # setting currency to bitcoin see CryptoCurrency table
    df = df.dropna()
    df['currency'] = 1
    engine = initialize()
    df.to_sql('btc_price', engine, index = False, if_exists = 'append')
    volatility = calculateVolatility(df)
    volatility.to_sql('btc_volatility', engine, index=False, if_exists = 'append')

    
if __name__ == '__main__':
    print('Application started')
    etl()
    print('Extract Transform and Load is completed')