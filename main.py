from turtle import *
from random import choice,randint

# 製造下方的移動桿
stick = Turtle()
stick.hideturtle()
stick.shape("square")
stick.shapesize(1,10)
stick.color("white")
stick.penup()
stick.goto(0,-300)
stick.showturtle()

# 製造上方磚塊
class Target(Turtle):
    colors = ['green','orange','yellow','pink','purple','gold','gray','brown','white']
    def __init__(self,x,y):
        super().__init__()
        self.white = False
        self.shapesize(1,2.5)
        self.color(choice(self.colors))
        self.shape('square')
        self.penup()
        self.goto(x,y)

tracer(0)
tx,ty = -250,300
targets = []
for _ in range(10):
    target = Target(tx, ty)
    targets.append(target)
    tx += 55
tracer(1)

# 製造一顆球
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = -4
        self.y_move = -3
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

ball = Ball()

# 製造螢幕跟桿子左右移動
screen = Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.onkey(lambda: stick.forward(-10), 'Left')
screen.onkey(lambda: stick.forward(10), 'Right')
screen.listen()

# 開始遊戲
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    for i in range(0,len(targets)):
        if targets[i].distance(ball) < 30:
            ball.bounce_y()
            targets[i].color("black")
    if ball.xcor() > 300 or ball.xcor() < -300:
        ball.bounce_x()
    if ball.distance(stick) < 60:
        ball.bounce_y()
    if ball.ycor() < -350:
        ball.reset_position()

screen.mainloop()