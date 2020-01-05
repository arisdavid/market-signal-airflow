import pandas as pd
import os
from scipy.stats import kurtosis, skew


def create_quotes_table(data_store):

    # | Ticker | Price | PctChange | Volume | Average_Volume | Last Trading Date | 1Sigma
    tickers = [ticker.replace(".pkl", "") for ticker in os.listdir(f"{data_store}/raw_data")]

    stats_table = []
    for ticker in tickers:
        try:

            df = pd.read_pickle(f'{data_store}/raw_data/{ticker}.pkl')

            # Daily Return
            df['Return'] = df['Adj Close'].pct_change()
            last_date = df.index[-1]
            last_volume = float(df.at[last_date, 'Volume'])
            mean_volume = float(df['Volume'].tail(20).mean())

            stats_table.append({

                'Ticker': df.at[last_date, 'Ticker'],
                'Price': df.at[last_date, 'Adj Close'],
                'Pct_Change': df.at[last_date, 'Return'],
                'Volume': last_volume,
                'Average_Volume': mean_volume,
                'RVOL': last_volume / mean_volume,
                'Trade_Date': df.index[-1],
                'Kurtosis': kurtosis(df['Return'], nan_policy='omit'),
                'Skewness': skew(df['Return'], nan_policy='omit'),
                'Pocket_Pivot': 0
            })

        except Exception as err:
            print(err)
            continue

    quotes_df = pd.DataFrame(stats_table)

    # yield quotes_df

    # Store in DataStore
    quotes_df.to_pickle(f'{data_store}/processed_data/quotes_df.pkl')

"""
from pathlib import Path
data_store = os.path.join(Path(__file__).parent.parent.parent, 'artifacts')
df = pd.read_pickle(f'{data_store}/processed_data/quotes_df.pkl')
cols = ['Volume']
df[cols] = df[df[cols] > 1000000][cols]
df.dropna(inplace=True)

cols = ['Price']
df[cols] = df[df[cols] < 20][cols]
df.dropna(inplace=True)

cols = ['Pct_Change']
df[cols] = df[df[cols] > 0.05][cols]
df.dropna(inplace=True)

cols = ['RVOL']
df[cols] = df[df[cols] > 2][cols]
df.dropna(inplace=True)

df.sort_values(by='RVOL', ascending=False, inplace=True)

x = 0

"""