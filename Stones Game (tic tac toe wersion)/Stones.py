from random import randint

def check1(player, p, peg, board):
    #elegxoume ean i epilogi mas einai sosti
    choice = input(f"Player {player} peg no. {p}.Enter the board position to put your peg: ").upper()
    while True:
        #elegxo ean den exei mikos=2
        if len(choice) != 2:
            print('Invalid position. Not a board position. Please re-enter. ')
            choice = input(f"Player {player} peg no. {p}.Enter the board position to put your peg: ").upper()
        else:
            #elegxo ean to proto den einai alfarithmitiko kai to deutero akeraios
            if choice[0].isalpha() and choice[1].isdigit():
                #elegxo ean to proto den einai metaksi A kai C
                if choice[0] >='A' and choice[0] <='C' :
                    #elegxo ean to deutero, o akeraios, den einai apo 1 mexri kai 3
                    if int(choice[1]) >= 1 and int(choice[1]) <= 3:
                        #ean einai ola sosta, tote kalw tin sinartisi Valid oste na elekso oti mporo na topothetiso ekei tin kinisi mou
                        flag = check2(choice,peg, board)
                        #ean einai False i timi pou epistrefei i sinartisi, tote simainei oti den mporo na topothetiso ekei tin kinisi mou
                        if flag == False:
                            choice = input(f"Player {player} peg no. {p}.Enter the board position to put your peg: ").upper()
                        else:
                            break
                    else:
                        print('Invalid position. Not a board position. Please re-enter. ')
                        choice = input(f"Player {player} peg no. {p}.Enter the board position to put your peg: ").upper()
                else:
                    print('Invalid position. Not a board position. Please re-enter. ')
                    choice = input(f"Player {player} peg no. {p}.Enter the board position to put your peg: ").upper()
            else:
                print('Invalid position. Not a board position. Please re-enter. ')
                choice = input(f"Player {player} peg no. {p}.Enter the board position to put your peg: ").upper()

    return choice


def check2(choice, peg, board):
    #i valid elegxei ean sto simeio pou epeleksa na topothetiso tin kinisi mou einai epitrepto
    flag=False
    #prepei na sindesoume p.x. to A me ti grammi 1 tou pinaka
    lines = [0, 1, 2, 3]
    ch = [' ', 'A', 'B', 'C']
    for i in range(1, 4):
        if choice[0] == ch[i]:
            line = lines[i]

    #elegxo ean to simeio den exei kapoio allo pioni
    if board[line][int(choice[1])] != ' ':
        print('Position taken by another peg. Please re-enter.')
    else:
        #elegxo ean me tin kinisi mou kano idi triliza
        board[line][int(choice[1])] = peg
        if board[1][1] == peg and board[1][2] == peg and board[1][3] == peg:
            print('Invalid position. Cannot complete 3-in-a-row at this stage.')
            board[line][int(choice[1])] = ' '
        elif board[2][1] == peg and board[2][2] == peg and board[2][3] == peg:
            print('Invalid position. Cannot complete 3-in-a-row at this stage.')
            board[line][int(choice[1])] = ' '
        elif board[3][1] == peg and board[3][2] == peg and board[3][3] == peg:
            print('Invalid position. Cannot complete 3-in-a-row at this stage.')
            board[line][int(choice[1])] = ' '
        elif board[1][1] == peg and board[2][1] == peg and board[3][1] == peg:
            print('Invalid position. Cannot complete 3-in-a-row at this stage.')
            board[line][int(choice[1])] = ' '
        elif board[1][2] == peg and board[2][2] == peg and board[3][2] == peg:
            print('Invalid position. Cannot complete 3-in-a-row at this stage.')
            board[line][int(choice[1])] = ' '
        elif board[1][3] == peg and board[2][3] == peg and board[3][3] == peg:
            print('Invalid position. Cannot complete 3-in-a-row at this stage.')
            board[line][int(choice[1])] = ' '
        elif board[1][1] == peg and board[2][2] == peg and board[3][3] == peg:
            print('Invalid position. Cannot complete 3-in-a-row at this stage.')
            board[line][int(choice[1])] = ' '
        elif board[1][3] == peg and board[2][2] == peg and board[3][1] == peg:
            print('Invalid position. Cannot complete 3-in-a-row at this stage.')
            board[line][int(choice[1])] = ' '
        else:
            flag = True

    return flag


def check3(pl,peg_play,board):
    #elegxo ean i thesi pou eixa to pioni kai i thesi pou thelo na to metakiniso einai sostes, p.x. A1A2 kai oxi A1A5
    choice = input(f"Player {pl} enter your movie: ").upper()
    while True:
        if len(choice) != 4:
            print('Invalid move. Enter origin and destination positions in 4 characters, e.g., A2B1')
            choice = input(f"Player {pl} enter your movie: ").upper()
        else:
            if choice[0].isalpha() and choice[1].isdigit() and choice[2].isalpha() and choice[3].isdigit():
                if choice[0] >='A' and choice[0] <='C' :
                    if int(choice[1]) >= 1 and int(choice[1]) <= 3:
                        if choice[2] >='A' and choice[2] <='C' :
                            if int(choice[3]) >= 1 and int(choice[3]) <= 3:
                                flag1 = check4(choice,peg_play, board)
                                if flag1 == False:
                                    choice = input(f"Player {pl} enter your movie: ").upper()
                                else:
                                    break
                            else:
                                print('Invalid position. Not a board position. Please re-enter.')
                                choice = input(f"Player {pl} enter your movie: ").upper()
                        else:
                            print('Invalid position. Not a board position. Please re-enter.')
                            choice = input(f"Player {pl} enter your movie: ").upper()
                    else:
                        print('Invalid position. Not a board position. Please re-enter.')
                        choice = input(f"Player {pl} enter your movie: ").upper()
                else:
                    print('Invalid position. Not a board position. Please re-enter.')
                    choice = input(f"Player {pl} enter your movie: ").upper()
            else:
                print('Invalid position. Not a board position. Please re-enter.')
                choice = input(f"Player {pl} enter your movie: ").upper()

    return choice


def check4(choice,peg_play, board):
    flag1 = False
    lines = [0, 1, 2, 3]
    ch = [' ', 'A', 'B', 'C']
    for i in range(1, 4):
        if choice[0] == ch[i]:
            line1 = lines[i]
        if choice[2]== ch[i]:
            line2 = lines[i]

    #elegxo ean i thesi pou eixa to pioni kai i thesi pou thelo na to metakiniso einai epitrepti
    if board[line1][int(choice[1])] == ' ':
        print("Invalid move. Origin is not occupied by player's 1 peg")
    elif board[line2][int(choice[3])] != ' ':
        print("Invalid move. Destination position is not empty. Please re-enter move.")
    elif board[line1][int(choice[1])] != peg_play:
        print("Invalid move. Origin is not occupied by player's 1 peg")
    elif line1 != line2 and abs(line1-line2) != 1:
        print("Invalid move. The lines is too far each other")
    elif int(choice[1]) != int(choice[3]) and abs(int(choice[1]) - int(choice[3])) != 1:
        print("Invalid move. The lines is too far each other")
    else:
        flag1 = True


    return flag1


while True:
    stones = [
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
    ]
    # tixaia klirosi protou
    protos = randint(1, 2)

    print(f"Player {protos} starts first.")
    print('  1       2       3')
    print(f"A {stones[1][1]} - - - {stones[1][2]} - - - {stones[1][3]}")
    print(' ', '|', '\\', ' ', ' ', '|', ' ', ' ', '/', '|'),
    print(' ', '|', ' ', '\\', ' ', '|', ' ', '/', ' ', '|'),
    print(' ', '|', ' ', ' ', '\\', '|', '/', ' ', ' ', '|'),
    print(f"B {stones[2][1]} - - - {stones[2][2]} - - - {stones[2][3]}")
    print(' ', '|', ' ', ' ', '/', '|', '\\', ' ', ' ', '|'),
    print(' ', '|', ' ', '/', ' ', '|', ' ', '\\', ' ', '|'),
    print(' ', '|', '/', ' ', ' ', '|', ' ', ' ', '\\', '|'),
    print(f"C {stones[3][1]} - - - {stones[3][2]} - - - {stones[3][3]}")

    if protos == 1:
        # oi simaies orizoun poios paizei protos kai deuteros
        protos1 = True
    else:
        protos1 = False

    # analoga poios ksekinaei protos, tote tha paiksoun kai ta antistoixa pionia
    if protos == 1:
        player = 1
        peg = 'X'
    else:
        player = 2
        peg = 'O'
    # protos paiktis
    counter1 = 1
    while True:
        # check tin kinisi
        choice = check1(player, counter1, peg, stones)

        # ektelei tin kinisi
        if choice[0] == 'A':
            line = 1
        elif choice[0] == 'B':
            line = 2
        else:
            line = 3

        stones[line][int(choice[1])] = peg
        print('  1       2       3')
        print(f"A {stones[1][1]} - - - {stones[1][2]} - - - {stones[1][3]}")
        print(' ', '|', '\\', ' ', ' ', '|', ' ', ' ', '/', '|'),
        print(' ', '|', ' ', '\\', ' ', '|', ' ', '/', ' ', '|'),
        print(' ', '|', ' ', ' ', '\\', '|', '/', ' ', ' ', '|'),
        print(f"B {stones[2][1]} - - - {stones[2][2]} - - - {stones[2][3]}")
        print(' ', '|', ' ', ' ', '/', '|', '\\', ' ', ' ', '|'),
        print(' ', '|', ' ', '/', ' ', '|', ' ', '\\', ' ', '|'),
        print(' ', '|', '/', ' ', ' ', '|', ' ', ' ', '\\', '|'),
        print(f"C {stones[3][1]} - - - {stones[3][2]} - - - {stones[3][3]}")
        # metraei tis kiniseis tou protou
        counter1 += 1
        # otan oi kiniseis ginoun 4 simainei oti exei idi valei ta 3 pionia tou kai ara tha prepei na paiksei o deuteros me ta 3 pionia tou
        if counter1 == 4:
            if protos == 1:
                player1 = 2
                peg1 = 'O'
            else:
                player1 = 1
                peg1 = 'X'
            break

    # deuteros paiktis
    counter2 = 1
    while True:
        # tsekarei ean i thesi einai sosti, alla kai ean i kinisi einai sosti meso tis valid
        choice = check1(player1, counter2, peg1, stones)

        # ektelei tin kinisi
        if choice[0] == 'A':
            line = 1
        elif choice[0] == 'B':
            line = 2
        else:
            line = 3

        stones[line][int(choice[1])] = peg1
        print('  1       2       3')
        print(f"A {stones[1][1]} - - - {stones[1][2]} - - - {stones[1][3]}")
        print(' ', '|', '\\', ' ', ' ', '|', ' ', ' ', '/', '|'),
        print(' ', '|', ' ', '\\', ' ', '|', ' ', '/', ' ', '|'),
        print(' ', '|', ' ', ' ', '\\', '|', '/', ' ', ' ', '|'),
        print(f"B {stones[2][1]} - - - {stones[2][2]} - - - {stones[2][3]}")
        print(' ', '|', ' ', ' ', '/', '|', '\\', ' ', ' ', '|'),
        print(' ', '|', ' ', '/', ' ', '|', ' ', '\\', ' ', '|'),
        print(' ', '|', '/', ' ', ' ', '|', ' ', ' ', '\\', '|'),
        print(f"C {stones[3][1]} - - - {stones[3][2]} - - - {stones[3][3]}")
        counter2 += 1
        if counter2 == 4:
            break

    # ksekinaei to paixnidi paizontas enallax
    while True:
        if protos1 == True:
            pl = 1
            peg_play = 'X'
            protos1 = False
        else:
            pl = 2
            peg_play = 'O'
            protos1 = True

        # tsekarei ean i thesi einai sosti, alla kai ean i kinisi einai sosti meso tis valid
        play = check3(pl, peg_play, stones)

        # ektelei tin kinisi
        if play[0] == 'A':
            line1 = 1
        elif play[0] == 'B':
            line1 = 2
        else:
            line1 = 3

        if play[2] == 'A':
            line2 = 1
        elif play[2] == 'B':
            line2 = 2
        else:
            line2 = 3

        stones[line2][int(play[3])] = peg_play
        stones[line1][int(play[1])] = ' '
        print('  1       2       3')
        print(f"A {stones[1][1]} - - - {stones[1][2]} - - - {stones[1][3]}")
        print(' ', '|', '\\', ' ', ' ', '|', ' ', ' ', '/', '|'),
        print(' ', '|', ' ', '\\', ' ', '|', ' ', '/', ' ', '|'),
        print(' ', '|', ' ', ' ', '\\', '|', '/', ' ', ' ', '|'),
        print(f"B {stones[2][1]} - - - {stones[2][2]} - - - {stones[2][3]}")
        print(' ', '|', ' ', ' ', '/', '|', '\\', ' ', ' ', '|'),
        print(' ', '|', ' ', '/', ' ', '|', ' ', '\\', ' ', '|'),
        print(' ', '|', '/', ' ', ' ', '|', ' ', ' ', '\\', '|'),
        print(f"C {stones[3][1]} - - - {stones[3][2]} - - - {stones[3][3]}")

        # elegxos gia nikiti
        flag_win = False
        if stones[1][1] == peg_play and stones[1][2] == peg_play and stones[1][3] == peg_play:
            flag_win = True
        elif stones[2][1] == peg_play and stones[2][2] == peg_play and stones[2][3] == peg_play:
            flag_win = True
        elif stones[3][1] == peg_play and stones[3][2] == peg_play and stones[3][3] == peg_play:
            flag_win = True
        elif stones[1][1] == peg_play and stones[2][2] == peg_play and stones[3][3] == peg_play:
            flag_win = True
        elif stones[3][1] == peg_play and stones[2][2] == peg_play and stones[1][3] == peg_play:
            flag_win = True
        elif stones[1][1] == peg_play and stones[2][1] == peg_play and stones[3][1] == peg_play:
            flag_win = True
        elif stones[1][2] == peg_play and stones[2][2] == peg_play and stones[3][2] == peg_play:
            flag_win = True
        elif stones[1][3] == peg_play and stones[2][3] == peg_play and stones[3][3] == peg_play:
            flag_win = True
        if flag_win == True:
            break

    # nikitis autos pou epaikse teleutaios
    if peg_play == 'X':
        print(f"Player 1 wins!")
    else:
        print(f"Player 2 wins!")

    # next game
    apantisi = input("Type 'Y' or 'y' to play again:")
    if apantisi != 'Y' and apantisi != 'y':
        break