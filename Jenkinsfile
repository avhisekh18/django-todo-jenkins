pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
        stage('Build Docker Image'){
            steps {
                bat 'docker run -d -p 8002:8000 myapp:%BUILD_NUMBER%'
            }
        }
    }
}
