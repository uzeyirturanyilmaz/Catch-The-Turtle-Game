import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ("Arial", 25, "normal")
score = 0
gameOver = False

#turtlelist

turtleList = []

#score
tScore = turtle.Turtle()

#countdown turtle
countdownturtle = turtle.Turtle()
def scoreTurtle ():
    tScore.hideturtle()
    tScore.penup()
    topHeight = screen.window_height() / 2
    y = topHeight * 0.8
    tScore.setpos(0,y)
    tScore.color("dark blue")
    tScore.write(arg="Score : 0", move=False, align="center",font=(FONT))

gridSize = 13
def makeTurtle (x, y):
    t = turtle.Turtle()

    def handleClick(x,y):
        global score
        score  += 1
        tScore.clear()
        tScore.write(arg=f"Score : {score}", move=False, align="center",font=(FONT))
        print(x,y)

    t.onclick(handleClick)

    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * gridSize,y * gridSize )
    turtleList.append(t)


xCordi = [-20, -10, 0, 10, 20]
yCordi = [16, 6, -4, -14 ]

def setupTurtles ():

    for x in xCordi :
        for y in yCordi:
            makeTurtle(x,y)

def hideTurtles():
    for t in turtleList:
        t.hideturtle()

#recursive function
def showTurtlesRandomly():
    if not gameOver:
        hideTurtles()
        random.choice(turtleList).showturtle()
        screen.ontimer(showTurtlesRandomly, 600)

def countdown(time):
    global gameOver
    countdownturtle.hideturtle()
    countdownturtle.penup()
    topHeight = screen.window_height() / 2
    y = topHeight * 0.7
    countdownturtle.setpos(0, y - 0)
    countdownturtle.color("black")
    countdownturtle.clear()
    if time > 0:
        countdownturtle.clear()
        countdownturtle.write(arg=f"Time : {time}", move=False, align="center", font=(FONT))
        screen.ontimer(lambda : countdown(time - 1), 1000)
    else:
        gameOver = True
        countdownturtle.clear()
        hideTurtles()
        countdownturtle.write(arg="Game Over Gardaş ! ", move=False, align="center", font=(FONT))


def start():
    turtle.tracer(0)
    scoreTurtle()
    setupTurtles()
    hideTurtles()
    showTurtlesRandomly()
    countdown(10)

    turtle.tracer(1)


start()
turtle.mainloop()
