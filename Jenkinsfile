pipeline {
    agent any

    environment {
        IMAGE_NAME = "myapp:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/yourapp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Run Docker Container') {
            steps {
                bat """
                docker stop myapp || echo 'No container running'
                docker rm myapp || echo 'No container to remove'
                docker run -d --name myapp -p 8000:8000 %IMAGE_NAME%
                """
            }
        }
    }
}
