pipeline {
  agent any
  stages {
    stage('prepare_environment') {
      steps {
        echo 'build start'
        sh 'python3 ./test_environment/create_data_sample.py'
        sh '$PATH'
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
}