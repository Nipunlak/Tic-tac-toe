from tabulate import tabulate


def main():
    game_board = board()
    PLAYER_ONE = "X"
    PLAYER_TWO = "O"

    print("Tic Tac Toe")
    print()
    print_board(game_board)
    print()
    print("Please Provide number to play (1 - 9)")
    print()

    while True:
        if check_winner(game_board, PLAYER_ONE):
            print(f"{PLAYER_ONE} Won")
            break
        if check_winner(game_board, PLAYER_TWO):
            print(f"{PLAYER_TWO} Won")
            break
        if check_draw(game_board):
            print("Game Draw")
            break
        while True:
            if not (
                check_draw(game_board)
                or check_winner(game_board, PLAYER_ONE)
                or check_winner(game_board, PLAYER_TWO)
            ):
                try:
                    inp1 = int(input(f"{PLAYER_ONE}'s Turn (1 - 9): "))
                    print()
                    if valid_move(inp1, game_board):
                        mark(inp1, game_board, PLAYER_ONE)
                        break
                    else:
                        print("Invalid Value")
                except ValueError:
                    print("Invalid Value")
                    continue
            else:
                break

        print_board(game_board)
        print()
        while True:
            if not (
                check_draw(game_board)
                or check_winner(game_board, PLAYER_ONE)
                or check_winner(game_board, PLAYER_TWO)
            ):
                try:
                    inp2 = int(input(f"{PLAYER_TWO}'s Turn (1 - 9): "))
                    print()
                    if valid_move(inp2, game_board):
                        mark(inp2, game_board, PLAYER_TWO)
                        break
                    else:
                        print("Invalid Value")
                except ValueError:
                    print("Invalid Value")
                    continue
            else:
                break

        print_board(game_board)
        print()


# creates 2d array and popluate it with int 1- 9
def board() -> list:
    board = []
    num = 1
    for i in range(3):
        row = []
        for j in range(3):
            row.append(num)
            num += 1
        board.append(row)

    return board


# marking the board
def mark(value: int, board: list, payer: str) -> None:
    if value < 1 or value > 9:
        raise ValueError
    else:
        r, c = map_value_matrix(value, len(board))
        board[r][c] = payer


# check if the user's move is valid
def valid_move(value: int, board: list) -> bool:
    if value < 1 or value > 9:
        return False
    else:
        r, c = map_value_matrix(value, len(board))

        if board[r][c] == "X" or board[r][c] == "O":
            return False
        else:
            return True


# prints the game board
def print_board(board: list) -> None:
    print(tabulate(board, tablefmt="grid"))


def check_winner(board: list, player: str) -> str:
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return player
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return player
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return player
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return player

    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return player
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return player

    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return player


def check_draw(board: list) -> bool:
    for i in range(len(board)):
        for j in range(len(board)):
            if isinstance(board[i][j], int):
                return False
    return True


# helper funtion
def map_value_matrix(value: int, b_length: int) -> tuple:
    r = (value - 1) // b_length
    c = (value - 1) % b_length

    return r, c


if __name__ == "__main__":
    main()