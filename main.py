def check_win(board):

    def check_verticals():
        for row in range(len(board)):
            count_ver = 1
            for column in range(1, len(board)):
                if board[row][0] == board[row][column]:
                    count_ver += 1
                # print(count_ver)
            if count_ver == len(board):
                return 1
            else:
                return 0

    def check_horizontals():
        for column in range(len(board)):
            count_hor = 1
            for row in range(1, len(board)):
                if board[0][column] == board[row][column]:
                    count_hor += 1
                # print(count_hor)
            if count_hor == len(board):
                return 1
            else:
                return 0

    def check_diagonals():
        def primary():
            count_dia1 = 1
            for i in range(1, len(board)):
                if board[0][0] == board[i][i]:
                    count_dia1 += 1
                # print(count_dia)
            if count_dia1 == len(board):
                return 1
            else:
                return 0

        def secondary():
            count_dia1 = 1
            for i in range(1, len(board)):
                if board[0][len(board) - 1] == board[i][len(board) - 1 - i]:
                    count_dia1 += 1
                # print(count_dia)
            if count_dia1 == len(board):
                return 1
            else:
                return 0

        p = primary()
        s = secondary()
        if p == 1 or s == 1:
            return 1
        else:
            return 0

    count_verticals = check_verticals()
    count_horizontals = check_horizontals()
    count_diagonals = check_diagonals()

    if count_verticals == 1 or count_horizontals == 1 or count_diagonals == 1:
        return True
    return False


game = [['x', 'o', 'x', 'o', ''], ['x', 'x', 'o', 'x', 'o'], ['x', 'o', 'o', 'o', 'x'], ['x', 'o', 'o', 'x', 'o'], ['x', 'o', 'o', 'o', 'o']]  # change here to test
if check_win(game):
    print('!! WE HAVE A WINNER !!')
else:
    print(" -_- DRAW -_- ")
# print(len(game))
print()
for i in range(len(game)):
    for j in range(len(game)):
        print(game[i][j], end='|')
    print("\n-----------")
