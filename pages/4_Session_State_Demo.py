import streamlit as st

st.set_page_config(page_title="Diagnostic Intelligence System", page_icon="🩺", layout="wide")

st.title("Session State Architecture")

st.markdown("""
This module demonstrates memory persistence mechanisms ensuring operational continuity across iterative application re-runs.
""")

st.header("Volatile vs Session State Counters")

# --- UNDERSTANDING STATEFULNESS IN STREAMLIT ---
# Streamlit inherently executes the entire python script top-to-bottom on every user interaction.
# Therefore, normal Python variables (like `count = 0` below) are "volatile" and will reset 
# back to zero on every button press.
col1, col2 = st.columns(2)

with col1:
    st.subheader("Volatile Counter (Resets)")
    count = 0
    if st.button('Increment Volatile', key='increment_volatile_counter'):
        count += 1
    st.write(f'Count: {count}')

with col2:
    # To maintain state across these top-to-bottom re-runs, we utilize `st.session_state`.
    # This acts as a persistant dictionary tied uniquely to the current user's browser session.
    st.subheader("Session State Counter (Persists)")
    if 'count' not in st.session_state:
        st.session_state.count = 0
    if st.button('Increment Session', key='increment_session_counter'):
        st.session_state.count += 1
    st.write(f'Count: {st.session_state.count}')

st.divider()

# --- STATEFUL MACHINE LEARNING PIPELINE DEMO ---
st.header("Stateful ML Pipeline Demo")

# Initializing global operational flags in session state. By doing this ONCE, we ensure 
# the user keeps their current training history, dataset configurations, and models 
# even if they navigate temporarily to another page within the application.
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

# Callback functions are invoked *before* the script re-runs.
# When a user changes the underlying algorithm, we use a callback to instantly reset the 
# global `is_trained` boolean flag preventing inference on mismatched architecture definitions.
def on_model_change():
    st.session_state.model = None
    st.session_state.is_trained = False
    st.toast('Model parameters reset. Retraining required.', icon='⚠️')

with st.sidebar:
    st.header("Pipeline Controls")
    # Tying the `on_model_change` callback explicitly to the selectbox interaction.
    algorithm = st.selectbox(
        'Algorithm',
        ['Random Forest', 'SVM', 'XGBoost'],
        on_change=on_model_change
    )
    if st.button('Train Model', type='primary', key='train_model_sidebar_stateful'):
        with st.spinner(f'Training {algorithm}...'):
            # Updating our persistent state variables indicating the model is effectively deployed.
            st.session_state.is_trained = True
            st.session_state.training_history.append(
                {'epoch': len(st.session_state.training_history)+1,'accuracy': 0.94}
            )
            st.success('Model ready!')

# Guard clause testing against our state boolean: Inference is strictly locked 
# unless the ML pipeline confirms successful compilation and training.
if st.session_state.is_trained:
    st.success(f'Model compiled and trained — {len(st.session_state.training_history)} iteration(s)')
    if st.button('Predict', key='predict_stateful'):
        st.info("Executing inference pipeline on test subset...")
        st.write("Prediction Probabilities: [0.12, 0.84, 0.67]")
else:
    st.warning('Please initialize and train the model via the sidebar controls.')
