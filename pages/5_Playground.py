import streamlit.components.v1 as components
import streamlit as st
import io



st.info('Portfolio under construction. Have patience. I will add more things soon......,', icon="⚠️")

'---'

drop_down = st.multiselect(
    "Choose a shipping method",
    ("Standard (5-15 days)", "Express (2-5 days)")
)


if 'Standard (5-15 days)' in drop_down:
    st.write(" Huh Cheap Person ")
if 'Express (2-5 days)' in drop_down :
    st.write(" Oho, Paisa Vadi Party")

'---'
# st.markdown("""<iframe src="https://web.powerva.microsoft.com/environments/Default-ea8fd955-5287-40f2-b3b4-bf458393f5a0/bots/new_bot_89c36dbf702a4b0591fbd13aa82d546f/webchat" frameborder="2" style="width: 450px; height: 400px;"></iframe>""",
#             unsafe_allow_html=True)



'---'
