pipeline {
    agent any

    stages {
        stage('Instalar dependencias') {
            steps {
                sh 'pip install -r requirements.txt || true'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest test_calculadora.py'
            }
        }
    }
}
