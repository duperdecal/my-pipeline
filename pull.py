#Скрипт чтобы 
#скачивать с AWS S3 файл 
import boto3
import pandas as pd

def pull_rawfile():
    session= boto3.Session(    aws_access_key_id='AKIAWXTIADOVZYJLTKFN',
        aws_secret_access_key='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')
    s3=session.client('s3')
    bucket_name='dprdclbucket'
    file_path_s3='csv/cust_info.csv'
    local_file='/home/dprdcl/archive/crm_db.csv'
    s3.download_file(bucket_name,file_path_s3,local_file)

pull_rawfile()
#Верхним кодом скачивается файл и загружается в ./archive
