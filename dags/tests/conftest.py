from dags.lse.tasks import download_stock_universe
import pytest


@pytest.fixture(scope='module')
def get_lse_data():

    return download_stock_universe()