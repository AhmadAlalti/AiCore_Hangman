'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = [len(list(self.word)) * ["_"]]
        self.num_letters = len(list(self.word))
        self.num_lives = num_lives
        self.list_letters = []

        print(f"The mystery word has {len(self.word)} characters")
        print(self.word_guessed)

    def check_letter(self, letter):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        if letter in list(self.word):
            self.word_guessed[list(self.word).index(letter)] = letter
            self.num_letters -= 1
            print(f"'Nice! {letter} is in the word!")
            print(self.word_guessed)

        elif letter not in list(self.word):
            self.list_letters.append(letter)
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word")
            print(f"You have {self.num_lives} lives left")

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        print("Let's play! Please enter your letter")

        letter = input()

        while True:
            if len(letter) > 1:
                print("Please, enter just one character")
                letter = input()

            elif letter in self.list_letter:
                print(f"{letter} was already tried")
                    
            else:
                self.list_letter.append(str.lower(letter))
                break

        letter.checkletter(letter)

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations, you won!"
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"

    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
