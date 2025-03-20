pipeline {
    agent
    stages {
        stage('Checkout to correct Branch') {
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
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}