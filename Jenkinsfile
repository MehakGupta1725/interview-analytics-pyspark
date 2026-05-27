pipeline {

    agent any

    stages {

        stage('Clone') {
            steps {
                git branch: 'main',
                url: 'https://github.com/MehakGupta1725/interview-analytics-pyspark.git'
            }
        }

        stage('Install Dependencies') {
            steps {

                sh '''
                python3.11 -m venv venv

                source venv/bin/activate

                pip install --upgrade pip

                pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy') {
            steps {

                sh '''
                pkill -f streamlit || true

                source venv/bin/activate

                nohup streamlit run app.py \
                --server.port 8501 \
                --server.address 0.0.0.0 &
                '''
            }
        }

    }

}