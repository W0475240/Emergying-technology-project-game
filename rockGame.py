
"""
    Author: Shaghayegh Amouhossein
    Date: 28 Sep 2023.
    name: the Rock Paper Scissors game.
"""
import random
# Adding the welcome sentence
print("Welcome to the Rock Paper Scissors game");

# Ask question and give user optios
#print("Choose Rock, Paper or Scissors :")

# available options
options = ["Rock", "Paper", "Scissors" ]

# get the user user's choice
def get_user_choice():
    while True:
        userChoice = input("Choose Rock, Paper or Scissors :").lower()
        if userChoice in ["Rock, Paper or Scissors"]:
            return userChoice
        else:
            print("Your choice is invalid!! Please choose Rock, Paper or Scissors. ")
 
def get_computer_choice():
    computerChoice =["Rock", "Paper", "Scissors"]           


        if userChoice == "Rock":
                random_answer = random.choice(["Rock", "Paper", "Scissors"])
                answer = f" my answer is {random_answer}."


