"""
Pacman - A classic arcade game.

The objective of the game is to eat all of the
dots placed in the maze while avoiding four ghosts.

Excercise (Changes to implement)

1. Change the shape and color of the board.
2. Change shape and color of the dots.
3. Make the ghosts faster.
"""

from random import choice
import turtle

from freegames import floor, vector

# Dictionary to keep track of the score
state = {'score': 0}

# Turtle objects for drawing path and displaying score
path = turtle.Turtle(visible=False)
writer = turtle.Turtle(visible=False)

# Initial movement direction for Pacman
aim = vector(5, 0)

# Initial position of Pacman
pacman = vector(-40, -80)

# List of ghosts with their starting positions and movement directions
ghosts = [
    [vector(-180, 160), vector(8, 0)],
    [vector(-180, -160), vector(0, 8)],
    [vector(100, 160), vector(0, -8)],
    [vector(100, -160), vector(-8, 0)],
]

# Tile layout of the maze (0 = empty, 1 = wall, 2 = eaten dot)
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]


def square(x, y):
    """
    Draw a square at the given (x, y) position using the path object.

    Args:
        x (int): The x-coordinate of the square's top-left corner.
        y (int): The y-coordinate of the square's top-left corner.
    """
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    """
    Calculate the tile offset for a given point.

    Args:
        point (vector): The point for which the offset is calculated.

    Returns:
        int: The tile index corresponding to the given point.
    """
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    """
    Check if a point is valid in the current tile layout.

    Args:
        point (vector): The point to be checked.

    Returns:
        bool: True if the point is valid, False otherwise.
    """
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    """
    Draw the game world (maze) using the path object.
    """
    turtle.bgcolor('white')
    path.color('green')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(5, 'black')


def move():
    """
    Move pacman and all ghosts, update the game state,
    and check for collisions.
    """
    writer.undo()
    writer.write(state['score'])

    turtle.clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    turtle.up()
    turtle.goto(pacman.x + 10, pacman.y + 10)
    turtle.dot(20, 'yellow')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(8, 0),
                vector(-8, 0),
                vector(0, 8),
                vector(0, -8),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        turtle.up()
        turtle.goto(point.x + 10, point.y + 10)
        turtle.dot(20, 'red')

    turtle.update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    turtle.ontimer(move, 100)


def change(x, y):
    """
    Change pacman's direction if the new direction is valid.

    Args:
        x (int): The x-direction change.
        y (int): The y-direction change.
    """
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


# Set up the turtle window size and position
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)

# Display the initial score
writer.goto(160, 160)
writer.color('black')
writer.write(state['score'])

# Set up the keyboard input handlers
turtle.listen()
turtle.onkey(lambda: change(5, 0), 'Right')
turtle.onkey(lambda: change(-5, 0), 'Left')
turtle.onkey(lambda: change(0, 5), 'Up')
turtle.onkey(lambda: change(0, -5), 'Down')

# Start the game
world()
move()
turtle.done()
