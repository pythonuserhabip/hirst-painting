# import colorgram
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
color_list = [(246, 242, 234), (248, 241, 244), (239, 246, 242), (238, 241, 246), (195, 166, 120), (138, 81, 59), (219, 202, 139), (63, 94, 116), (162, 152, 56), (138, 162, 178), (127, 36, 26), (69, 38, 32), (56, 115, 87), (188, 97, 81), (148, 177, 150), (21, 91, 69), (165, 143, 156), (114, 74, 79), (33, 59, 73), (132, 27, 31), (225, 178, 165), (75, 28, 32), (180, 203, 178), (15, 68, 57), (29, 80, 87), (93, 145, 128), (45, 65, 85), (183, 95, 98), (219, 177, 180), (68, 63, 58)]

# rgb_colors = []
# colors = colorgram.extract('indir.jpg.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b= color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
# print(rgb_colors)
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100
# tim.shape("turtle")
tim.hideturtle()

for dot_count in range(1, number_of_dots+1):

    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle.Screen()
screen.exitonclick()



