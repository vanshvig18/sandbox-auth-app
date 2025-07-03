import streamlit as st
import pandas as pd
from utils.file_handler import handle_uploaded_file

st.title("📤 Document Uploader & Preview")

uploaded_files = st.file_uploader(
    "Upload your documents (.txt, .csv, .xlsx, .mdv)", 
    type=['txt', 'csv', 'xlsx', 'mdv'], 
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.subheader(f"Preview: {uploaded_file.name}")
        content = handle_uploaded_file(uploaded_file)
        st.write(content)
