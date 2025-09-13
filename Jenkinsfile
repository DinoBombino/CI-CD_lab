pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/DinoBombino/CI-CD_lab.git', 
                branch: 'main'
            }
        }
        stage('Test (CI)') {
            steps {
                bat 'python test-main.py'
            }
        }
        stage('Deploy (CD)') {
            when {
                branch 'main'  // Только для main-ветки
            }
            steps {
                echo 'Deploying to production...'  // Симуляция деплоя
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished'
        }
    }
}