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

with st.container():

    def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="820" height="680" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)


    st.markdown("<h1 style='text-align: center; '> My Certificates </h1>",
                unsafe_allow_html=True)

    st.write("#")
    st.write("#")


    with st.expander("Python Zero to Mastery Certificate - Udemy"):

        st.balloons()
        st.write('''
        More information about the certification. Validate this Certificate Here! 	:point_right: [:heavy_check_mark:](https://www.udemy.com/certificate/UC-90653b4c-a49d-40f2-80d2-b43b3e14c563/)
        ''')
        col3, col1, col2 = st.columns([1, 4, 1])
        with col1:
            show_pdf(os.path.join('Certificates','python_ztm.pdf'))

        '---'


    '---'

    with st.expander("Python and SQL for Data Science - Scaler "):
        st.balloons()
        st.write('''
        More information about the certification.  Validate this Certificate Here! 	:point_right: [:heavy_check_mark:](https://moonshot.scaler.com/s/sl/QQZTt-z4He)
        ''')
        '---'
        col3, col1, col2 = st.columns([1, 4, 1])
        with col1:
            show_pdf(os.path.join('Certificates','python_scaler.pdf'))

        '---'
    # with st.expander("Test PDF"):
    #
    #     file = os.path.join('Certificates','python_ztm.pdf')
    #     with open(file, "rb") as f:
    #         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    #     pdf_display = F'<iframe src="data:{file};base64,{base64_pdf}" width="700" height="1000" type="application/pdf">PDF</iframe>'
    #     st.markdown(pdf_display, unsafe_allow_html=True)