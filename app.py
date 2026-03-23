import streamlit as st
import pandas as pd
import joblib

# Set page config
st.set_page_config(page_title="Student Marks Predictor", layout="centered")

# Load the trained model
try:
    model = joblib.load("model.pkl")
    model_loaded = True
except:
    model_loaded = False
    st.error("Error: Trained model 'model.pkl' not found. Please run main.py first.")

# UI Elements
st.title("🎓 Student Marks Predictor")
st.markdown("Enter your study details below to predict your exam marks.")

# Input fields
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        study_hours = st.number_input("Study Hours per Day", min_value=0.0, max_value=24.0, value=5.0, step=0.5)
        sleep_hours = st.number_input("Sleep Hours per Day", min_value=0.0, max_value=24.0, value=7.0, step=0.5)
    with col2:
        attendance = st.slider("Attendance Percentage (%)", min_value=0, max_value=100, value=80)

# Prediction Button
if st.button("Predict Marks"):
    if model_loaded:
        # Prepare input data
        input_data = pd.DataFrame({
            'study_hours': [study_hours],
            'sleep_hours': [sleep_hours],
            'attendance': [attendance]
        })
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        
        # Cap prediction at 100
        prediction = min(max(prediction, 0), 100)
        
        # Display Result
        st.success(f"### Predicted Marks: **{prediction:.2f}%**")
        
        if prediction > 80:
            st.balloons()
            st.info("Excellent! Keep maintaining your study and attendance.")
        elif prediction < 40:
            st.warning("Prediction is low. You might want to increase study hours or attendance.")
    else:
        st.error("Cannot predict without a trained model.")

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit & Scikit-Learn")