from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load(r"E:\banking-fraud-detection-pipeline\models\fraud_model.pkl")

FEATURE_COLUMNS = [
    "transaction_amount",
    "transaction_type",
    "location",
    "device_type",
    "account_balance"
]

@app.route("/")
def home():
    return """
    <h2>Banking Fraud Detection API is running</h2>
    <p>Open <a href="/test">/test</a> to test prediction in browser.</p>
    """

@app.route("/test", methods=["GET"])
def test_prediction():
    sample_data = {
        "transaction_amount": 120000,
        "transaction_type": 2,
        "location": 1,
        "device_type": 0,
        "account_balance": 50000
    }

    input_df = pd.DataFrame([sample_data], columns=FEATURE_COLUMNS)

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    risk_level = "High" if probability > 0.75 else "Medium" if probability > 0.40 else "Low"

    return jsonify({
        "sample_input": sample_data,
        "predicted_fraud": int(prediction),
        "fraud_probability": float(probability),
        "risk_level": risk_level
    })

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        sample_data = {
            "transaction_amount": 120000,
            "transaction_type": 2,
            "location": 1,
            "device_type": 0,
            "account_balance": 50000
        }
        data = sample_data
    else:
        data = request.get_json()

    input_df = pd.DataFrame([data], columns=FEATURE_COLUMNS)

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    risk_level = "High" if probability > 0.75 else "Medium" if probability > 0.40 else "Low"

    return jsonify({
        "input_data": data,
        "predicted_fraud": int(prediction),
        "fraud_probability": float(probability),
        "risk_level": risk_level
    })

if __name__ == "__main__":
    app.run(debug=True)