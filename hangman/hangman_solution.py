import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = [len(list(self.word)) * ["_"]]
        self.num_letters = len(list(self.word))
        self.num_lives = num_lives
        self.list_letters = []

        print(f"The mystery word has {len(self.word)} characters")
        print(self.word_guessed)

    def check_letter(self, letter):

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

    while "_" in game.word_guessed:
        game.ask_letter()

    if game.num_letters == 0:
        print("Congratulations, you won!")
    elif game.num_lives == 0:
        print(f"You ran out of lives. The word was {game.word}")

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
