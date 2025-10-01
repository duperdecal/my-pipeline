from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from datetime import datetime, timedelta
import s3fs
import pandas as pd
from sqlalchemy import create_engine

def s3_to_db():
    df= pd.read_csv("s3:///dprdclbucket/csv/cust_info.csv", storage_options={"key":"AKIAWXTIADOVZYJLTKFN","secret":"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"})
    engine= create_engine("postgresql+psycopg2://airflow:airflow@postgres:5432/airflow")
    df.to_sql("raw_data", engine, if_exists="replace", index=False, schema="raw")
    
default_args= {
    'owner': 'airflow',
    'start_date': datetime(2025, 9, 25),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id="pipeline_orchestrate",
    default_args=default_args,
    schedule=timedelta(hours=1),
    catchup=False,
    description="main DAG of the pipeline",
) as dag:
    task1=PythonOperator(
        task_id="EL_in_ELT",
        python_callable= s3_to_db
    )
    task2=DockerOperator(
        task_id="T_in_ELT",
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(source='/home/dprdcl/repos/pipeline/dbt/my_project',
                  target='/usr/app',
                  type='bind' ),
            Mount(source='/home/dprdcl/repos/pipeline/dbt/profiles.yml',
                  target='/root/.dbt/profiles.yml',
                  type='bind' ),
            Mount(source='/home/dprdcl/repos/pipeline/dbt/target',
                  target='/usr/app/target',
                  type='bind' )
        ],
        network_mode='pipeline_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
        )
    task3=DockerOperator(
        task_id="test",
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='test',
        working_dir='/usr/app',
        mounts=[
            Mount(source='/home/dprdcl/repos/pipeline/dbt/my_project',
                  target='/usr/app',
                  type='bind' ),
            Mount(source='/home/dprdcl/repos/pipeline/dbt/profiles.yml',
                  target='/root/.dbt/profiles.yml',
                  type='bind' ),
            Mount(source='/home/dprdcl/repos/pipeline/dbt/target',
                  target='/usr/app/target',
                  type='bind' )
        ],
        network_mode='pipeline_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
        )
    task4=DockerOperator(
        task_id="docs",
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='docs generate',
        working_dir='/usr/app',
        mounts=[
            Mount(source='/home/dprdcl/repos/pipeline/dbt/my_project',
                  target='/usr/app',
                  type='bind' ),
            Mount(source='/home/dprdcl/repos/pipeline/dbt/profiles.yml',
                  target='/root/.dbt/profiles.yml',
                  type='bind' ),
            Mount(source='/home/dprdcl/repos/pipeline/dbt/target',
                  target='/usr/app/target',
                  type='bind' )
        ],
        network_mode='pipeline_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
        )
task1>>task2>>task3
