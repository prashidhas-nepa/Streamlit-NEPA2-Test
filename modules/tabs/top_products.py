# tabs/top_products.py

import streamlit as st

def display_top_products(filtered_data):
    st.header("Top 10 Products Purchased by Searched Customers")
    if not filtered_data.empty:
        top_products = filtered_data['Order Lines/Product/Display Name'].value_counts().head(10)
        st.bar_chart(top_products)
    else:
        st.write("No data to display.")
