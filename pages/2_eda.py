import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Step 2: Exploratory Data Analysis (EDA)")

# Check if data is loaded in session state
if 'data' in st.session_state:
    df = st.session_state['data']
    st.write("📊 Data Preview:")
    st.dataframe(df.head())

    # Show scatter plot
    st.subheader("📈 Scatter Plot: Experience vs Salary")
    
    x_col = st.selectbox("Select X-axis (Independent Variable):", df.columns, index=0)
    y_col = st.selectbox("Select Y-axis (Dependent Variable):", df.columns, index=1)

    fig, ax = plt.subplots()
    ax.scatter(df[x_col], df[y_col], color='green')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(f"{y_col} vs {x_col}")
    st.pyplot(fig)
else:
    st.warning("Please load the data first from 'Step 1: Load Data'.")
