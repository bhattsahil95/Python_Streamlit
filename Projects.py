


ccv = '''


import re

def validate_card(card):
  p1 = re.compile(r'(((4|5|6)\d{3}-?\d{4}-?\d{4}-?\d{4}$))')
  p2 = re.compile(r"(\d)")
  p3 = re.compile(r'(\d)\1{3}')

# checking p1 
  valid_1 = False
  if p1.match(card):
    valid_1 = True

#Checking p3 using p2

  digits = []
  rep_digits = []
  valid_2 = False
  digits = re.findall(p2,card)
  rep_digits = re.findall(p3,''.join(digits))
  
  if rep_digits == []:
    valid_2 = True

  if valid_1 == valid_2 == True:
    print("Valid")
  else:
    print("Invalid")


n = int(input())
cards = []
for i in range(n):
  card = input()
  cards.append(card)


for e in cards:
  validate_card(e)


'''


tg = '''

while True:
  table_num = input("Please enter table_num: ")
  try:
    table_num = int(table_num)
    break

  except ValueError:
    print("Please use the correct format")

while True:
  till = input("Please enter range: ")
  try:
    till = int(till)
    break

  except ValueError:
    print("Please use the correct format")

x = 1 
while x <= till:
    y = table_num * x
    print(table_num, "*",x,"   =  ", y)
    x += 1
    


'''


ng = ''' 

from os import initgroups
import random
import time

### 
start = (time.time())
count = 0
up_limit = 0
down_limit = 0
min = 0
max = 1000000000
#nput = int(input(f"Please enter an integer from {min} to {max}: "))
# nput = random.randint(min,max)
nput = int(input())
print(f"Your selection is {nput}")
num1 = ""
print(num1)


while count<500:
    count += 1
    num1 = (min+max)//2
    print(f"We are trying {num1}")
    if nput > num1 and (nput-num1) > 1:
        min = num1
        down_limit += 1
        continue
    elif nput < num1 and (num1 - nput) > 1: 
        max = num1
        up_limit += 1
        continue
    elif nput > num1 and (nput - num1 ) == 1:
        num1 += 1
        break
    elif nput <num1 and (num1 - nput) == 1: 
        num1 -= 1
        break
    elif nput == num1:
        count -= 1
        break

print(f"Congratulations, you found the right number : {num1}")


print(f"Your total count was {count}")
print(f"Your total uplimit was {up_limit}")
print(f"Your total down limit was {down_limit}")

end = time.time()

print(f"Total compuation time {end-start}")


'''


wc = '''


import string

def word_count(a):
    
    for char in string.punctuation:
        if char in a:
            a = a.replace(char, "")

    b= (a.lower()).split()
    total = len(b)
    u_b = []
    c = {}

    for e in b:
        if e not in u_b:
            u_b.append(e)


 
    for el in u_b:
        c[el] = b.count(el)
    
 
    c_sorted = (sorted(c.items(), key = lambda x:(-x[1],x[0]), ))

    print(f"Total words {len(b)} \n")
    
    for e,i in c_sorted:
      print(f"{e} : {i} ({round((i*100/total),2)}%)  ")

    print(f"Top 3 words are {c_sorted[:3]} " )
   
    
    

word_count(input())



'''


bc = '''

while True:
  num1 = input("Please enter number 1: ")
  try:
    num1 = int(num1)
    break

  except ValueError:
    print("Please use the correct format")

while True:
  num2 = input("Please enter number 2: ")
  try:
    num2 = int(num2)
    break

  except ValueError:
    print("Please use the correct format")

while True: 
  opr = str(input("Please choose from Add, Sub, Mul, Div: "))
  try:
    if opr.lower() in ("add", "sub", "mul", "div", "+", "-","*","/"):
        break
  
  except:
    print("Please use correct opeartor")

if opr.lower() == "add" or opr == "+" :
  num3 = num1 + num2
elif opr.lower() == "sub" or opr == "-" :
  num3 = num1 - num2
elif opr.lower() == "mul" or opr == "*" :
  num3 = num1 * num2
elif opr.lower() == "div" or opr == "/" :
  num3 = num1 / num2
else:
  print("Invalid Selection")

print(num3)

print("{} of {} and {} are {}".format(opr,num1,num2,num3))



'''

pc2 = '''

import time
password = "!@"

def password_checker(password):
    
    valid = False
    upper = False
    lower = False
    digit = False
    length = False
    special_char = False

    print("Checking Password Length....")
    time.sleep (1)
    for i in password:
      if len(password) >= 8:
        length = True
        print("VALID")
        break
    if length is not True:
        print("NOT VALID")

    print("Checking Upper Case....")
    time.sleep (1)
    for i in password:
      if i.isupper():
        upper = True
        print("VALID")
        break
    if upper is not True:
        print("NOT VALID")

    
    print("Checking Lower Case....")
    time.sleep (1)
    for i in password:
      if i.islower():
        lower = True
        print("VALID")
        break
    if lower is not True:
        print("NOT VALID")


    print("Checking digits....")
    time.sleep (1)
    for i in password:
      if i.isdigit():
        digit = True
        print("VALID")
        break
    if digit is not True:
        print("NOT VALID")


    print("Checking special character....")
    time.sleep (1)
    for i in password:
      if i in string.punctuation:
        special_char = True
        print("VALID")
        break
    if special_char is not True:
        print("NOT VALID")


    if (digit and length and upper and lower and special_char == True):
      valid = True

    time.sleep(1)

    

    print("\n"*2)


    if valid is True:
      print("Your password is valid !")
    else: 
      print("Please re-enter your password, you knobhead!! ")


password_checker(password)



'''

pc1 = '''

from itertools import permutations 
length = False
upper_case = False
lower_case = False
punctuations = False
numbers = False
score = 0
Valid = False

import string

print(" Password Requirements : \n => Upper Case  \n =>  Lower Case \n => Special Character \n =>  Minimun length : 8")


while Valid != True:
    password = input("Please enter the secure password:  ")

    check = []
    for e in password:
        check.append(e)

    for el in check:
        if el.islower():
                lower_case = True
        if el.isupper():
                upper_case = True
        if el in string.punctuation:
                punctuations = True
        if el.isdigit():
                numbers = True

    if (upper_case and lower_case and punctuations and numbers == True) and len(password) >= 8:
        Valid = True


if Valid == True and len(check) >= 12: 
    print("Very Strong Password !! ")
    print(len(password))
 
elif Valid == True and len(check) >= 8 :
    print("Strong Password !! ")
    print(len(password))

check_all = permutations(check)

for i in check_all:
    score += 1
    if score >= 10000000:
        print("More than a Billion Possible combination for your password")
        break
print(f"Your password has possible {score} combinations")

'''

ls = '''


words = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose \
 hawk lion lizard llama mole monkey moose \
 mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan \
  tiger toad trout turkey turtle weasel whale wolf wombat zebra"

b = words.split()
find ="a"
position = 2
printed = []

for e in b:
  if e[0] not in printed:
    printed.append(e[0])
    print(f"Words starting with {printed[-1]}: ")
  if find in e:
    if e.index(find) == position-1:
      print(e)
    else:
      continue




'''