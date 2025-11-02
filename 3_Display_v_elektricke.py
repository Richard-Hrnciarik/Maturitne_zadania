import tkinter
canvas = tkinter.Canvas(height = 100, width = 400, bg = 'black')
canvas.pack()

subor = open('zastavky.txt', 'r')
zastavky = []
for riadok in subor:
    zastavky.append(riadok)
subor.close()

i = -1
def zmena(event):
    global i
    if i < len(zastavky) - 1:
        i += 1
    else:
        i = 0
    kresli()

def kresli():
    global i, aktualna, x, dlzka, znovu
    aktualna = zastavky[i]
    canvas.delete('napis')
    dlzka = len(aktualna)
    for j in range(dlzka):
        x = j + 20
        canvas.create_text(x * 20 + 30, 50, text = aktualna[j], font = 'Arial 20', fill = 'red', tags = 'napis')
    znovu = dlzka * 20 + 30
    #animuj()

'''def animuj():
    global znovu
    if znovu > 0:
        canvas.move('napis', -5, 0)
        znovu -= 5
        print(znovu)
    else:
        znovu = dlzka * 20 + 430
        canvas.move('napis', +znovu + 400, 0)
    canvas.after(100, animuj)'''

'''def animuj():
    global znovu, x
    if znovu > 0:
        canvas.delete('napis')
        x -= 1
        canvas.after(100, kresli)
        znovu -= 5
        print(znovu)
    else:
        znovu = dlzka * 20 + 430
        canvas.move('napis', +znovu + 400, 0)
    canvas.after(100, animuj)'''

canvas.bind_all('<Key>', zmena)

canvas.mainloop()
print(zastavky)
