import streamlit as st

def get_selected_files(file_names):
    st.sidebar.title("Select Files to Load")
    selected_files = [file_name for file_name in file_names if st.sidebar.checkbox(file_name)]
    return selected_files
