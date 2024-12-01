# TURTLEBOT: Mandela

import turtle

# Ekranı Oluştur
screen = turtle.Screen()
screen.title("Mandela Deseni")

# Turtle Oluştur
mandela = turtle.Turtle()
mandela.speed(0)
mandela.width(3)

# Renk Paleti
colors = ["red","blue","green","yellow","black"]

# Mandela Oluşturma
for i in range(36):
    mandela.color(colors[i % len(colors)])
    mandela.circle(100)
    mandela.left(10)

screen.mainloop()