import turtle
turtle.left(270)
for i in range(4):
    turtle.circle(100,90)
    turtle.left(180)
    turtle.circle(100,90) 
    turtle.seth(i*90)