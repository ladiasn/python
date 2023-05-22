from random import randint

def create_board():
    board=[
            [' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ']
            ]
    return board


def print_board1(board1, board2):
    print('     P1            P2')
    print(' ','1','2','3','4','5', '  ', '1', '2', '3', '4', '5')

    print(f"a {board1[0][0]} {board1[0][1]} {board1[0][2]} {board1[0][3]} {board1[0][4]}  a {board2[0][0]} {board2[0][1]} {board2[0][2]} {board2[0][3]} {board2[0][4]}")
    print(f"b {board1[1][0]} {board1[1][1]} {board1[1][2]} {board1[1][3]} {board1[1][4]}  b {board2[1][0]} {board2[1][1]} {board2[1][2]} {board2[1][3]} {board2[1][4]}")
    print(f"c {board1[2][0]} {board1[2][1]} {board1[2][2]} {board1[2][3]} {board1[2][4]}  c {board2[2][0]} {board2[2][1]} {board2[2][2]} {board2[2][3]} {board2[2][4]}")
    print(f"d {board1[3][0]} {board1[3][1]} {board1[3][2]} {board1[3][3]} {board1[3][4]}  d {board2[3][0]} {board2[3][1]} {board2[3][2]} {board2[3][3]} {board2[3][4]}")
    print(f"e {board1[4][0]} {board1[4][1]} {board1[4][2]} {board1[4][3]} {board1[4][4]}  e {board2[4][0]} {board2[4][1]} {board2[4][2]} {board2[4][3]} {board2[4][4]}")


def check_ship(ship,board):

    while True:
        if len(ship) == 2 and ship[0].isalpha() and ship[1].isdigit():
            if ship[0] == 'a' or ship[0] == 'b' or ship[0] == 'c' or ship[0] == 'd' or ship[0] == 'e':
                if int(ship[1]) >= 1 and int(ship[1]) <= 5:
                    if ship[0] == 'a':
                        x = 0
                    elif ship[0] == 'b':
                        x = 1
                    elif ship[0] == 'c':
                        x = 2
                    elif ship[0] == 'd':
                        x = 3
                    elif ship[0] == 'e':
                        x = 4

                    y = int(ship[1]) - 1
                    if board[x][y] == ' ':
                        break
                    else:
                        ship = input('Invalid position, or position already taken. Try again: ')
                else:
                    ship = input('Invalid position, or position already taken. Try again: ')
            else:
                ship = input('Invalid position, or position already taken. Try again: ')
        else:
            ship = input('Invalid position, or position already taken. Try again: ')
    return ship


def insert_ships(choice1,board):
    for i in range(1, 6):
        ship = input(f"Player {choice1} enter the position of your ship no {i}: ")
        ship=check_ship(ship,board)
        if ship[0] == 'a':
            x = 0
        elif ship[0] == 'b':
            x = 1
        elif ship[0] == 'c':
            x = 2
        elif ship[0] == 'd':
            x = 3
        elif ship[0] == 'e':
            x = 4
        y = int(ship[1]) - 1
        board[x][y]='B'

    return board


def insert_ships_cpu(board):
    for i in range(5):
        while True:
            x = randint(1, 5)
            if x == 1:
                xa = 'a'
            elif x == 2:
                xa = 'b'
            elif x == 3:
                xa = 'c'
            elif x == 4:
                xa = 'd'
            elif x == 5:
                xa = 'e'
            y = randint(1, 5)
            if board[x-1][y-1]==' ':
                board[x-1][y-1] = 'B'
                break
    return board


def main():

    board1=create_board()
    board_1_b=create_board()
    board2=create_board()
    board_2_b=create_board()

    #print_board1(board1,board2)
    print('BATTLESHIP GAME')
    print("The objective is to sink the opponent's ships before the opponent sinks yours.")
    choice = int(input("Input 1 for 1-player game or 2 for 2-player game: "))
    while True:
        if choice==1 or choice==2:
            break
        else:
            choice = int(input('Wrong! Input 1 for 1-player game or 2 for 2-player game: '))

    #player against player
    if choice==1:

        print('--- Player 1 Create your Board ---')
        choice1=1
        board_1_b=insert_ships(choice1, board_1_b)
        choice1=2
        print('--- Player 2 Create your Board ---')
        board_2_b = insert_ships(choice1, board_2_b)

        print('----- Where are the ships -----')
        print_board1(board_1_b,board_2_b)

        player=randint(1,2)
        print(f"Player {player} starts first")
        print_board1(board1, board2)
        while True:

            if player==1:
                b_ship=input(f"Player {player} enter the position to throw your missile: ")
                b_ship=check_ship(b_ship,board2)
                print(f"Missible thrown at {b_ship}")
                if b_ship[0] == 'a':
                    x = 0
                elif b_ship[0] == 'b':
                    x = 1
                elif b_ship[0] == 'c':
                    x = 2
                elif b_ship[0] == 'd':
                    x = 3
                elif b_ship[0] == 'e':
                    x = 4
                y = int(b_ship[1]) - 1
                if board_2_b[x][y] != 'B':
                    print('Target missed!')
                    board2[x][y] = 'x'
                else:
                    print('Target hit!')
                    board2[x][y] = 'o'

                print_board1(board1, board2)

            else:
                b_ship = input(f"Player {player} enter the position to throw your missile: ")
                b_ship = check_ship(b_ship, board1)
                print(f"Missible thrown at {b_ship}")
                if b_ship[0] == 'a':
                    x = 0
                elif b_ship[0] == 'b':
                    x = 1
                elif b_ship[0] == 'c':
                    x = 2
                elif b_ship[0] == 'd':
                    x = 3
                elif b_ship[0] == 'e':
                    x = 4
                y = int(b_ship[1]) - 1
                if board_1_b[x][y] != 'B':
                    print('Target missed!')
                    board1[x][y] = 'x'
                else:
                    print('Target hit!')
                    board1[x][y] = 'o'

                print_board1(board1, board2)

            p1 = 0
            p2 = 0
            for i in range(5):
                for j in range(5):
                    if board2[i][j] == 'o':
                        p1 += 1
                    if board1[i][j] == 'o':
                        p2 += 1
            if p1 == 5:
                print('GAME OVER. PLAYER 1 WINS!!!')
                break
            if p2 == 5:
                print('GAME OVER. PLAYER 2 WINS!!!')
                break

            if player==1:
                player=2
            else:
                player=1

    #player against cpu
    else:

        print('--- Player 1 Create your Board ---')
        choice1 = 1
        board_1_b = insert_ships(choice1, board_1_b)

        print('--- CPU Create the Board ---')
        board_2_b = insert_ships_cpu(board_2_b)

        print('----- Where are the ships -----')
        print_board1(board_1_b, board_2_b)

        player = randint(1, 2)
        player22=' '
        if player == 2:
            player22 = '(CPU)'
        print(f"Player {player}{player22} starts first")
        
        print_board1(board1, board2)

        while True:

            if player==1:
                b_ship=input(f"Player {player} enter the position to throw your missile: ")
                b_ship=check_ship(b_ship,board2)
                print(f"Missible thrown at {b_ship}")
                if b_ship[0] == 'a':
                    x = 0
                elif b_ship[0] == 'b':
                    x = 1
                elif b_ship[0] == 'c':
                    x = 2
                elif b_ship[0] == 'd':
                    x = 3
                elif b_ship[0] == 'e':
                    x = 4
                y = int(b_ship[1]) - 1
                if board_2_b[x][y] != 'B':
                    print('Target missed!')
                    board2[x][y] = 'x'
                else:
                    print('Target hit!')
                    board2[x][y] = 'o'

                print_board1(board1, board2)

            else:
                while True:
                    x = randint(1, 5)
                    if x == 1:
                        xa = 'a'
                    elif x == 2:
                        xa = 'b'
                    elif x == 3:
                        xa = 'c'
                    elif x == 4:
                        xa = 'd'
                    elif x == 5:
                        xa = 'e'
                    y = randint(1, 5)
                    if board1[x - 1][y - 1] == ' ':
                        break
                print(f"Missible thrown at {xa+str(y)}")

                if board_1_b[x-1][y-1] != 'B':
                    print('Target missed!')
                    board1[x-1][y-1] = 'x'
                else:
                    print('Target hit!')
                    board1[x-1][y-1] = 'o'

                print_board1(board1, board2)

            p1 = 0
            p2 = 0
            for i in range(5):
                for j in range(5):
                    if board2[i][j] == 'o':
                        p1 += 1
                    if board1[i][j] == 'o':
                        p2 += 1
            if p1 == 5:
                print('GAME OVER. PLAYER 1 WINS!!!')
                break
            if p2 == 5:
                print('GAME OVER. PLAYER 2 (CPU) WINS!!!')
                break

            if player == 1:
                player = 2
            else:
                player = 1

main()