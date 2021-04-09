# Airflow-R-tutorial
## Airflow tutorial for running R scripts

### How to run

Create a virtual environment (with Python and R) and activate it. In this case, I created it using anaconda:

    cd path/to/Airflow-R-tutorial
    conda create -n my_airflow_env r-essentials r-base
    conda activate my_airflow_env

Now, install apache-airflow:

    sudo pip3 install apache-airflow

(Note: It is possible that you'll need to execute sudo pip3 install SQLAlchemy==1.3.18to override the newer SQLAlchemy version.)

It is necessary to create the AIRFLOW_HOME directory and set the environment variable AIRFLOW_HOME. To be more explicit, I called this directory airflow_home:

    cd path/to/Airflow-R-tutorial
    mkdir airflow_home
    export AIRFLOW_HOME=`pwd`/airflow_home

Now check if everything is ok:

    airflow version

Start the database

    airflow db init

Create a user

    airflow users create \
      --username admin \
      --firstname FIRST_NAME \
      --lastname LAST_NAME \
      --role Admin \
      --email admin@example.org

Start the Webserver to acccess to the UI:

    airflow webserver

In a new terminal start the Scheduler:

    cd path/to/Airflow-R-tutorial
    conda activate my_airflow_env   
    export AIRFLOW_HOME=`pwd`/airflow_home

    airflow scheduler

To access Airflow UI open localhost:8080.
You will find your DAG there. Unpaused if it is paused.
Trigger it by clicking the "play" button in the upper right corner.

For more detailed instructions, visit  [this post](https://lcalcagni.medium.com/running-r-scripts-in-airflow-using-airflow-bashoperators-6d827f5da5b1).