pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'python3 -m pytest tests/ -v'
            }
        }
    }
}
