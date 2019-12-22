import pandas as pd
import os


def create_stats_table(artifacts_dir):

    # | Ticker | Price | Pct Change | Volume | Average_Volume | Last Trading Date |

    tickers = [ticker.replace(".pkl", "") for ticker in os.listdir(artifacts_dir)]

    with open(f'{tickers}.pkl', 'a') as f:
        df = pd.read_pickle(f)

    return df




def second_day_play(artifacts_dir):

    """
    Second Day Play Scanner
    Criteria: Liquid over 1M in volume
              Relative Volume 3
              stock price above the 75% quantile of its range
    :return:
    """

    pass


import yfinance as yf
import datetime

today = datetime.datetime.today().strftime("%Y-%m-%d")


def dl_hist_data(ticker, start_date, end_date=today):
    """

    :param ticker: Ticker Symbol default is current date
    :param start_date: Starting Date
    :param end_date: Ending Date
    :return: DataFrame
    """

    try:

        data = yf.download(ticker, start=start_date, end=end_date)
        data["Ticker"] = ticker

        return data

    except Exception as e:
        print(e)


