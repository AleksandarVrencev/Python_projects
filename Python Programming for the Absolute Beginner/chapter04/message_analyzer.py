# Message Analyzer
#Prikazuje koriscenje len() funkcije
# i in operatora
# Aleksandar Vrencev
# 11.01.2017

message = input("Enter a message:")

print("\nThe length of your message is :",len(message))

print("\nThe most common letter in the English language,'e',")
if "e" in message:
    print("is in your message.")
else:
    print("is not in your message.")

input("\n\nPress the enter key to exit.")    
