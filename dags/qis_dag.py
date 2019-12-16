import datetime
import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from us_markets.tasks import (get_us_tickers, dl_data_and_pickle)

from folder_manager.tasks import create_folder

default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
    'schedule_interval': '@daily',
}

with DAG(dag_id='qis_dag', default_args=default_args) as dag:
    create_folder = PythonOperator(
        task_id='create_folders',
        python_callable=create_folder,
        op_kwargs={'data_store': 'artifacts'}
    )

    dl_us_tickers = PythonOperator(
        task_id='download_us_tickers',
        python_callable=get_us_tickers,
        op_kwargs={'data_store': 'artifacts'}
    )

    dl_and_pickle_us_stocks = PythonOperator(
        task_id='download_us_historical_data',
        python_callable=dl_data_and_pickle,
        op_kwargs={'data_store': 'artifacts',
                   'start_date':'2000-01-01',
                   'end_date': datetime.datetime.today().strftime("%Y-%m-%d")
                   }
    )

    create_folder >> dl_us_tickers >> dl_and_pickle_us_stocks
