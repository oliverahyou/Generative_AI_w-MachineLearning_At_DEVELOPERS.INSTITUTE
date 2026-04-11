# Mini-Project - Tic Tac Toe
# Instructions

#     The game is played on a grid that’s 3 squares by 3 squares.
#     Players take turns putting their marks (O or X) in empty squares.
#     The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
#     When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
# Step 1: Create the board
# Create a 3 by 3 list to represent the tic tac toe board. Each element of the list should be a string with a single space in it. This will represent an empty square on the board.
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# Step 2: Create a function to print the board
# Create a function called print_board that prints the board to the console. The function should print
# the board in a way that looks like a tic tac toe board. For example:
#  |   |
#  |   |
#  |   |
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
# Step 3: Create a function to check for a win
# Create a function called check_win that takes the board as an argument and checks if there is a winner. The function should return "X" if player X has won, "O" if player O has won, and None if there is no winner yet.
def check_win(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None
# Step 4: Create a function to check for a tie
# Create a function called check_tie that takes the board as an argument and checks if there is a tie. The function should return True if there is a tie and False if there is not.
def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True
# Step 5: Create a function to play the game
# Create a function called play_game that allows two players to play the game. The function should alternate turns between the two players and allow them to input their moves. The function should also check for a win or a tie after each move and end the game if there is a winner or a tie.
def play_game():
    current_player = "X"
    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_tie(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That square is already taken. Try again.")
play_game()



