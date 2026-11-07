# "ROCK PAPER SCISSORS GAME USER VS COMPUTER"

# WorkFlow of The Game :
# 1. Input of the user (Rock,paper,Scissor)
# 2. Computer choice (Computer will choose randomly not conditionally)
# 3.Result print

# Cases :

# A - Rock
# Rock - Rock = tie 
# Rock - paper = paper win
# Rock - Scissor = Rock win

# B - Paper 
# paper - rock = paper win
# paper - paper = tie
# paper - scissor = scissors win 

# C - Scissor
# scissor - rock = rock win
# scissor - scissor = tie
# scissor - paper = scissor win

import random
item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your move Among(Rock,paper,Scissor) : ")
comp_choice = random.choice(item_list)

print(f"User Choice is : {user_choice}")
print(f"Computer Choice is : {comp_choice}")

if user_choice == comp_choice :
    print("Both Choose The Same Move [Match Tie]")

elif user_choice == "Rock" :
    if comp_choice == "paper" :
        print("Paper covers Rock ,So Computer Win")
    else :
        print("Rock smashes Scissor, So You Win")

elif user_choice == "Paper" :
    if comp_choice == "Scissor" :
        print("Scissor cuts Paper ,So Computer Win")
    else :
        print("Paper covers Rock , So You Win")


elif user_choice == "Scissor" :
    if comp_choice == "Paper" :
        print("Scissor cuts Paper ,So You Win")
    else :
        print("Rock samshes Scissor, So Computer Win")



