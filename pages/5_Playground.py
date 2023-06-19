import streamlit.components.v1 as components
import streamlit as st
import base64
import os

st.warning( '''🚧‍ This is a playground. I usually test things here. 
If you see something unusual, don't get alarmed. ''')




drop_down = st.multiselect(
    "Choose a shipping method",
    ("Standard (5-15 days)", "Express (2-5 days)")
)




if 'Standard (5-15 days)' in drop_down:
    st.write(" Huh Cheap Person ")
if 'Express (2-5 days)' in drop_down :
    st.write(" Oho, Paisa Vadi Party")

'---'


def get_base64_encoded_data(file_path):
    with open(file_path, "rb") as file:
        encoded_data = base64.b64encode(file.read()).decode("utf-8")
    return encoded_data


# Set the relative path to your PDF file
file_path = "Certificates/python_scaler.pdf"

# Read the PDF file and convert it to base64 format
encoded_pdf = get_base64_encoded_data(file_path)

# Create a collapsible section
with st.expander("View Resume"):
    # Generate the PDF viewer HTML code
    pdf_viewer = f'<embed src="data:application/pdf;base64,{encoded_pdf}" width="100%" height="600px" type="application/pdf">'

    # Display the PDF viewer using Markdown
    st.markdown(pdf_viewer, unsafe_allow_html=True)

    # Add a download button
    download_button_html = f'<a href="data:application/pdf;base64,{encoded_pdf}" download="resume.pdf">Download Resume</a>'
    st.markdown(download_button_html, unsafe_allow_html=True)