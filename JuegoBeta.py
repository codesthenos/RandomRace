from random import randint
from turtle import *

circuito = Screen()
circuito.setup(1500, 600)
circuito.bgcolor('plum2')

circuito.register_shape('Sara75x125.gif')
circuito.register_shape('Guille75x125.gif')

sara = Turtle()
guille = Turtle()

sara.penup()
guille.penup()

sara.shape('Sara75x125.gif')
guille.shape('Guille75x125.gif')

sara.setpos(-700,150)
guille.setpos(-700,-150)

winner = ''
while winner == '':
    input("TURNO DE GUILLE")
    g = randint(50,100)
    guille.fd(g)
    input("TURNO DE SARA")
    s = randint(50,100)
    sara.fd(s)
    if guille.pos()[0] >= 710:
        winner = 'El ganador es Guille'
    elif sara.pos()[0] >= 710:
        winner = 'La ganadora es Sara'
    else:
        winner = ''


circuito.mainloop()        
