import streamlit.components.v1 as components
import streamlit as st

drop_down = st.multiselect(
    "Choose a shipping method",
    ("Standard (5-15 days)", "Express (2-5 days)")
)




if 'Standard (5-15 days)' in drop_down:
    st.write(" Huh Cheap Person ")
if 'Express (2-5 days)' in drop_down :
    st.write(" Oho, Paisa Vadi Party")

'---'

components.html('''

  

''',height=600)


# Certificates/python_ztm.pdf