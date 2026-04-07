import streamlit as st
import time

st.set_page_config(page_title="Diagnostic Intelligence System", page_icon="🩺", layout="wide")

st.title("Patient Diagnosis Form")
st.write("Secure interface for clinical data entry and diagnostic model inference.")

st.divider()

# --- Machine Learning Model Integration ---
# We use @st.cache_resource for objects that should be shared globally across all 
# users and sessions, such as machine learning models, database connections, or API clients.
# By caching the model, we prevent the heavy operation of deserializing it into memory 
# every time the Streamlit script re-executes.
@st.cache_resource
def load_ml_model():
    with st.spinner("Loading Machine Learning Model..."):
        time.sleep(2) # Simulate delay for loading a large model binary into memory
        return "Random_Forest_Classifier_v1" # Placeholder for the instantiated model

model = load_ml_model()

# --- CLINICAL DATA COLLECTION FORM ---
# st.form bundles multiple input widgets together. This means the Streamlit app will NOT
# re-run immediately as the user types or clicks toggles. It will only re-run, capturing all 
# inputs simultaneously, when the user explicitly hits the st.form_submit_button.
with st.form('patient_form'):
    st.subheader('Patient Information')
    
    # Utilizing columns to layout the UI neatly
    form_col1, form_col2 = st.columns(2)
    
    with form_col1:
        age = st.number_input('Age', 0, 120, 35)
        gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
        
    with form_col2:
        weight = st.number_input('Weight (kg)', 30.0, 200.0, 70.0)
        height = st.number_input('Height (cm)', 100.0, 250.0, 170.0)
        
    symptoms = st.multiselect('Symptoms', ['Fever', 'Cough', 'Fatigue', 'Breathlessness'])
    notes = st.text_area('Clinical Notes')
    
    # Form submit button triggering the execution block below
    submitted = st.form_submit_button('Run Diagnosis', type='primary')
    
    # --- MODEL INFERENCE LOGIC ---
    if submitted:
        st.info(f"Using Model: {model}")
        
        with st.spinner("Analyzing patient data..."):
            time.sleep(1) # Simulate real-time inference delay computationally
            
            # Feature engineering step: Calculate BMI dynamically based on inputs
            bmi = weight / ((height/100) ** 2)
            
            # Mock Classification Logic.
            # In production, this would be replaced with: `prediction = model.predict(X_test)`
            # Here, it determines "High Risk" if age > 60 or if the patient presents 2+ symptoms.
            if len(symptoms) >= 2 or age > 60:
                st.error("Prediction: High Risk of Disease (Confidence: 87%)")
            else:
                st.success("Prediction: Low Risk (Confidence: 92%)")
                
            st.write(f'Calculated BMI: {bmi:.1f} | Symptoms reported: {len(symptoms)}')

st.divider()

# --- Performance Optimisation Debugging ---
# Provides utility buttons to clear caches, helpful for examiners and testers to observe 
# the performance difference between a cold start and a cached execution.
st.subheader("Performance Optimisation Debug")
st.write("Use the button below to clear all caches and witness the difference in load speeds on your next run.")

if st.button('Clear All Caches', type='primary', help="Clears both data and resource caches."):
    st.cache_data.clear()
    st.cache_resource.clear()
    st.rerun()