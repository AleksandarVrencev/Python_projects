#Pisanje pseudokoda i izrada programa
#Kompjuter pogadja broj
#izabran od strane igraca
#Aleksandar Vrencev
#10.01.2017

import random

print("\tZdravo")
print("\nU ovoj igri vi birate broj a racunar \
ima zadatak da ga pogodi.")

broj = int(input("\nIzaberite broj izmedju 1 i 100:"))
counter = 0
racunar = 0

while racunar != broj:
    counter+=1
    racunar = random.randint(1,100)
    if racunar < broj:
        print("Racunaru biraj veci broj")
    elif racunar > broj:
        print("Racunaru biraj manji broj")

print("\n\tBravo pogodio si,trazeni broj je",broj)
print("\tPogodio si iz",counter,"pokusaja.")
input("\tPritisni Enter da izadjes iz igre...")


#Pseudokod

#Komentari
#Objasnjenje igre
#Igrac bira broj
#Racunar pogadja------------
#Ako pogodi,cestitka------Pogadjacka petlja
#Ako ne pogodi,Game Over----
#Izlazak iz igre
