pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/swethagandham2003/note_automation_framework.git'
            }
        }

        stage('Install Dependencies') {
            steps {
        git branch: 'main',
        url: 'https://github.com/swethagandham2003/note_automation_framework.git'
        }

        stage('Run Pytest') {
            steps {
                bat 'pytest tests/ --html=report.html --self-contained-html'
            }
        }

        stage('Generate Allure Results') {
            steps {
                bat 'pytest tests/ --alluredir=allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

    post {

        always {

            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report'
            ])
        }

        success {
            echo 'CI/CD Pipeline Executed Successfully'
        }

        failure {
            echo 'Pipeline Failed'
        }
    }
}