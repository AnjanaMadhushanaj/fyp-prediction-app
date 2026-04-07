import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="Diagnostic Intelligence System", page_icon="🏥", layout="wide")

st.title("Data Visualizations")

# Generating structured mock data to represent aggregate model performance metrics across 20 simulated epochs
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=['Model A', 'Model B', 'Baseline']
)

# --- NATIVE STREAMLIT CHARTS ---
# Utilizing built-in Streamlit graphing functionality for rapid, lightweight visual reporting
col1, col2 = st.columns(2)

with col1:
    st.subheader('Line Chart — Training Loss')
    st.line_chart(chart_data)

    st.subheader('Area Chart — Cumulative Accuracy')
    st.area_chart(chart_data)

with col2:
    st.subheader('Bar Chart — Feature Importance')
    feat_imp = pd.DataFrame({'importance':[0.35,0.28,0.19,0.11,0.07]},
        index=['income','age','score','region','edu'])
    st.bar_chart(feat_imp)

    st.subheader('Scatter Chart')
    st.scatter_chart(chart_data, x='Model A', y='Model B')

st.divider()

# --- ADVANCED STATISTICAL PLOTS (matplotlib & seaborn) ---
# Leveraging matplotlib and seaborn constructs tailored for rigorous statistical representation, 
# common in machine learning evaluation pipelines.
st.header("Seaborn & Matplotlib")
c1, c2 = st.columns(2)

with c1:
    # A Confusion Matrix visualizes true vs predicted classification frequencies. It is critical for
    # understanding the misclassification logic (False Positives vs False Negatives).
    cm = np.array([[85, 5], [8, 102]])
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
        xticklabels=['Pred Neg','Pred Pos'],
        yticklabels=['True Neg','True Pos'], ax=ax)
    ax.set_title('Confusion Matrix')
    ax.set_ylabel('Actual')
    ax.set_xlabel('Predicted')
    st.pyplot(fig)
    plt.close(fig) # IMPORTANT: Explicitly closing figures manually to prevent RAM memory leaks on server

with c2:
    # An ROC (Receiver Operating Characteristic) curve plots True Positive Rates against False Positive Rates.
    # It demonstrates the diagnostic ability of a binary classifier as its discrimination threshold is varied.
    fpr = np.linspace(0, 1, 100)
    tpr = np.sqrt(fpr)
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    ax2.plot(fpr, tpr, 'b-', lw=2, label='ROC (AUC=0.94)')
    ax2.plot([0,1],[0,1],'r--', label='Random')
    ax2.set_xlabel('False Positive Rate')
    ax2.set_ylabel('True Positive Rate')
    ax2.legend()
    ax2.set_title('ROC Curve')
    st.pyplot(fig2)
    plt.close(fig2)

st.divider()

# --- INTERACTIVE PLOTLY VISUALIZATIONS ---
# Plotly is used here to enable rich user engagement, such as hovertool tips, zooming, and dynamic scaling.
st.header("Plotly Visualizations")

c3, c4 = st.columns(2)
with c3:
    # Dimensionality visualization utilizing internal datasets to demonstrate scatter matrices
    df_iris = px.data.iris()
    fig_plotly = px.scatter(df_iris, x='sepal_width', y='sepal_length',
        color='species', size='petal_length',
        title='Iris Dataset — Feature Correlation')
    st.plotly_chart(fig_plotly, use_container_width=True)

with c4:
    # Comparative bar charts illustrating cross-model accuracy scores
    models = ['Logistic Reg', 'Random Forest', 'SVM', 'XGBoost']
    scores = [0.87, 0.94, 0.91, 0.96]
    fig_bar = go.Figure(go.Bar(x=models, y=scores,
        marker_color=['#636EFA','#EF553B','#00CC96','#AB63FA'],
        text=[f'{s:.0%}' for s in scores], textposition='outside'))
    fig_bar.update_layout(title='Model Accuracy Comparison',
        yaxis_range=[0.8, 1.0])
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# --- STATIC MULTIMEDIA HANDLING ---
st.header("Media Elements")
col_media1, col_media2 = st.columns(2)
with col_media1:
    # Loading external image buffers dynamically via HTTP URLs
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Profile_avatar_placeholder_large.png/400px-Profile_avatar_placeholder_large.png',
        caption='Sample Image via URL', width=200)

with col_media2:
    # Fallback pattern for querying and streaming static multimedia binaries from the host OS
    demo_video_path = Path('demo.mp4')
    if demo_video_path.exists():
        st.video(demo_video_path.read_bytes())
    else:
        st.info('demo.mp4 not found for video playback')
