# bacac novcica
# baca novcic 100 puta i prikazuje
# broj glava i pisama
# Aleksandar Vrencev
# 09.01.2017

import random

print("Bacamo novcic 100 puta i brojimo glave i pisma...\n")

glava = 0
pismo = 0
counter = 0

while counter < 100:
    novcic = random.randint(1,2)
    if novcic == 1:
        glava += 1
        counter += 1
        print("Glava")
    elif novcic == 2:
        pismo += 1
        counter += 1
        print("Pismo")
    else:
        print("Nesto je poslo naopako...")
        break

print("\nBroj glava:",glava,"\nBroj pisama:",pismo)
input("Pritisni Enter za izlazak...")
    
    
