import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")


def rand_color():
    r = random.randint(0,255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    tup=(r,b,g)
    return tup

for _ in range(200):
    tim.color(rand_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))  #sets the direction of cursor pointing/of turtle

