from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(".."))
from scripts.dataloader import DataLoader
from scripts.db_connection import Connection

default_args = {
    'owner': 'Haylemicheal',
    'depends_on_past': False,
    'email': ['haylemicheal.mekonnen.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'start_date': datetime(2022, 9, 23),
    'retry_delay': timedelta(minutes=5)
}


def read_data():
    """csv data reading
    """
    dl = DataLoader()
    headers, rows = dl.read_csv('/opt/airflow/data/20181024_d1_0900_0930.csv')
    vehicles, trajectories = dl.data_to_dataframe(headers, rows)
    vehicles.to_csv('/opt/airflow/data/vehicles.csv', index=False)
    trajectories.to_csv('/opt/airflow/data/trajectories.csv',index=False)

def create_table():
    con = Connection()
    con.create_table()

def insert_data_to_db():
    """Insert data to db"""
    con = Connection()
    vehicles = pd.read_csv('/opt/airflow/data/vehicles.csv')
    trajectories = pd.read_csv('/opt/airflow/data/trajectories.csv')
    con.df_to_sql('vehicles', vehicles)
    con.df_to_sql('trajectories', trajectories)

with DAG(
    dag_id='data_to_postgres_loader',
    default_args=default_args,
    description='Read csv, extract, and put to postgres',
    schedule_interval='@once',
    catchup=False
) as dag:
    data_reader = PythonOperator(
        task_id='read_data',
        python_callable=read_data
    )
    table_creator = PythonOperator(
        task_id='table_creator',
        python_callable=create_table
    )
    insert_data = PythonOperator(
        task_id='insert_data_to_db',
        python_callable=insert_data_to_db
    )

data_reader>>table_creator>>insert_data


