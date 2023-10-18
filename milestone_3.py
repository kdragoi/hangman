#%%

# Code needed to generate chosen word for testing purposes
import random

word_list = ["apples", "bananas", "oranges", "grapes", "strawberries"]
chosen_word = random.choice(word_list)

#%%

# Task 1: Create a while loop for input validation

valid_input = True

while valid_input == True :
    guess = input("Guess a letter: ")
    
    if len(guess) == 1 and guess.isalpha() == True:
        break

    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

# %%

# Task 2: Check if the letter guessed is in the chosen word using a if-else statement

if chosen_word.count(guess) != 0:
    print(f"Good guess! {guess} is in the word")

else:
    print(f"Sorry, {guess} is not in the word. Try again")

# %%

# Task 3: Cleaning up code using functions

def check_guess(guess):
    standardised_guess = guess.lower()
    
    if chosen_word.count(guess) != 0:
        print(f"Good guess! {guess} is in the word")

    else:
        print(f"Sorry, {guess} is not in the word. Try again")


def ask_for_input():
    valid_input = True

    while valid_input == True :
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha() == True:
            break

        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    check_guess(guess)


ask_for_input()
