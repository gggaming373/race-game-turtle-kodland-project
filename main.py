
import turtle
import random

t = turtle.Turtle()
t.up()
t.goto(-100,100)
t.down()
t.speed(0)


# yarış pisti
for a in range(15):
    t.write(a)
    t.right(90)
    t.forward(200)
    t.backward(200)
    t.left(90)
    t.forward(20)
t.right(90)
t.forward(200)
t.right(90)
t.forward(300)
t.hideturtle()


p1 = turtle.Turtle()
p1.shape("classic")
p1.color("#4958CA")
p1.up()
p1.goto (-110, 80)
p1.down()

p2 = turtle.Turtle()
p2.shape("classic")
p2.color("#E88181")
p2.up()
p2.goto (-110, 60)
p2.down()

p3 = turtle.Turtle()
p3.shape("classic")
p3.color("#FAD460")
p3.up()
p3.goto (-110, 40)
p3.down()


for a in range(random.randint(1,10)):
    taraftar = turtle.Turtle()
    taraftar.up()
    taraftar.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    taraftar.backward(a*-20)
    taraftar.left(90)
    taraftar.backward(110)



kazanan = input ("Hangi kablumbağa kazanacak:")
yazi = turtle.Turtle()
yazi.up()
yazi.goto(-120,120)
yazi.write(kazanan +" kablumbağanın kazanacağını düşünüyorsunuz ")

x_p1 = 0
x_p2 = 0
x_p3 = 0

while x_p2 < 350 or x_p1 < 350 or x_p3 < 350:
    r1 = random.randint(1, 5)
    x_p1 += r1
    p1.forward(r1)
    r2 = random.randint(1, 5)
    x_p2 += r2
    p2.forward(r2)
    r3 = random.randint(1, 5)
    x_p3 += r3
    p3.forward(r3)
if x_p1 > x_p2 and x_p1 > x_p3:
    print("1. Oyuncu Kazandı")
    printwinner = turtle.Turtle()
    printwinner.write("1. Oyuncu Kazandı")
elif x_p2 > x_p1 and x_p2 > x_p3:
    print("2. Oyuncu Kazandı")
    printwinner = turtle.Turtle()
    printwinner.write("2. Oyuncu Kazandı")
elif x_p3 > x_p2 and x_p3 > x_p1:
    print("3. Oyuncu Kazandı")
    printwinner = turtle.Turtle()
    printwinner.write("3. Oyuncu Kazandı")


