import random

def shuffledDeck():
    figoura = {'heart', 'diamond', 'spade', 'club'}
    number = {'A', 2, 3, 4, 7, 8, 9, 10}

    deck = [(item, value) for item in number for value in figoura]
    random.shuffle(deck)
    return deck


def dealCard(deck, player):
    player.append(deck.pop(0))
    return player


def total(hand):
    s = 0
    for c in hand:
        if c[0] == 'A':
            s += 11
        else:
            s += c[0]
    return s


def compareHands(house_value, player_value):
    if player_value > house_value:
        return 1
    else:
        return -1


def printHistory(history):
    print(history)


def main():

    choice_start = input('Start new game (n) or continue previous game (c)?: ').upper()
    while True:
        if choice_start=='N' or choice_start=='C':
            break
        else:
            choice_start = input('Wrong! Start new game (n) or continue previous game (c)?: ').upper()

    if choice_start == 'N':
        round=1
        with open('round.txt','w') as f:
            f.write(str(round))

        bank=10
        with open('bank.txt','w') as f:
            f.write(str(bank))
    else:
        with open('round.txt','r') as f:
            round=int(f.read())+1
            print(f"Continue round = {round}")

        with open('bank.txt','r') as f:
            bank=int(f.read())
            print(f"Continue bank = {bank}")
            if bank==0:
                round = 1
                with open('round.txt', 'w') as f:
                    f.write(str(round))

                bank = 10
                with open('bank.txt', 'w') as f:
                    f.write(str(bank))

    flag_bank_0 = False
    last_round=False
    stop=False
    last=0

    while True and flag_bank_0 == False:
        if round == 1:
            with open('history.txt', 'w') as f:
                f.write(('Γύρος' + '\t').expandtabs(8) + \
                        ('Ποντάρισμα($)' + '\t').expandtabs(15) +\
                        ('Παίκτης' + '\t').expandtabs(10) + ('Μάνα' + '\t').expandtabs(8)+\
                        ('Νικητής' + '\t').expandtabs(10) +  ('Τράπεζα($)' + '\t').expandtabs(15)+'\n')

        deck = shuffledDeck()
        print(deck)
        print('*' * 30)
        print(f"Round : {round}")
        print(f"Bank's balance is {bank}")
        print('*' * 30)

        # player
        r = 0
        flag_win_player = False
        flag_lose_player = False
        while True:
            if r == 0:
                # protofillo
                player = []
                print('Player is playing!')
                dealCard(deck, player)
                print(f"You got {player[r][0]} {player[r][1]}")
                money = int(input('Place your bet: '))
                while True:
                    if money > bank:
                        money = int(input('Wrong! Place your bet: '))
                    else:
                        break
                r += 1
            elif r == 1:
                # deuterofillo
                dealCard(deck, player)
                print(f"You got {player[r][0]} {player[r][1]}")
                player_value = total(player)
                print(f"Your total now is {player_value}")
                pl = 0
                for c in player:
                    if c[0] == 'A':
                        pl += 1
                if pl == 2:
                    print('Player Win - 21 !')
                    bank -= money
                    print(f"Bank's balance is now {bank}")
                    flag_win_player = True
                    winner='παίκτης'
                    house_value=' '
                    with open('history.txt', 'a') as f:
                        f.write((str(round) + '\t').expandtabs(8) + \
                                (str(money) + '\t').expandtabs(15) + \
                                (str(player_value) + '\t').expandtabs(10) + ((house_value) + '\t').expandtabs(8) + \
                                ((winner) + '\t').expandtabs(10) + (str(bank) + '\t').expandtabs(15) + '\n')
                    break
                if player_value == 21:
                    print('Player Win - 21 !')
                    bank -= money
                    print(f"Bank's balance is now {bank}")
                    flag_win_player = True
                    winner = 'παίκτης'
                    house_value = ' '
                    with open('history.txt', 'a') as f:
                        f.write((str(round) + '\t').expandtabs(8) + \
                                (str(money) + '\t').expandtabs(15) + \
                                (str(player_value) + '\t').expandtabs(10) + ((house_value) + '\t').expandtabs(8) + \
                                ((winner) + '\t').expandtabs(10) + (str(bank) + '\t').expandtabs(15) + '\n')
                    break
                r += 1
            else:
                # ipoloipafilla
                choice = input(f"Hit(h) or stand (s) ?: ")
                if choice == 's':
                    break
                else:
                    dealCard(deck, player)
                    print(f"You got {player[r][0]} {player[r][1]}")
                    player_value = total(player)
                    print(f"Your total now is {player_value}")
                    if r == 2:
                        pl = 0
                        for c in player:
                            if c[0] == 7:
                                pl += 1
                        if pl == 3:
                            print('Player Win - 3 sevens !')
                            bank = 0
                            print(f"Bank's balance is now {bank}")
                            flag_bank_0 = True
                            flag_win_player = True
                            winner = 'παίκτης'
                            house_value = ' '
                            with open('history.txt', 'a') as f:
                                f.write((str(round) + '\t').expandtabs(8) + \
                                        (str(money) + '\t').expandtabs(15) + \
                                        (str(player_value) + '\t').expandtabs(10) + ((house_value) + '\t').expandtabs(8) + \
                                        ((winner) + '\t').expandtabs(10) + (str(bank) + '\t').expandtabs(15) + '\n')
                            break
                    if r == 4:
                        if player_value <= 21:
                            print('Player Win - 5 cards !')
                            bank -= money
                            print(f"Bank's balance is now {bank}")
                            flag_win_player = True
                            winner = 'παίκτης'
                            house_value = ' '
                            with open('history.txt', 'a') as f:
                                f.write((str(round) + '\t').expandtabs(8) + \
                                        (str(money) + '\t').expandtabs(15) + \
                                        (str(player_value) + '\t').expandtabs(10) + ((house_value) + '\t').expandtabs(8) + \
                                        ((winner) + '\t').expandtabs(10) + (str(bank) + '\t').expandtabs(15) + '\n')
                            break
                    if player_value > 21:
                        print('Player is losing!')
                        bank += money
                        print(f"Bank's balance is now {bank}")
                        flag_lose_player = True
                        winner = 'μάνα'
                        house_value = ' '
                        with open('history.txt', 'a') as f:
                            f.write((str(round) + '\t').expandtabs(8) + \
                                    (str(money) + '\t').expandtabs(15) + \
                                    (str(player_value) + '\t').expandtabs(10) + ((house_value) + '\t').expandtabs(8) + \
                                    ((winner) + '\t').expandtabs(10) + (str(bank) + '\t').expandtabs(15) + '\n')
                        break
                    if player_value == 21:
                        print('Player WIN - 21 !')
                        bank -= money
                        print(f"Bank's balance is now {bank}")
                        flag_win_player = True
                        winner = 'παίκτης'
                        house_value = ' '
                        with open('history.txt', 'a') as f:
                            f.write((str(round) + '\t').expandtabs(8) + \
                                    (str(money) + '\t').expandtabs(15) + \
                                    (str(player_value) + '\t').expandtabs(10) + ((house_value) + '\t').expandtabs(8) + \
                                    ((winner) + '\t').expandtabs(10) + (str(bank) + '\t').expandtabs(15) + '\n')
                        break
                    r += 1

        # CPU
        r = 0
        flag_win_house = False
        flag_lose_house = False
        while True and flag_win_player == False and flag_lose_player == False:
            if r == 0:
                # proto_fillo
                house = []
                print('*' * 30)
                print('House is playing!')
                dealCard(deck, house)
                print(f"House got {house[r][0]} {house[r][1]}")
                house_value = total(house)
                print(f"House total now is {house_value}")
                r += 1
            elif r == 1:
                # deuterofillo
                dealCard(deck, house)
                print(f"House got {house[r][0]} {house[r][1]}")
                house_value = total(house)
                print(f"House total now is {house_value}")
                pl = 0
                for c in house:
                    if c[0] == 'A':
                        pl += 1
                if pl == 2:
                    print('House Win - 21 !')
                    bank += money
                    print(f"House's balance is now {bank}")
                    flag_win_house = True
                    winner = 'μάνα'
                    with open('history.txt', 'a') as f:
                        f.write((str(round) + '\t').expandtabs(8) + \
                                (str(money) + '\t').expandtabs(15) + \
                                (str(player_value) + '\t').expandtabs(10) + (str(house_value) + '\t').expandtabs(8) + \
                                ((winner) + '\t').expandtabs(10) + (str(bank) + '\t').expandtabs(15) + '\n')
                    break
                if house_value == 21:
                    print('House Win - 21 !')
                    bank += money
                    print(f"House's balance is now {bank}")
                    flag_win_house = True
                    winner = 'μάνα'
                    with open('history.txt', 'a') as f:
                        f.write((str(round) + '\t').expandtabs(8) + \
                                (str(money) + '\t').expandtabs(15) + \
                                (str(player_value) + '\t').expandtabs(10) + (str(house_value) + '\t').expandtabs(8) + \
                                ((winner) + '\t').expandtabs(10) + (str(bank) + '\t').expandtabs(15) + '\n')
                    break
                r += 1
            else:
                if house_value >= 17:
                    break
                else:
                    dealCard(deck, house)
                    print(f"House got {house[r][0]} {house[r][1]}")
                    house_value = total(house)
                    print(f"House's total now is {house_value}")
                    if r == 2:
                        pl = 0
                        for c in house:
                            if c[0] == 7:
                                pl += 1
                        if pl == 3:
                            print('House Win - 3 sevens !')
                            bank += money
                            print(f"House's balance is now {bank}")
                            flag_win_house = True
                            winner = 'μάνα'
                            with open('history.txt', 'a') as f:
                                f.write((str(round) + '\t').expandtabs(8) + \
                                        (str(money) + '\t').expandtabs(15) + \
                                        (str(player_value) + '\t').expandtabs(10) + (str(house_value) + '\t').expandtabs(8) + \
                                        ((winner) + '\t').expandtabs(10) + (str(bank) + '\t').expandtabs(15) + '\n')
                            break
                    if r == 4:
                        if house_value <= 21:
                            print('House Win - 5 cards !')
                            bank += money
                            print(f"House's balance is now {bank}")
                            flag_win_house = True
                            winner = 'μάνα'
                            with open('history.txt', 'a') as f:
                                f.write((str(round) + '\t').expandtabs(8) + \
                                        (str(money) + '\t').expandtabs(15) + \
                                        (str(player_value) + '\t').expandtabs(10) + (str(house_value) + '\t').expandtabs(8) + \
                                        ((winner) + '\t').expandtabs(10) + (str(bank) + '\t').expandtabs(15) + '\n')
                            break
                    if house_value > 21:
                        print('House is losing!')
                        bank -= money
                        print(f"House's balance is now {bank}")
                        flag_lose_house = True
                        winner = 'παίκτης'
                        with open('history.txt', 'a') as f:
                            f.write((str(round) + '\t').expandtabs(8) + \
                                    (str(money) + '\t').expandtabs(15) + \
                                    (str(player_value) + '\t').expandtabs(10) + (str(house_value) + '\t').expandtabs(8) + \
                                    ((winner) + '\t').expandtabs(10) + (str(bank) + '\t').expandtabs(15) + '\n')
                        break
                    if house_value == 21:
                        print('House WIN - 21 !')
                        bank += money
                        print(f"House's balance is now {bank}")
                        flag_win_house = True
                        winner = 'μάνα'
                        with open('history.txt', 'a') as f:
                            f.write((str(round) + '\t').expandtabs(8) + \
                                    (str(money) + '\t').expandtabs(15) + \
                                    (str(player_value) + '\t').expandtabs(10) + (str(house_value) + '\t').expandtabs(8) + \
                                    ((winner) + '\t').expandtabs(10) + (str(bank) + '\t').expandtabs(15) + '\n')
                        break
                    r += 1

        if flag_win_player == False and flag_lose_player == False and flag_win_house == False and flag_lose_house == False:
            result = compareHands(house_value, player_value)
            if result == 1:
                print('Player Win!')
                bank -= money
                print(f"House's balance is now {bank}")
                winner = 'παίκτης'
                with open('history.txt', 'a') as f:
                    f.write((str(round) + '\t').expandtabs(8) + \
                            (str(money) + '\t').expandtabs(15) + \
                            (str(player_value) + '\t').expandtabs(10) + (str(house_value) + '\t').expandtabs(8) + \
                            ((winner) + '\t').expandtabs(10) + (str(bank) + '\t').expandtabs(15) + '\n')
            else:
                print('House Win!')
                bank += money
                print(f"House's balance is now {bank}")
                winner = 'μάνα'
                with open('history.txt', 'a') as f:
                    f.write((str(round) + '\t').expandtabs(8) + \
                            (str(money) + '\t').expandtabs(15) + \
                            (str(player_value) + '\t').expandtabs(10) + (str(house_value) + '\t').expandtabs(8) + \
                            ((winner) + '\t').expandtabs(10) + (str(bank) + '\t').expandtabs(15) + '\n')

        with open('bank.txt','w') as f:
            f.write(str(bank))

        if bank == 0:
            break

        if bank >= 30 and choice_start=='N':
            last_round=True

        if last_round==True and last==1:
            stop = True

        with open('round.txt', 'w') as f:
            f.write(str(round))

        round += 1
        if last_round==True and last==0:
            choice = 'C'
            last=1
        elif stop==True:
            choice='X'
        else:
            choice = input('Continue(c) , print history (h) or exit game (x) ?: ').upper()
            while True:
                if choice == 'C' or choice == 'H' or choice == 'X':
                    break
                else:
                    choice = input('Wrong answer,Continue(c) , print history (h) or exit game (x) ?: ').upper()

        if choice == 'X':
            break
        elif choice == 'H':
            history = open('history.txt','r').read()
            printHistory(history)

            choice = input('Continue(c) , print history (h) or exit game (x) ?: ').upper()
            while True:
                if choice == 'C' or choice == 'H' or choice == 'X':
                    break
                else:
                    choice = input('Wrong answer,Continue(c) , print history (h) or exit game (x) ?: ').upper()
        else:
            pass

    if bank > 10:
        print(f"Ο Παίκτης έχασε {bank-10}")
    elif bank < 10:
        print(f"Ο Παίκτης κέρδισε {10-bank}")
    else:
        print(f"Ο Παίκτης ούτε κέρδισε ούτε έχασε")



main()
