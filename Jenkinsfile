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