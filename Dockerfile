FROM puckel/docker-airflow:latest

WORKDIR /usr/local/airflow

COPY requirements.txt requirements.txt

COPY ./dags ./dags

RUN pip install --user -r requirements.txt

