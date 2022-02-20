# Kolacici srece
# Prikazuje koriscenje random modula
# Aleksandar Vrencev
# 09.01.2017

import random

rand_num = random.randint(1,5)

kolac_1 = "Pazi sta zelis,mozda ti se i ostvari."
kolac_2 = "Rad te cini zdravim."
kolac_3 = "Bez bola nema napretka."
kolac_4 = "Strpljen,spasen"
kolac_5 = "Posten i lud,dva brata"

if rand_num == 1:
    print("Vas kolacic srece kaze: \n\t",kolac_1)
elif rand_num == 2:
    print("Vas kolacic srece kaze: \n\t",kolac_2)    
elif rand_num == 3:
    print("Vas kolacic srece kaze: \n\t",kolac_3)
elif rand_num == 4:
    print("Vas kolacic srece kaze: \n\t",kolac_4)
elif rand_num == 5:
    print("Vas kolacic srece kaze: \n\t",kolac_5)
else:
    print("Something went wrong...")

input("Pritisni enter za izlazak")    
