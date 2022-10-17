from urllib import request
import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.decorators import task
import random



 
with DAG (dag_id="xcoms_dag",start_date=airflow.utils.dates.days_ago(1),schedule_interval=None) as dag:
  @task
  def train_model():
    model_id = str(random.random())
    print("model_idmodel_idmodel_id",model_id)
    # context["task_instance"].xcom_push(key="model_id", value=model_id)
    return model_id

  @task
  def deploy_model(model_id):
   print(f"Deploying model ** {model_id}")

  model_id = train_model()
  deploy_model(model_id)

#   train_model = PythonOperator(
#   task_id="train_model",
#   python_callable=_train_model,
#   dag=dag
#   )

#   deploy_model = PythonOperator(
#   task_id="deploy_model",
#   python_callable=_deploy_model,
#   dag=dag
#   )

# train_model >> deploy_model 
