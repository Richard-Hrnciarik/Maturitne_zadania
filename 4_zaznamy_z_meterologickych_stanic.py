subor = open('meteo_stanice.txt', 'r')
pocet_merani = 0
priemer = 0
najvyssia = -9999
print('Teploty: ')

for riadok in subor:
    pocet_merani += 1
    riadok.strip()
    if '+' in riadok:
        znamienko = riadok.find('+')
        kladne = True
    else:
        znamienko = riadok.find('-')
        kladne = False
    cislo = riadok[znamienko:znamienko + 5]
    cislo = cislo.replace(',', '.')
    if kladne == True:
        priemer += float(cislo)
    else:
        priemer -= float(cislo)
    if float(cislo[1::]) > float(najvyssia):
        najvyssia = cislo
        medzera = riadok.find(' ')
        najvyssie_2 = ' ' + riadok[:medzera]
    print(str(cislo))
najvyssia = najvyssia.replace('.', ',')

print('Pocet merani je: ' + str(pocet_merani))
print('Najvyssia namerana teplota je ' + str(najvyssia) + najvyssie_2)
print('Priemerna teplota je: ' + str(float(priemer)/pocet_merani))