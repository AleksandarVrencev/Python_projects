# Maitre D'
# Demonstrates treating a value as a condition
# Aleksandar Vrencev
# 08.01.2017

print("Welcome to the Chateau D' Food")
print("It seems we are quite full this evening.\n")

money = int(input("How many dollars do you slip the Maitre D'? "))

# ako je money vise ili manje od 0 vrednost te
# varijable je True i izvrsava se if statement
# ako je vrednost nula ili prazna crta vrednost je False
# i izvrsava se else statement

if money:
    print("Ah, I am reminded of a table.  Right this way.")    
else:
    print("Please, sit.  It may be a while.")

input("\n\nPress the enter key to exit.")

