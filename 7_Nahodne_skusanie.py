from random import *
studenti = input('Zadaj pocet studentov: ')
otazky = input('Zadaj pocet otazok: ')
cislo = []
otazky_2_parne, otazky_2_neparne = [], []
vybrate, vybrate_otazky = [], []
podmienka, podmienka_otazky = True, True
parne = False

if int(otazky) > int(studenti):
    for i in range(1, (int(studenti) + 1)):
        cislo.append(i)
    for i in range(1, (int(otazky) + 1)):
        if i % 2 == 0:
            otazky_2_parne.append(i)
        else:
            otazky_2_neparne.append(i)

    print('Poradie odpovedajucich a ich cislo otazky:')
    for i in range(int(studenti)):
        podmienka = True
        while podmienka == True:
            jedno = choice(cislo)
            if jedno not in vybrate:
                vybrate.append(jedno)
                podmienka = False
        podmienka_otazky = True
        while podmienka_otazky == True:
            if parne == True:
                jedna = choice(otazky_2_parne)
            else:
                jedna = choice(otazky_2_neparne)
            if jedna not in vybrate_otazky:
                vybrate_otazky.append(jedna)
                podmienka_otazky = False
        print(str(i + 1) + '. student: ' + str(vybrate[i]) + ', otazka: ' + str(vybrate_otazky[i]))
        if parne == True:
            parne = False
        else:
            parne = True
else:
    print('Nie je dostatok otazok.')
