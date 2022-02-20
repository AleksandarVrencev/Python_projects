# Craps Roller
# Demonstrates random number generation
# Aleksandar Vrencev
# 08.01.2017

# uvozi random modul
import random

# generate random numbers 1 - 6
# generise brojeve od 1 do 6
die1 = random.randint(1, 6)
# generise brojeve od 0 do 5 i svakom dodaje + 1
die2 = random.randrange(6) + 1

total = die1 + die2

print("You rolled a", die1, "and a", die2, "for a total of", total)

input("\n\nPress the enter key to exit.")
