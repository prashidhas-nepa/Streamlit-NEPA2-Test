import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from modules.config import load_config
from modules.data_loader import load_data
from modules.sidebar import get_selected_files
from modules.multiple_tabs import multiple_tabs
from modules.tabs.top_products import display_top_products
from modules.tabs.product_list import display_daily_transactions
from modules.tabs import product_list, top_products, daily_sales, daily_product_sales

# Load environment variables from .env file
load_dotenv()

def main():
    st.title("Data Ingestion App")

    # Load configuration
    config_file = "config.yaml"
    config = load_config(config_file)

    # Get data directory from environment variables
    data_dir = os.getenv('DATA_PATH')
    if not data_dir:
        st.error("DATA_PATH environment variable is not set.")
        return

    # Sidebar with multiple sections/pages
    page = st.sidebar.selectbox(
        "Select Section",
        ["Marketing", "Salesperson", "Inventory Management"]
    )

    if page == "Marketing":
        st.sidebar.header("Marketing Tools")
        # Add marketing-related options or tools
        st.sidebar.write("Add your marketing tools or options here.")
        # Example: Add more filters specific to marketing

    elif page == "Salesperson":
        st.sidebar.header("Salesperson Tools")
        # Add salesperson-related options or tools
        st.sidebar.write("Add your salesperson tools or options here.")
        # Example: Add more filters specific to sales

    elif page == "Inventory Management":
        st.sidebar.header("Inventory Management Tools")
        # Add inventory-related options or tools
        st.sidebar.write("Add your inventory management tools or options here.")
        # Example: Add more filters specific to inventory management

    # Automatically get selected files from the directory
    selected_files = get_selected_files()

    if selected_files:
        # Load data based on selected files
        if 'data_frames' not in st.session_state:
            st.session_state['data_frames'] = load_data(data_dir, selected_files)

        data_frames = st.session_state['data_frames']

        # Collect unique customer names
        unique_customers = set()
        for file_name, info in data_frames.items():
            if 'data' in info:
                if 'Customer' in info['data'].columns:
                    unique_customers.update(info['data']['Customer'].unique())

        # Filter out non-string values and sort the customer names
        unique_customers = sorted([customer for customer in unique_customers if isinstance(customer, str)])

        # Sidebar search functionality
        st.sidebar.header("Search and Filter")

        # Search Customers
        search_query = st.sidebar.text_input("Search Customers")
        filtered_data = pd.DataFrame()
        if search_query:
            search_results = [customer for customer in unique_customers if search_query.lower() in customer.lower()]
            st.sidebar.write("Search Results:")
            for customer in search_results:
                st.sidebar.write(customer)
                
            # Filter data by searched customers
            for file_name, info in data_frames.items():
                if 'data' in info:
                    customer_filtered = info['data'][info['data']['Customer'].isin(search_results)]
                    filtered_data = pd.concat([filtered_data, customer_filtered])

        # Date range filtering
        st.sidebar.header("Filter by Date")
        for file_name, info in data_frames.items():
            if 'data' in info:
                min_date = info['data']['Date'].min().date()
                max_date = info['data']['Date'].max().date()
                start_date = st.sidebar.date_input(
                    f"Start Date {file_name}", 
                    value=min_date, 
                    min_value=min_date, 
                    max_value=max_date, 
                    key=f'start_{file_name}'
                )
                end_date = st.sidebar.date_input(
                    f"End Date {file_name}", 
                    value=max_date, 
                    min_value=min_date, 
                    max_value=max_date, 
                    key=f'end_{file_name}'
                )
                
                if st.sidebar.button(f"Filter Data for {file_name}"):
                    # Ensure end_date includes the entire day
                    end_date = pd.to_datetime(end_date) + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)
                    filtered_data = filter_data(filtered_data, start_date, end_date)
                    st.session_state[f'filtered_data_{file_name}'] = filtered_data

        # Main content tabs
        tab1, tab2, tab3, tab4 = st.tabs(["Daily Transactions", "Top 10 Products", "Daily Sales", "Daily Sales per Product"])

        with tab1:
            product_list.display_daily_transactions(filtered_data, search_query)

        with tab2:
            top_products.display_top_products(filtered_data)

        with tab3:
            daily_sales.display_daily_sales(filtered_data)

        with tab4:
            product_sales.display_product_sales(filtered_data)

def filter_data(data, start_date, end_date):
    mask = (data['Date'] >= pd.to_datetime(start_date)) & (data['Date'] <= pd.to_datetime(end_date))
    return data[mask]

if __name__ == "__main__":
    main()