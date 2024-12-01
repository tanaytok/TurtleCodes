# Ekrana dolgu rengi sarı ve kenar çizgi renkleri birbirinden farklı kare çizen program.

from turtle import *

shape("turtle")
color("yellow")
begin_fill()
pensize(4)
speed(1)

for renk in ["black","violet","cyan","red"]:
    pencolor(renk)
    forward(200)
    right(90)
end_fill()

