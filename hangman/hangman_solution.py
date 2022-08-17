from dis import dis
import random

def display_hangman(num_lives):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[num_lives]

class Hangman:

    def __init__(self, word_list, num_lives=6):
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ["_"]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_letters = []

        print(f"The mystery word has {len(self.word)} characters")
        print(display_hangman(num_lives))
        print(self.word_guessed)

    def check_letter(self, letter):
        
        if letter in list(self.word):
            self.list_letters.append(letter)
            for i in range(0, len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] = letter
                    self.num_letters -= 1
            print(f"'Nice! {letter} is in the word!")
            print(self.word_guessed)
            
        elif letter not in list(self.word):
            self.list_letters.append(letter)
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word")
            print(f"You have {self.num_lives} lives left")
            print(display_hangman(self.num_lives))

    def ask_letter(self):

        while True:
            letter = input("Please enter your letter: ")
            letter = letter.lower()
            if len(letter) != 1:
                print("Please, enter just one character")

            elif letter in self.list_letters:
                print(f"{letter} was already tried")
                    
            else:
                self.check_letter(letter)
                break
        
def play_game(word_list):
    game = Hangman(word_list, num_lives=6)
    while True:
        game.ask_letter()
        
        if '_' not in game.word_guessed:
            print("Congratulations, you won!")
            break
        
        elif game.num_lives == 0:
            print(f"You ran out of lives. The word was {game.word}")
            break

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
