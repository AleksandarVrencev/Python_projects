#Brojac
#Aleksandar Vrencev
#13.01.2017

print("Dobrodosli u brojac")

pocetak=int(input("Upisite pocetni broj:"))
kraj=int(input("Upisite zavrsni broj:"))
korak=int(input("Upisite korak po kojem brojimo:"))

for i in range(pocetak,kraj,korak):
    print(i)

print("Brojanje zavrseno")
input("Pritisnite enter za izlazak.")
