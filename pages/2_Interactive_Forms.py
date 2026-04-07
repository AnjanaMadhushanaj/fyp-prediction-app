import streamlit as st
import time

st.set_page_config(page_title="Interactive Forms", page_icon="🎛️", layout="wide")

st.title("Patient Diagnosis Form")
st.write("Using `st.form` to collect patient data and run ML predictions.")

st.divider()

# --- SECTION 10: ML Model Integration ---
# Model eka load karanna @st.cache_resource pawichi karanawa. 
# (Meka hamathissema run wena eka nawaththanawa)
@st.cache_resource
def load_ml_model():
    with st.spinner("Loading Machine Learning Model..."):
        time.sleep(2) # Model eka load wenna wela yanawa kiyala pennanna thapara 2k hold karanawa
        
        # OYA ATHATHA MODEL EKAK DAPU DAWSAKA ME TIKA WENAS KARANNA:
        # import pickle
        # return pickle.load(open('models/classifier.pkl', 'rb'))
        
        return "Random_Forest_Classifier_v1" # Danata api fake model namak denawa

model = load_ml_model()

# --- FORM EKA ---
with st.form('patient_form'):
    st.subheader('Patient Information')
    
    form_col1, form_col2 = st.columns(2)
    
    with form_col1:
        age = st.number_input('Age', 0, 120, 35)
        gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
        
    with form_col2:
        weight = st.number_input('Weight (kg)', 30.0, 200.0, 70.0)
        height = st.number_input('Height (cm)', 100.0, 250.0, 170.0)
        
    symptoms = st.multiselect('Symptoms', ['Fever', 'Cough', 'Fatigue', 'Breathlessness'])
    notes = st.text_area('Clinical Notes')
    
    # Form submit button
    submitted = st.form_submit_button('Run Diagnosis', type='primary')
    
    # --- PREDICTION LOGIC EKA ---
    if submitted:
        st.info(f"Using Model: {model}")
        
        with st.spinner("Analyzing patient data..."):
            time.sleep(1) # Prediction eka hadenawa wage pennanna
            
            bmi = weight / ((height/100) ** 2)
            
            # Meka fake prediction logic ekak (Aththa model eka dapu dawasaka meka wenas wenawa)
            # Api hithamu wayasa 60ta wadi nam hari, symptoms 2kata wadi nam hari "High Risk" kiyala
            if len(symptoms) >= 2 or age > 60:
                st.error("🚨 Prediction: High Risk of Disease (Confidence: 87%)")
            else:
                st.success("✅ Prediction: Low Risk (Confidence: 92%)")
                
            st.write(f'Calculated BMI: {bmi:.1f} | Symptoms reported: {len(symptoms)}')