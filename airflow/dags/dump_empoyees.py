"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/incubator-airflow/blob/master/airflow/example_dags/tutorial.py
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.oracle_operator import OracleOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('dump_employees', default_args=default_args)

sql = """CREATE OR REPLACE VIEW test.prog_empoyees AS
SELECT * FROM test.employees
WHERE JOB_ID = 'IT_PROG'
)"""

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = OracleOperator(
    task_id='dump_empoyees_database',
    oracle_conn_id='oracle_prod',
    sql=sql,
    )
