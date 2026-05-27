# Interview Analytics Platform using PySpark, AWS EC2, Jenkins CI/CD and Streamlit

## Project Overview

The Interview Analytics Platform is a cloud-based analytics application developed to analyze interview performance data using distributed processing and interactive dashboard visualization.

The project combines **PySpark**, **Streamlit**, **AWS EC2**, **Jenkins CI/CD**, and **GitHub** to demonstrate modern Big Data, Cloud Computing, and DevOps practices.

The platform provides analytics dashboards, KPI insights, deployment automation, and cloud hosting.

---

## Features

- Interactive Analytics Dashboard
- KPI Metrics Visualization
- PySpark Data Processing
- Streamlit User Interface
- AWS Cloud Deployment
- Jenkins CI/CD Pipeline
- GitHub Version Control Integration
- Automated Deployment Workflow

---

## Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Development |
| PySpark | Distributed Analytics |
| Streamlit | Dashboard UI |
| AWS EC2 | Cloud Deployment |
| Jenkins | CI/CD Automation |
| GitHub | Source Control |
| Git | Version Management |

---

## System Architecture

```txt
Developer
   ↓
VS Code Development
   ↓
GitHub Repository
   ↓
Jenkins CI/CD Pipeline
   ↓
AWS EC2 Deployment
   ↓
PySpark Analytics Engine
   ↓
Streamlit Dashboard
   ↓
End User
```

---

## Project Structure

```txt
interview-analytics-pyspark/
│
├── app.py
├── requirements.txt
├── Jenkinsfile
├── README.md
├── dataset/
└── screenshots/
```

---

## Installation & Setup

### Clone Repository

```bash
git clone https://github.com/MehakGupta1725/interview-analytics-pyspark.git
```

### Navigate to Project

```bash
cd interview-analytics-pyspark
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running Application

Start Streamlit server:

```bash
streamlit run app.py
```

Application runs on:

```txt
http://localhost:8501
```

---

## AWS Deployment

Application deployed using:

- AWS EC2
- Amazon Linux
- Python Virtual Environment
- Streamlit Server

Deployment Steps:

1. Launch EC2 Instance
2. Install Dependencies
3. Clone GitHub Repository
4. Configure Environment
5. Run Streamlit Application

---

## Jenkins CI/CD Workflow

The project uses Jenkins automation for deployment.

Pipeline Flow:

```txt
Code Change
    ↓
Git Push
    ↓
GitHub Repository
    ↓
Jenkins Build Trigger
    ↓
Dependency Installation
    ↓
AWS EC2 Deployment
    ↓
Live Application Update
```

---



## Future Scope

- Real-time Analytics Processing
- Machine Learning Integration
- Enhanced Security Features
- Docker Container Deployment
- Multi-User Support

---

## Author

**Mehak Gupta**

B.E Computer Science Engineering

Cloud Computing & DevOps Project