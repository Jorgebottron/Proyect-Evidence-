"""Tic Tac Toe

Exercises:
1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import Screen, Turtle
from freegames import line


# Function to draw the tic-tac-toe grid
def grid():
    """Draw the tic-tac-toe grid."""
    line(-67, 200, -67, -200)  # Vertical line 1
    line(67, 200, 67, -200)  # Vertical line 2
    line(-200, -67, 200, -67)  # Horizontal line 1
    line(-200, 67, 200, 67)  # Horizontal line 2


# Function to draw the 'X' symbol
def drawx(x, y):
    """Draw the X symbol."""
    t = Turtle()
    t.hideturtle()  # Hide the turtle to only show the X
    t.color('red')  # Set the X color to red
    t.width(4)  # Set the X line width
    t.up()
    t.goto(x + 20, y + 20)  # Start point for the first diagonal
    t.down()
    t.goto(x + 113, y + 113)  # Draw first diagonal
    t.up()
    t.goto(x + 20, y + 113)  # Start point for the second diagonal
    t.down()
    t.goto(x + 113, y + 20)  # Draw second diagonal
    screen.update()  # Refresh the screen to display the X


# Function to draw the 'O' symbol
def drawo(x, y):
    """Draw the O symbol."""
    t = Turtle()
    t.hideturtle()  # Hide the turtle to only show the O
    t.color('blue')  # Set the O color to blue
    t.width(4)  # Set the O line width
    t.up()
    t.goto(x + 67, y + 30)  # Move to the start position of the circle
    t.down()
    t.circle(40)  # Draw the circle for O
    screen.update()  # Refresh the screen to display the O


# Function to round the given value to the nearest grid position
def floor(value):
    """Round the value down to the nearest grid position."""
    return ((value + 200) // 133) * 133 - 200


# Initial game state
state = {'player': 0, 'game_over': False}  # Track player and game status
players = [drawx, drawo]  # Define player symbols
board = {}  # Dictionary to store the board state


# Function to check if a player has won
def check_winner():
    """Check if there is a winner or a tie and end the game."""
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

    # Check all win conditions for player X
    for positions in win_positions:
        if all(board.get(pos) == 0 for pos in positions):
            end_game("Player X wins!")  # Declare X as the winner
            return True

        # Check all win conditions for player O
        if all(board.get(pos) == 1 for pos in positions):
            end_game("Player O wins!")  # Declare O as the winner
            return True

    # Check for a tie if the board is full
    if len(board) == 9:
        end_game("It's a tie!")  # Declare a tie
        return True

    return False


# Function to stop the game and display the result
def end_game(message):
    """Stop the game and display the result."""
    print(message)  # Display the result in the console
    state['game_over'] = True  # Set the game as over
    screen.onscreenclick(None)  # Disable further clicks
    screen.ontimer(screen.bye, 5000)  # Close the window after 5 seconds


# Function to handle user taps and place X or O
def tap(x, y):
    """Handle user taps and place X or O in the selected square."""
    # Do nothing if the game is over
    if state['game_over']:
        return

    # Round the coordinates to the nearest grid position
    x = floor(x)
    y = floor(y)

    # Do nothing if the spot is already taken
    if (x, y) in board:
        return

    # Get the current player (0 = X, 1 = O)
    player = state['player']
    draw = players[player]
    draw(x, y)  # Draw X or O in the selected square
    board[(x, y)] = player  # Update the board with the player's move

    # Check if the game is won or tied after the move
    check_winner()

    # Switch to the other player if the game is not over
    if not state['game_over']:
        state['player'] = not player


# Set up the game window
screen = Screen()
screen.setup(420, 420, 370, 0)  # Set window size and position
screen.tracer(False)  # Disable automatic updates

# Draw the initial grid
grid()
screen.update()  # Update the screen to display the grid

# Listen for user clicks to trigger the tap function
screen.onscreenclick(tap)

# Keep the game running
screen.mainloop()
