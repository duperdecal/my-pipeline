#Mini-Pipeline Project

Это мой первый проект мини-пайплайн построенный на Airflow, dbt, docker compose и Postgres

Все запускалось с чистого WSL-Ubuntu, проект построен на контейнерах docker-compose

все нужные библиотеки указаны в requirement.txt

Архитектура проекта:
AWS S3>>Python-s3fs>>Airflow>>Postgres>>dbt

в Базе Данных были построены три слоя:
1. Полностью сырые данные - Data Lakehouse
2. Частично обработанные данные с нецелостными строками, но готовые для анализа- Silver Layer
3. Полностью очищенные данные - Gold Layer

#Стек технологий 
    - Python
    - Airflow 2.9.3
    - PostgreSQL
    - Docker Compose 
    - AWS S3
    - dbt

