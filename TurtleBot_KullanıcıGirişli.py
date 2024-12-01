# Kullanıcıdan alınan kenar sayısı ile şekil çizelim.

import turtle

pencere = turtle.Screen()
pencere.title("Kullanıcıya Şekil Çizdirme")

tosbaga = turtle.Turtle()
tosbaga.shape("turtle")
tosbaga.color("red")
tosbaga.pensize(3)

kenar_sayisi = int(input("Kenar sayısı giriniz: "))
derece = kenar_sayisi / 360

for i in range(kenar_sayisi):
    tosbaga.forward(100)
    tosbaga.right(derece)
    pencere.exitonclick()
