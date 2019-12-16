# Daily Trading Signal

Experimental daily trading signal generation with apache-airflow

## Pre-requisites:
Ensure docker for desktop is installed


## Steps:

1. Clone the repository and cd into the root directory.
2. Launch the services.
    ```
    docker-compose up -d --build
    ```
3. Server should be running on port 8080
    ```
    curl -I http://localhost:8080/
    ```
... TBC   

## Disclaimer:
All information found on this software, including any ideas, opinions, views, predictions, forecasts, commentaries or suggestions expressed or implied herein, are for informational and educational purposes only and should not be construed as personal investment advice.


## Screenshots
![airflow-dashboard](img/airflow_workflow.PNG?raw=true)

![airflow-pickles](img/pickles.PNG?raw=true)