import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="banking_fraud_db"
)

cursor = db.cursor()

transaction_types = ["ATM Withdrawal", "Online Transfer", "POS Payment", "UPI Payment", "Card Payment"]
locations = ["Kolkata", "Delhi", "Mumbai", "Bangalore", "Chennai", "Hyderabad", "Pune"]
devices = ["Mobile", "Desktop", "ATM", "POS Machine", "Tablet"]

insert_query = """
INSERT INTO transactions (
    transaction_id, customer_id, transaction_amount, transaction_type,
    location, device_type, account_balance, transaction_time, is_fraud
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for i in range(5000):
    amount = round(random.uniform(100, 150000), 2)
    balance = round(random.uniform(1000, 300000), 2)
    transaction_time = fake.date_time_between(start_date="-90d", end_date="now")

    is_fraud = 1 if (
        amount > 90000 or
        balance < amount or
        random.random() < 0.07
    ) else 0

    values = (
        fake.uuid4(),
        "CUST" + str(random.randint(1000, 9999)),
        amount,
        random.choice(transaction_types),
        random.choice(locations),
        random.choice(devices),
        balance,
        transaction_time,
        is_fraud
    )

    cursor.execute(insert_query, values)

db.commit()
cursor.close()
db.close()

print("5000 banking transactions inserted successfully.")