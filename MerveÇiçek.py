# TURTLEBOT: Çokgen Çiçek Deseni

import turtle

# Ekran oluştur
screen = turtle.Screen()
screen.title("Seni Seviyorum")
screen.bgcolor("pink")

# Turtle Oluştur
flower = turtle.Turtle()
flower.speed(10)
flower.color("purple")

# Çokgen Çizme
def draw_polygon(side,length):
    angle = 360 / side
    
    for _i in range(side):
        flower.forward(length)
        flower.left(angle)

for _i in range(36): # 36 kez dönecek
    draw_polygon(6,50) # 6 kenarlı bir çokgen
    flower.left(10)

screen.mainloop()