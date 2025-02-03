# using turtle for og pong
#update from linux
import turtle


# create screen
usr_scn = turtle.Screen()
usr_scn.title("Pong game @7HE-Lucky-FISH")
usr_scn.bgcolor("black")
usr_scn.setup(width=1000, height=600)
usr_scn.tracer(0)

# player score
left_player = 0
right_player = 0

# Left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-400, 0)


# Right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(400, 0)


# ball
hit_ball = turtle.Turtle()
hit_ball.speed(0)
hit_ball.shape("circle")
hit_ball.color("white")
hit_ball.penup()
hit_ball.goto(0, 0)

hit_ball.dx = 4
hit_ball.dy = -4




# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Player 1: {}   Player 2: {}".format(left_player, right_player),align="center", font=("Courier", 24, "normal"))


# func to move paddles
def paddleaup():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)


def paddleadown():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)


def paddlebup():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)


def paddlebdown():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)
def game_end():
    hit_ball.dx=0
    hit_ball.dy=0

# bindings
usr_scn.listen()
usr_scn.onkeypress(paddleaup, "e")

usr_scn.listen()
usr_scn.onkeypress(paddleadown, "d")

usr_scn.listen()
usr_scn.onkeypress(paddlebup, "Up")

usr_scn.listen()
usr_scn.onkeypress(paddlebdown, "Down")


while True:
    usr_scn.update()

    if left_player ==7:
        game_end()
    if right_player ==7:
        game_end()

    
    hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)

    # Checking borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Player 1: {}    Player 2: {}".format(left_player, right_player), align="center",font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Player 1: {}    Player 2: {}".format(left_player, right_player), align="center",font=("Courier", 24, "normal"))

    # Paddle ball collision
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_paddle.ycor()+40 and hit_ball.ycor() > right_paddle.ycor()-40):
        hit_ball.setx(360)
        hit_ball.dx*=-1

    if (hit_ball.xcor()<-360 and hit_ball.xcor()>-370) and (hit_ball.ycor()<left_paddle.ycor()+40 and hit_ball.ycor()>left_paddle.ycor()-40):
        hit_ball.setx(-360)
        hit_ball.dx*=-1
