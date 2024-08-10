# tabs/product_sales.py

import streamlit as st
import pandas as pd

def display_product_sales(filtered_data):
    st.header("Daily Sales for Each Product")

    if filtered_data.empty:
        st.write("No data to display.")
        return

    # Provide a unique key for the radio button widget
    analysis_type = st.radio(
        "Select Analysis Type",
        ('Quantity', 'Subtotal'),
        key="product_sales_analysis_type"
    )

    # Group by Date and Product, then calculate sum for either Quantity or Subtotal
    if analysis_type == 'Quantity':
        # Assuming the column for quantity is 'Order Lines/Quantity'
        sales_data = filtered_data.groupby(['Date', 'Order Lines/Product/Display Name'])['Order Lines/Quantity'].sum().reset_index(name='Total Quantity')
        column_to_display = 'Total Quantity'
        st.subheader("Daily Sales in Terms of Quantity for Each Product")
    else:
        sales_data = filtered_data.groupby(['Date', 'Order Lines/Product/Display Name'])['Order Lines/Subtotal'].sum().reset_index(name='Total Subtotal')
        column_to_display = 'Total Subtotal'
        st.subheader("Daily Sales in Terms of Subtotal for Each Product")

    # Display the data in a table format
    st.write("Daily Sales Data for Each Product")
    st.dataframe(sales_data)

    # Display the data in a line graph for each product
    st.write("Daily Sales Trend for Each Product")
    products = sales_data['Order Lines/Product/Display Name'].unique()
    for product in products:
        product_data = sales_data[sales_data['Order Lines/Product/Display Name'] == product]
        st.write(f"Sales Trend for {product}")
        st.line_chart(product_data.set_index('Date')[column_to_display])
