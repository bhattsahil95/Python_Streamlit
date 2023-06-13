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
import streamlit as st

def authenticate(username, password):
    # Perform authentication logic here
    # You can check against a database or any other authentication mechanism
    # Return True if the username and password are valid, otherwise return False
    # For simplicity, this example hardcodes the credentials
    valid_username = "admin"
    valid_password = "password"
    return username == valid_username and password == valid_password

# Title for the app
st.title("Login Page")

# Check if login details are cached
if 'username' not in st.session_state:
    st.session_state['username'] = ''
if 'password' not in st.session_state:
    st.session_state['password'] = ''

# Get user credentials
username = st.text_input("Username", value=st.session_state['username'])
password = st.text_input("Password", type="password", value=st.session_state['password'])

# Login button
if st.button("Login"):
    if authenticate(username, password):
        st.success("Login successful!")

        # Cache the login details for future sessions
        st.session_state['username'] = username
        st.session_state['password'] = password
        # Add your app's main functionality here after successful login
    else:
        st.error("Invalid username or password")


if authenticate(username,password):
    st.write("You are currently logged in! ")