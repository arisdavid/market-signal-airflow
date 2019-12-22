import datetime
import airflow
from airflow import DAG
import os
from pathlib import Path
from airflow.operators.python_operator import PythonOperator
from us_markets.tasks import (get_us_tickers,
                              dl_data_and_pickle)
from common import (folder_manager,
                     calculator)


default_args = {
    'owner': 'arisdavid',
    'start_date': airflow.utils.dates.days_ago(1),
    'schedule_interval': '@daily',

}

with DAG(dag_id='qis_dag', default_args=default_args, params={
    'data_store': os.path.join(Path(__file__).parent.parent, 'artifacts')
}) as dag:

    create_folders = PythonOperator(
        task_id='create_folders',
        python_callable=folder_manager.create_folder,
        op_kwargs={'data_store': '{{params.data_store}}',
                   'sub_folders': ['raw_data', 'processed_data']}
    )

    dl_us_tickers = PythonOperator(
        task_id='download_us_tickers',
        python_callable=get_us_tickers,
        op_kwargs={'data_store': '{{params.data_store}}'}
    )

    dl_and_pickle_us_stocks = PythonOperator(
        task_id='download_us_historical_data',
        python_callable=dl_data_and_pickle,
        op_kwargs={'data_store': '{{params.data_store}}',
                   'start_date': (datetime.datetime.today() - datetime.timedelta(days=365)).strftime("%Y-%m-%d"),
                   'end_date': datetime.datetime.today().strftime("%Y-%m-%d")
                   }
    )

    create_quotes_table = PythonOperator(
        task_id='create_quotes_table',
        python_callable=calculator.create_quotes_table,
        op_kwargs={'data_store': '{{params.data_store}}'}
    )

    create_folders >> dl_us_tickers >> dl_and_pickle_us_stocks >> create_quotes_table
