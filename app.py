import streamlit as st

st.set_page_config(
    page_title="Salary Prediction App",
    page_icon="💼",
    layout="centered"
)

st.title("💼 Salary Prediction App")

st.markdown("""
Welcome to the **Salary Prediction App** built with Streamlit!

This app allows you to:
1. Load and preview salary dataset
2. Explore the data visually
3. Train a machine learning model
4. Predict salary based on experience

👉 Use the sidebar to navigate through the steps.
""")
