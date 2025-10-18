pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-credentials')  // ID из Jenkins
        IMAGE_NAME = 'brodyagaexe/calc-api'  // Замени на твой логин
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/DinoBombino/CI-CD_lab.git', branch: env.BRANCH_NAME
            }
        }
        stage('Build Docker (CI)') {
            steps {
                bat 'docker build -t calc-api .'
            }
        }
        stage('Test (CI)') {
            steps {
                bat 'docker run --rm calc-api pytest test_api.py -k test_functions'
            }
        }
        stage('Push Docker (CD)') {
            when { branch 'main' }
            steps {
                bat 'docker login -u %DOCKERHUB_CREDENTIALS_USR% -p %DOCKERHUB_CREDENTIALS_PSW%'
                bat 'docker tag calc-api %IMAGE_NAME%:latest'
                bat 'docker push %IMAGE_NAME%:latest'
            }
        }
        stage('Deploy (CD)') {
            when { branch 'main' }
            steps {
                bat 'docker-compose down || exit 0'  // Останавливаем старые контейнеры, если есть
                bat 'docker-compose up -d'
                echo 'Deploy successful: API running at http://localhost:5000'
            }
        }
    }
    post {
        always {
            bat 'docker-compose down || exit 0'  // Останавливаем контейнеры
            echo 'Pipeline finished'
        }
    }
}