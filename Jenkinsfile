pipeline {
    agent any

    tools {
        allure 'Allure'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/swethagandham2003/note_automation_framework_one.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Pytest with Allure') {
            steps {
                bat 'python -m pytest -v --html=report.html --self-contained-html --alluredir=allure-results'
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure(
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                )
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

            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
        }

        success {
            echo 'Pipeline Success'
        }

        failure {
            echo 'Pipeline Failed'
        }
    }
}