#%%

# Creates class and methods needed for one round of hangman to play

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = []
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()

        if self.word.count(guess) != 0:
            print(f"Good guess! {guess} is in the word")
            for index in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
                
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left.")
            

    def ask_for_input(self):
        valid_input = True
    
        while valid_input == True :
            guess = input("Guess a letter: ")
    
            if len(guess) == 1 and guess.isalpha() == True:
                break
            
            elif self.list_of_guesses.count(guess) != 0:
                print("You already tried that letter!")

            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
        
        self.check_guess(guess)
        self.list_of_guesses.append(guess)



# %%

# Initiates one round of the game 

import random
word_list = ["apples", "bananas", "oranges", "grapes", "strawberries"]

hangman_game = Hangman(word_list)
hangman_game.ask_for_input()
