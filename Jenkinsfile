pipeline {
    agent none
    stages {
        stage('Checkout to correct Branch') {
            agent any
            steps {
                git branch: 'dev', url: 'https://github.com/Maxime-Pages/Jenkins'
                sh 'ls -R ${WORKSPACE}'
                stash name: 'stuff', includes :'**'
            }
        }
        stage('Build Backend') {
            agent {
                label 'jpydock'
            }
            steps {
                unstash 'stuff'
                sh 'ls -R ${WORKSPACE}'
                sh 'pip install -r back/requirements.txt'
            }
        }
        stage('Test') {
            agent {
                label 'jpytest'
            }
            steps {
                unstash 'stuff'
                sh 'ls -R ${WORKSPACE}'
                sh 'pip install -r back/requirements.txt'
                sh 'pip install pytest'
                echo 'Testing..'
                sh 'pytest'
            }
        }
        stage('Deploy') {
            agent {
                label 'pyprod'
            }
            steps {
                unstash 'stuff'
                sh 'ls -R ${WORKSPACE}'
                sh 'pip install -r back/requirements.txt'
                echo 'Deploying..'
                sh 'python3 back/main.py'
            }
        }
    }
}