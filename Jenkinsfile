pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/shamanth-shivakumar/shamanth-s.git'
            }
        }

        stage('Build User Service Image') {
            steps {
                sh 'docker build -t user-service ./user-service'
            }
        }

        stage('Build Order Service Image') {
            steps {
                sh 'docker build -t order-service ./order-service'
            }
        }

        stage('Build Payment Service Image') {
            steps {
                sh 'docker build -t payment-service ./payment-service'
            }
        }

    }
}

