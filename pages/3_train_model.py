import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

st.title("Step 3: Train Linear Regression Model")

# Check if data is loaded
if 'data' not in st.session_state:
    st.warning("Please load data first from 'Step 1: Load Data'")
else:
    df = st.session_state['data']
    st.write("📄 Preview of Data:")
    st.dataframe(df.head())

    # Select columns for X and Y
    st.subheader("Select Features (X) and Target (Y)")
    columns = df.columns.tolist()
    x_col = st.selectbox("Select Independent Variable (X):", columns)
    y_col = st.selectbox("Select Dependent Variable (Y):", columns, index=1)

    if st.button("Train Model"):
        X = df[[x_col]]
        y = df[y_col]

        model = LinearRegression()
        model.fit(X, y)

        st.success("✅ Model trained successfully!")

        # Save model
        model_path = "model.pkl"
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)
        
        # Save selected feature name
        feature_path = "features.pkl"
        with open(feature_path, 'wb') as f:
            pickle.dump([x_col], f)

        st.success("✅ Model and feature files saved successfully!")

        # Download buttons
        with open(model_path, 'rb') as f:
            st.download_button("📥 Download Trained Model (.pkl)", f, file_name="model.pkl")

        with open(feature_path, 'rb') as f:
            st.download_button("📥 Download Feature File (.pkl)", f, file_name="features.pkl")
