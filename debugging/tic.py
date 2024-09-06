#!/usr/bin/python3
def print_board(board):
    """Prints the tic-tac-toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if there's a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_draw(board):
    """Checks if the board is full and it's a draw."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main function to run the tic-tac-toe game."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 2.")
            continue

        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Invalid input! Please enter a number between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
