import streamlit as st

# Configure the main application page settings.
# This acts as the global entry point and establishes the layout for the Multi-Page app architecture.
st.set_page_config(
    page_title='FYP Home',
    page_icon='🏠', 
    layout='wide', 
    initial_sidebar_state='expanded'
)

# Landing Page Content
st.title('Welcome to My FYP Application')
st.write('This is the Home Page of my Multi-Page Streamlit App.')

# Centralized navigation guide for end-users
st.markdown('''
### Navigation
Please select a page from the sidebar to explore different components of the project:
1. **Data & Metrics:** Explore data metrics and load datasets.
2. **Interactive Forms:** Interactive controls and inputs.
3. **Visualizations:** Visual charts and plots using various libraries.
4. **Session State Demo:** Demonstrating Streamlit state persistence.
''')

# Demonstration of code rendering for documentation purposes
st.code('''
def main():
    print("Welcome to the final year project!")
''', language='python')

# Mathematical formula rendering for research/academic components
st.latex(r'\hat{y} = \sigma(W \cdot X + b)')

st.caption('Navigate using the sidebar to view different pages.')

# Link to external version control repository for examiner review
st.link_button('Open GitHub Repo', 'https://github.com/AnjanaMadhushanaj/fyp-prediction-app')
