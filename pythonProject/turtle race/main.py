import turtle
from turtle import Turtle, Screen
import random

colors = ['red','blue','green','yellow','cyan','magenta']
y_cords = [-70,-40,-10, 20, 50, 80]
list_of_turtles = []

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

for color in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[color])
    new_turtle.penup()
    new_turtle.goto(-230, y_cords[color])
    list_of_turtles.append(new_turtle)

bet = turtle.textinput(title='Turtle Race', prompt='Which turtle will win the race?')

if bet:
    is_race_on = True

while is_race_on:
    for turtle in list_of_turtles:
        if turtle.xcor() >= 230:
            if bet == turtle.pencolor():
                print('you won 🎊🎉',)
            else:
                print(f'you lost, {turtle.pencolor()} color turtle was won 😔')
            is_race_on = False
        num = random.randint(1, 10)
        turtle.forward(num)

screen.exitonclick()