import builtins
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
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color('red')
    enemy.shape('invader.gif')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

bullet = turtle.Turtle()
bullet.coloer('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 70
bulletstate = "ready"

def move_left():
    x = player.xcor()
    x -=playerspeed
    if x < -280:
        x =- 280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound('laser.wav', winsound.SND_ASYNC)
        bulletstate = 'fire'
        x = player.xcor()
        y = player.ycor() +10 
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

# Make the keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main loop for the game

while True: