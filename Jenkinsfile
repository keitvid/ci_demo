pipeline {
  agent any
  stages {
    stage('prepare_environment') {
      steps {
        echo 'build start'
        sh 'pip3 install -r ./test_environment/requirements.txt'
        sh 'python3 ./test_environment/create_data_sample.py'
      }
    }
    stage('build') {
      steps {
        sh 'echo $WORKSPACE'
      }
    }
    stage('test') {
      steps {
        sh 'echo test'
      }
    }
  }
  environment {
    LD_LIBRARY_PATH = '/opt/oracle/instantclient_18_3'
  }
}