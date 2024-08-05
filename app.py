import streamlit as st
import os
from dotenv import load_dotenv
from modules.config import load_config
from modules.data_loader import load_data
from modules.sidebar import get_selected_files

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
    
    # Get selected files from sidebar
    selected_files = get_selected_files(config['file_names'])
    
    if selected_files:
        # Load data based on selected files
        data_frames = load_data(data_dir, selected_files)
        
        # Display each dataframe and its analysis
        if data_frames:
            st.write("Data Loaded Successfully")
            for file_name, info in data_frames.items():
                st.subheader(f"Data from {file_name}")
                st.dataframe(info['data'])
                
                st.write("Data Analysis:")
                st.dataframe(info['analysis'])
        else:
            st.write("No data to display")
    else:
        st.write("No files selected")

if __name__ == "__main__":
    main()