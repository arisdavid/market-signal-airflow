import datetime
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from lse.tasks import download_stock_universe

def cleanse(s):
    return s

# 2. Configure params / default arguments
default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    # If a task fails, retry it once after waiting at least 5 minutes
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
}

# 3. Instantiate a DAG
dag = DAG('qis_dag',
          default_args=default_args,
          # Continue to run DAG once per day
          schedule_interval=datetime.timedelta(days=1))

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = PythonOperator(
    task_id = 'download_stock_universe',
    python_callable=download_stock_universe,
    dag=dag
)

t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    dag=dag,
)

templated_command = """
{% for i in range(5) %}
    echo "{{ ds }}"
    echo "{{ macros.ds_add(ds, 7)}}"
    echo "{{ params.my_param }}"
{% endfor %}
"""

t3 = BashOperator(
    task_id='templated',
    depends_on_past=False,
    bash_command=templated_command,
    params={'my_param': 'Parameter I passed in'},
    dag=dag,
)

t1 >> [t2, t3]