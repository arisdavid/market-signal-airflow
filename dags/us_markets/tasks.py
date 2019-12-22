import pandas as pd
import os
from common.dl_hist_data import dl_hist_data


def get_us_tickers(data_store=None):

    url = 'ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt'

    nasdaq_df = pd.read_csv(url, sep='|')
    nasdaq_df.dropna(inplace=True)
    nasdaq_df = nasdaq_df[['Symbol', 'Security Name', 'ETF']]

    url = 'ftp://ftp.nasdaqtrader.com/symboldirectory/otherlisted.txt'

    other_df = pd.read_csv(url, sep='|')
    other_df.dropna(inplace=True)
    other_df = other_df[['ACT Symbol', 'Security Name', 'ETF']]
    other_df.rename(columns={'ACT Symbol': 'Symbol'}, inplace=True)

    us_tickers_df = nasdaq_df.append(other_df)
    us_tickers_df.index = range(len(us_tickers_df.index))

    if os.path.exists(data_store):
        us_tickers_df.to_pickle(f'{data_store}/us_tickers.pkl')

    pass


def dl_data_and_pickle(data_store, start_date, end_date):

    tickers_df = pd.read_pickle(f'{data_store}/us_tickers.pkl')

    for ticker in tickers_df['Symbol'].tolist():
        try:
            hist_data_df = dl_hist_data(ticker, start_date, end_date)
            hist_data_df.to_pickle(f'{data_store}/{ticker}.pkl')
        except Exception as err:
            print(err)
            continue

    pass

