import airflow
from airflow.models import DAG
from airflow.operators.bash import BashOperator
import os

# Get current directory
cwd = os.getcwd()
cwd = cwd + '/airflow_home/scripts/'

# Define the default arguments
args = {
    'owner': 'your_name',
    'start_date': airflow.utils.dates.days_ago(2),
}

# Instantiate the DAG passing the args as default_args
dag = DAG(
    dag_id='my_dag_id',
    default_args=args,
    schedule_interval=None
)

# Define the 4 tasks:
A = BashOperator(
    task_id='A_get_users',
    bash_command=f'{cwd}run_r.sh {cwd}A_task.R ',
    dag=dag,
    )
B = BashOperator(
    task_id='B_counts_by_gender',
    bash_command=f'{cwd}run_r.sh {cwd}B_task.R ',
    dag=dag,
    )
C = BashOperator(
    task_id='C_counts_by_age',
    bash_command=f'{cwd}run_r.sh {cwd}C_task.R ',
    dag=dag,
    )
command_line = 'Rscript -e "rmarkdown::render('+ "'" + f'{cwd}D_task.Rmd' + "')" + '"'
D = BashOperator(
    task_id='D_html_report',
    bash_command=f'{command_line} ',
    dag=dag,
    )

# Define the task dependencies
A >> B
A >> C
[B, C] >> D