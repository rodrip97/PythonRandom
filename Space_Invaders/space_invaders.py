import turtle
import winsound
import math
import random

#Setting up the screen
wn = turtle.screen()
wn.bgcolor('black')
wn.title('Alien Invaders v1.0')
wn.bgpic('Space_invaders_background.gif')

#creating and registering the shapes
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
    border_pen.hideturtle()

#set the score
score = 0

#draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = 'Score: %s' %score
score_pen.write(scorestring, False, align='left', font=('Arial',14,'normal'))
score_pen.hideturtle()

#create the player
player = turtle.Turtle()
player.color('blue')
player.shape('player.gif')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15


enemyspeed = 2
number_of_enemies = 5
enemies = []


for i in range(number_of_enemies):
    