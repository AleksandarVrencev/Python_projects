#Pogadjanje reci
#Aleksandar Vrencev
#13.01.2017

import random

WORDS=("igra","sport","porodica","pisanje","lopta","knjiga")

word=random.choice(WORDS)
correct=word
jumble=""

print("Racunar bira rec,a vas zadatak je da pogodite koja je to rec.\n")
print("Izabrana rec ima",len(correct),"slova\n")
print("Imate pravo da 10 puta pogadjate koje slovo sadrzi izabrana rec.\n")
print("Racunar ce odgovoriti sa da ili ne.")

for i in range(10):
    pitanje=input("Izaberite slovo:")
    if pitanje in correct and pitanje !="":
        print("da")
        jumble+=pitanje
    else:
        print("ne")

print("Izabrana rec sadrzi slova",jumble)
kon_odg=input("Koji je vas konacan odgovor:")

if kon_odg == correct:
    print("Bravo pogodili ste.")
else:
    print("Nazalost niste pogodili.")

input("Pritisnite enter za izlazak.")
