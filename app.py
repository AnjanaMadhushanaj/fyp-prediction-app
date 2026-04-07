import streamlit as st

st.set_page_config(
    page_title='FYP Home',
    page_icon='🏠', 
    layout='wide', 
    initial_sidebar_state='expanded'
)

st.title('Welcome to My FYP Application')
st.write('This is the Home Page of my Multi-Page Streamlit App.')

st.markdown('''
### Navigation
Please select a page from the sidebar to explore different components of the project:
1. **Data & Metrics:** Explore data metrics and load datasets.
2. **Interactive Forms:** Interactive controls and inputs.
3. **Visualizations:** Visual charts and plots using various libraries.
4. **Session State Demo:** Demonstrating Streamlit state persistence.
''')

st.code('''
def main():
    print("Welcome to the final year project!")
''', language='python')

st.latex(r'\hat{y} = \sigma(W \cdot X + b)')

st.caption('Navigate using the sidebar to view different pages.')
st.link_button('Open GitHub Repo', 'https://github.com/AnjanaMadhushanaj')
