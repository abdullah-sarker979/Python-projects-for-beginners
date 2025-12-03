import turtle
import random
import time

HEIGHT, WIDTH = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow',
          'black', 'purple', 'pink', 'brown', 'cyan']


def race(colours):
    turtles = create_turtles(color)

    while True:
        for racer in turtles:
            distace = random.randrange(1, 15)
            racer.forward(distace)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return color[turtles.index(racer)]


def numbers_of_racers():
    while True:
        racers = 0
        racers = input(
            "Enter the nubers of turtles you want to race (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input not numeric...... Try again!")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range. Try again!")


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx,  -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init__turtle():
    screen = turtle.Screen()
    screen.setup(HEIGHT, WIDTH)
    screen.title("Turtle racing!")


num_of_racers = numbers_of_racers()
init__turtle()
random.shuffle(COLORS)
color = COLORS[:num_of_racers]

winner = race(color)

print(f"The winner is the turtle with the colour {winner}")
time.sleep(5)
