import turtle
import winsound

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('green')
wn.setup(width=800, height=600)
wn.tracer(0)

# 1st Player Paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape('square')
paddle_1.color('black')
paddle_1.penup()
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.goto(-350, 0) # Coordinates starting from the center of the screen.

# 2nd Player Paddle
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape('square')
paddle_2.color('black')
paddle_2.penup()
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.goto(350, 0) # Coordinates starting from the center of the screen.

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0, 0) # Coordinates starting from the center of the screen.
ball.dx = 0.3 # Number of pixels by which the ball will move
ball.dy = 0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('blue')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player 1: 0 Player 2: 0', align='center', font=('Courier', 24, 'normal'))

# Scoreboard
score_1 = 0
score_2 = 0

# Functions
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

# Keyboard binding
wn.listen() # From the turtle library. Checks to see if keyboard is pressed.
wn.onkeypress(paddle_1_up, 'w') # if w is pressed then function 'paddle_1_up()' function gets called
wn.onkeypress(paddle_1_down, 's')
wn.onkeypress(paddle_2_up, 'Up')
wn.onkeypress(paddle_2_down, 'Down')


# Main game
while True:
    wn.update()

    # To move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check the border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('ballbounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('ballbounce.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write('Player 1: {} Player 2: {}'.format(score_1, score_2), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write('Player 1: {} Player 2: {}'.format(score_1, score_2), align='center', font=('Courier', 24, 'normal'))


    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('ballbounce.wav', winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('ballbounce.wav', winsound.SND_ASYNC)







