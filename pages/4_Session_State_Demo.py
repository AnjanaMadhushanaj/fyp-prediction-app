import streamlit as st

st.set_page_config(page_title="Session State Demo", page_icon="⚙️", layout="wide")

st.title("Session State & Statefulness")

st.markdown("""
This page demonstrates how to persist variables and models across re-runs.
""")

st.header("Volatile vs Session State Counters")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Volatile Counter (Resets)")
    count = 0
    if st.button('Increment Volatile', key='increment_volatile_counter'):
        count += 1
    st.write(f'Count: {count}')

with col2:
    st.subheader("Session State Counter (Persists)")
    if 'count' not in st.session_state:
        st.session_state.count = 0
    if st.button('Increment Session', key='increment_session_counter'):
        st.session_state.count += 1
    st.write(f'Count: {st.session_state.count}')

st.divider()

st.header("Stateful ML Pipeline Demo")

defaults = {
    'model': None,
    'training_history': [],
    'current_dataset': None,
    'predictions': None,
    'is_trained': False,
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

def on_model_change():
    st.session_state.model = None
    st.session_state.is_trained = False
    st.toast('Model reset — please retrain.', icon='⚠️')

with st.sidebar:
    st.header("Pipeline Controls")
    algorithm = st.selectbox(
        'Algorithm',
        ['Random Forest', 'SVM', 'XGBoost'],
        on_change=on_model_change
    )
    if st.button('Train Model', type='primary', key='train_model_sidebar_stateful'):
        with st.spinner(f'Training {algorithm}...'):
            st.session_state.is_trained = True
            st.session_state.training_history.append(
                {'epoch': len(st.session_state.training_history)+1,'accuracy': 0.94}
            )
            st.success('Model ready!')

if st.session_state.is_trained:
    st.success(f'Model trained — {len(st.session_state.training_history)} run(s)')
    if st.button('Predict', key='predict_stateful'):
        st.info("Running dummy prediction on test set...")
        st.write("Prediction: [0.12, 0.84, 0.67]")
else:
    st.warning('Please use the sidebar to train the model first.')
