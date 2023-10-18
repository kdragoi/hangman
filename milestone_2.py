
#%%

# Task 1: Create and print a list of my favourite 5 fruits called "word_list"

word_list = ["apples", "bananas", "oranges", "grapes", "strawberries"]

print(word_list)

# %%

# Task 2: Using random import randomly generate a word from "word_list" and assign to variable "word"

import random

chosen_word = random.choice(word_list)

print(chosen_word)

# %%

# Task 3: Ask the user for an input and store value in variable "guess"

guess = input("Guess a single letter: ")

print(guess)

# %%

# Task 4: Use an if-else statement to validate input

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")

else:
    print("Oops! That is not a valid input")
