# Prodavac automobila
auto = float(input('Unesite cenu automobila: '))
porez = auto/100*10
reg = auto/100*5
pro_prodavca = 100
trans_troskovi = 50
print('\t Porez na kupovinu iznosi 10%: ',porez,'\n\
\t registracija iznosi 5%: ',reg,'\n\
\t provizija prodavca je : ',pro_prodavca,'\n\
\t i transportni troskovi su : ',trans_troskovi,'\n\
\t ukupna cena iznosi : ',auto+porez+reg+pro_prodavca+trans_troskovi) 
