import s3fs
import pandas as pd
from sqlalchemy import create_engine
def s3_to_db():
    storage_options={"key":"AKIAWXTIADOVZYJLTKFN","secret":"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"}
    df= pd.read_csv("s3:///dprdclbucket/csv/cust_info.csv", storage_options)
    engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres:5432/airflow")
    df.to_sql("raw_data", engine, if_exists="replace", index=False)
s3_to_db()