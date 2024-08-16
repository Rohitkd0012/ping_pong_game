import turtle

# Set up the screen
scr = turtle.Screen()
scr.title("Ping Pong Game")
scr.bgcolor("black")
scr.setup(width=1000, height=600)

# Set up the paddles
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("blue")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# Set up the ball
hit_ball = turtle.Turtle()
hit_ball.speed(100)
hit_ball.shape("circle")
hit_ball.color("orange")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 6
hit_ball.dy = -6

# Initialize scores
left_player = 0
right_player = 0

# Set up the score display
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("gold")
sketch.pendown()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write(f"Left Player: {left_player}    Right Player: {right_player}", align="center", font=("Courier", 24, "normal"))

# Paddle movement functions
def paddleaup():
    y = left_pad.ycor()
    if y < 250:  # Prevent the paddle from going off the screen
        y += 20
    left_pad.sety(y)

def paddleadown():
    y = left_pad.ycor()
    if y > -240:  # Prevent the paddle from going off the screen
        y -= 20
    left_pad.sety(y)

def paddlebup():
    y = right_pad.ycor()
    if y < 250:  # Prevent the paddle from going off the screen
        y += 20
    right_pad.sety(y)

def paddlebdown():
    y = right_pad.ycor()
    if y > -240:  # Prevent the paddle from going off the screen
        y -= 20
    right_pad.sety(y)

# Keyboard bindings
scr.listen()
scr.onkeypress(paddleaup, "w")
scr.onkeypress(paddleadown, "s")
scr.onkeypress(paddlebup, "Up")
scr.onkeypress(paddlebdown, "Down")

# Main game loop
game_over = False

while not game_over:
    scr.update()

    # Move the ball
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Border collision
    if hit_ball.ycor() > 290:
        hit_ball.sety(290)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -290:
        hit_ball.sety(-290)
        hit_ball.dy *= -1

    # Scoring
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dx *= -1
        left_player += 1
        sketch.clear()
        sketch.write(f"Left Player: {left_player}    Right Player: {right_player}", align="center", font=("Courier", 24, "normal"))
        hit_ball.dx *= 1.1
        hit_ball.dy *= 1.1

    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dx *= -1
        right_player += 1
        sketch.clear()
        sketch.write(f"Left Player: {left_player}    Right Player: {right_player}", align="center", font=("Courier", 24, "normal"))
        hit_ball.dx *= 1.1
        hit_ball.dy *= 1.1
        
    # Paddle collision
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor() + 40 and hit_ball.ycor() > right_pad.ycor() - 40):
        hit_ball.setx(360)
        hit_ball.dx *= -1
        hit_ball.dx *= 1.05
        hit_ball.dy *= 1.05


    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor() + 40 and hit_ball.ycor() > left_pad.ycor() - 40):
        hit_ball.setx(-360)
        hit_ball.dx *= -1
        hit_ball.dx *= 1.05
        hit_ball.dy *= 1.05


    # Check for win
    if left_player == 3:
        sketch.clear()
        sketch.write("Left Player Wins!", align="center", font=("Courier", 24, "normal"))
        game_over = True

    if right_player == 3:
        sketch.clear()
        sketch.write("Right Player Wins!", align="center", font=("Courier", 24, "normal"))
        game_over = True

scr.mainloop()
