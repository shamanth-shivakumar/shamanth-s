pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/shamanth-shivakumar/shamanth-s.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker build -t shamanth/user-service ./user-service'
                sh 'docker build -t shamanth/order-service ./order-service'
                sh 'docker build -t shamanth/payment-service ./payment-service'
            }
        }

        stage('Push Docker Images') {
            steps {
                sh 'docker push shamanth/user-service:latest'
                sh 'docker push shamanth/order-service:latest'
                sh 'docker push shamanth/payment-service:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }

    }
}
