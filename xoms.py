from urllib import request
import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import random


def _train_model(**context):
 model_id = str(random.random())
 print("model_idmodel_idmodel_id",model_id)
 context["task_instance"].xcom_push(key="model_id", value=model_id)


def _deploy_model(**context):
 model_id = context["task_instance"].xcom_pull(
 task_ids="train_model", key="model_id")
 print(f"Deploying model {model_id}")

 
with DAG (dag_id="xcoms_dag",start_date=airflow.utils.dates.days_ago(1),schedule_interval=None) as dag:
  train_model = PythonOperator(
  task_id="train_model",
  python_callable=_train_model,
  dag=dag
  )

  deploy_model = PythonOperator(
  task_id="deploy_model",
  python_callable=_deploy_model,
  dag=dag
  )

train_model >> deploy_model 
