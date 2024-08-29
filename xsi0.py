board = [" ", "1", "2", "3", "1", "-", "-", "-", "2", "-", "-", "-", "3", "-", "-", "-"]
player_1_turn = True
have_winner = False


def print_board():
    for i in range(0, 16, 4):
        print(board[i] + "|" + board[i + 1] + "|" + board[i + 2] + "|" + board[i + 3])
    print()


def verificacastigatorul(symbol):
    for i in range(1, 4):
        if board[4 * i + 1] == symbol and board[4 * i + 2] == symbol and board[4 * i + 3] == symbol:
            return True

    for j in range(1, 4):
        if board[4 * 1 + j] == symbol and board[4 * 2 + j] == symbol and board[4 * 3 + j] == symbol:
            return True

    if board[4 * 1 + 1] == symbol and board[4 * 2 + 2] == symbol and board[4 * 3 + 3] == symbol:
        return True
    if board[4 * 1 + 3] == symbol and board[4 * 2 + 2] == symbol and board[4 * 3 + 1] == symbol:
        return True

    return False


def minimax(is_maximizing):
    if verificacastigatorul("x"):
        return 10
    if verificacastigatorul("0"):
        return -10
    if "-" not in board[5:15]:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(1, 4):
            for j in range(1, 4):
                index = 4 * i + j
                if board[index] == "-":
                    board[index] = "x"
                    score = minimax(False)
                    board[index] = "-"
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(1, 4):
            for j in range(1, 4):
                index = 4 * i + j
                if board[index] == "-":
                    board[index] = "0"
                    score = minimax(True)
                    board[index] = "-"
                    best_score = min(score, best_score)
        return best_score


def miscareabotului():
    best_score = -float('inf')
    best_move = None
    for i in range(1, 4):
        for j in range(1, 4):
            index = 4 * i + j
            if board[index] == "-":
                board[index] = "x"
                score = minimax(False)
                board[index] = "-"
                if score > best_score:
                    best_score = score
                    best_move = index
    board[best_move] = "x"


while not have_winner:
    print_board()

    if player_1_turn:
        print("Jucatorul 1")
        new_place = False
        while not new_place:
            row, column = -1, -1
            while row < 1 or row > 3:
                row = int(input("Linia (1-3):\n"))
            while column < 1 or column > 3:
                column = int(input("Coloana (1-3):\n"))

            index = 4 * row + column

            if board[index] == "-":
                new_place = True
                board[index] = "0"
    else:
        print("Jucatorul 2 (Bot)")
        miscareabotului()


    if verificacastigatorul("0"):
        print_board()
        print("Jucatorul 1 a castigat!")
        have_winner = True
    elif verificacastigatorul("x"):
        print_board()
        print("Jucatorul 2 (Bot) a castigat!")
        have_winner = True

    player_1_turn = not player_1_turn

    if "-" not in board[5:15] and not have_winner:
        print_board()
        print("Remiza!")
        have_winner = True




        






















