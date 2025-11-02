import tkinter
canvas = tkinter.Canvas(height = 1000, width = 400)
canvas.pack()

subor = open('noty.txt', 'r')
noty = subor.readline()
x, y = 10, 50

def kresli():
    global x, y, poloha, noty
    for i in range(0, 41, 10):
        canvas.create_line(0, i + y, 400, i + y)
    if noty[0] == 'c':
        poloha = 0
    elif noty[0] == 'd':
        poloha = 3
    elif noty[0] == 'e':
        poloha = 6
    elif noty[0] == 'f':
        poloha = 9
    elif noty[0] == 'g':
        poloha = 12
    else:
        poloha = 15
    canvas.create_oval(x - 5, y - 3 + poloha, x + 5, y + 3 + poloha)
    noty = noty[1::]
    x += 15

for i in range(len(noty) // 400):
    for i in range(400//15):
        kresli()
        #noty = noty[(400//15)::]
    y += 100
    x = 10

y += 100
x = 10
for i in range(len(noty) % 15):
    kresli()
canvas.mainloop()