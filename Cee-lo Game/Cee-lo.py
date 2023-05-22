from random import randint

def auto_win_banker(ch1,ch2,ch3):
    flag=False
    if ch1==ch2 and ch2==ch3:
        #print(f"WIN - {ch1}, {ch2}, {ch3}")
        flag = True
    elif (ch1==ch2 and ch3==6) or (ch1==ch3 and ch2==6) or (ch2==ch3 and ch1==6):
        #print(f"WIN - {ch1}, {ch2}, {ch3}")
        flag = True
    else:
        if ch1==4:
            if ch2==5:
                if ch3==6:
                    #print(f"WIN - {ch1}, {ch2}, {ch3}")
                    flag=True
            elif ch2==6:
                if ch3==5:
                    #print(f"WIN - {ch1}, {ch2}, {ch3}")
                    flag = True
        elif ch1==5:
            if ch2==4:
                if ch3==6:
                    #print(f"WIN - {ch1}, {ch2}, {ch3}")
                    flag = True
            elif ch2==6:
                if ch3==4:
                    #print(f"WIN - {ch1}, {ch2}, {ch3}")
                    flag = True
        elif ch1==6:
            if ch2==5:
                if ch3==4:
                    #print(f"WIN - {ch1}, {ch2}, {ch3}")
                    flag = True
            elif ch2==4:
                if ch3==6:
                    #print(f"WIN - {ch1}, {ch2}, {ch3}")
                    flag = True

    return flag


def auto_lose_banker(ch1,ch2,ch3):
    flag=False
    if (ch1==ch2 and ch1!=1 and ch3==1) or (ch1==ch3 and ch1!=1 and ch2==1) or (ch2==ch3 and ch2!=1 and ch1==1):
        #print(f"Lose everything - {ch1}, {ch2}, {ch3}")
        flag = True
    else:
        if ch1==1:
            if ch2==2:
                if ch3==3:
                    #print(f"Lose everything - {ch1}, {ch2}, {ch3}")
                    flag = True
            elif ch2==3:
                if ch3==2:
                    #print(f"Lose everything - {ch1}, {ch2}, {ch3}")
                    flag = True
        elif ch1==2:
            if ch2==1:
                if ch3==3:
                    #print(f"Lose everything - {ch1}, {ch2}, {ch3}")
                    flag = True
            elif ch3==3:
                if ch3==1:
                    #print(f"Lose everything - {ch1}, {ch2}, {ch3}")
                    flag = True
        elif ch1==3:
            if ch2==1:
                if ch3==2:
                    #print(f"Lose everything - {ch1}, {ch2}, {ch3}")
                    flag = True
            elif ch2==2:
                if ch3==1:
                    #print(f"Lose everything - {ch1}, {ch2}, {ch3}")
                    flag = True

    return flag


def win_player(ch1,ch2,ch3):
    flag = False
    if ch1 == ch2 and ch2 == ch3:
        # print(f"WIN - {ch1}, {ch2}, {ch3}")
        flag = True
    else:
        if ch1 == 4:
            if ch2 == 5:
                if ch3 == 6:
                    # print(f"WIN - {ch1}, {ch2}, {ch3}")
                    flag = True
            elif ch2 == 6:
                if ch3 == 5:
                    # print(f"WIN - {ch1}, {ch2}, {ch3}")
                    flag = True
        elif ch1 == 5:
            if ch2 == 4:
                if ch3 == 6:
                    # print(f"WIN - {ch1}, {ch2}, {ch3}")
                    flag = True
            elif ch2 == 6:
                if ch3 == 4:
                    # print(f"WIN - {ch1}, {ch2}, {ch3}")
                    flag = True
        elif ch1 == 6:
            if ch2 == 5:
                if ch3 == 4:
                    # print(f"WIN - {ch1}, {ch2}, {ch3}")
                    flag = True
            elif ch2 == 4:
                if ch3 == 6:
                    # print(f"WIN - {ch1}, {ch2}, {ch3}")
                    flag = True

    return flag


def lose_player(ch1,ch2,ch3):
    flag = False
    if ch1 == 1:
        if ch2 == 2:
            if ch3 == 3:
                # print(f"Lose everything - {ch1}, {ch2}, {ch3}")
                flag = True
        elif ch2 == 3:
            if ch3 == 2:
                # print(f"Lose everything - {ch1}, {ch2}, {ch3}")
                flag = True
    elif ch1 == 2:
        if ch2 == 1:
            if ch3 == 3:
                # print(f"Lose everything - {ch1}, {ch2}, {ch3}")
                flag = True
        elif ch3 == 3:
            if ch3 == 1:
                # print(f"Lose everything - {ch1}, {ch2}, {ch3}")
                flag = True
    elif ch1 == 3:
        if ch2 == 1:
            if ch3 == 2:
                # print(f"Lose everything - {ch1}, {ch2}, {ch3}")
                flag = True
        elif ch2 == 2:
            if ch3 == 1:
                # print(f"Lose everything - {ch1}, {ch2}, {ch3}")
                flag = True

    return flag



def main():

    #arxikopoihsh metavliton
    players = input('Number of players (between 2 and 6): ')
    if players.isdigit():
        if int(players) <2 or int(players) >6:
            print('I expected between 2 and 6 players')
            print("I'm setting the number of players to 3")
            players = 3
    elif players.isalpha():
        print('I expected between 2 and 6 players')
        print("I'm setting the number of players to 3")
        players = 3
    else:
        print('I expected between 2 and 6 players')
        print("I'm setting the number of players to 3")
        players = 3

    coins = input('Number of coins per player (between 5 and 100):')
    if coins.isdigit():
        if int(coins) < 5 or int(coins) > 100:
            print("I'm setting the number of coins to 10")
            coins = 10
    elif coins.isalpha():
        print(f"Something wrong happened: invalid literal for int() with base 10: {coins}")
        print("I'm setting the number of coins to 10")
        coins = 10
    else:
        print(f"Something wrong happened: invalid literal for int() with base 10: {coins}")
        print("I'm setting the number of coins to 10")
        coins = 10

    players=int(players)
    coins=int(coins)
    #print(f"players={players}")
    #print(f"coins={coins}")

    players_list=[0]
    coins_list = [0]
    flags_list=[False]
    coins_play_list=[0]
    for i in range(1,players+1):
        players_list.append(i)
        coins_list.append(coins)
        flags_list.append(False)
        coins_play_list.append(0)

    #print(f"players={players_list}")
    #print(f"coins={coins_list}")
    #print(f"flags={flags_list}")
    zari1 = [0, 1, 2, 3, 4, 5, 6]
    zari2 = [0, 1, 2, 3, 4, 5, 6]
    zari3 = [0, 1, 2, 3, 4, 5, 6]

    exit=False
    # protos paixtis
    banker = randint(1, players-1)
    banker_flag=False
    round = 0
    print("START GAME")
    while True:
        flags_list = [False]
        for i in range(1, players + 1):
            flags_list.append(False)

        round +=1
        print(f"Round no {round}")
        print(f"Banker is player no: {banker} ")

        for i in range(1, players+1):
                print(f"Player {i} has {coins_list[i]} coins")

        banka = 0

        bank = int(input('The Banker says the money: '))
        while True:
            if bank >= 1 and bank <= coins_list[banker]:
                break
            else:
                bank = int(input('Wrong! The Banker says the money: '))

        banka += bank
        coins_list[banker] -= bank

        s=0
        i = banker
        while True:
            i += 1
            if i==players+1:
                i=1
            if i==banker:
                break
            #pontarisma kathe paikti
            if s!=bank:
                play=int(input(f"Player {i} What's your play money? "))
                while True:
                    if play>=1 and play<=coins_list[i] and play<=bank-s:
                        coins_play_list[i]=play
                        coins_list[i] -= coins_play_list[i]
                        banka += coins_play_list[i]
                        s += play
                        break
                    elif play<1 or play>coins_list[i]:
                        play = int(input(f"Wrong!! Out of rate. Player {i} What's your play money? "))
                    elif play >bank-s:
                        play = int(input(f"Wrong!! Bet less. Player {i} What's your play money? "))
                    else:
                        flags_list[i]=True
            else:
                flags_list[i]=True
        #print(f"bank= {bank}")
        print('-'*30)
        i = banker
        while True:
            i +=1
            if i==players+1:
                i=1
            if i==banker:
                break
            if flags_list[i] != True:
                print(f"Player no {i} plays with {coins_play_list[i]}")
        print('-' * 30)

        print('Banker shoot the dies')

        score_banker=False
        win_banker=False
        lose_banker=False
        round_win_banker = False
        round_win_player = False
        score_flag_banker = False
        first_player456_flag = False
        #zaria banker
        while True:
            ch1 = randint(1, len(zari1) - 1)
            ch2 = randint(1, len(zari2) - 1)
            ch3 = randint(1, len(zari3) - 1)
            print(str(ch1) + '-' + str(ch2) + '-' + str(ch3))
            f1 = auto_win_banker(ch1, ch2, ch3)
            #print(f1)
            if f1==True:
                win_banker=True
                break
            else:
                f2 = auto_lose_banker(ch1, ch2, ch3)
                #print(f2)
                if f2==True:
                    lose_banker=True
                    break
                else:
                    if ch1 == ch2 and ch3 != ch1:
                        if ch3 != 1 and ch3 != 6:
                            score_banker = ch3
                            score_flag_banker =True
                            break
                    elif ch1 == ch3 and ch3 != ch2:
                        if ch2 != 1 and ch2 != 6:
                            score_banker = ch2
                            score_flag_banker = True
                            break
                    elif ch3 == ch2 and ch1 != ch2:
                        if ch1 != 1 and ch1 != 6:
                            score_banker = ch1
                            score_flag_banker = True
                            break
                    else:
                        print('Banker plays again')

        if win_banker==True:
            print(f"Banker Win! Take everything with {ch1},{ch2},{ch3}")
            round_win_banker=True
            """
            for i in range(1, players + 1):
                if i == banker:
                    coins_list[i] += banka
            """
        elif lose_banker==True:
            print(f"Banker lose everything with {ch1},{ch2},{ch3}")
            for i in range(1, players + 1):
                if i != banker:
                    if flags_list[i] != True:
                        coins_list[i] += 2*coins_play_list[i]
            banka = 0
        elif score_flag_banker==True:
            #zaria player2
            firt_player456 = 0
            first_player456_flag = False
            first_player_j=0
            j = banker
            while True:
                j += 1
                if j == players + 1:
                    j = 1
                if j == banker:
                    break
                if j != banker and flags_list[j] !=True:
                    print(f"Player no {j} plays the dies")
                    score_flag_player = False
                    while True:
                        pl1 = randint(1, len(zari1) - 1)
                        pl2 = randint(1, len(zari2) - 1)
                        pl3 = randint(1, len(zari3) - 1)
                        fp1=win_player(pl1,pl2,pl3)
                        if fp1==True:
                            coins_list[j] += 2*coins_play_list[j]
                            #coins_list[banker] -= coins_play_list[j]
                            banka -= 2*coins_play_list[j]
                            round_win_player=True
                            print(f"Player win banker with {pl1}, {pl2},{pl3}")
                            firt_player456 +=1
                            if firt_player456 == 1:
                                first_player456_flag = True
                                first_player_j=j
                            break
                        else:
                            fp2=lose_player(pl1,pl2,pl3)
                            if fp2==True:
                                #coins_list[j] -= coins_play_list[j]
                                #coins_list[banker] += coins_play_list[j]
                                print(f"Player lose from banker with {pl1}, {pl2},{pl3}")
                                break
                            else:
                                if pl1 == pl2:
                                    score_player=pl3
                                    score_flag_player=True
                                    break
                                elif pl1 == pl3:
                                    score_player=pl2
                                    score_flag_player = True
                                    break
                                elif pl2 ==pl3:
                                    score_player=pl1
                                    score_flag_player = True
                                    break
                                else:
                                    print('Player is playing again')

                    if score_flag_player==True:
                        print(f"Banker's score is: {score_banker} and player's has score is {score_player}")
                        if score_banker > score_player:
                            #coins_list[j] -= coins_play_list[j]
                            #coins_list[banker] += coins_play_list[j]
                            print(f"Banker wins with with {ch1},{ch2},{ch3} against player with with {pl1},{pl2},{pl3}")
                        elif score_banker < score_player:
                            coins_list[j] += 2*coins_play_list[j]
                            banka -= 2*coins_play_list[j]
                            #coins_list[banker] -= coins_play_list[j]
                            print(f"Banker lose with with {ch1},{ch2},{ch3} against player with with {pl1},{pl2},{pl3}")
                        else:
                            coins_list[j] += coins_play_list[j]
                            print('DRAW')

        if exit==False:
            coins_list[banker] += banka
            print('-' * 70)
            print('-' * 70)
            print('-' * 70)
            print('- - -  The result of this round are - - -')
            for j in range(1, players +1):
                if j!=banker:
                    if flags_list[j]!=True:
                        print(f"Player with no {j} has {coins_list[j]} at the end of this round")
                    else:
                        print(f"Player with no {j} still has {coins_list[j]} and he did not play at ths this round ")
                else:
                    print(f"Banker player with no {j} has {coins_list[j]} at the end of this round")
            print('-' * 70)
            print('-' * 70)
            print('-' * 70)

        exit=False
        for i in range(1, players + 1):
            if coins_list[i] == 0:
                exit = True

        if exit==True:
            break

        if exit==False:
            if round_win_player == True:
                banker = first_player_j
            else:
                if round_win_banker==True or players_list[banker]>0:
                    banker = banker
                else:
                    banker +=1
                    while True:
                        if i==players+1:
                            i=1

    max = -1
    max_player=0
    for i in range(1, players + 1):
            if coins_list[i] > max:
                max = coins_list[i]
                max_player=i

    print(f"The winner is {max_player}")



main()