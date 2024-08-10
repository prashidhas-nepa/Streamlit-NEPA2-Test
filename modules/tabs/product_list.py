# tabs/product_list.py

import streamlit as st
import pandas as pd

def display_daily_transactions(filtered_data, search_query):
    st.header("Daily Transactions of Searched Customers")
    if not filtered_data.empty:
        st.write(f"Showing daily transactions for customers matching '{search_query}':")
        
        # Group by Customer and Date, and then count the number of transactions
        daily_transactions = filtered_data.groupby(['Customer', 'Date']).size().reset_index(name='Transaction Count')
        
        # Display the daily transactions in a table format
        st.dataframe(daily_transactions)
    else:
        st.write("No transactions found for the searched customers.")
