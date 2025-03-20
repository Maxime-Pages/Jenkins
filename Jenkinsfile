pipeline {
    agent none
    stages {
        stage('Checkout to correct Branch') {
            agent any
            steps {
                git branch 'dev', url: 'https://github.com/Maxime-Pages/Jenkins'
            }
        }
        stage('Build Backend') {
            agent {
                label 'jpydock'
            }
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            agent any
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            agent any
            steps {
                echo 'Deploying....'
            }
        }
    }
}