""" Importing libraries to use in system.
Import random allows access to the random modules,
creates random number generation.
Hangman words are imported from file words.py
Hangman stages are imported from status.py
Import time represents time in code
Os module provides functions for creating
and removing directory.
"""

import os
import random
import time

from status import HANGMAN_STAGE
from words import computer_names

ATTEMPTS = "global"
DISPLAY = "global"
WORD = "global"
ALREADY_GUESSED = "global"
LENGTH = "global"
PLAY_GAME = "global"
ORIGINAL_WORD = "global"
MAX_ATTEMPTS = 5
USERNAME = None


def get_user_detail():
    """
    get user name and store it in the username
    """
    global USERNAME
    # Initial Steps to invite in the game:
    print("\nWelcome to Hangman game\n")
    USERNAME = input("Please enter your name: ")
    print("Hello " + USERNAME + "! Good Luck!" "The game is about to start")


def rules_help():
    """ Displays rules to the user
    """
    rules = ''' \n <------------------------------------------------------------>
    \n \033[3;33m Rules: \033[0;0m \n
    The Hangman is a simple, WORD game
    where the goal is to find the missing words.
    The theme of the game is 'Computer'\n
    1. From the list of computer-words a random WORD is generated.
    2. You will be presented with a number of blank spaces/n
    3. You must enter one letter.
    4. You can have only 5 guesses to find out the secret WORD.
    5. You can only use characters from the latin alphabet.
    6. Use the keyboard to guess the letter. It is better to start with vowels.
    7. You wont be penalized for using symbol or number or for reusing the
    letters.
    \n <------------------------------------------------------------>\n'''
    return rules


# Initializing all the conditions required for the game:
def initialize_game():
    """ Displays the parameters used in the game
    """
    global ATTEMPTS
    global DISPLAY
    global WORD
    global ALREADY_GUESSED
    global LENGTH
    global PLAY_GAME
    global ORIGINAL_WORD
    global MAX_ATTEMPTS
    ATTEMPTS = 0
    WORD = random.choice(computer_names)
    ORIGINAL_WORD = WORD
    LENGTH = len(WORD)
    DISPLAY = '-' * LENGTH
    ALREADY_GUESSED = []
    PLAY_GAME = ""
    MAX_ATTEMPTS = 5
    get_user_detail()


# A loop to re-execute the game when the first round ends


def game_loop():
    """ This function will be executed when the first round of the game ends
    """
    global PLAY_GAME
    PLAY_GAME = input("Do you want to play again? y = yes, n = no \n")
    while PLAY_GAME not in ["y", "n", "Y", "N"]:
        PLAY_GAME = input("Do You want to play again? y = yes, n = no \n")
    if PLAY_GAME == "y":
        initialize_game()
    elif PLAY_GAME == "n":
        print("Thank you for Playing! We expect you back again!")
        exit()


def is_user_ready_to_play():
    """check_if_user_needs_help"""
    is_help_needed = input(
        f"Hey {USERNAME}, Do You want help? y = yes, n = no \n").lower()
    while is_help_needed == 'y':
        play_rules = rules_help()
        print(play_rules)
        is_help_needed = input("Do You want help? y = yes, n = no \n").lower()
    return True


def is_guess_included_in_word(guess):
    """ This function checks if the guess entered by user is
        present in the word or not. If present, the guess will
        be displayed in the blank spaces.
    """
    global WORD, DISPLAY

    ALREADY_GUESSED.extend([guess])
    index = WORD.find(guess)
    # print(f"ALREADY_GUESSED: {ALREADY_GUESSED}")
    # print(f"WORD: {WORD}")

    if index < 0:
        return False
    # Loop as along as there as letters to replace
    while index >= 0:
        WORD = WORD[:index] + "_" + WORD[index + 1:]
        DISPLAY = DISPLAY[:index] + guess + DISPLAY[index + 1:]
        index = WORD.find(guess, index)
    return True


def increase_attempts():
    """This function is to count increased attempts"""

    global ATTEMPTS, MAX_ATTEMPTS
    ATTEMPTS += 1
    print(f"Attempted {ATTEMPTS}")


def display_remaining_attemts():
    """Displays remaining attempts="""
    global MAX_ATTEMPTS, ATTEMPTS
    if ATTEMPTS in [0, 1, 2]:
        print(str(MAX_ATTEMPTS - ATTEMPTS) + " guesses remaining\n")
    elif ATTEMPTS == 3:
        attemtps = MAX_ATTEMPTS - ATTEMPTS
        print(f"{attemtps} last guess remaining\n")
    elif ATTEMPTS == 4:
        print("Sorry!! You have lost this game. You are hanged!!!\n")
        # print the correct WORD
        print("The WORD was:", ORIGINAL_WORD)
        # game_loop()
    # print(f"{ALREADY_GUESSED}")


def display_hangman_status():
    """Displays hangman status on screen"""

    global MAX_ATTEMPTS, ATTEMPTS
    # print(ATTEMPTS)
    print(HANGMAN_STAGE[ATTEMPTS])


def clear_screen():
    """This function to clear the screen and delay execution time """
    time.sleep(3)
    os.system("clear")


def is_winner():
    """ This function checks whether all the guesses entered by the user
        are actually present in original word. If all the guesses are correct,
        the player wins the game.
    """
    global WORD, LENGTH, ATTEMPTS, MAX_ATTEMPTS
    if WORD == '_' * LENGTH:
        print("Congrats! You have won this game!")
        return True
    elif ATTEMPTS != MAX_ATTEMPTS:
        return False


def play_game():
    """ Play_game function is the core part of the game.
    This is responsible for initializing all the conditions
    required to guess, DISPLAY letters and formation of
    hangman structure
    """
    global ATTEMPTS
    global DISPLAY
    global WORD
    global ALREADY_GUESSED
    global MAX_ATTEMPTS

    while ATTEMPTS < MAX_ATTEMPTS:
        guess = input("This is the Hangman WORD: " +
                      DISPLAY + "\nEnter your guess: \n").strip()

        if len(guess.strip()) > 1 or not guess.isalpha():
            print("Input is Invalid, Try a letter\n")
        elif guess in ALREADY_GUESSED:
            print("Try another letter.\n")
        elif is_guess_included_in_word(guess):
            # print("Debug-> is included")
            display_remaining_attemts()
            display_hangman_status()
        else:
            # print("Debug-> invalid choice made")
            display_remaining_attemts()
            display_hangman_status()
            increase_attempts()
            clear_screen()
        if is_winner():
            break
        time.sleep(1)


def init_game_engine():
    """
    This function intializes game again
    """
    initialize_game()
    if is_user_ready_to_play():
        print("Starting Game....!\n Let's play...!")
        os.system('clear')
        play_game()


if __name__ == "__main__":
    while True:
        init_game_engine()
