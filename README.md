# Hangman Project

Hangman is a classic game in which one player thinks of a word and the other player tries to guess that word, letter by letter, within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it by entering single letter guesses when promted to by the program. 

## Description

The program will select a random word from a given list of word and prompt the user to provide one lettered guesses. After each successful guess the program will display the word in the traditional hangman format with successfully guessed letters in their places (e.g " a , p , p , l , _ , _ "). User starts with a default of 5 lives for the game and the program will declare whether the player has won or lost along with the word that was initially chosen.


## Instructions of use

To play fully functioning game, the user must run the python file [`hangman.py`](hangman.py). Running this python file without modification will use a list of words defined my the author while testing. To modify the selection of words, `line 88` must be modified by the user.

To observe the development of the project, python files [`milestone_2.py`](milestone_files/milestone_2.py), [`milestone_3.py`](milestone_files/milestone_3.py) and [`milestone_4.py`](milestone_files/milestone_4.py) contain the code used to develop the final outcome. The code in these files are bookmarked by the task number and description in comments.

