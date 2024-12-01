# Birden fazla Turtle ile birden fazla işlem

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Ahmet ile Mehmet")

mehmet = turtle.Turtle()
ahmet = turtle.Turtle()

mehmet.color("red")
mehmet.pensize(5)
mehmet.shape("turtle")
mehmet.speed(1)

ahmet.color("blue")
ahmet.pensize(4)
ahmet.shape("arrow")
ahmet.speed(1)

# Mehmet Eşkenar Üçgen
for i in range(3):
    mehmet.forward(180)
    mehmet.left(120)
mehmet.right(180)
mehmet.forward(80)

# Ahmet Kare 
for i in range(4):
    ahmet.forward(50)
    ahmet.right(90)