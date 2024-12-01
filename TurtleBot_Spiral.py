# TURTLEBOT: Spiral çizimi

import turtle

# Ekranı Oluştur
screen = turtle.Screen()
screen.title("Merveral")
screen.bgcolor("Dark Red")

# Turtle Oluştur
spiral = turtle.Turtle()
spiral.speed(0)

# Spiral Çizme
colors = ["black","gray","pink","beige","brown"]

for i in range(100):
    spiral.color(colors[i % len(colors)])
    spiral.forward(i * 2)
    spiral.left(59)

screen.mainloop()