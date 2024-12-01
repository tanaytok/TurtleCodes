import turtle

# Ekranı Oluştur
screen = turtle.Screen()
screen.title("Renkli Daireler")
screen.bgcolor("darkred")  # Arka plan rengini koyu kırmızı olarak ayarla

# Turtle Oluştur
circle_drawer = turtle.Turtle()
circle_drawer.speed(5)

# Renk listesi
renkler = ["black","gray","pink","beige","brown"]

# Daireleri çiz
for i in range(4):  # 4 daire çizmek için döngü
    renk = renkler[i % len(renkler)]  # Renk listesinden sırayla renk seç
    circle_drawer.color(renk)
    circle_drawer.circle(50)  # Yarıçapı 50 olan bir daire çiz
    circle_drawer.penup()
    circle_drawer.forward(100)  # Bir sonraki daire için pozisyonu değiştir
    circle_drawer.pendown()  # Çizimi tekrar başlat

screen.mainloop()
