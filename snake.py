import turtle
import time
import random

delay = 0.05
original_value = delay
score = 0
high_score = 0

#Set up the screen

wn = turtle.Screen()
wn.title("Hungry Python")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)        #Turns off the screen updates

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("triangle")
head.color("orange")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake Food
food = turtle.Turtle()
foodsize = 0.5
food.speed(0)
food.shape("square")
food.shapesize(foodsize,foodsize)
food.color("white")
food.penup()
food.goto(0,100)

segments = []


#Functions for the snake

def go_up():
    if head.direction != "down":
        head.direction = "up"
        head.setheading(90)

def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.setheading(270)

def go_right():
    if head.direction != "left":
        head.direction = "right"
        head.setheading(0)

def go_left():
    if head.direction != "right":
        head.direction = "left"
        head.setheading(180)

def move():
    move_dist = 20
    move_body_segments_with_head()
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+move_dist)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-move_dist)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+move_dist)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-move_dist)

    

#Snake body

def add_body_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)

def move_body_segments_with_head():
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
        # print(segments[index].xcor(), segments[index].ycor())

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

#Generate food randomly
def generate_food():
    x = random.randint(-380, 380)
    y = random.randint(-380, 380)
    food.goto(x,y)

#Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")

#Check for collisions
def check_for_border_collision():
    if head.xcor() > 380 or head.xcor() < -380 or head.ycor() > 380 or head.ycor() < -380:
        time.sleep(1)
        head.home()
        head.direction = "stop"
        
        for segment in segments:
            # segment.reset()
            segment.goto(1000,1000)
            # segment.bye()
        
        segments.clear()

        global score
        global high_score
        score = 0
        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        global delay
        delay = original_value

def check_for_body_collision():
    for segment in segments:
        if segment.distance(head) < 1:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment2 in segments:
                segment2.goto(1000,1000)

            segments.clear()

            global score
            global high_score
            score = 0
            pen.clear()
            pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            global delay
            delay = original_value

def speed_up():
    global delay
    delay -= 0.001

#Scoring
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.ht()
pen.goto(0,370)
pen.write("Hungry Python", align="center", font=("Arial", 28, "normal"))
pen.goto(0,330)
pen.write("Score: 0     High Score: 0", align="center", font=("Courier", 24, "normal"))


def set_score():
    global score
    global high_score
    score += 10

    if score > high_score:
        high_score = score
    
    pen.clear()
    pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


#Main game loop
while True:
    wn.update()
    
    check_for_border_collision()
    check_for_body_collision()

    #Check if food is consumed
    if head.distance(food) < 20:
        generate_food()
        add_body_segment()
        set_score()
        speed_up()

    
    move()
    
    time.sleep(delay)

wn.mainloop()
