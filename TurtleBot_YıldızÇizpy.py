# Ekrana çizgi renki kırmızı dolgu rengi sarı olan bir yıldız çizen program yaz.

from turtle import *

shape("turtle")
color("red","yellow")
bgcolor("blue")
speed(1)

begin_fill()

for i in range(5):

    forward(100)
    right(144)
end_fill()