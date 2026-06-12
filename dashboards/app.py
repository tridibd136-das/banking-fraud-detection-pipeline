import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

st.set_page_config(
    page_title="Banking Fraud Analytics Dashboard",
    layout="wide"
)

st.title("Banking Fraud Analytics Dashboard")

@st.cache_data
def load_data():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="banking_fraud_db"
    )

    query = "SELECT * FROM transactions"
    df = pd.read_sql(query, db)
    db.close()
    return df

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())

total_transactions = len(df)
fraud_count = df["is_fraud"].sum()
non_fraud_count = total_transactions - fraud_count
fraud_rate = round((fraud_count / total_transactions) * 100, 2)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Transactions", total_transactions)
col2.metric("Fraud Transactions", int(fraud_count))
col3.metric("Non-Fraud Transactions", int(non_fraud_count))
col4.metric("Fraud Rate", f"{fraud_rate}%")

st.divider()

col5, col6 = st.columns(2)

with col5:
    fig1 = px.histogram(
        df,
        x="is_fraud",
        title="Fraud vs Non-Fraud Transactions"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col6:
    fig2 = px.histogram(
        df,
        x="transaction_amount",
        color="is_fraud",
        title="Transaction Amount Distribution"
    )
    st.plotly_chart(fig2, use_container_width=True)

col7, col8 = st.columns(2)

with col7:
    fraud_by_type = df.groupby("transaction_type")["is_fraud"].sum().reset_index()

    fig3 = px.bar(
        fraud_by_type,
        x="transaction_type",
        y="is_fraud",
        title="Fraud Count by Transaction Type"
    )
    st.plotly_chart(fig3, use_container_width=True)

with col8:
    fraud_by_device = df.groupby("device_type")["is_fraud"].sum().reset_index()

    fig4 = px.bar(
        fraud_by_device,
        x="device_type",
        y="is_fraud",
        title="Fraud Count by Device Type"
    )
    st.plotly_chart(fig4, use_container_width=True)

fraud_by_location = df.groupby("location")["is_fraud"].sum().reset_index()

fig5 = px.bar(
    fraud_by_location,
    x="location",
    y="is_fraud",
    title="Fraud Count by Location"
)

st.plotly_chart(fig5, use_container_width=True)

st.subheader("High-Risk Transactions")

high_risk_df = df[
    (df["transaction_amount"] > 90000) |
    (df["account_balance"] < df["transaction_amount"]) |
    (df["is_fraud"] == 1)
]

st.dataframe(high_risk_df)