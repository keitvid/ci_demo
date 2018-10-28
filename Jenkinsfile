pipeline {
  agent any
  stages {
    stage('Setup Oracle') {
      steps {
        echo 'build start'
        sh 'pip3 install -r ./test_environment/requirements.txt'
        sh 'python3 ./test_environment/create_data_sample.py'
      }
    }
    stage('Run DAGs') {
      steps {
        sh 'airflow trigger_dag  dump_employees'
      }
    }
    stage('Test \'employees\' db') {
      steps {
        sh 'python3 ./tests/test_employees.py'
      }
    }
    stage('Deploy') {
      when {
        tag 'release-*'
      }
      steps {
        sh 'echo deployed'
      }
    }
  }
  environment {
    LD_LIBRARY_PATH = '/opt/oracle/instantclient_18_3'
    PATH = '/home/kirill/bin:/home/kirill/.local/bin:/home/kirill/bin:/home/kirill/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin'
  }
}