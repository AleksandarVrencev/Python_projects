# Exclusive Network
# Demonstrates logical operators and compound conditions
# Aleksandar Vrencev
# 08.01.2017

print("\tExclusive Computer Network")
print("\t\tMembers only!\n")

security = 0
# kada je username prazno,odnosno 0 ili "" ima vrednost False
username = ""
# ako je username False, not username je True i obrnuto
while not username:
    username = input("Username: ")

password = ""
while not password:
    password = input("Password: ")
# ako su oba uslova tacna stampaj poruku koja sledi
if username == "M.Dawson" and password == "secret":
    print("Hi, Mike.")
    security = 5
elif username == "S.Meier" and password == "civilization":
    print("Hey, Sid.")
    security = 3
elif username == "S.Miyamoto" and password == "mariobros":
    print("What's up, Shigeru?")
    security = 3
elif username == "W.Wright" and password == "thesims":
    print("How goes it, Will?")
    security = 3
# ako je bar jedan uslov tacan stampaj poruku koja sledi    
elif username == "guest" or password == "guest":
    print("Welcome, guest.")
    security = 1
# ako nista nije tacno stampaj poruku koja sledi    
else:
    print("Login failed.  You're not so exclusive.\n")

input("\n\nPress the enter key to exit.")
