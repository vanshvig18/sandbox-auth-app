import streamlit as st
from utils.template_engine import generate_document

st.title("📑 Template-Based Document Generator")

template_option = st.selectbox(
    "Choose Template Type",
    ["ML Documentation", "SAR Repository"]
)

st.markdown("### Fill in Required Data")
project_name = st.text_input("Project Name")
author = st.text_input("Author Name")
description = st.text_area("Project Description")

if st.button("Generate Document"):
    output = generate_document(template_option, {
        "project_name": project_name,
        "author": author,
        "description": description
    })
    st.success("Document Generated Successfully!")
    st.download_button("Download Document", data=output, file_name="generated_doc.txt")
    st.markdown("### Preview")
    st.code(output)
