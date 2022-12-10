from turtle import Turtle, Screen
from random import randint, choice

racing = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
offset = -100
turtles = []

for color in colors:
    turt = Turtle(shape="turtle")
    turt.color(color)
    turt.penup()
    offset += 30
    turt.goto(x=-230, y=offset)
    turtles.append(turt)

if user_bet:
    racing = True

while racing:

    for turtle in turtles:
        if turtle.xcor() > 220:
            racing = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = randint(0, 10)
        choice(turtles).forward(rand_distance)

screen.exitonclick()
