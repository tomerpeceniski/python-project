pipeline {
    agent any

    environment {
        TMPDIR = '/var/tmp'
        EC2_HOST = "ec2-user@18.212.53.114"
        APP_DIR = "/home/ec2-user/flask-ci-app"
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Deploy to EC2') {
            when {
                branch 'main'
            }
            steps {
                sshagent(['ec2-ssh-key']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no $EC2_HOST '
                            cd $APP_DIR &&
                            git pull origin main &&
                            docker build -t flask-ci-app . &&
                            docker stop flask-container || true &&
                            docker rm flask-container || true &&
                            docker run -d --name flask-container -p 5000:5000 flask-ci-app
                        '
                    """
                }
            }
        }
    }
}
