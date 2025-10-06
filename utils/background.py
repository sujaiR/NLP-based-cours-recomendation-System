import base64
import streamlit as st

def set_background(image_path):
    """Set background image for the Streamlit app."""
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    page_bg = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg, unsafe_allow_html=True)
