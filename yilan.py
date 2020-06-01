
import time
import turtle
import random
renkler = ["orange", "red", "yellow", "green", "brown", "purple"]
a = random.choice(renkler)
b = random.choice(renkler)
c = random.choice(renkler)
puan = 0
enyuksek=0
delay = 0.05
oyunAlani = turtle.Screen()
yilan = turtle.Turtle()
yiyecek = turtle.Turtle()
yilanvucut = turtle.Turtle()
notifier = turtle.Turtle()
yilanVucutParcalari = []

# oyun ekranı setupı

oyunAlani.title("CRAZY PYTHON")
oyunAlani.bgcolor("black")
oyunAlani.setup(width=600, height=600)
# ekranın her seferinde güncellenmesini kapat.
oyunAlani.tracer(0)

#yilan
yilan.speed(0)
yilan.shape("circle")
yilan.color(a)
# yilan ekranda hareket edecek.
yilan.penup()
yilan.goto(0,0)
yilan.direction = "stop"

# yiyecek
yiyecek.speed(0)
yiyecek.shape("square")
yiyecek.color(b)
yiyecek.penup()
#yiyeceği absolüt bir pozisyona yerleştir.
yiyecek.goto(0,100)

yilanvucut.speed(0)
yilanvucut.shape("square")
yilanvucut.color("gray")
yilanvucut.penup()
yilanvucut.hideturtle()
yilanvucut.goto(0, 260)
yilanvucut.write("Puan: 0  En Yüksek Puan: 0", align="center", font=("Arial", 22, "normal"))


# yönlere hareket kuralları
# gittiği yönün aksine tek seferde dönmemeli
def yukari():
    if yilan.direction != "asagi":
        yilan.direction = "yukari"

def asagi():
    if yilan.direction != "yukari":
        yilan.direction = "asagi"

def sola():
    if yilan.direction != "sag":
        yilan.direction = "sol"

def saga():
    if yilan.direction != "sol":
        yilan.direction = "sag"

def hareket():
    if yilan.direction == "yukari":
        y = yilan.ycor()
        yilan.sety(y + 20)

    if yilan.direction == "asagi":
        y = yilan.ycor()
        yilan.sety(y - 20)

    if yilan.direction == "sol":
        x = yilan.xcor()
        yilan.setx(x - 20)

    if yilan.direction == "sag":
        x = yilan.xcor()
        yilan.setx(x + 20)

def oyunuKapat():
	oyunAlani.bye()
#Klavye atamaları, yön tuşlarıyla oynanıyor. ESC ile çıkış yapılıyor.

oyunAlani.listen()
oyunAlani.onkeypress(yukari, "Up")
oyunAlani.onkeypress(asagi, "Down")
oyunAlani.onkeypress(sola, "Left")
oyunAlani.onkeypress(saga, "Right")
oyunAlani.onkeypress(oyunuKapat, "Escape")
count = 0

while True:
    oyunAlani.update()
    count += 1

    # Köşelerle çakışmayı kontrol et
    if yilan.xcor()>290 or yilan.xcor()<-290 or yilan.ycor()>290 or yilan.ycor()<-290:

        time.sleep(2)
        turtle.write("OYUN YENIDEN BAŞLIYOR!", align="center", font=("Arial", 26, "normal"))
        yilan.goto(0,0)
        yiyecek.goto(100,100)
        yilan.direction = "stop"
        # yılanı merkeze al
        for parca in yilanVucutParcalari:
            parca.goto(1000, 1000)

        # vücudu sil
        yilanVucutParcalari.clear()

        # skoru sıfırla
        puan = 0

        # delayı resetle
        delay = 0.05

        yilanvucut.clear()
        yilanvucut.write("Skor: {}  En Yüksek Skor: {}".format(puan, enyuksek), align="center", font=("Courier", 24, "normal"))


        # yiyecekle çakışmayı kontrol et
    if yilan.distance(yiyecek) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        yiyecek.goto(x,y)

        # yeni bir parça ekle
        yeniParca = turtle.Turtle()
        yeniParca.speed(0)
        yeniParca.shape("square")
        yeniParca.color(c)
        yeniParca.penup()
        yilanVucutParcalari.append(yeniParca)

        # yeni parça eklendikçe oyun hızlansın
        delay -= 0.001

        # puanı arttır
        puan += 10

        if puan > enyuksek:
            enyuksek = puan

        yilanvucut.clear()
        yilanvucut.write("Skor: {}  En Yüksek Skor: {}".format(puan, enyuksek), align="center", font=("Courier", 24, "normal"))

        #son parçayı başa al
    for index in range(len(yilanVucutParcalari)-1, 0, -1):
        x = yilanVucutParcalari[index-1].xcor()
        y = yilanVucutParcalari[index-1].ycor()
        yilanVucutParcalari[index].goto(x, y)

    # başlangıç parçasını kafa neredeyse oraya al
    if len(yilanVucutParcalari) > 0:
        x = yilan.xcor()
        y = yilan.ycor()
        yilanVucutParcalari[0].goto(x,y)

    hareket()


    # kafa ile vücut çakışması kontrolü
    for parca in yilanVucutParcalari:
        if parca.distance(yilan) < 20:
            turtle.write("OYUN YENIDEN BAŞLIYOR!", align="center", font=("Arial", 26, "normal"))
            time.sleep(1)
            yilan.goto(0,0)
            yilan.direction = "stop"


            for parca in yilanVucutParcalari:
                parca.goto(1000, 1000)


            yilanVucutParcalari.clear()


            puan = 0


            delay = 0.1

            # skor ekranını güncelle
            yilanvucut.clear()
            yilanvucut.write("Score: {}  High Score: {}".format(puan, enyuksek), align="center-top", font=("Courier", 24, "normal"))

    #ekranı bir süre uyut
    time.sleep(delay)

oyunAlani.mainloop()