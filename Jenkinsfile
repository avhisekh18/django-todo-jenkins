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
        stage('Build Docker Image') {
            steps {
                bat "docker build -t django-todo-jenkins:${env.BUILD_NUMBER} ."
            }
        }

        stage('Run Docker Container') {
            steps {
                bat "docker run -d -p 8002:8000 django-todo-jenkins:${env.BUILD_NUMBER}"
            }
        }

    }
}
