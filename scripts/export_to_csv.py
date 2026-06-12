import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="banking_fraud_db"
)

query = "SELECT * FROM transactions"

df = pd.read_sql(query, db)

df.to_csv("data/banking_transactions.csv", index=False)

db.close()

print("Data exported successfully to data/banking_transactions.csv")
print(df.head())