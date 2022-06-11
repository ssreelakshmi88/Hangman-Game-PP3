import random

# Initial Steps to invite in the game:

def user_name_input():
    user_name = input ("Please enter your name")
    print("Hello +name")

def rules_game():
    """ Displays rules to the user
    """
    rules = ''' \n <------------------------------------------------------------>
    \n \033[3;33m Rules: \033[0;0m \n
    The Hangman is a simple, word game where the goal is to find the missing word or words.
    The theme of the game is 'Animals'\n
    1. From the list of animals a random word is generated.
    2. You will be presented with a number of blank spaces representing the missing letters/n
    3. You must enter one letter.
    4. You can have only 8 guesses to find out the secret word.
    5. You can only use characters from the latin alphabet. 
    6. Use the keyboard to guess the letter. It is better to start with vowels.
    7. You wont be penalized for using symbol or number or for reusing the letters.
    \n <------------------------------------------------------------>\n'''
    return rules

def introduction():
    print("\nWelcome to Hangman game\n")






