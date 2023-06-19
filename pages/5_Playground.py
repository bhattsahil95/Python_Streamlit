import streamlit.components.v1 as components
import streamlit as st
import base64
import os

drop_down = st.multiselect(
    "Choose a shipping method",
    ("Standard (5-15 days)", "Express (2-5 days)")
)




if 'Standard (5-15 days)' in drop_down:
    st.write(" Huh Cheap Person ")
if 'Express (2-5 days)' in drop_down :
    st.write(" Oho, Paisa Vadi Party")

'---'


def read_pdf_file(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)

# Get the current directory
current_directory = os.path.dirname(os.path.realpath(__file__))

# Set the relative path to your PDF file
file_path = os.path.join(current_directory, "..", "Certificates", "python_scaler.pdf")

read_pdf_file(file_path)