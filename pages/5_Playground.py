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

import streamlit as st
import base64
import os

def get_base64_encoded_data(file_path):
    with open(file_path, "rb") as file:
        encoded_data = base64.b64encode(file.read()).decode("utf-8")
    return encoded_data

# Get the directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Set the relative path to your PDF file
file_path = os.path.join(current_directory, "..", "Certificates", "python_scaler.pdf")

# Read the PDF file and convert it to base64 format
encoded_pdf = get_base64_encoded_data(file_path)

# Create a collapsible section
with st.expander("View Resume"):
    # Display the PDF inline
    st.image(f"data:application/pdf;base64,{encoded_pdf}", caption='Resume', use_column_width=True)

    # Add a download button
    download_button_html = f'<a href="data:application/pdf;base64,{encoded_pdf}" download="resume.pdf">Download Resume</a>'
    st.markdown(download_button_html, unsafe_allow_html=True)
