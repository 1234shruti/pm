# Function to print the chessboard
def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))


# Function to check whether placing a queen is safe
def is_safe(board, row, col):

    # Check the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < 8:
        if board[i][j] == 1:
            return False

        i -= 1
        j += 1

    return True


# Function to solve 8-Queens using Backtracking
def solve(board, row):

    # All 8 queens are placed
    if row == 8:
        return True

    # Try placing queen in each column
    for col in range(8):

        if is_safe(board, row, col):

            board[row][col] = 1

            if solve(board, row + 1):
                return True

            # Backtracking
            board[row][col] = 0

    return False


# Create an empty 8x8 chessboard
board = [[0 for _ in range(8)] for _ in range(8)]


# Main Program
if solve(board, 0):
    print("Solution for 8-Queens Problem:")
    print_board(board)
else:
    print("No solution exists.")