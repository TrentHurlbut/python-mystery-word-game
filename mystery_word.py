#READ IN FILE
#CLEAN FILE AND BREAK INTO LIST [MAY BE A GOOD IDEA TO USE STOP WORDS TO FILTER]
#SELECT WORD FROM LIST
#CREATE LIST OF BLANKS WHICH MATCHES LENGTH OF WORD
#CREATE LIST TO HOLD GUESSED LETTERS
#CREATE PROMPT FOR USER TO GUESS LETTERS
#CHECK INPUT: IS IT A LETTER? IS IT A LETTER THAT HAS ALREADY BEEN GUESSED? THROW ERROR
#IF IT'S A LETTER THAT HASN'T BEEN GUESSED, IS IT IN THE WORD?
#IF IT'S IN THE WORD, UPDATE BLANKS LIST. IF IT'S NOT, KEEP TRACK OF BAD GUESSES.
#EITHER WAY, UPDATE GUESSED LETTER LIST.
#WIN/LOSE CON.

import string
import random

"""WELCOME TO THE PYTHON MYSTERY WORD GAME! A word is randomly selected from
a read-in text file and the user has to submit letters in order to correctly
guess the word. The word is stored in a list, there is also a list of blanks
which displays and updates based on correct guesses, and there is a third
list which stores guessed letters. The user gets 8 guesses."""

STOP_WORDS = [
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "he",
    "i",
    "in",
    "is",
    "it",
    "its",
    "of",
    "on",
    "that",
    "the",
    "to",
    "were",
    "will",
    "with",
]

def mystery_word_game(file):
    
    mystery_word_letter_list = list(generate_random_word(file))
    blanks_list = ["_" for letter in mystery_word_letter_list]
    guessed_letter_list = []

    print('WELCOME TO THE MYSTERY WORD GAME! A word has randomly been selected from the English language and it is your job to guess what it is!')

    while "_" in blanks_list or len(guessed_letter_list) < 8:
        guess = input('Please make a guess: ')

        if len(guess) != 1 or type(guess) != 'string':
            print('Ooooooh... I\'m so sorry that was not a letter.')
        else:
            pass
        
        


def generate_random_word(text_file):

    """This function opens the text file, removes all punctuation, converts it
    to lowercase, creates a list where each word is an index, and selects a random
    word from the list."""

    with open(file) as text:
        content = text.read()
        formatted_content = content.replace(string.punctuation, "")
        word_list = (
            formatted_content.replace("-", " ")
            .replace("—", " ")
            .replace(".", "")
            .replace(",", "")
            .replace(":", "")
            .replace("'", "")
            .replace('"', "")
            .replace("-\n", "")
            .lower()
            .split()
        )
    
    return random.choice(word_list)








if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description="Get the word frequency in a text file."
    )
    parser.add_argument("file", help="file to read")
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        mystery_word_game(file)
    else:
        print(f"{file} does not exist!")
        exit(1)