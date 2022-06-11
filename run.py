import random

# Initial Steps to invite in the game:


def get_user_input(message):
    user_input = input(message).strip()
    return user_input

   
def rules_help():
    """ Displays rules to the user
    """
    rules = ''' \n <------------------------------------------------------------>
    \n \033[3;33m Rules: \033[0;0m \n
    The Hangman is a simple, word game 
    where the goal is to find the missing words.
    The theme of the game is 'Animals'\n
    1. From the list of animals a random word is generated.
    2. You will be presented with a number of blank spaces/n
    3. You must enter one letter.
    4. You can have only 8 guesses to find out the secret word.
    5. You can only use characters from the latin alphabet. 
    6. Use the keyboard to guess the letter. It is better to start with vowels.
    7. You wont be penalized for using symbol or number or for reusing the 
    letters.
    \n <------------------------------------------------------------>\n'''
    return rules


def intro():
    """ Welcoming user to the Hangman Game"
    """

    print("\nWelcome to Hangman game\n")
    name = input("Enter your name: ")
    print("Hello " + name + "! All the best!")
    print('''\n \033[3;33m***** Main menu *****\033[0;0m \n
        \033[1;33m(1)\033[0;0m HELP\n
        \033[1;32m(2)\033[0;0m PLAY\n
        \033[1;31m(3)\033[0;0m EXIT
        ''')

        







