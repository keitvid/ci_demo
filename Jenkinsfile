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
        sh 'echo $WORKSPACE'
      }
    }
    stage('Test \'employees\' db') {
      steps {
        sh 'python3 ./tests/test_empoyees.py'
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
  }
}