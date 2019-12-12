# Download Stock Universe from LSE
# Download Historical Data from yahoo finance
# Store Data in PostgresDB


import pandas as pd


class StockUniverse:

    @staticmethod
    def universe_from_excel(source_url, sheet_name, skiprows):
        """

        :param source_url: source url
        :param sheet_name: sheet name
        :param skiprows: skiprows
        :return: df
        """

        df = pd.read_excel(source_url, sheet_name, skiprows=skiprows)
        df.dropna(subset=['Issuer Name', 'Instrument Name'], inplace=True)

        return df


def download_stock_universe():

    source_url = 'https://www.londonstockexchange.com/statistics/companies-and-issuers/instruments-defined-by-mifir-identifiers-list-on-lse.xlsx'
    sheet_name = '1.1 Shares'
    universe_df = StockUniverse.universe_from_excel(source_url, sheet_name, 7)
    # Remove column spaces
    universe_df.columns = universe_df.columns.str.replace(' ', '')

    return universe_df.to_dict(orient='records')




