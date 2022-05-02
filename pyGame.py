import turtle
import pygame

wn = turtle.Screen()
wn.bgcolor("dark blue")
wn.title("Just a Maze Game")
wn.setup(700,700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("light blue")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0) 

    def go_up(self):
        self.goto(self.xcor(), self.ycor() +24)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() -24)

    def go_left(self):
        self.goto(self.xcor(), -24, self.ycor())

    def go_right(self):
        self.goto(self.xcor(), +24, self.ycor())

        
levels = [""]

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXO XXXXXXXXXXXXXXXXXX",
"XXXXX  XXXXXXXXXXXXXXXXXX",
"XXXXX      XXXXXXXXXXXXXX",
"XXXXXXXX   XXXXXXXXXXXXXX",
"XXXXXXXX   XXXXXXXXXXXXXX",
"XXXXXXXX XXXXXXXXXXXXXXXX",
"XXXXXXXX XXXXXXXXXXXXXXXX",
"XXXXXXXX XXXXXXXXXXXXXXXX",
"XXXXXXXX XXXXXXXXXXXXXXXX",
"XXXXXXXX XXXXXXXXXXXXXXXX",
"XXXXXXXX     XXXXXXXXXXXX",
"XXXXXXXXXXXX XXXXXXXXXXXX",
"XXXXXXXXXXXX XXXXXXXXXXXX",
"XXXXXXXXXXXX XXXXXXXXXXXX",
"XXXXXXXXXXX  XXXXXXXXXXXX",
"XXXXXXXXXXX  XXXXXXXXXXXX",
"XXXXXXXXXXX  XXXXXXXXXXXX",
"XXXXXXXXXXX  XXXXXXXXXXXX",
"XXXXXXXXXXX  XXXXXXXXXXXX",
"XXXXXXXXXXX  XXXXXXXXXXXX",
"XXXXXXXX     XXXXXXXXXXXX",
"XXXXXXXX  XXXXXXXXXXXXXXX",
"XXXXXXXX  XXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

levels.append(level_1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level [y] [x]
            screen_x = -288 + (x* 24)
            screen_y = 288 - (y* 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()

            if character == "O":
                player.goto(screen_x, screen_y)  

pen = Pen()
player = Player()

setup_maze(levels[1])

turtle.listen
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")

while True:
    pass