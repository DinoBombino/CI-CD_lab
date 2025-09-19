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
                //bat 'python test-main.py'
                // bat '"C:\Users\Dmitriy\AppData\Local\Programs\Python\Python312\" test-main.py'
                bat '"C:\\Users\\Dmitriy\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" test-main.py'
            }
        }
        stage('Deploy (CD)') {
            // when {
            //     branch 'main'  
            // }
            steps {
                // echo 'Deploying to production...'  

                // bat 'pip install pyinstaller'  // Установка, если нет (Jenkins может кэшировать)
                // bat 'pyinstaller --onefile --name calc-app main.py'  // Генерация exe (--onefile = один файл)
                // bat 'mkdir production'  // Создай папку, если нет
                // bat 'copy dist\\calc-app.exe production\\'  // Копируем exe в "production" (деплой)
                // echo 'Deploy successful: calc-app.exe deployed to production folder!'

                bat 'pip install pyinstaller'  // Устанавливаем PyInstaller
                bat '"C:\\Users\\Dmitriy\\AppData\\Local\\Programs\\Python\\Python312\\pyinstaller.exe" --onefile --name calc-app main.py'
                bat 'mkdir production || echo "Directory exists"'  // Создаём папку, игнорируем ошибку если есть
                bat 'copy dist\\calc-app.exe production\\'
                echo 'Deploy successful: calc-app.exe deployed to production folder!'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished'
        }
    }
}