import os.path
import streamlit as st
import  base64
import webbrowser
import urllib

def page():
    return st.set_page_config(
         page_title="My First Web App",
         page_icon=":shark:",
         layout="wide",
         initial_sidebar_state="expanded",
         menu_items={
             'Get Help': 'https://www.extremelycoolapp.com/help',
             'Report a bug': "https://www.extremelycoolapp.com/bug",
             'About': "# This is a header. This is an *extremely* cool app!"

         }
     )

page()



with st.sidebar:
    select = st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
    )
