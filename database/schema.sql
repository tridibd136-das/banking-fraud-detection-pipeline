CREATE DATABASE banking_fraud_db;

USE banking_fraud_db;

CREATE TABLE raw_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id VARCHAR(50),
    customer_id VARCHAR(50),
    transaction_amount FLOAT,
    transaction_type VARCHAR(50),
    location VARCHAR(100),
    device_type VARCHAR(50),
    account_balance FLOAT,
    transaction_time DATETIME,
    is_fraud INT
);

USE banking_fraud_db;

CREATE TABLE fraud_predictions (
    prediction_id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id VARCHAR(100),
    customer_id VARCHAR(50),
    transaction_amount FLOAT,
    transaction_type VARCHAR(50),
    location VARCHAR(100),
    device_type VARCHAR(50),
    account_balance FLOAT,
    actual_fraud INT,
    predicted_fraud INT,
    fraud_probability FLOAT,
    risk_level VARCHAR(20),
    prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE model_logs (
    model_id INT AUTO_INCREMENT PRIMARY KEY,
    model_name VARCHAR(100),
    accuracy FLOAT,
    precision_score FLOAT,
    recall_score FLOAT,
    f1_score FLOAT,
    roc_auc FLOAT,
    trained_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);