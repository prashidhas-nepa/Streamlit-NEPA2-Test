import pandas as pd
import os
import streamlit as st

def load_data(data_dir, selected_files):
    data_frames = {}
    for file_name in selected_files:
        file_path = os.path.join(data_dir, file_name)
        st.write(f"Loading file: {file_path}")
        if os.path.exists(file_path):
            data = pd.read_excel(file_path)
            empty_rows_percentage = data.isnull().mean() * 100
            data_types = data.dtypes
            
            # Combine empty rows percentage and data types into one DataFrame
            analysis_df = pd.DataFrame({
                'Empty Rows Percentage': empty_rows_percentage,
                'Data Type': data_types
            })
            
            data_frames[file_name] = {
                'data': data,
                'analysis': analysis_df
            }
        else:
            st.error(f"Data file not found: {file_path}")
    return data_frames
