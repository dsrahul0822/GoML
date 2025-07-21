import streamlit as st
import pandas as pd

st.title("Step 1: Load Employee Salary Data")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['data'] = df
    st.success("File uploaded and data loaded into session.")
    st.write("Preview of the Data:")
    st.dataframe(df.head())
