pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                bat "python -m venv venv"
                bat "call venv/scripts/activate && pip install -r requirements.txt"
                bat "call venv/scripts/activate && python manage.py migrate"
                bat "call venv/scripts/activate && python manage.py collectstatic --noinput"
               
            }
        }
        stage('Test') {
            steps {
                
                
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat "docker build -t django-todo-jenkins:latest ."
            }
        }

        stage('Run Docker Container') {
            steps {
                bat """
                   docker stop django-todo-container || exit 0
                   docker rm django-todo-container || exit 0
                   docker run -d -p 8003:8000 --name django-todo-container django-todo-jenkins:latest 
                """
            }
        }

    }
}
