# AI-Powered Banking Fraud Detection & Analytics Platform

## Overview

This project is an end-to-end Banking Fraud Detection & Analytics Platform designed using Data Engineering, Machine Learning, Big Data Analytics, and Deployment technologies.

The system simulates banking transactions, stores them in MySQL, performs fraud analytics using Python and Spark, trains machine learning models for fraud prediction, and deploys a real-time fraud detection API and dashboard.

---

# Tech Stack

## Programming & Data Processing

* Python
* Pandas
* NumPy

## Database

* MySQL

## Data Visualization

* Matplotlib
* Seaborn
* Plotly

## Machine Learning

* Scikit-learn
* XGBoost
* Spark MLlib

## Big Data & Cloud Analytics

* Databricks
* Apache Spark

## Deployment & Dashboard

* Flask API
* Streamlit Dashboard

## Version Control

* Git
* GitHub

---

# Project Architecture

```text
Transaction Generator
        ↓
MySQL Database
        ↓
CSV Export Pipeline
        ↓
Google Colab EDA + ML
        ↓
Databricks Spark Analytics
        ↓
Saved ML Model (.pkl)
        ↓
Flask Fraud Prediction API
        ↓
Streamlit Real-Time Dashboard
```

---

# Features

* Generated 5000+ synthetic banking transactions
* Built ETL workflows using Python and MySQL
* Performed Exploratory Data Analysis (EDA)
* Conducted fraud trend and risk analysis
* Trained Random Forest and XGBoost fraud detection models
* Implemented Spark-based analytics using Databricks
* Developed Flask REST API for fraud prediction
* Created Streamlit dashboard for fraud monitoring
* Added Spark MLlib distributed machine learning workflows

---

# Folder Structure

```text
banking-fraud-detection-pipeline/
│
├── api/
│   └── app.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── banking_transactions.csv
│
├── database/
│   └── schema.sql
│
├── databricks/
│   └── spark_mllib_model.ipynb
│
├── models/
│   └── fraud_model.pkl
│
├── notebooks/
│   ├── 01_EDA_and_ML.ipynb
│   └── 02_Advanced_ML.ipynb
│
├── scripts/
│   ├── generate_transactions.py
│   └── export_to_csv.py
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Database Schema

## Transactions Table

Stores generated banking transaction data.

## Fraud Predictions Table

Stores ML/API fraud prediction outputs.

## Model Logs Table

Stores model performance metrics and training logs.

---

# Machine Learning Models

The following models were implemented:

* Random Forest Classifier
* XGBoost Classifier
* Spark MLlib Random Forest

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC
* Confusion Matrix

---

# Databricks Spark Analytics

Implemented:

* Spark SQL analytics
* Fraud aggregation queries
* Fraud risk analysis
* Feature engineering
* Spark MLlib model training

---

# Flask API

The Flask API provides:

* Real-time fraud prediction
* Fraud probability scoring
* Risk level classification

API Routes:

* `/`
* `/test`
* `/predict`

---

# Streamlit Dashboard

The Streamlit dashboard provides:

* Fraud KPI monitoring
* Fraud trend analysis
* Transaction visualizations
* High-risk transaction monitoring
* Interactive analytics

---

# How to Run the Project

## 1. Clone Repository

```bash
git clone https://github.com/your-username/banking-fraud-detection-pipeline.git
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Run Flask API

```bash
python api/app.py
```

## 6. Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

# Future Enhancements

* Kafka real-time streaming
* Docker deployment
* Cloud hosting
* Power BI dashboard integration
* User authentication
* Real-time alert system
* Advanced deep learning fraud detection

---

# Screenshots

Add project screenshots inside the `screenshots/` folder.

Recommended screenshots:

* Streamlit Dashboard
* Flask API Output
* Databricks Analytics
* Google Colab ML Notebook
* MySQL Tables

---

# Author

TRIDIB DAS

GitHub:
https://github.com/tridibd136-das

LinkedIn:
www.linkedin.com/in/tridib-das-a8064627b

