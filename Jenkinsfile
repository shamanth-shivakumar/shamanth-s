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
                sh '''
                docker build -t shamanth0411/user-service:latest ./user-service
                docker build -t shamanth0411/order-service:latest ./order-service
                docker build -t shamanth0411/payment-service:latest ./payment-service
                '''
            }
        }

        stage('Push Docker Images') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                    echo $PASS | docker login -u $USER --password-stdin

                    docker push shamanth0411/user-service:latest
                    docker push shamanth0411/order-service:latest
                    docker push shamanth0411/payment-service:latest
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s/
                '''
            }
        }
    }
}}
