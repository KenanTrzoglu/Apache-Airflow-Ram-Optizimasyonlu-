from airflow.decorators import dag , task
from datetime import datetime

@dag(dag_id="First_dag",
     start_date=datetime(2026,1,1),
     schedule=None,
     catchup=False)
def first_dag():
    @task
    def first_task():
        print("first task")
    @task
    def second_task():
        print("Second Task")

    @task
    def third_task():
        print("Third Task")

    first_task() >> second_task() >> third_task()

daggs = first_dag()