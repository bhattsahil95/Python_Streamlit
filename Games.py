sps = '''

import random
valid_input = ["r","p","s"]
input_attempt = 0


# r < p, r < s, p < s

def game(best_of):
    player_win = 0
    computer_win = 0
    tied_game = 0
    
    for i in range(best_of):
        player_input = input("Please choose your selection. \n\"R\" for Roack \"P\" for Paper and \"S\" for Scissors:        ").lower()
        while player_input not in valid_input:
            print("\n Please try with a valid input agian! ")
            player_input= input("\"R\" for Roack \"P\" for Paper and \"S\" for Scissors:        ").lower()

        player2 = random.choice(valid_input)
        print(f"Player 1 : {player_input} and player 2 : {player2} ")

        a = player_input
        b = player2

        print(a)
        print(b)

        if (a == "r" and b == "p") or (a == "r" and b == "s") or (a == "p" and b == "s"):
            print(" You won ! ")
            player_win += 1
        elif (a == "p" and b == "p") or (a == "r" and b == "r") or (a == "s" and b == "s"):
            print(" It's ties !")
            computer_win += 1
        else:
            print("computer won !! ")
            tied_game += 1

    total_games = player_win + computer_win + tied_game
    print("\n")
    print("Final Results : ")
    print(f"Total games played: {player_win + computer_win + tied_game}") 
    print(f"Player wins: {player_win} {round((player_win/total_games)*100,2)}% ")
    print(f"Computer wins : {computer_win} ({round((computer_win/(player_win + computer_win + tied_game)*100),2)})% ")
       
game(3)



'''


ttt = '''

import time

#Global variables for the game 

add_line = "\n"
player_1_inputs = [] 
player_2_inputs = []
player_1_turn = None
player_1_score = 0
player_2_score = 0
draw_score = 0
  

def game_rules():
    print(add_line*2)
    print("This is a classic Tic, Tac, Toe Game. ")
    time.sleep(1)
    print("To put your symbol in the location, please select the associated number from the desired location")
    time.sleep(1)
    print(add_line)

    print("Here is the grid of the board. :  ! ")
    print(add_line*3)
    for i in range(1,10)[:3]: print(f"  {i}  ", end=" ") 
    print("\n")
    for i in range(1,10)[3:6]: print(f"  {i}  ", end=" ")
    print("\n")
    for i in range(1,10)[6:]: print(f"  {i}  ", end=" ")
    
       
    print(add_line*3)
    time.sleep(2)
    print(" Good luck ! ")


def player_move(value,player1input, player2input): 

    try:
        value = int(value)
        if value <= 9 and value >= 1:           
            if value not in player1input and value not in player2input:
                return value
            else:
                print("Inavalid input, Input already exsists. ")
                return 0
        else:
            print("Invalid input. Value must be between 1 - 9.")
            return 0

    except:
        print("Only integer inputs are valid. ")
        return 0


def display_board():
    board_values = [ ] 
    global player_1_inputs 
    global player_2_inputs 
    

    for i in range(1,10):
        if i in player_1_inputs: 
            board_values.append("X")
        elif i in player_2_inputs: 
            board_values.append("O")
        else:
            board_values.append("_")

    print(add_line*2)
    for i in board_values[:3]: print(f"  {i}  ", end=" ") 
    print("\n")
    for i in board_values[3:6]: print(f"  {i}  ", end=" ")
    print("\n")
    for i in board_values[6:]: print(f"  {i}  ", end=" ")
    print(add_line*2)


def check_winner(player_input):
 
    winning_combinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9], [1,5,9], [3,5,7]]
    
    
    for i in winning_combinations:
      if(set(i).issubset(set(player_input))):  
        return 1 
        break
      else:
        pass

  
def game_play():
    
   

    global player_1_name
    global player_2_name
    global player_1_turn
      
    game_status = True 
    player_1_attempts = 5
    player_2_attempts = 4
    
    player_1_win = False
    player_2_win = False
    

    while game_status is True:

        while player_1_attempts > 0 :  
            
             while player_1_turn is True or player_1_turn is None: 
                print(add_line)
               
                x =  player_move(input((f"{player_1_name} Please Enter Value:")), player_1_inputs, player_2_inputs) 
                if x == 0: 
                    continue
                else:

                    player_1_inputs.append(x) 
                    player_1_attempts -= 1 
                    player_1_turn = False
                    
                    
                    
                    continue
            
             display_board()
             if check_winner(player_1_inputs) == 1:
                 print(f"{player_1_name} WON !! ")

                 player_1_inputs.clear()
                 player_2_inputs.clear()
                 

                 player_1_win = True
                 game_status = False
                 break

        

             while player_1_turn is False and player_2_attempts > 0:
                print(add_line)
           
                y =  player_move(input(f"{player_2_name} Please Enter Value:"), player_1_inputs, player_2_inputs)
                if y == 0: 
                    continue
                else:

                    player_2_inputs.append(y) 
                    player_2_attempts -= 1 
                    player_1_turn = True
                   
                  
                    
                    continue

             display_board()
             if check_winner(player_2_inputs) == 1:
                 print(f"{player_2_name} WON !! ")
                 player_1_inputs.clear()
                 player_2_inputs.clear()
                 player_2_win = True
               
                 game_status = False
                 break


        if player_1_win is True or player_2_win is True:
            pass
        else:
            print("Oh, It's DRAWWWW ! ")
            player_1_inputs.clear()
            player_2_inputs.clear()
            game_status = False
           

    print(add_line*2)
    print("Thank You for playing Tic, Tac, Toe by Sahil Bhatt. ")
    if player_1_win:
        return 0
    elif player_2_win:
        return 1
    else:
        return 2

    game_status = True 
    player_2_attempts = 4
    player_1_win = False
    player_2_win = False
   


########################################     GAME STARTS HERE       ##################################



print("Welcome to Tic, Tac, Toe game ! ")
print(add_line)
time.sleep(1)
player_1_name = input("Please enter player 1 name  : ")
print(f"{player_1_name}, Welcome to the game. You're 'X'. ")

print(add_line)
player_2_name = input("Please enter player 2 name  : ")
print(f"{player_2_name}, Welcome to the game. You're 'O'. ")

game_rules()


while True:
    result = game_play()
    if result == 0:
        player_1_score += 1
    elif result == 1:
        player_2_score += 1
    else:
        draw_score += 1



    while True:
        answer = str(input('Would you like to play again ? (y/n): ')).lower()
        if answer in ('y', 'n'):
            break
        print("invalid input.Plase choose correct input.")
    if answer == 'y':
        continue
    else:
       print(add_line*3)
       print("Final Score Tally : ")
       print(add_line)
       print(f"Total games : {(player_1_score+player_2_score+draw_score)} ")
  
       print(f"{player_1_name}: {player_1_score} {round(player_1_score/(player_1_score+player_2_score+draw_score),2)*100}% ")
 
       print(f"{player_2_name}: {player_2_score} {round(player_2_score/(player_1_score+player_2_score+draw_score),2)*100}% ")
    
       print(f"Draw: {draw_score} {round(draw_score/(player_1_score+player_2_score+draw_score),2)*100}% ")
       print(add_line*3)

       print("Thank you for playing ! Please close the window. ")
       break

'''

hangman = '''

import random
import time
from wordhoard import Definitions



lives = 5
unused_words = []
used_words = []
words = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose \
 hawk lion lizard llama mole monkey moose \
 mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan \
  tiger toad trout turkey turtle weasel whale wolf wombat zebra".split()



def add_line(a=1):
    print('\n'*a)

while True :
  game_word = words[random.randint(0,(len(words)-1))].lower()
  
  if len(game_word) >2 :
    break
  else:
    print(f"Tried this {game_word}")
   

def hangman(lives=len(game_word)):

  hint_valid = True
  symbol = '$'

  for w in game_word:
    if w not in unused_words:
      unused_words.append(w)

  while len(unused_words) > 0 and lives > 0:

    if lives == 1 and hint_valid is True: 
      print("Only 1 life left, play very carefully!! ")
      print("Do you need a hint? ")
      while True:
        hint = input("Y for yes and N for no:  ").lower()
        if hint == "y" or "n":
          break
        else:
          ("Make a valid Selection")
      if hint == "y":
        for w in game_word:
          if w not in used_words:
            print(f"Hint : {w}")
            unused_words.remove(w)
            used_words.append(w)
            hint_valid = False
            break
      elif hint == "n":
        ("Alright, go ahead without the help")
        hint_valid = False
        continue
          

    display_word = [letter if letter in used_words else  symbol  for letter in game_word] 
    add_line()
    print(f"Lives left: {lives} ")
      
    player_input = input(f" Word :   {''.join(display_word)}   ").lower()
    if len(player_input)>1:
        print("Incorrect : Please choose only 1 letter")
        print
        continue 

    if player_input in used_words:
        print("You have already used this letter, You DUMMY !! ")
        used_words.append(player_input)
        continue
            
    if player_input in game_word:
        unused_words.remove(player_input)
        used_words.append(player_input)        
        continue

    else: 
        used_words.append(player_input)
        lives -= 1  
      
    add_line()
  
  add_line(2)
  time.sleep(2)  
  if lives > 0: 
    print(f"Congratulations, you have guessed the word {game_word}")
  else:
    print(f"You have ran out of guesses. Please try again. Word was {game_word}!! ")
    

print("Welcome to Hangman ! ")
add_line()
time.sleep(1)
player_1_name = input("Please enter player name  : ")
time.sleep(1)
print(f"{player_1_name}, Goodluck for your game ")
time.sleep(1)
print("Setting up your Game ........")
time.sleep(2)
add_line(2)


definition = Definitions(search_string=game_word).find_definitions()
print(f"Definition of the word:  {definition[0]}")

hangman()

'''