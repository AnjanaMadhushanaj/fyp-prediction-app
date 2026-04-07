import streamlit as st
import pandas as pd
from pathlib import Path
import time

st.set_page_config(page_title="Data & Metrics", page_icon="📊", layout="wide")

st.title("Data and Metrics")
st.write("This page demonstrates data loading, summary metrics, and dataset viewing.")

st.divider()
st.header("KPI Metrics")

col1, col2, col3, col4 = st.columns(4)
col1.metric(label='Accuracy', value='94.5%', delta='+2.1%')
col2.metric(label='Precision', value='91.2%', delta='-0.8%')
col3.metric(label='Recall', value='96.3%', delta='+1.5%')
col4.metric(label='F1 Score', value='93.7%', delta='+0.6%')
st.metric('Loss', '0.082', delta='-0.014', delta_color='inverse')

st.divider()

@st.cache_data
def load_patient_data():
    """Simulates a slow data loading process using caching to improve performance."""
    with st.spinner("Loading heavy dataset... please wait..."):
        time.sleep(3)  # App eka thapara 3k hold karanawa test karanna
        return pd.DataFrame({
            'Patient_ID': range(1, 6),
            'Age': [34, 45, 56, 29, 67],
            'Diagnosis': ['Positive', 'Negative', 'Positive', 'Negative', 'Positive'],
            'Confidence': [0.92, 0.87, 0.95, 0.73, 0.89]
        })

col_hdr, col_btn = st.columns([4, 1])
with col_hdr:
    st.header("Dataset Overview")
with col_btn:
    # Clear cache and rerun to test performance difference
    if st.button("Reload Data", type="secondary"):
        load_patient_data.clear()
        st.rerun()

df = load_patient_data()

tab1, tab2 = st.tabs(['Data Editor', 'Static Table'])

with tab1:
    st.dataframe(df, use_container_width=True,
        column_config={
        'Patient_ID': st.column_config.NumberColumn('ID'),
        'Confidence': st.column_config.ProgressColumn(
            'Confidence', min_value=0, max_value=1, format='%.2f'),
        'Diagnosis': st.column_config.SelectboxColumn(
            'Diagnosis', options=['Positive','Negative'])
        }
    )

with tab2:
    st.table(df)

st.divider()
st.header("Data Loading")

uploaded = st.file_uploader('Upload Dataset (CSV)', type=['csv', 'xlsx'])
if uploaded:
    suffix = Path(uploaded.name).suffix.lower()
    if suffix == '.xlsx':
        df_uploaded = pd.read_excel(uploaded)
    else:
        df_uploaded = pd.read_csv(uploaded)
    st.success(f'Loaded {len(df_uploaded)} rows, {len(df_uploaded.columns)} columns')
    st.dataframe(df_uploaded.head())
    
csv = df.to_csv(index=False)
st.download_button(
    label='Download Results as CSV',
    data=csv,
    file_name='predictions.csv',
    mime='text/csv'
)