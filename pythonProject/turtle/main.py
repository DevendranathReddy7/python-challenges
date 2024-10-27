import random
from turtle import Turtle, Screen

tomy = Turtle()
tomy.shape('arrow')
tomy.color('blue')


# for i in range(3):
#     tomy.forward(100)
#     tomy.right(120)
#
# for i in range(4):
#     tomy.forward(100)
#     tomy.right(90)
#
# for i in range(5):
#     tomy.forward(100)
#     tomy.right(72)
#
# for i in range(6):
#     tomy.forward(100)
#     tomy.right(60)
#
# for i in range(7):
#     tomy.forward(100)
#     tomy.right(52)
#
# for i in range(8):
#     tomy.forward(100)
#     tomy.right(45)
#
# for i in range(9):
#     tomy.forward(100)
#     tomy.right(40)
#
# for i in range(10):
#     tomy.forward(100)
#     tomy.right(36)

# class draw:
#     def __init__(self,count,angle):
#         self.count = count
#         self.angle=angle
#         for i in range(count):
#             tomy.forward(100)
#             tomy.right(angle)
#
# triangle = draw(3,120)
# square = draw(4,90)
# pentagon = draw(5,72)
# hexagon = draw(6,60)
# heptagon = draw(7,51)
# octagon = draw(8,45)
# nonagon = draw(9,40)
# decagon = draw(10,36)


def random_color():
        r = random.randint(0,255)
        g = random.randint(0, 255)
        b = random.randint(0,255)
        color = (r,g,b)
        return color

tomy.speed(0)
def spirograph(size):
    for i in range(int(360/size)):
        tomy.circle(50)
        tomy.setheading(tomy.heading()+size)
spirograph(10)

screen = Screen()
screen.exitonclick()