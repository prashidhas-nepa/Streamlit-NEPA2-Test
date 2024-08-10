# import streamlit as st

# def get_selected_files(file_names):
#     st.sidebar.title("Select Files to Load")
#     selected_files = [file_name for file_name in file_names if st.sidebar.checkbox(file_name)]
#     return selected_files


# modules/sidebar.py

import os
import streamlit as st

def get_selected_files():
    # Get the data directory from environment variables
    data_dir = os.getenv('DATA_PATH')
    
    # Check if the data directory exists
    if not os.path.exists(data_dir):
        st.error("Data directory does not exist.")
        return []
    
    # List all files in the data directory (e.g., .xlsx files)
    available_files = sorted([f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f)) and f.endswith('.xlsx')])
    
    # Allow the user to select files from the available files
    selected_files = st.sidebar.multiselect(
        "Select Data Files to Load",
        options=available_files,
        default=[]  # No files are selected by default
    )
    
    return selected_files
