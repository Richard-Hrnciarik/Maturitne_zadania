import tkinter
from random import *
canvas = tkinter.Canvas(height = 400, width = 1400)
canvas.pack()

def tanier(x, y, pismeno):
    canvas.create_oval(x - 50, y - 50, x + 50, y + 50, fill = 'blue')
    canvas.create_text(x, y, text = pismeno, font = 'Arial 10', fill = 'white', tags = str(i))


x, y = 0, 100
pismeno = ['A','B','C','D','E','F','G','H','I','J']
puknuty_index = randint(0, 9)
puknuty = 'False ' * puknuty_index + 'True ' + 'False ' * (9 - puknuty_index)
print(puknuty)
for i in range(10):
    x += 125
    tanier(x, y, pismeno[i])

zoznam = [0] * 10
def klik(suradnice):
    tag = (canvas.gettags('current'))
    print(tag[0])
    if int(tag[0]) == puknuty_index:
        canvas.delete('all')
        canvas.create_text(700, 200, text = 'Gratulujem, oznacil si spravny tanier!', font = 'Arial 20', fill = 'blue')
        print(zoznam)
    else:
        cislo = int(zoznam[tag])
        cislo += 1
        zoznam = zoznam[:tag] + cislo + zoznam[tag + 1:]


canvas.bind('<Button-1>', klik)
canvas.mainloop()