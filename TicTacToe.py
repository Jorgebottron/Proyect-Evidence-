"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""
"""Tic Tac Toe"""

from turtle import Screen, Turtle
from freegames import line

# Function to draw the tic-tac-toe grid
def grid():
    """Draw the tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

# Function to draw the 'X' symbol
def drawx(x, y):
    """Draw the X symbol."""
    t = Turtle()
    t.hideturtle()
    t.color('red')
    t.width(4)
    t.up()
    t.goto(x + 20, y + 20)
    t.down()
    t.goto(x + 113, y + 113)
    t.up()
    t.goto(x + 20, y + 113)
    t.down()
    t.goto(x + 113, y + 20)
    screen.update()

# Function to draw the 'O' symbol
def drawo(x, y):
    """Draw the O symbol."""
    t = Turtle()
    t.hideturtle()
    t.color('blue')
    t.width(4)
    t.up()
    t.goto(x + 67, y + 30)
    t.down()
    t.circle(40)
    screen.update()

# Function to round the given value to the nearest grid position
def floor(value):
    """Round the value down to the nearest grid position."""
    return ((value + 200) // 133) * 133 - 200

state = {'player': 0, 'game_over': False}  # Track current player and game state
players = [drawx, drawo]  # List of player drawing functions
board = {}  # Dictionary to store occupied positions

def check_winner():
    """Check if there is a winner and stop the game."""
    win_positions = [
        [(-200, 200), (-67, 200), (67, 200)],  # Top row
        [(-200, 67), (-67, 67), (67, 67)],  # Middle row
        [(-200, -67), (-67, -67), (67, -67)],  # Bottom row
        [(-200, 200), (-200, 67), (-200, -67)],  # Left column
        [(-67, 200), (-67, 67), (-67, -67)],  # Middle column
        [(67, 200), (67, 67), (67, -67)],  # Right column
        [(-200, 200), (-67, 67), (67, -67)],  # Diagonal \
        [(67, 200), (-67, 67), (-200, -67)],  # Diagonal /
    ]

    for positions in win_positions:
        if all(board.get(pos) == 0 for pos in positions):
            end_game("Player X wins!")
            return
        if all(board.get(pos) == 1 for pos in positions):
            end_game("Player O wins!")
            return

    if len(board) == 9:
        end_game("It's a tie!")

def end_game(message):
    """Stop the game and display the result."""
    print(message)  # Show the winner in the console
    state['game_over'] = True
    screen.onscreenclick(None)  # Disable further clicks
    screen.ontimer(screen.bye, 3000)  # Close the window after 3 seconds

def tap(x, y):
    """Handle user taps and place X or O in the selected square."""
    if state['game_over']:  # Prevent moves if game is over
        return

    x = floor(x)
    y = floor(y)

    if (x, y) in board:
        return

    player = state['player']
    draw = players[player]
    draw(x, y)
    board[(x, y)] = player

    check_winner()

    state['player'] = not player

# Set up the game window
screen = Screen()
screen.setup(420, 420, 370, 0)
screen.tracer(False)

# Draw the initial grid
grid()
screen.update()

# Listen for user clicks to trigger the tap function
screen.onscreenclick(tap)

# Keep the game running
screen.mainloop()
