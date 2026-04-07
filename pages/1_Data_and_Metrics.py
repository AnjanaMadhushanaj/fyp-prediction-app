import streamlit as st
import pandas as pd
from pathlib import Path
import time

# Configure the Streamlit page metadata, which appears in the browser tab and sidebar.
st.set_page_config(page_title="Data & Metrics", page_icon="📊", layout="wide")

st.title("Data and Metrics")
st.write("This page demonstrates data loading, summary metrics, and dataset viewing.")

st.divider()

# --- Key Performance Indicators (KPIs) ---
# Displaying high-level model evaluation metrics. These give the end-user immediate 
# context into the current operational efficacy of the trained machine learning models.
st.header("KPI Metrics")

col1, col2, col3, col4 = st.columns(4)
col1.metric(label='Accuracy', value='94.5%', delta='+2.1%')
col2.metric(label='Precision', value='91.2%', delta='-0.8%')
col3.metric(label='Recall', value='96.3%', delta='+1.5%')
col4.metric(label='F1 Score', value='93.7%', delta='+0.6%')
st.metric('Loss', '0.082', delta='-0.014', delta_color='inverse')

st.divider()

# --- Data Loading and Caching ---
# @st.cache_data is utilized here to drastically improve web application performance.
# By caching the returned dataframe, Streamlit guards against redundant heavy I/O operations 
# (e.g., querying remote databases or reading large CSV files) upon every UI refresh or interaction.
@st.cache_data
def load_patient_data():
    """Simulates a slow data loading process using caching to improve performance."""
    with st.spinner("Loading heavy dataset... please wait..."):
        time.sleep(3)  # Hold execution for 3 seconds to test caching performance
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
    # Provides a manual override for the user to flush the cache and force fresh data retrieval.
    if st.button("Reload Data", type="secondary"):
        load_patient_data.clear()
        st.rerun()

df = load_patient_data()

# Tabs provide a clean UI pattern for categorizing different views of the same underlying data.
tab1, tab2 = st.tabs(['Data Editor', 'Static Table'])

with tab1:
    # Interactive dataframe utilizing custom column configurations to enhance readability 
    # (e.g., Progress bars for Confidence levels and categorical dropdowns for Diagnosis).
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

# --- File Operations ---
# Allowing the user to dynamically upload ad-hoc datasets for local analysis.
st.header("Data Loading")

uploaded = st.file_uploader('Upload Dataset (CSV)', type=['csv', 'xlsx'])
if uploaded:
    suffix = Path(uploaded.name).suffix.lower()
    # Handle different file protocols safely based on the user's uploaded extension
    if suffix == '.xlsx':
        df_uploaded = pd.read_excel(uploaded)
    else:
        df_uploaded = pd.read_csv(uploaded)
    st.success(f'Loaded {len(df_uploaded)} rows, {len(df_uploaded.columns)} columns')
    st.dataframe(df_uploaded.head())
    
# Facilitating data extraction by providing a direct download link of the processed dataset.
csv = df.to_csv(index=False)
st.download_button(
    label='Download Results as CSV',
    data=csv,
    file_name='predictions.csv',
    mime='text/csv'
)