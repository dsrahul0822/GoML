import streamlit as st
import pickle
import numpy as np

st.title("Step 4: Predict Salary")

# Upload trained model
model_file = st.file_uploader("Upload Trained Model (.pkl)", type=["pkl"], key="model")
feature_file = st.file_uploader("Upload Feature File (.pkl)", type=["pkl"], key="feature")

if model_file is not None and feature_file is not None:
    # Load model
    model = pickle.load(model_file)

    # Load feature names (should be a list like ['YearsExperience'])
    features = pickle.load(feature_file)

    st.success(f"Model and features loaded successfully! Feature used: {features[0]}")

    # Input form for prediction
    user_input = st.number_input(f"Enter value for {features[0]} (e.g., Years of Experience)", min_value=0.0, format="%.2f")

    if st.button("Predict Salary"):
        prediction = model.predict(np.array([[user_input]]))[0]
        st.success(f"💰 Predicted Salary: ₹{prediction:,.2f}")
else:
    st.info("Please upload both the model and feature files.")
