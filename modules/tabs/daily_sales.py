# tabs/daily_sales.py

import streamlit as st
import pandas as pd

def display_daily_sales(filtered_data):
    st.header("Daily Sales Analysis")

    if filtered_data.empty:
        st.write("No data to display.")
        return

    # Option to select based on Quantity or Subtotal
    analysis_type = st.radio(
        "Select Analysis Type",
        ('Quantity', 'Subtotal')
    )

    # Group by Date and calculate sum
    if analysis_type == 'Quantity':
        sales_data = filtered_data.groupby('Date').size().reset_index(name='Total Quantity')
        column_to_display = 'Total Quantity'
        st.subheader("Daily Sales in Terms of Quantity")
    else:
        sales_data = filtered_data.groupby('Date')['Order Lines/Subtotal'].sum().reset_index(name='Total Subtotal')
        column_to_display = 'Total Subtotal'
        st.subheader("Daily Sales in Terms of Subtotal")

    # Display the data in a table format
    st.write("Daily Sales Data")
    st.dataframe(sales_data)

    # Display the data in a line graph
    st.write("Daily Sales Trend")
    st.line_chart(sales_data.set_index('Date')[column_to_display])
