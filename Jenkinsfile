pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'pytest -v --html=report.html --self-contained-html'
            }
        }

        stage('Generate Allure Results') {
            steps {
                bat 'pytest --alluredir=allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat 'allure generate allure-results -o allure-report --clean'
            }
        }
    }

    post {

        always {
            publishHTML([
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report',
                keepAll: true,
                allowMissing: true,
                alwaysLinkToLastBuild: true
            ])
        }

        success {
            echo 'Pipeline Success'
        }

        failure {
            echo 'Pipeline Failed'
        }
    }
}