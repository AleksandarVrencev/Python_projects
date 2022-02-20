#Pizza Slicer
#Prikazuje isecanje znakovnih nizova
#Aleksandar Vrencev
#12.01.2017

word="pizza"

print(
"""
 Slicing 'Cheat Sheet'

 0   1   2   3   4   5
 +---+---+---+---+---+ 
 | p | i | z | z | a | 
 +---+---+---+---+---+ 
-5  -4  -3  -2  -1

"""
)

print("Enter the beginning and ending index for your slice of'pizza'.")
print("Press the enter key at 'Begin' to exit.")

start= None
#Dok start nije None/False/Empty pokreci start a zatim finish
#kada pitanje Start ostavis prazno petlja se prekida.
while start !="":
    start=(input("\nStart:"))

    if start:
        start=int(start)

        finish=int(input("Finish:"))

        print("word[",start,":",finish,"] is ",end="")
        print(word[start:finish])

input("\n\nPress the enter key to exit.")
