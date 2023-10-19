#%%

# Creates class and methods needed for one round of hangman to play

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initializes the Hangman game.

        Parameters:
        - word_list (list): A list of words to choose from.
        - num_lives (int): Number of lives the player has. (Default 5)

        Initializes game state and selects a random word from the word_list.
        """

        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = []
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word and updates game state.

        Parameters:
        - guess (str): The guessed letter.

        Checks if the guess is correct, updates word_guessed and lives left.
        """

        guess = guess.lower()

        if self.word.count(guess) != 0:
            print(f"Good guess! {guess} is in the word")
            for letter in self.word:
                if letter == guess:
                    index = self.word.index(guess)
                    self.word_guessed[index] = guess
            self.num_letters -= 1
                
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left.")
            

    def ask_for_input(self):
        """
        Prompts the player to guess a letter and handle input validation.

        Repeatedly prompts the player until a valid letter is provided.
        """

        valid_input = True
    
        while valid_input == True :
            guess = input("Guess a letter: ")
    
            if len(guess) == 1 and guess.isalpha() == True:
                if self.list_of_guesses.count(guess) != 0:
                    print("You already tried that letter!")
                
                else:
                    break

            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
        
        self.check_guess(guess)
        self.list_of_guesses.append(guess)



# %%

# Creating function which executes the  game

def play_game(word_list):
    """
    Play a Hangman game with a given list of words.

    Parameters:
    - word_list (list): A list of words to choose from.

    This function initializes a Hangman game, prompts the player for input,
    and continues until the player wins or runs out of lives.
    """

    num_lives = 5 # Why are we assigning this when we have created a default parameter inside the __init__ method?
    game = Hangman(word_list, num_lives)
    continue_game = True
    while continue_game == True:
        print(game.word_guessed)
        game.ask_for_input()
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}")
            break
        elif game.num_letters == 0:
            print(f"Congratulations. You won the game! The word was {game.word}")
            break

        else:
            continue



#%%

# Code for execution and testing
import random
word_list = ["apples", "bananas", "oranges", "grapes", "strawberries"]

play_game(word_list)
