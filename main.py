from word_list import word_list 
from random import randint
import itertools

word = word_list[randint(0, len(word_list) - 1)].upper()
word_list = list(word.upper())
print(word) #TODO delete before final push
print(word_list)

count = 6

output = ""

print("_ _ _ _ _")
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
                output += guess_letter + " "
                #print green
            elif guess_letter in word:
                output += guess_letter + " "
                #print yellow
            else:
                output += guess_letter + " "
                #print grey
        print(output)

