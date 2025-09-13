pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/твой_юзернейм/ci-cd-lab.git', branch: env.BRANCH_NAME
            }
        }
        stage('Test (CI)') {
            steps {
                sh 'python3 test_main.py'  // Запуск тестов. Для Windows: bat 'python test_main.py'
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