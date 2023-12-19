import turtle
import random

screen = turtle.Screen()
screen.bgcolor("#262626")
screen.title("Catch the Turtle")
FONT = ('Arial', 15, 'bold')
turtle_list = []
score = 0
game_over = False

grid_size = 12
score_turtle = turtle.Turtle()

# countdown turtle
countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("white")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9

    score_turtle.setposition(0, y)
    score_turtle.write(arg="Score: 0", move=False, align='center', font=FONT)

def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align='center', font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("light green")
    t.goto(grid_size * x, grid_size * y)
    turtle_list.append(t)

def setup_turtles():
    for i in range(20, -30, -10):
        for j in range(-20, 30, 10):
            make_turtle(j, i)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtle_random():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtle_random, 1000)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("white")
    countdown_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9

    countdown_turtle.setposition(0, y - 40)
    countdown_turtle.clear()

    if time > 0 and not game_over:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align='center', font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        countdown_turtle.write(arg="Game Over!", move=False, align='center', font=FONT)
        hide_turtles()  # Süre bittikten sonra turtle'ları gizle

def start_game_up():
    turtle.tracer(0)

    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtle_random()
    countdown(10)

    turtle.tracer(1)

start_game_up()
turtle.mainloop()
