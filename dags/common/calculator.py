import pandas as pd
import os


def create_quotes_table(data_store):

    # | Ticker | Price | PctChange | Volume | Average_Volume | Last Trading Date |
    tickers = [ticker.replace(".pkl", "") for ticker in os.listdir(f"{data_store}/raw_data")]

    stats_table = []
    for ticker in tickers:
        try:

            df = pd.read_pickle(f'{data_store}/raw_data/{ticker}.pkl')

            # Daily Return
            df['Return'] = df['Adj Close'].pct_change()
            last_date = df.index[-1]
            last_volume = float(df.at[last_date, 'Volume'])
            mean_volume = float(df['Volume'].tail(20).mean()) #TODO: Last n Volume

            stats_table.append({

                'Ticker': df.at[last_date, 'Ticker'],
                'Price': df.at[last_date, 'Adj Close'],
                'Pct_Change': df.at[last_date, 'Return'],
                'Volume': last_volume,
                'Average_Volume': mean_volume,
                'RVOL': last_volume / mean_volume,
                'Trade_Date': df.index[-1]
            })

        except Exception as err:
            print(err)
            continue

    quotes_df = pd.DataFrame(stats_table)

    # yield quotes_df

    # Store in DataStore
    quotes_df.to_pickle(f'{data_store}/processed_data/quotes_df.pkl')


def second_day_play(data_store):

    """
    Second Day Play Scanner
    Criteria: Liquid over 1M in volume
              Relative Volume 3
              stock price above the 75% quantile of its range
    :return:
    """

    pass




