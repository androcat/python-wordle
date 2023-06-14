from word_list import word_list 
from random import randint

from colorama import init as colorama_init
from colorama import Fore, Style
import itertools

colorama_init()

word = word_list[randint(0, len(word_list) - 1)].upper()
word_list = list(word.upper())

count = 6

output = ""

print(f"Welcome to {Fore.GREEN}W{Style.RESET_ALL}O{Fore.YELLOW}RD{Style.RESET_ALL}L{Fore.GREEN}E{Style.RESET_ALL}")
while count > 0:
    guess = input("Enter a 5-letter word: ").upper()
    guess_list = list(guess)
    count -= 1
    if guess == word:
        print("You win! You guessed",word,"correctly in",count,"guesses.")
        break
    else:
        for (guess_letter, word_letter) in zip(guess_list, word_list):
            if guess_letter == word_letter:
                output += f"{Fore.GREEN}"+guess_letter + f"{Style.RESET_ALL} "
                #print green
            elif guess_letter in word:
                output += f"{Fore.YELLOW}"+guess_letter + f"{Style.RESET_ALL} "
                #print yellow
            else:
                output += f"{Style.RESET_ALL}"+guess_letter + " "
                #print grey
        print(output)
        output = ""

