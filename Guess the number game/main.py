#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

hard_tentatives = 5
easy_tentatives = 10

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
answer = input("Do you wanna play? 'hard' or 'easy'?\n")

tentatives_left = hard_tentatives if answer == 'hard' else easy_tentatives
number_to_guess = random.randint(0, 100)

print(f"You have {tentatives_left} attempts to guess the number.")

while tentatives_left > 0:
    number_guessed = int(input("Make a guess: "))
    
    if number_guessed < number_to_guess:
        print(f"Too low.\nYou have {tentatives_left} more guess.\n")
    elif number_guessed > number_to_guess:
        print(f"Too high.\nYou have {tentatives_left} more guess.\n")
    else:
        print(f"You got it! The answer is {number_guessed}")
        tentatives_left = 0
    
    if tentatives_left == 0:
        print("You have no more tries left!\n")
    
    tentatives_left -= 1
