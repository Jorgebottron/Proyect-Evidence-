"""
Memory Game - A simple puzzle game of number pairs.

This game presents a grid of hidden tiles, each containing a number. The goal 
is to find matching pairs by clicking on the tiles.

Features:
- Randomized tile positions.
- Interactive gameplay using turtle graphics.
- Tiles hide when not matched.
- Game ends when all tiles are revealed.

Exercises:
1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile numbers.
5. Use letters instead of numbers on tiles.
"""


import random
import turtle

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64


def square(x, y):
    """
    Draw a white square with a black outline at the given coordinates.

    Parameters:
    x (int): The x-coordinate of the square's top-left corner.
    y (int): The y-coordinate of the square's top-left corner.
    """
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black', 'white')
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()


def index(x, y):
    """
    Convert (x, y) screen coordinates to the corresponding tile index.

    Parameters:
    x (int): The x-coordinate of the click.
    y (int): The y-coordinate of the click.

    Returns:
    int: The index of the tile in the tiles list.
    """
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """
    Convert a tile index into (x, y) screen coordinates.

    Parameters:
    count (int): The index of the tile in the grid.

    Returns:
    tuple: A tuple (x, y) representing the top-left coordinate of the tile.
    """
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """
    Handle user clicks and update game state.

    This function determines which tile was clicked, checks if it matches 
    another revealed tile, and updates the game state accordingly.

    Parameters:
    x (int): The x-coordinate of the tap.
    y (int): The y-coordinate of the tap.
    """
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """
    Render the game board, including the background and tiles.

    This function clears the screen, draws the background image, and updates 
    the tiles. If a tile is taped, its number is displayed.

    The function runs recursively every 100 milliseconds to refresh the screen.
    """
    turtle.clear()
    turtle.goto(0, 0)
    turtle.shape(car)
    turtle.stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        turtle.up()
        turtle.goto(x + 2, y)
        turtle.color('black')
        turtle.write(tiles[mark], font=('Arial', 30, 'normal'))

    turtle.update()
    turtle.ontimer(draw, 100)


random.shuffle(tiles)
turtle.setup(420, 420, 370, 0)
turtle.addshape(car)
turtle.hideturtle()
turtle.tracer(False)
turtle.onscreenclick(tap)
draw()
turtle.done()
