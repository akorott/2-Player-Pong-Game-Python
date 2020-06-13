import turtle
import winsound

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('khaki')
wn.setup(width=600, height=800)
wn.tracer(0)

# 1st Player Paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape('square')
paddle_1.color('black')
paddle_1.penup()
paddle_1.shapesize(stretch_wid=1, stretch_len=5)
paddle_1.goto(0, 350) # Coordinates starting from the center of the screen.

# 2nd Player Paddle
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape('square')
paddle_2.color('black')
paddle_2.penup()
paddle_2.shapesize(stretch_wid=1, stretch_len=5)
paddle_2.goto(0, -350) # Coordinates starting from the center of the screen.

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('tomato')
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
pen.goto(0, 0)
pen.write('Player 1: 0 Player 2: 0', align='center', font=('Courier', 10, 'normal'))

# Scoreboard
score_1 = 0
score_2 = 0

# Functions
def paddle_1_left():
    x = paddle_1.xcor()
    x -= 20
    paddle_1.setx(x)

def paddle_1_right():
    x = paddle_1.xcor()
    x += 20
    paddle_1.setx(x)

def paddle_2_left():
    x = paddle_2.xcor()
    x -= 20
    paddle_2.setx(x)

def paddle_2_right():
    x = paddle_2.xcor()
    x += 20
    paddle_2.setx(x)

# Keyboard binding
wn.listen() # From the turtle library. Checks to see if keyboard is pressed.
wn.onkeypress(paddle_1_left, 'a') # if a is pressed on the keyboard then the function 'paddle_1_left()' gets called
wn.onkeypress(paddle_1_right, 's')
wn.onkeypress(paddle_2_left, 'Left')
wn.onkeypress(paddle_2_right, 'Right')


# Main game
while True:
    wn.update()

    # To move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # wid = x = 800
    # len = y = 600

    # Check the border
    if ball.ycor() > 390:
        ball.goto(0, 0)
        ball.dy *= -1
        score_2 += 1
        pen.clear()
        pen.write('Player 1: {} Player 2: {}'.format(score_1, score_2), align='center', font=('Courier', 10, 'normal'))

    if ball.ycor() < -390:
        ball.goto(0, 0)
        ball.dy *= -1
        score_1 += 1
        pen.clear()
        pen.write('Player 1: {} Player 2: {}'.format(score_1, score_2), align='center', font=('Courier', 10, 'normal'))

    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1
        winsound.PlaySound('ballbounce.wav', winsound.SND_ASYNC)

    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1
        winsound.PlaySound('ballbounce.wav', winsound.SND_ASYNC)

    # Paddle and ball collisions
    if (ball.ycor() > 340 and ball.ycor() < 350) and (ball.xcor() < paddle_1.xcor() + 40 and ball.xcor() > paddle_1.xcor() - 40):
        ball.sety(340)
        ball.dy *= -1
        winsound.PlaySound('ballbounce.wav', winsound.SND_ASYNC)

    if (ball.ycor() < -340 and ball.ycor() > -350) and (ball.xcor() < paddle_2.xcor() + 40 and ball.xcor() > paddle_2.xcor() - 40):
        ball.sety(-340)
        ball.dy *= -1
        winsound.PlaySound('ballbounce.wav', winsound.SND_ASYNC)







