import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task

# Using task decorator, we don't need to instantiate the operator

# OLD WAY: We need to instantiate the python operator
"""
def one():
    print("one")

def two():
   print(f"Two")

with DAG (dag_id="task_decorator",start_date=airflow.utils.dates.days_ago(1),schedule_interval=None) as dag:
  one11 = PythonOperator(
  task_id="one",
  python_callable=one,
  dag=dag
  )
  two22 = PythonOperator(
  task_id="two",
  python_callable=two,
  dag=dag
  )

one11 >> two22 
"""

#NEW WAY
@task.python
def one():
    print("one new")

@task.python
def two():
   print(f"Two new")

with DAG (dag_id="task_decorator",start_date=airflow.utils.dates.days_ago(1),schedule_interval=None) as dag:
  one() >> two()
