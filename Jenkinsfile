pipeline {
  agent any
  stages {
    stage('prepare_environment') {
      steps {
        echo 'build start'
        sh 'echo hello'
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