# Guess My Number--Pogadjanje brojeva
# Aleksandar Vrencev
# 08.01.2017
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

# ucitava random modul
import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in 7 attempts\n")

# set the initial values
the_number = random.randint(1, 100)
tries = 1
guess = 0

# guessing loop
while tries <= 7 and the_number != guess:
    guess = int(input("Enter the number:"))
    tries+=1
    print(tries,"attempt")
    if guess < the_number:
        print("Higher...")
    elif guess > the_number:
        print("Lower...")

if tries > 7:
    print("\nSorry you reached the maximum number of tries.")
    print("\nGame Over")
    input("\nPress Enter to exit...")
elif the_number == guess:
    print("You guessed it!")
    print("\nThe secret number was",the_number,"!")
    print("\nAnd it took you",tries - 1,"attempts to guess!")
    input("\nPress Enter to exit...")
else:
    print("Something went wrong...")
    input("\nPress Enter to exit...")
