"""
    Author: Shaghayegh Amouhossein
    Date: 28 Sep 2023.
    name: the Rock Paper Scissors game.
"""
import random
# Adding the welcome sentence
def display_welcome_message():
    print("Welcome to the Rock Paper Scissors game")

# Call this function 
display_welcome_message()


# Ask question and give user optios

# available options
options = ["Rock", "Paper", "Scissors" ]

# get the user user's choice
def get_user_choice():
    while True:
        userChoice = input("Choose Rock, Paper or Scissors :").lower()
        if userChoice.lower() in ["rock", "paper", "scissors"]:
            return userChoice
        else:
            print("Your choice is invalid!! Please choose Rock, Paper or Scissors. ")
            
 # option for cumputer's choice
def get_computer_choice():
    
    return random.choice(["Rock", "Paper", "Scissors"])
    
# function for deciding who wins
def determine_the_winner(userChoice, computerChoice):
    if userChoice == computerChoice:
        return "It is a tie! Please try again."
         
    elif ( 
        (userChoice == "rock" and computerChoice == "scissors") or 
        (userChoice == "scissors" and computerChoice == "paper") or
        (userChoice == "paper" and computerChoice == "rock")
):
        
            return "You win!"
    else: 
            return "Computer wins!"

# Main game loop
while True:
    userChoice = get_user_choice()
    computerChoice = get_computer_choice()
    print(f"You chose {userChoice}, and the computer chose {computerChoice}.")
    result = determine_the_winner(userChoice, computerChoice)
    print(result)
    
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ["yes", "no"]:
            break
        else:
            # invalid choice for yes or no
            print("Invalid choice! Please enter 'yes' or 'no'.")

    if play_again == "no":
        break

print("Thank you for playing the Rock Paper Scissors game!")
