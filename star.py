from turtle import*
import turtle
colours=['silver','green','purple','grey']
colours=['pitchblue','lemongreen']
draw =turtle.pen()
turtle.bgcolor('white')
pen = 1
speed(1)



for a in range(360):
    draw.pencolor(colours)
    draw.width(a/100+2)
    draw.forward(a)
    draw.left(-180)
    draw.right(30)
    
draw.hideturtle()