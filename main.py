import turtle
import time

# Setup
wn = turtle.Screen()
wn.title("Underwater Adventures")
wn.bgpic("background.gif")
wn.bgcolor("blue")
wn.setup(1.0, 1.0)
wn.addshape("kraken.gif")
wn.addshape("submarine1.gif")
wn.addshape("submarine2.gif")
wn.addshape("fishes1.gif")  # Changed to "fishes1.gif" to match your image filename
wn.addshape("fishes2.gif")  # Added shape for the second fish image
wn.addshape("blast.gif")  # submarine blast
start_time = time.time()  # Get the current time when the game starts
countdown_duration = 180  # 180 seconds (3 minutes)
# Create a timer display turtle
timer_display = turtle.Turtle()
timer_display.penup()
timer_display.goto(-450, 280)
timer_display.color("white")
timer_display.hideturtle()

# Set up the score
score = 0
score_display = turtle.Turtle()
score_display.penup()
score_display.goto(0, 350)
score_display.color("white")
score_display.write("Underwater Adventures - Score: {}".format(score), align="left", font=("Courier", 20, "normal"))
score_display.hideturtle()

# Fish logic
fish = turtle.Turtle()
fish.shape("fishes1.gif")
fish.penup()
fish.speed(1)
fish.setx(-300)
right = ["fishes2.gif"]
left = ["fishes1.gif"]

# Kraken Logic
kraken = turtle.Turtle()
kraken.shape("kraken.gif")
kraken.penup()
kraken.speed(10)
kraken.setposition(500, 0)
kraken.direction = "up"  # Start with the kraken moving up

# Additional player submarine logic
man = turtle.Turtle()
man.shape("submarine1.gif")
man.penup()
man.speed(5)
man.direction = "stop"

# Blast logic
blast = turtle.Turtle()
blast.shape("blast.gif")  # Assuming you have a blast.gif image
blast.penup()
blast.speed(0)
blast.setposition(0, -300)
blast.hideturtle()
blast_speed = 200  # Adjust blast speed as needed

blast_count = 0  # Initialize the blast count
win_threshold = 5  # Number of blasts needed to win


# Timer
def update_timer_display():
    elapsed_time = int(time.time() - start_time)  # Calculate elapsed time in seconds
    remaining_time = max(0, countdown_duration - elapsed_time)  # Calculate remaining time
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    timer_display.clear()  # Clear the previous timer display
    timer_display.write(f"Time: {minutes:02}:{seconds:02}", align="left", font=("Courier", 16, "normal"))


# Submarine Blast
def blast_fire():
    global blast_count
    if not blast.isvisible():
        blast.setposition(man.xcor(), man.ycor())
        blast.showturtle()
        check_collision()  # Check for collision after firing the blast


# Check if the blast touched the monster
def check_collision():
    global blast_count, score
    if blast.isvisible() and blast.distance(kraken) < 50:  # Adjust the collision distance as needed
        blast.hideturtle()
        blast_count += 1
        score += 1  # Increase the score
        update_score_display()  # Update the score display
        check_win()


# score
def update_score_display():
    score_display.clear()  # Clear the previous score display
    score_display.write("Underwater Adventures - Score: {}".format(score), align="left", font=("Courier", 20, "normal"))


# Win function
def check_win():
    if blast_count == win_threshold:
        wn.bgcolor("black")
        man.hideturtle()
        fish.hideturtle()
        blast.hideturtle()
        score_display.clear()  # Clear the score display
        message = turtle.Turtle()
        message.speed(0)
        message.color("white")
        message.penup()
        message.hideturtle()
        message.goto(0, 0)
        message.write("Congratulations! You Win!\n"
                      " Developed by Guy Bracha", align="center", font=("Courier", 60, "normal"))
        time.sleep(2)
        wn.bye()


def move():
    x, y = man.xcor(), man.ycor()

    if man.direction == "up":
        if y + 20 < wn.window_height() / 2:  # Increased speed
            man.sety(y + 20)  # Increased speed
    if man.direction == "down":
        if y - 20 > -wn.window_height() / 2:  # Increased speed
            man.sety(y - 20)  # Increased speed
    if man.direction == "right":
        if x + 20 < wn.window_width() / 2:  # Increased speed
            man.setx(x + 20)  # Increased speed
    if man.direction == "left":
        if x - 20 > -wn.window_width() / 2:  # Increased speed
            man.setx(x - 20)  # Increased speed


def move_kraken():
    if kraken.ycor() > 250:
        kraken.direction = "down"
    if kraken.ycor() < -250:
        kraken.direction = "up"

    if kraken.direction == "up":
        kraken.sety(kraken.ycor() + 25)
    elif kraken.direction == "down":
        kraken.sety(kraken.ycor() - 25)


def go_up():
    # if man.direction != "down":
    man.direction = "up"


def go_down():
    # if man.direction != "up":
    man.direction = "down"


def go_left():
    # if man.direction != "right":
    man.direction = "left"
    man.shape("submarine2.gif")


def go_right():
    # if man.direction != "left":
    man.direction = "right"
    man.shape("submarine1.gif")


def move_fish():
    global dx  # Declare dx as global
    x = fish.xcor()
    fish.setx(x + dx)

    # Check if the fish is at the left or right edge
    if fish.position()[0] < -wn.window_width() / 2:
        fish.setx(-wn.window_width() / 2)  # Set it to the left edge
        dx = abs(dx)  # Reverse the direction
    elif fish.position()[0] > wn.window_width() / 2:
        fish.setx(wn.window_width() / 2)  # Set it to the right edge
        dx = -abs(dx)  # Reverse the direction

    # Change the fish's image while moving
    if dx > 0:
        fish.shape(right[0])
    else:
        fish.shape(left[0])


def move_blast():
    if blast.isvisible():
        x = blast.xcor()
        blast.setx(x + blast_speed)
        if blast.xcor() > wn.window_width() / 2:
            blast.hideturtle()


def game_over(message):
    wn.bgcolor("black")
    man.hideturtle()
    fish.hideturtle()
    blast.hideturtle()
    kraken.hideturtle()
    message_display = turtle.Turtle()
    message_display.speed(0)
    message_display.color("white")
    message_display.penup()
    message_display.hideturtle()
    message_display.goto(0, 0)
    message_display.write(message, align="center", font=("Courier", 48, "normal"))
    time.sleep(2)
    wn.bye()


# Keyboard bindings
wn.listen()
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(blast_fire, "space")

# Main loop
dx = -5
index = 0

while True:
    move()
    move_fish()
    move_kraken()
    move_blast()
    update_timer_display()  # Update and display the countdown timer

    # Check for collision between blast and kraken
    check_collision()

    if blast.isvisible() and blast.distance(kraken) < 50:  # Adjust the collision distance as needed
        blast.hideturtle()
        blast_count += 1
        score += 1  # Increase the score
        update_score_display()  # Update the score display
        check_win()

    if time.time() - start_time >= countdown_duration:
        # Handle game over due to timeout
        game_over("Time's up! You lose!")

    # Move kraken up and down
    if kraken.ycor() > 250:
        kraken.direction = "down"
    if kraken.ycor() < -250:
        kraken.direction = "up"

    if kraken.direction == "up":
        kraken.sety(kraken.ycor() + 2)
    elif kraken.direction == "down":
        kraken.sety(kraken.ycor() - 2)

    index = (index + 1) % len(right)
    if dx > 0:
        fish.shape(right[index])
    else:
        fish.shape(left[index])
    wn.update()
    time.sleep(0.1)

turtle.done()
