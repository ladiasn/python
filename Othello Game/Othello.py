from random import randrange, seed


def create_board():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return board


def computer_board():
    board1 = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return board1


def print_board(board):
    print(f"   0   1   2   3   4   5   6   7  ")
    print('-' * 34)
    for i in range(8):
        print(i, end='')
        for j in range(8):
            print(f"| {board[i][j]} ", end='')
        print('|')
        print(' ')
    print('-' * 34)


def print_computer_board(board1):
    print(f"### Computer Board ###")
    print(f"   0   1   2   3   4   5   6   7  ")
    print('-' * 34)
    for i in range(8):
        print(i, end='')
        for j in range(8):
            print(f"| {board1[i][j]} ", end='')
        print('|')
        print(' ')
    print('-' * 34)


def move_up(board, x, y, color):
    line = x - 1
    if color == 1:
        upp = []
        p = 0
        thesi = -1
        for i in range(line, -1, -1):
            if board[i][y] == 1:
                p += 1

        if p >= 1:
            while True:
                if board[line][y] == 1:
                    thesi = line
                    break
                line -= 1
        if p >= 1:
            p1 = 0
            line1 = x - 1
            for i in range(line1, thesi, -1):
                if board[i][y] == 2:
                    p1 += 1

            plithos = (x - 1) - thesi
            #gia na doume oti sta endiamesa kelia iparxei to 2 kai oxi to 0
            if p1 == plithos:
                for i in range(line1, thesi, -1):
                    upp.append((i, y))
    else:
        upp = []
        p = 0
        thesi = -1
        for i in range(line, -1, -1):
            if board[i][y] == 2:
                p += 1

        if p >= 1:
            while True:
                if board[line][y] == 2:
                    thesi = line
                    break
                line -= 1
        if p >= 1:
            p1 = 0
            line1 = x - 1
            for i in range(line1, thesi, -1):
                if board[i][y] == 1:
                    p1 += 1

            plithos = (x - 1) - thesi

            if p1 == plithos:
                for i in range(line1, thesi, -1):
                    upp.append((i, y))

    return upp


def move_down(board, x, y, color):
    line = x + 1
    if color == 1:
        upd = []
        p = 0
        thesi = -1
        for i in range(line, 8):
            if board[i][y] == 1:
                p += 1

        if p >= 1:
            while True:
                if board[line][y] == 1:
                    thesi = line
                    break
                line += 1

        if p >= 1:
            p1 = 0
            line1 = x + 1
            for i in range(line1, thesi):
                if board[i][y] == 2:
                    p1 += 1

            plithos = thesi - (x + 1)

            if p1 == plithos:
                for i in range(line1, thesi):
                    upd.append((i, y))
    else:
        upd = []
        p = 0
        thesi = -1
        for i in range(line, 8):
            if board[i][y] == 2:
                p += 1

        if p >= 1:
            while True:
                if board[line][y] == 2:
                    thesi = line
                    break
                line += 1
        if p >= 1:
            p1 = 0
            line1 = x + 1
            for i in range(line1, thesi):
                if board[i][y] == 1:
                    p1 += 1

            plithos = thesi - (x + 1)

            if p1 == plithos:
                for i in range(line1, thesi):
                    upd.append((i, y))

    return upd


def move_right(board, x, y, color):
    col = y + 1
    if color == 1:
        right = []
        p = 0
        thesi = -1
        for j in range(col, 8):
            if board[x][j] == 1:
                p += 1

        if p >= 1:
            while True:
                if board[x][col] == 1:
                    thesi = col
                    break
                col += 1

        if p >= 1:
            p1 = 0
            col1 = y + 1
            for j in range(col1, thesi):
                if board[x][j] == 2:
                    p1 += 1

            plithos = thesi - (y + 1)

            if p1 == plithos:
                for j in range(col1, thesi):
                    right.append((x, j))
    else:
        right = []
        p = 0
        thesi = -1
        for j in range(col, 8):
            if board[x][j] == 2:
                p += 1

        if p >= 1:
            while True:
                if board[x][col] == 2:
                    thesi = col
                    break
                col += 1

        if p >= 1:
            p1 = 0
            col1 = y + 1
            for j in range(col1, thesi):
                if board[x][j] == 1:
                    p1 += 1

            plithos = thesi - (y + 1)

            if p1 == plithos:
                for j in range(col1, thesi):
                    right.append((x, j))
    return right


def move_left(board, x, y, color):
    col = y - 1
    if color == 1:
        left = []
        p = 0
        thesi = -1
        for j in range(col, -1, -1):
            if board[x][j] == 1:
                p += 1

        if p >= 1:
            while True:
                if board[x][col] == 1:
                    thesi = col
                    break
                col -= 1

        if p >= 1:
            p1 = 0
            col1 = y - 1
            for j in range(col1, thesi - 1, -1):
                if board[x][j] == 2:
                    p1 += 1

            plithos = (y - 1) - thesi

            if p1 == plithos:
                for j in range(col1, thesi, -1):
                    left.append((x, j))
    else:
        left = []
        p = 0
        thesi = -1
        for j in range(col, -1, -1):
            if board[x][j] == 2:
                p += 1

        if p >= 1:
            while True:
                if board[x][col] == 2:
                    thesi = col
                    break
                col -= 1

        if p >= 1:
            p1 = 0
            col1 = y - 1
            for j in range(col1, thesi - 1, -1):
                if board[x][j] == 1:
                    p1 += 1

            plithos = (y - 1) - thesi

            if p1 == plithos:
                for j in range(col1, thesi, -1):
                    left.append((x, j))
    return left


def move_up_right(board, x, y, color):
    line = x - 1
    col = y + 1
    if color == 1:
        upright = []
        p = 0
        thesi_i = -1
        thesi_j = -1
        for i in range(line, -1, -1):
            for j in range(col, 8):
                if i + j == x + y:
                    if board[i][j] == 1:
                        p += 1

        if p >= 1:
            p2 = 1
            for i in range(line, -1, -1):
                for j in range(col, 8):
                    if i + j == x + y:
                        if board[i][j] == 1:
                            if p2 == 1:
                                thesi_i = i
                                thesi_j = j
                                p2 += 1
        if p >= 1:
            p1 = 0
            col1 = y + 1
            line1 = x - 1
            for i in range(line1, thesi_i, -1):
                for j in range(col1, thesi_j):
                    if i + j == x + y:
                        if board[i][j] == 2:
                            p1 += 1

            plithos = x - thesi_i - 1

            if p1 == plithos:
                for i in range(line1, thesi_i, -1):
                    for j in range(col1, thesi_j):
                        if i + j == x + y:
                            upright.append((i, j))
    else:
        upright = []
        p = 0
        thesi_i = -1
        thesi_j = -1
        for i in range(line, -1, -1):
            for j in range(col, 8):
                if i + j == x + y:
                    if board[i][j] == 2:
                        p += 1

        if p >= 1:
            p2 = 1
            for i in range(line, -1, -1):
                for j in range(col, 8):
                    if i + j == x + y:
                        if board[i][j] == 2:
                            if p2 == 1:
                                thesi_i = i
                                thesi_j = j
                                p2 += 1

        if p >= 1:
            p1 = 0
            col1 = y + 1
            line1 = x - 1
            for i in range(line1, thesi_i, -1):
                for j in range(col1, thesi_j):
                    if i + j == x + y:
                        if board[i][j] == 1:
                            p1 += 1

            plithos = x - thesi_i - 1

            if p1 == plithos:
                for i in range(line1, thesi_i, -1):
                    for j in range(col1, thesi_j):
                        if i + j == x + y:
                            upright.append((i, j))
    return upright


def move_down_right(board, x, y, color):
    line = x + 1
    col = y + 1
    if color == 1:
        downright = []
        p = 0
        thesi_i = -1
        thesi_j = -1
        sum = x + y
        for i in range(line, 8):
            for j in range(col, 8):
                if i + j == sum + 2:
                    if board[i][j] == 1:
                        p += 1
            sum += 2

        if p >= 1:
            p2 = 1
            sum = x + y
            for i in range(line, 8):
                for j in range(col, 8):
                    if i + j == sum + 2:
                        if board[i][j] == 1:
                            if p2 == 1:
                                thesi_i = i
                                thesi_j = j
                                p2 += 1
                sum += 2

        if p >= 1:
            p1 = 0
            col1 = y + 1
            line1 = x + 1
            sum = x + y
            for i in range(line1, thesi_i):
                for j in range(col1, thesi_j):
                    if i + j == sum + 2:
                        if board[i][j] == 2:
                            p1 += 1
                sum += 2

            plithos = thesi_i - x - 1

            if p1 == plithos:
                sum = x + y
                for i in range(line1, thesi_i):
                    for j in range(col1, thesi_j):
                        if i + j == sum + 2:
                            downright.append((i, j))
                    sum += 2
    else:
        downright = []
        p = 0
        thesi_i = -1
        thesi_j = -1
        sum = x + y
        for i in range(line, 8):
            for j in range(col, 8):
                if i + j == sum + 2:
                    if board[i][j] == 2:
                        p += 1
            sum += 2

        if p >= 1:
            p2 = 1
            sum = x + y
            for i in range(line, 8):
                for j in range(col, 8):
                    if i + j == sum + 2:
                        if board[i][j] == 2:
                            if p2 == 1:
                                thesi_i = i
                                thesi_j = j
                                p2 += 1
                sum += 2
        if p >= 1:
            p1 = 0
            col1 = y + 1
            line1 = x + 1
            sum = x + y
            for i in range(line1, thesi_i):
                for j in range(col1, thesi_j):
                    if i + j == sum + 2:
                        if board[i][j] == 1:
                            p1 += 1
                sum += 2

            plithos = thesi_i - x - 1

            if p1 == plithos:
                sum = x + y
                for i in range(line1, thesi_i):
                    for j in range(col1, thesi_j):
                        if i + j == sum + 2:
                            downright.append((i, j))
                    sum += 2
    return downright


def move_up_left(board, x, y, color):
    line = x - 1
    col = y - 1
    if color == 1:
        upleft = []
        p = 0
        thesi_i = -1
        thesi_j = -1
        sum = x+y
        for i in range(line, -1, -1):
            for j in range(col, -1, -1):
                if i + j == sum -2:
                    if board[i][j] == 1:
                        p += 1
            sum -=2

        if p >= 1:
            p2 = 1
            sum =x+y
            for i in range(line, -1, -1):
                for j in range(col, -1, -1):
                    if i+j==sum-2:
                        if board[i][j] == 1:
                            if p2 == 1:
                                thesi_i = i
                                thesi_j = j
                                p2 += 1
                sum -=2
        if p >= 1:
            p1 = 0
            col1 = y - 1
            line1 = x - 1
            sum=x+y
            for i in range(line1, thesi_i, -1):
                for j in range(col1, thesi_j, -1):
                    if i+j==sum-2:
                        if board[i][j] == 2:
                            p1 += 1
                sum -=2

            plithos = x - thesi_i - 1

            if p1 == plithos:
                sum=x+y
                for i in range(line1, thesi_i, -1):
                    for j in range(col1, thesi_j, -1):
                        if i+j==sum-2:
                            upleft.append((i, j))
                    sum -=2
    else:
        upleft = []
        p = 0
        thesi_i = -1
        thesi_j = -1
        sum = x + y
        for i in range(line, -1, -1):
            for j in range(col, -1, -1):
                if i + j == sum - 2:
                    if board[i][j] == 2:
                        p += 1
            sum -= 2

        if p >= 1:
            p2 = 1
            sum = x + y
            for i in range(line, -1, -1):
                for j in range(col, -1, -1):
                    if i + j == sum - 2:
                        if board[i][j] == 2:
                            if p2 == 1:
                                thesi_i = i
                                thesi_j = j
                                p2 += 1
                sum -= 2

        if p >= 1:
            p1 = 0
            col1 = y - 1
            line1 = x - 1
            sum = x + y
            for i in range(line1, thesi_i, -1):
                for j in range(col1, thesi_j, -1):
                    if i + j==sum-2:
                        if board[i][j] == 1:
                            p1 += 1
                sum -= 2

            plithos = x - thesi_i - 1

            if p1 == plithos:
                sum = x + y
                for i in range(line1, thesi_i, -1):
                    for j in range(col1, thesi_j, -1):
                        if i + j == sum - 2:
                            upleft.append((i, j))
                    sum -= 2
    return upleft


def move_down_left(board, x, y, color):
    line = x + 1
    col = y - 1
    if color == 1:
        downleft = []
        p = 0
        thesi_i = -1
        thesi_j = -1
        for i in range(line, 8):
            for j in range(col, -1, -1):
                if i + j == x + y:
                    if board[i][j] == 1:
                        p += 1

        if p >= 1:
            p2 = 1
            for i in range(line, 8):
                for j in range(col, -1, -1):
                    if i + j == x + y:
                        if board[i][j] == 1:
                            if p2 == 1:
                                thesi_i = i
                                thesi_j = j
                                p2 += 1

        if p >= 1:
            p1 = 0
            line1 = x + 1
            col1 = y - 1
            for i in range(line1, thesi_i):
                for j in range(col1, thesi_j, -1):
                    if i + j == x + y:
                        if board[i][j] == 2:
                            p1 += 1

            plithos = thesi_i - x - 1

            if p1 == plithos:
                for i in range(line1, thesi_i):
                    for j in range(col1, thesi_j, -1):
                        if i + j == x + y:
                            downleft.append((i, j))
    else:
        downleft = []
        p = 0
        thesi_i = -1
        thesi_j = -1
        for i in range(line, 8):
            for j in range(col, -1, -1):
                if i + j == x + y:
                    if board[i][j] == 2:
                        p += 1

        if p >= 1:
            p2 = 1
            for i in range(line, 8):
                for j in range(col, -1, -1):
                    if i + j == x + y:
                        if board[i][j] == 2:
                            if p2 == 1:
                                thesi_i = i
                                thesi_j = j
                                p2 += 1

        if p >= 1:
            p1 = 0
            line1 = x + 1
            col1 = y - 1
            for i in range(line1, thesi_i):
                for j in range(col1, thesi_j, -1):
                    if i + j == x + y:
                        if board[i][j] == 1:
                            p1 += 1

            plithos = thesi_i - x - 1

            if p1 == plithos:
                for i in range(line1, thesi_i):
                    for j in range(col1, thesi_j, -1):
                        if i + j == x + y:
                            downleft.append((i, j))
    return downleft


def reverse_count(board, i, j, color):
    if board[i][j] != 0:
        return 0
    else:
        upp_list = move_up(board, i, j, color)
        # print(f" upp_list {upp_list}")
        down_list = move_down(board, i, j, color)
        # print(f" down_list {down_list}")
        right_list = move_right(board, i, j, color)
        # print(f" right_list {right_list}")
        left_list = move_left(board, i, j, color)
        # print(f" left_list {left_list}")
        upright_list = move_up_right(board, i, j, color)
        # print(f" upright_list {upright_list}")
        downright_list = move_down_right(board, i, j, color)
        # print(f" downright_list {downright_list}")
        upleft = move_up_left(board, i, j, color)
        # print(f" upleft {upleft}")
        downleft = move_down_left(board, i, j, color)
        # print(f" downleft {downleft}")
        sum = len(upp_list) + len(down_list) + len(right_list) + len(left_list) + len(upright_list) + len(downright_list) + \
              len(upleft) + len(downleft)
        return sum


def add_checker(board, i, j, color):
    board[i][j] = color
    upp_list = move_up(board, i, j, color)
    if upp_list != []:
        for c in upp_list:
            board[c[0]][c[1]] = color

    down_list = move_down(board, i, j, color)
    if down_list != []:
        for c in down_list:
            board[c[0]][c[1]] = color

    right_list = move_right(board, i, j, color)
    if right_list != []:
        for c in right_list:
            board[c[0]][c[1]] = color

    left_list = move_left(board, i, j, color)
    if left_list != []:
        for c in left_list:
            board[c[0]][c[1]] = color

    upright_list = move_up_right(board, i, j, color)
    if upright_list != []:
        for c in upright_list:
            board[c[0]][c[1]] = color

    downright_list = move_down_right(board, i, j, color)
    if downright_list != []:
        for c in downright_list:
            board[c[0]][c[1]] = color

    downleft = move_down_left(board, i, j, color)
    if downleft != []:
        for c in downleft:
            board[c[0]][c[1]] = color

    upleft = move_up_left(board, i, j, color)
    if upleft != []:
        for c in upleft:
            board[c[0]][c[1]] = color


def human_play(board, color):
    flag = False
    for i in range(8):
        for j in range(8):
            x = reverse_count(board, i, j, color)
            if x == 0:
                pass
            else:
                flag = True
    if flag == True:
        while True:
            x = int(input('Give your line (0-7): '))
            while True:
                if x >= 0 and x <= 7:
                    break
                else:
                    x = int(input('Wrong!!! Give your line (0-7): '))

            y = int(input('Give your column (0-7): '))
            while True:
                if y >= 0 and y <= 7:
                    break
                else:
                    y = int(input('Wrong!!! Give your column (0-7): '))

            result = reverse_count(board, x, y, color)
            if result == 0:
                print(f"This line {x} and column {y} are not good movement")
            else:
                add_checker(board, x, y, color)
                break
    return flag


def compute_counts(board,board1,color):
    for i in range(8):
        for j in range(8):
            if board[i][j] ==0:
                upp_list = move_up(board, i, j, color)
                if len(upp_list) !=0:
                    board1[i][j]=len(upp_list)

                down_list = move_down(board, i, j, color)
                if len(down_list) !=0:
                    board1[i][j]=len(down_list)

                right_list = move_right(board, i, j, color)
                if len(right_list) !=0:
                    board1[i][j]=len(right_list)

                left_list = move_left(board, i, j, color)
                if len(left_list) !=0:
                    board1[i][j]=len(left_list)

                upright_list = move_up_right(board, i, j, color)
                if len(upright_list) !=0:
                    board1[i][j]=len(upright_list)

                downright_list = move_down_right(board, i, j, color)
                if len(downright_list) !=0:
                    board1[i][j]=len(downright_list)

                upleft = move_up_left(board, i, j, color)
                if len(upleft) !=0:
                    board1[i][j]=len(upleft)

                downleft = move_down_left(board, i, j, color)
                if len(downleft) !=0:
                    board1[i][j]=len(downleft)

    return board1


def computer_play(board,board1,color):
    flag = False
    for i in range(8):
        for j in range(8):
            x = reverse_count(board, i, j, color)
            if x != 0:
                flag = True
    if flag == True:
        compute_counts(board,board1,color)
        #print_computer_board(board1)
        max=-1
        for i in range(8):
            for j in range(8):
                if board1[i][j] > max:
                    max = board1[i][j]
                    thesi_i = i
                    thesi_j = j
        p=0
        for i in range(8):
            for j in range(8):
                if board1[i][j] == max:
                    p +=1
        if p==1:
            add_checker(board, thesi_i, thesi_j, color)
        else:
            maxlist=[]
            for i in range(8):
                for j in range(8):
                    if board1[i][j] == max:
                        maxlist.append((i,j))
            x=randrange(len(maxlist))
            #print(maxlist)
            thesi_i =maxlist[x][0]
            thesi_j =maxlist[x][1]
            add_checker(board, thesi_i, thesi_j, color)

    return flag


def print_score(board):
    p1 = 0
    p2 = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                p1 += 1
            elif board[i][j] == 2:
                p2 += 1
    return p1, p2


def main():

    board = create_board()
    board1 = computer_board()
    print_board(board)

    choice = input('Play against another player (p) or against computer (c) ?: ').upper()
    while True:
        if choice == 'P' or choice == 'C':
            break
        else:
            choice = input('Wrong!!! Play against another player (p) or against computer (c) ?: ').upper()

    #2_players
    if choice == 'P':
        color = 2
        color1 = 'White'
        flag_1=False
        flag_2=False
        while True:
            if color == 2:
                color = 1
                color1 = 'Black'
            else:
                color = 2
                color1 = 'White'
            print(f"Play the {color} - ({color1})")
            result = human_play(board, color)
            if result == True:
                print_board(board)
                if color==1:
                    flag_2=False
                if color==2:
                    flag_1=False
            else:
                print('No move')
                if color==1:
                    flag_1=True
                if color==2:
                    flag_2=True

            print('----- Score ------')
            print('- Black Vs White -')
            w1,w2=print_score(board)
            print(f"   -- {w1} - {w2} --")
            print('-'*18)

            p3=0
            for i in range(8):
                for j in range(8):
                    if board[i][j] !=0:
                        p3 += 1

            if p3==64:
                if w1>w2:
                    print('Black Wins!!!!!')
                else:
                    print('White Wins!!!!!')
                break

            if flag_1==True and flag_2==True:
                print('No more moves - end of the game')
                if w1 > w2:
                    print('Black  Wins!!!!!')
                else:
                    print('White  Wins!!!!!')
                break

    else:
        color = 2
        color1 = 'White'
        flag_1 = False
        flag_2 = False
        while True:
            if color == 2:
                color = 1
                color1 = 'Black - Player'
                print(f"Play the {color} - ({color1})")
                result = human_play(board, color)
                if result == True:
                    print_board(board)
                    if color == 1:
                        flag_2 = False
                else:
                    print('No move')
                    if color == 1:
                        flag_1 = True
            else:
                board1 = computer_board()
                #print_computer_board(board1)
                color = 2
                color1 = 'White - Computer'
                print(f"Play the {color} - ({color1})")
                result = computer_play(board, board1, color)
                if result == True:
                    print_board(board)
                    if color == 2:
                        flag_1 = False
                else:
                    print('No move')
                    if color == 2:
                        flag_2 = True

            print('----- Score ------')
            print('- Black Vs White -')
            print('-Player Vs Computer-')
            w1, w2 = print_score(board)
            print(f"   -- {w1} - {w2} --")
            print('-' * 18)

            p3 = 0
            for i in range(8):
                for j in range(8):
                    if board[i][j] != 0:
                        p3 += 1

            if p3 == 64:
                if w1 > w2:
                    print('Black - Player Wins!!!!!')
                else:
                    print('White - Computer Wins!!!!!')
                break

            if flag_1 == True and flag_2 == True:
                print('No more moves - end of the game')
                if w1 > w2:
                    print('Black - Player Wins!!!!!')
                else:
                    print('White - Computer Wins!!!!!')
                break


main()
