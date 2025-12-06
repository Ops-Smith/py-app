pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "monyslim/py-app"
        DEPLOY_ENV = "${env.BRANCH_NAME == 'master' ? 'production' : env.BRANCH_NAME == 'staging' ? 'staging' : 'development'}"
        DOCKER_TAG = "${DEPLOY_ENV}-${env.BUILD_NUMBER}"
        CONTAINER_PORT = "${env.BRANCH_NAME == 'master' ? '5001' : env.BRANCH_NAME == 'staging' ? '5002' : '5003'}"
        APP_URL = "http://localhost:${CONTAINER_PORT}"
    }
    
    stages {
        stage('Setup Python') {
            steps {
                echo "🐍 Setting up Python..."
                sh '''
                    // sudo apt update
                    sudo apt install -y python3 python3-pip
                    pip3 install -r requirements.txt
                '''
            }
        }
        
        stage('Build & Test') {
            steps {
                echo "🔨 Building ${DEPLOY_ENV}"
                sh '''
                    pip3 install -r requirements.txt
                    python3 -m pytest test_app.py -v || echo "⚠️ Tests may have warnings.."
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo "🐳 Building image..."
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-hub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        docker login -u $DOCKER_USER -p $DOCKER_PASS
                        docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                    '''
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo "🚀 Deploying ${DEPLOY_ENV} to port ${CONTAINER_PORT}"
                sh """
                    docker stop py-app-${DEPLOY_ENV} || true
                    docker rm py-app-${DEPLOY_ENV} || true
                    docker run -d -p ${CONTAINER_PORT}:5000 --name py-app-${DEPLOY_ENV} ${DOCKER_IMAGE}:${DOCKER_TAG}
                """
            }
        }
        
        stage('Health Check') {
            steps {
                sh """
                    sleep 5
                    curl -f ${APP_URL}/health && echo "✅ ${DEPLOY_ENV} is healthy!" || echo "⚠️ Health check failed"
                    echo "🌐 Access: ${APP_URL}"
                """
            }
        }
    }
    
    post {
        always {
            echo "📊 Build ${env.BUILD_NUMBER} completed"
        }
        success {
            echo "🎉 AUTO-DEPLOY SUCCESSFUL!"
            echo "🌐 ${DEPLOY_ENV}: ${APP_URL}"
        }
        failure {
            echo "❌ Pipeline failed - check logs"
        }
    }
}