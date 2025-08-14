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
                scripts{  
                    bat "docker build -t django-todo-jenkins:latesr ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script{
                    bat "docker run -d -p 8003:8000 django-todo-jenkins:latest"
                }
            }
        }

    }
}
