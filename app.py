import streamlit as st
import pandas as pd
import os
from datetime import date

CSV_FILE = "expenses.csv"

st.set_page_config(page_title="Smart Expense Tracker", page_icon="💰")
st.title("💰 Smart Expense Tracker + Fraud Detector")
st.write("Auto alert if amount > Rs. 4000")

with st.form("expense_form"):
    exp_date = st.date_input("Date", value=date.today())
    category = st.selectbox("Category", ["Food", "Travel", "Bills", "Shopping", "Other"])
    amount = st.number_input("Amount (Rs.)", min_value=1)
    desc = st.text_input("Description")
    submitted = st.form_submit_button("Add Expense")
    if submitted:
        if amount > 4000:
            st.error(f"🚨 FRAUD ALERT! Rs. {amount}")
        else:
            st.success("Expense Added!")
        new_data = pd.DataFrame([[exp_date, category, amount, desc]], columns=["Date","Category","Amount","Description"])
        if os.path.exists(CSV_FILE):
            new_data.to_csv(CSV_FILE, mode='a', header=False, index=False)
        else:
            new_data.to_csv(CSV_FILE, index=False)
