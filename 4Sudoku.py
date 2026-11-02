

grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# Display Sudoku Grid
def display():
    for r in range(9):

        if r % 3 == 0 and r != 0:
            print("------+-------+------")

        for c in range(9):

            if c % 3 == 0 and c != 0:
                print("|", end=" ")

            print(
                grid[r][c] if grid[r][c] != 0 else ".",
                end=" "
            )

        print()


# Check whether a number is valid
def valid(r, c, n):

    # Check row and column
    for i in range(9):
        if grid[r][i] == n or grid[i][c] == n:
            return False

    # Check 3x3 box
    br, bc = (r // 3) * 3, (c // 3) * 3

    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if grid[i][j] == n:
                return False

    return True


# Solve Sudoku using Backtracking
def solve():

    for r in range(9):
        for c in range(9):

            if grid[r][c] == 0:

                for n in range(1, 10):

                    if valid(r, c, n):

                        grid[r][c] = n

                        if solve():
                            return True

                        # Backtracking
                        grid[r][c] = 0

                return False

    return True


# Main Program
print("Initial State:")
display()

if solve():
    print("\nSolved State:")
    display()
else:
    print("No solution exists.")