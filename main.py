def check_win(board):
    count_verticals = [0] * len(board)
    count_horizontals = [0] * len(board)
    count_diagonals = [0, 0]

    def check_verticals():
        for row in range(len(board)):
            count_ver = 1
            for column in range(1, len(board)):
                if board[row][0] == board[row][column]:
                    count_ver += 1
                # print(count_ver)
            if count_ver == len(board):
                count_verticals[row] = 1
                break

    def check_horizontals():
        for column in range(len(board)):
            count_hor = 1
            for row in range(1, len(board)):
                if board[0][column] == board[row][column]:
                    count_hor += 1
                # print(count_hor)
            if count_hor == len(board):
                count_horizontals[column] = 1
                break

    def check_diagonals():
        def primary():
            count_dia1 = 1
            for i in range(1, len(board)):
                if board[0][0] == board[i][i]:
                    count_dia1 += 1
                # print(count_dia)
            if count_dia1 == len(board):
                count_diagonals[0] = 1

        def secondary():
            count_dia1 = 1
            for i in range(1, len(board)):
                if board[0][len(board) - 1] == board[i][len(board) - 1 - i]:
                    count_dia1 += 1
                # print(count_dia)
            if count_dia1 == len(board):
                count_diagonals[1] = 1

        primary()
        secondary()

    check_verticals()
    check_horizontals()
    check_diagonals()
    # print(count_verticals, 'v')
    # print(count_horizontals, "h")
    # print(count_diagonals, 'd')

    if 1 in count_verticals:
        # print(count_verticals, 'v')
        return True
    elif 1 in count_horizontals:
        # print(count_horizontals, "h")
        return True
    elif 1 in count_diagonals:
        # print(count_diagonals, 'd')
        return True
    else:
        return False


game = [['x', 'o', 'x', 'o'], ['o', 'x', 'o', 'x'], ['x', 'x', 'x', 'o'], ['x', 'o', 'o', 'x']]  # change here to test
if check_win(game):
    print('!! WE HAVE A WINNER !!')
else:
    print(" -_- DRAW -_- ")
# print(len(game))
