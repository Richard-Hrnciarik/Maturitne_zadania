subor = open('objednane_jedla.txt', 'r')
pocet, zelena, cervena, modra, oranzova = 0, 0, 0, 0, 0
for riadok in subor:
    pocet += 1
    medzera = riadok.find(' ')
    if riadok[medzera+1] == 'z':
        zelena += 1
    elif riadok[medzera+1] == 'c':
        cervena += 1
    elif riadok[medzera+1] == 'm':
        modra += 1
    else: #riadok[medzera+1] == 'o'
        oranzova += 1

print('Celkovy pocet jedal: ' + str(pocet))
print('Pocet zelenych: ' + str(zelena))
print('Pocet cervenych: ' + str(cervena))
print('Pocet modrych: ' + str(modra))
print('Pocet oranzovych: ' + str(oranzova))

if zelena < 20 or cervena < 20 or modra < 20 or oranzova < 20:
    print('Malo objednanych:')
    if zelena < 20:
        print('z')
    if cervena < 20:
        print('c')
    if modra < 20:
        print('m')
    if oranzova < 20:
        print('o')
else:
    print('Vsetkych jedal je objednanych dostatok.')
