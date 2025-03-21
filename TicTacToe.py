"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""
from turtle import *
from freegames import line

# Function to draw the tic-tac-toe grid
def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

# Function to draw the 'X' symbol
def drawx(x, y):
    """Draw X player."""
    color('red')  # Set X color to red
    width(4)  # Set line width
    up()
    goto(x + 20, y + 20)  # Adjust position to center
    down()
    line(x + 20, y + 20, x + 113, y + 113)
    line(x + 20, y + 113, x + 113, y + 20)

# Function to draw the 'O' symbol
def drawo(x, y):
    """Draw O player."""
    color('blue')  # Set O color to blue
    width(4)  # Set line width
    up()
    goto(x + 67, y + 30)  # Adjust position to center
    down()
    circle(40)  # Reduce the circle size

# Function to round the given value to the nearest grid position
def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200

# Dictionary to track the current player state
state = {'player': 0}
# List containing the drawing functions for each player
players = [drawx, drawo]
# Dictionary to track occupied positions
board = {}

# Function to handle user clicks and place 'X' or 'O'
def tap(x, y):
    """Draw X or O in tapped square if not already occupied."""
    x = floor(x)
    y = floor(y)
    
    # Check if the position is already taken
    if (x, y) in board:  
        # Do nothing if occupied
        return  
    
    player = state['player']
    draw = players[player]
    draw(x, y)
     # Mark position as taken
    board[(x, y)] = player 
    update()
    state['player'] = not player

# Set up the game window
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
# Draw the initial grid
grid()
update()
# Listen for user clicks to trigger the tap function
onscreenclick(tap)
# Keep the game running
done()
