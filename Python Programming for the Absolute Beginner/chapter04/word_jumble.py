# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word
# Aleksandar Vrencev
# 13.01.2017

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""
# dok word nije prazan
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
score = 100
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    hint=input("Would you like a hint? Y/n: ")
    if hint=="y":
        print("First letter is ",correct[0])
        score-=50
    guess = input("Your guess: ") 
    
if guess == correct and score==100:
    print("That's it!  You guessed it!\n")
    print("Because you never asked for hint you get",score,"points.\n")
elif guess == correct and score==50:
    print("That's it!  You guessed it!\n")
    print("Because you asked for hint you get",score,"points.\n")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
