#peg_solitaire

def create_board():
    board=[
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',1,1,1,' ',' '],
        [' ',' ',' ',1,1,1,' ',' '],
        [' ',1,1,1,1,1,1,1,' '],
        [' ',1,1,1,0,1,1,1,' '],
        [' ',1,1,1,1,1,1,1,' '],
        [' ',' ',' ',1,1,1,' ',' '],
        [' ',' ',' ',1,1,1,' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    ]

    return board


def print_board(board):
    print(' ','1','2','3','4','5','6','7')
    print(f"A {board[1][1]} {board[1][2]} {board[1][3]} {board[1][4]} {board[1][5]} {board[1][6]} {board[1][7]}")
    print(f"B {board[2][1]} {board[2][2]} {board[2][3]} {board[2][4]} {board[2][5]} {board[2][6]} {board[2][7]}")
    print(f"C {board[3][1]} {board[3][2]} {board[3][3]} {board[3][4]} {board[3][5]} {board[3][6]} {board[3][7]}")
    print(f"D {board[4][1]} {board[4][2]} {board[4][3]} {board[4][4]} {board[4][5]} {board[4][6]} {board[4][7]}")
    print(f"E {board[5][1]} {board[5][2]} {board[5][3]} {board[5][4]} {board[5][5]} {board[5][6]} {board[5][7]}")
    print(f"F {board[6][1]} {board[6][2]} {board[6][3]} {board[6][4]} {board[6][5]} {board[6][6]} {board[6][7]}")
    print(f"G {board[7][1]} {board[7][2]} {board[7][3]} {board[7][4]} {board[7][5]} {board[7][6]} {board[7][7]}")


def valid(choice,board):
    flag=False
    lines = [0, 1, 2, 3, 4, 5, 6, 7]
    ch = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    for i in range(1, 8):
        if choice[0] == ch[i]:
            line = lines[i]

    if board[line][int(choice[1])] != 0:
        if choice[2] == 'L':
            if int(choice[1])-2 <=0:
                print('Given peg position is out of board! ')
            else:
                if board[line][int(choice[1])-2] ==' ':
                    print('Moving peg will fall out of bounds!')
                elif board[line][int(choice[1])-1] == 0:
                    print('No peg at next position to jump over!')
                elif board[line][int(choice[1])-2] ==1:
                    print('Landing position is occupied!')
                else:
                    flag=True
        elif choice[2] == 'R':
            if int(choice[1])+2 >=8:
                print('Given peg position is out of board! ')
            else:
                if board[line][int(choice[1])+2] ==' ':
                    print('Moving peg will fall out of bounds!')
                elif board[line][int(choice[1])+1] ==0:
                    print('No peg at next position to jump over!')
                elif board[line][int(choice[1])+2] ==1:
                    print('Landing position is occupied!')
                else:
                    flag=True
        elif choice[2] == 'U':
            if line-2 <=0:
                print('Given peg position is out of board! ')
            else:
                if board[line-2][int(choice[1])] ==' ':
                    print('Moving peg will fall out of bounds!')
                elif board[line-1][int(choice[1])] == 0:
                    print('No peg at next position to jump over!')
                elif board[line-2][int(choice[1])] ==1:
                    print('Landing position is occupied!')
                else:
                    flag=True
        elif choice[2] == 'D':
            if line+2>=8:
                print('Given peg position is out of board! ')
            else:
                if board[line+2][int(choice[1])] ==' ':
                    print('Moving peg will fall out of bounds!')
                elif board[line+1][int(choice[1])] == 0:
                    print('No peg at next position to jump over!')
                elif board[line+2][int(choice[1])] ==1:
                    print('Landing position is occupied!')
                else:
                    flag=True
    else:
        print('Given peg position does not have a peg!')

    return flag


def check_point(board):
    #flag=True
    choice = input('Enter peg position followed by move (L, R, U, or D): ').upper()
    while True:
        if len(choice) !=3 :
            print('Something wrong with your input! ')
            choice = input('Enter peg position followed by move (L, R, U, or D): ').upper()
        else:
            if choice[0].isalpha() and choice[1].isdigit() and choice[2].isalpha():
                if choice[0] >='A' and choice[0] <='G' :
                    if int(choice[1])>=1 and int(choice[1])<=7:
                        if choice[2]=='L' or choice[2]=='R' or choice[2]=='U' or choice[2]=='D':
                            if choice[0]=='A' and int(choice[1])>=3 and int(choice[1])<=5:
                                flag = valid(choice, board)
                                if flag == False:
                                    choice = input('Enter peg position followed by move (L, R, U, or D): ').upper()
                                else:
                                    break
                            elif choice[0]=='B' and int(choice[1])>=3 and int(choice[1])<=5:
                                flag = valid(choice, board)
                                if flag == False:
                                    choice = input('Enter peg position followed by move (L, R, U, or D): ').upper()
                                else:
                                    break
                            elif choice[0]=='F' and int(choice[1])>=3 and int(choice[1])<=5:
                                flag = valid(choice, board)
                                if flag == False:
                                    choice = input('Enter peg position followed by move (L, R, U, or D): ').upper()
                                else:
                                    break
                            elif choice[0]=='G' and int(choice[1])>=3 and int(choice[1])<=5:
                                flag = valid(choice, board)
                                if flag == False:
                                    choice = input('Enter peg position followed by move (L, R, U, or D): ').upper()
                                else:
                                    break
                            elif choice[0]=='C' or choice[0]=='D' or choice[0]=='E':
                                flag = valid(choice, board)
                                if flag == False:
                                    choice = input('Enter peg position followed by move (L, R, U, or D): ').upper()
                                else:
                                    break
                            else:
                                print('Given peg position is out of board! ')
                                choice = input('Enter peg position followed by move (L, R, U, or D): ').upper()
                        else:
                            print('Direction is not L or R or U or D!')
                            choice = input('Enter peg position followed by move (L, R, U, or D): ').upper()
                    else:
                        print('Given peg position is out of board! ')
                        choice = input('Enter peg position followed by move (L, R, U, or D): ').upper()
                else:
                    print('Given peg position is out of board! ')
                    choice = input('Enter peg position followed by move (L, R, U, or D): ').upper()
            else:
                print('Something wrong with your input! ')
                choice = input('Enter peg position followed by move (L, R, U, or D): ').upper()

    return choice


def move_ok(choice,board):
    lines = [0, 1, 2, 3, 4, 5, 6, 7]
    ch = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    for i in range(1, 8):
        if choice[0] == ch[i]:
            line = lines[i]

    if choice[2]=='L':
        board[line][int(choice[1])] = 0
        board[line][int(choice[1])-1] = 0
        board[line][int(choice[1])-2] = 1
    elif choice[2]=='R':
        board[line][int(choice[1])] = 0
        board[line][int(choice[1])+1] = 0
        board[line][int(choice[1])+2] = 1
    elif choice[2]=='U':
        board[line][int(choice[1])] = 0
        board[line-1][int(choice[1])] = 0
        board[line-2][int(choice[1])] = 1
    elif choice[2]=='D':
        board[line][int(choice[1])] = 0
        board[line+1][int(choice[1])] = 0
        board[line+2][int(choice[1])] = 1

    return board


def check_finish_board(board):
    flag=False
    p =0
    for i in range(1,8):
        for j in range(1,8):
            if board[i][j] ==0:
                p +=1
    flag1=False
    if p !=32:
        for i in range(1,8):
            for j in range(1,8):
                if board[i][j]==1:
                    if board[i][j+1]==1 and board[i][j+2]==0:
                        flag1=True
                    elif board[i][j-1]==1 and board[i][j-2]==0:
                        flag1=True
                    elif board[i+1][j]==1 and board[i+2][j]==0:
                        flag1=True
                    elif board[i-1][j]==1 and board[i-2][j]==0:
                        flag1=True
    else:
        flag=True

    if flag1==False:
        flag=True

    return flag


def main():

    board=create_board()
    print_board(board)

    while True:
        #tsekarei ean i thesi einai sosti, alla kai ean i kinisi einai sosti meso tis valid
        choice=check_point(board)
        #ektelei tin kinisi
        board=move_ok(choice,board)
        print_board(board)

        #elegxei ean iparxei alli kinisi
        flag= check_finish_board(board)
        if flag==True:
            break

    p = 0
    for i in range(1, 8):
        for j in range(1, 8):
            if board[i][j] == 1:
                p += 1

    if p==1:
        print('You WON!!!')
    else:
        print(f"You lost, as left {p} pegs")

main()