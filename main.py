# coding=utf-8
# coding=utf-8

# Görsel işlemler için ilgili kütüphane ekleniyor
from visual import *

# Ekranda topun hızının yazılacağı yer, xPos ve yPos hazırlanıyor ve ilk değeri veriliyor
hizLabel =  label(pos=(-3, -2, 1), text='Hiz : 0')
xPosLabel = label(pos=(-3, 7, 1), text='xPos : 0')
yPosLabel = label(pos=(-3, 4, 1), text='yPos : 0')

xPos = ""
yPos = ""
inputMode = 1

#Kullanıcıdan değer alınıyor
# ilk sayi + enter = xPos
# ikinci sayi + enter = yPos
while(inputMode != 3):
        rate(50)
        if scene.kb.keys:
            s = scene.kb.getkey()
            if(s == '\n'):
                inputMode = inputMode + 1
            else:
                if(inputMode == 1):
                    xPos = str(xPos) + s
                if(inputMode == 2):
                    yPos = str(yPos) + s

xPosLabel.text = 'xPos : ' + str(xPos)
yPosLabel.text = 'yPos : ' + str(yPos)

# Ekranda kullanılacak olan top nesnesi oluşturuluyor,rengi, yarıçapı ve konumu ayarlanıyor
ball = sphere(pos=(int(float(xPos)), int(float(yPos)), 1), radius=1, color=color.red)
# Topun temas ediceği zemin oluşturuluyor, rengi ve konumu ayarlanıyor
floor = box(pos=(0, 0, 1), size=(10, 0.5, 10), color=color.green)


# Kullanılacak olan değişkenler ve ilk değerleri oluşturuluyor
t = 0.05
g = 10

# topun ilk konumundaki hızı ayarlanıyor
ball.velocity = vector(0, 0, 0)

# topun dikey konumu zeminden yukarıda kaldığı sürece çalışması için;
while (ball.pos.y > floor.pos.y + 1):
    # ekran yenileme
    rate(50)

    # topun dikey konumdaki hızı ve hızına göre konumu yeniden hesaplanıyor
    ball.velocity.y = ball.velocity.y - g * t
    ball.pos = ball.pos + ball.velocity * t
    if ball.pos.y < floor.pos.y + 0.5 + ball.radius:
        ball.velocity.y = -ball.velocity.y
    hizLabel.text = 'Hiz : ' + str(abs(ball.velocity.y - g * t))

hizLabel.text = 'Hiz : 0'