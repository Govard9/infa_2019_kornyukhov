from graph import *
#Основной круг
brushColor("yellow")
circle(250, 300, 150)
#Левый большой глаз
brushColor("red")
circle(190, 270, 35)
#Правый большой глаз
brushColor("red")
circle(330, 270, 25)
#Правый глаз маленький
brushColor("black")
circle(330, 270, 10)
#Левый маленький глаз
brushColor("black")
circle(190, 270, 15)
#Рот
rectangle(330, 365, 160, 400)
#Левая бровь
polygon([(93,150), (100,140),
         (248,255), (240,265)])
#Правая бровь
polygon([(300,260), (293,250),
         (390,190), (398,200)])

run()
