import os.path

import streamlit as st
from Games import *
from Projects import *

st.set_page_config(
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

st.info(
    'Please note, this code was part of my initial code practice. I may have improved significantly by the time you are here ! ',
    icon="⚠️")

with st.sidebar:
    python_101 = st.sidebar.selectbox(
        "List of Projects ",
        ("Game", "Algo", "Projects")
    )

if python_101 == "Game":
    with st.sidebar:
        '---'
        games = st.selectbox(("List of Games"), ('Hangman', 'Tic Tac Toe', 'Stone Paper Scissors'))

    if games == 'Hangman':
        with st.container():
            st.write('''

            Hangman is a classic word guessing game where players try to guess a word one letter at a time. 
            If the player makes a wrong guess, a part of a stick figure is drawn, representing a hanging man. 
            The player loses the game if the stick figure is completely drawn before the word is correctly guessed.
            The game can be played with a single player or with multiple players taking turns guessing letters.

            ''')
            '---'

            st.code(hangman, language='python')

    if games == 'Tic Tac Toe':
        with st.container():
            st.markdown('#')
            st.write('''

           Tic Tac Toe is a two-player pencil-and-paper game in which players take turns marking Xs and Os in a 3x3 grid. 
           The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row 
           is the winner. It is also known as Noughts and Crosses.
                   ''')
        '---'
        st.code(ttt, language='python')

    if games == 'Stone Paper Scissors':
        with st.container():
            st.markdown('###')
            st.write('''

          Stone-Paper-Scissors is a hand game usually played between two people, in which each player simultaneously
           forms one of three shapes with an outstretched hand. These shapes are "stone" (a closed fist), "paper" 
           (a flat hand), and "scissors" (a fist with the index and middle fingers extended). The object of the game 
           is to beat the opponent by selecting a gesture which defeats their gesture, according to the following rules: 
           stone blunts scissors, scissors cuts paper, and paper covers stone.
                   ''')
        '---'
        st.code(sps, language='python')

### Displaying Projects

if python_101 == "Projects":
    p = ['Credit Cared Validator', 'Table Generator', 'Number Guessing', 'Word Counter',
         'Basic Calculator', 'Password Checker', 'Letter Search @ specific place ']
    with st.sidebar:
        projects = st.selectbox(("List of Projects"), p)

    if projects == p[0]:
        st.write('''

      This was a project from Hackerrank: It checks the following conditions.  \n

       ►It must start with a 4, 5 or 6.  \n
       ► It must contain exactly 16 digits.   \n
       ► It must only consist of digits (0-9).   \n
       ► It may have digits in groups of 4, separated by one hyphen "-".   \n
       ► It must NOT use any other separator like ' ' , '_', etc.   \n
       ► It must NOT have 4 or more consecutive repeated digits.

                   ''')
        '---'
        st.code(ccv, language='python')

    if projects == p[1]:
        st.markdown('###')
        st.write('''

      Simple Table Generator. Prints Table for any integer. 
      
    

                   ''')
        '---'
        st.code(tg, language='python')

    if projects == p[2]:
        st.markdown('###')
        st.write('''

      Simple Number guessing thing. I don't if this qualifies as a game or a algo. Hence,
      it is here now.  

                   ''')
        '---'
        st.code(ng, language='python')

    if projects == p[3]:
        st.markdown('###')
        st.write('''

      Take an input and gives you a little analytics of words used. Gives you 
      all the words used by their % and top 3 words used.   

                   ''')
        '---'
        st.code(wc, language='python')

    if projects == p[4]:
        st.markdown('###')
        st.write('''

      The classic. It is just a basic calculator that can do four basic arithmatic operations.    

                   ''')
        '---'
        st.code(bc, language='python')

    if projects == p[5]:
        st.markdown('###')
        st.write('''

      Password Checker. .   Password Requirements :  \n => Upper Case   \n =>  Lower Case  \n => Special Character  \n =>  Minimum length : 8 

                   ''')
        '---'
        st.code(pc1, language='python')

        st.write('Basically same thing, different format')

        st.code(pc1, language='python')

    if projects == p[6]:
        st.markdown('###')
        st.write('''

      It displays all the words which matches the requirements. Takes 2 arguments, 1. Letter 2. Position. Pretty straight forward, hey !    

                   ''')
        '---'
        st.code(ls, language='python')

# Display the results for Algo selection in the sidebar

if python_101 == "Algo":
    with st.container():
        '---'

        col1, col2, col3 = st.columns([1, 3, 1])

        with col2:
            st.markdown("<h1 style='text-align: center; color: red;'>Why Do you think this section is EMPTY ?? </h1>",
                        unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            option = st.selectbox('', (
            'You are LAZY AF ! ', 'You are too DUMB to write any Algo your self.....', 'Okay, tell me the real reason.',
            'None'), index=3)

            st.write('''
                
                
                ''')

            if option == 'You are LAZY AF ! ':
                st.markdown(
                    "<h3 style='text-align: center;'>I might look like this....But no need to say the truth !</h3>",
                    unsafe_allow_html=True)

                st.image(os.path.join('images', 'lazy.jpg'), caption='This is Actual Photo of Me :)',
                         use_column_width='always')

            if option == 'You are too DUMB to write any Algo your self.....':
                st.markdown(
                    "<h3 style='text-align: center;'>I am still very new to coding and problem solving complex algos. I am trying, but ain't I cute?? That's something, ey?</h3>",
                    unsafe_allow_html=True)

                st.image(os.path.join('images', 'dumb.jpg'),
                         caption='Me trying to make sense of my code after two weeks !', use_column_width='always')

            if option == 'Okay, tell me the real reason.':
                st.markdown(
                    "<h6 style='text-align: center;'>So, far my experience has been that most of the required algos are easily available and accessible."
                    "I wrote this one insersion sorting algo on my own. </h6>",
                    unsafe_allow_html=True)

                st.markdown(
                    "<h6 style='text-align: center;'> However, there are tons of websites and resources available that "
                    "basically has all the used algos ready to use. So......I might attempt to write my own algorithm if I take up any project like that! "
                    " </h6>",
                    unsafe_allow_html=True)

                '---'

                st.code(i_sort, language='python')
                '---'
                st.image(os.path.join('images', 'dumb.jpg'),
                         caption='Me trying to make sense of my code after two weeks !', use_column_width='always')
