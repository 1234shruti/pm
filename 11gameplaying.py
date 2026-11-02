import math

HUMAN = "X"
AI = "O"


def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")


def check_winner(board, player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    return any(all(board[i] == player for i in line)
               for line in wins)


def minimax(board, is_maximizing):
    if check_winner(board, AI):
        return 1

    if check_winner(board, HUMAN):
        return -1

    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = AI
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = HUMAN
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def best_move(board):
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


def play_game():
    board = [" "] * 9

    print("Tic-Tac-Toe: You are X, AI is O")
    print("Enter positions from 1 to 9.")

    print_board([str(i) for i in range(1, 10)])

    while True:
        try:
            pos = int(input("Enter your move (1-9): ")) - 1

        except ValueError:
            print("Please enter a number.")
            continue

        if pos < 0 or pos > 8 or board[pos] != " ":
            print("Invalid move! Try again.")
            continue

        board[pos] = HUMAN

        if check_winner(board, HUMAN):
            print_board(board)
            print("You win!")
            break

        if " " not in board:
            print_board(board)
            print("It's a draw!")
            break

        move = best_move(board)
        board[move] = AI

        print("\nAI's move:")
        print_board(board)

        if check_winner(board, AI):
            print("AI wins!")
            break

        if " " not in board:
            print("It's a draw!")
            break


play_game()