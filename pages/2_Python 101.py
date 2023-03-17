import streamlit as st
from Games import *
from Projects import *


import time

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
                'Please note, this code was part of my inital code practice. I may have improved significantly by the time you are here ! ',
                icon="⚠️")


with st.sidebar:
    python_101 = st.sidebar.selectbox(
        "List of Projects ",
        ("Game", "Algo", "Projects")
    )

with st.container():
    if python_101 == 'Game':
        a, b= st.columns([4,1])

        with b:
            with st.expander('List of Games'):
                games = st.selectbox((""),
                ('Hangman', 'Tic Tac Toe', 'Stone Paper Scissors'))


        if games == 'Hangman':
            with a:

                st.write('''
                
                Hangman is a classic word guessing game where players try to guess a word one letter at a time. 
                If the player makes a wrong guess, a part of a stick figure is drawn, representing a hanging man. 
                The player loses the game if the stick figure is completely drawn before the word is correctly guessed.
                The game can be played with a single player or with multiple players taking turns guessing letters.
                
                ''')
            '---'


            st.code(hangman, language='python')

        if games == 'Tic Tac Toe':
            with a:
                st.markdown('#')
                st.write('''

               Tic Tac Toe is a two-player pencil-and-paper game in which players take turns marking Xs and Os in a 3x3 grid. 
               The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row 
               is the winner. It is also known as Noughts and Crosses.
                       ''')
            '---'
            st.code(ttt, language='python')

        if games == 'Stone Paper Scissors':
            with a:
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


with st.container():
    if python_101 == 'Projects':
        p = ['Credit Cared Validator', 'Table Generator', 'Number Guessing', 'Word Counter',
             'Basic Calculator', 'Password Checker', 'Letter Search @ specific place ']

        a, b= st.columns([4,2])

        with b:
            with st.expander('List of Projects'):
                projects = st.selectbox((""),p)



        if projects == p[0]:
            with a:

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
            with a:
                st.markdown('###')
                st.write('''

          Simple Table Generator. Prints Table for any integer. 

                       ''')
            '---'
            st.code(tg, language='python')

        if projects == p[2]:
            with a:
                st.markdown('###')
                st.write('''

          Simple Number guessing thing. I don't if this qualifies as a game or a algo. Hence,
          it is here now.  

                       ''')
            '---'
            st.code(ng, language='python')


        if projects == p[3]:
            with a:
                st.markdown('###')
                st.write('''

          Take an input and gives you a little analytics of words used. Gives you 
          all the words used by their % and top 3 words used.   

                       ''')
            '---'
            st.code(wc , language='python')

        if projects == p[4]:
            with a:
                st.markdown('###')
                st.write('''

          The classic. It is just a basic calculator that can do four baisc arithmatic operations.    

                       ''')
            '---'
            st.code(bc , language='python')


        if projects == p[5]:
            with a:
                st.markdown('###')
                st.write('''

          Password Checker. .   Password Requirements :  \n => Upper Case   \n =>  Lower Case  \n => Special Character  \n =>  NMinimun length : 8 

                       ''')
            '---'
            st.code(pc1 , language='python')

            st.write('Basically same thing, different format')

            st.code(pc1, language='python')


        if projects == p[6]:
            with a:
                st.markdown('###')
                st.write('''

          It searched displays all the words which matches the requirements. Takes 2 arguments, 1: Letter 2:Position. 
          
        Pretty straight forward, hey !    

                       ''')
            '---'
            st.code(ls , language='python')