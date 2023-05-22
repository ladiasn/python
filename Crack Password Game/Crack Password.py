from random import randrange, seed

def main():
    print('CODECRACKER')
    print('GAME The objective is to guess the secret code in as few attempts as possible.')
    choice= int(input('Input 1 for 1 - player game or 2 for 2-player game: '))
    while True:
        if choice==1 or choice==2:
            break
        else:
            choice = int(input('Wrong!!! Input 1 for 1 - player game or 2 for 2-player game: '))

    if choice==1:
        print('You play against CPU')
        code=str(randrange(1,7))+str(randrange(1,7))+str(randrange(1,7))+str(randrange(1,7))
        print(code)

        flag = False
        attempt = 1
        print('Player 1 please, enter your color code.')
        print("You can use any combination of 4 symbols in ['1','2','3','4','5','6'] as colors: ")
        code1 = ['1', '2', '3', '4', '5', '6']
        while True:
            print(f"Attempt {attempt} ")
            x = input('')
            while True:
                if x.isdigit() == False:
                    print("You can only use ['1', '2', '3', '4', '5', '6'] as colors. Try again!")
                    print(f"Attempt {attempt} ")
                    x = input('')
                elif len(x) > 4:
                    print('The secret code has exactly four colors. Try again!')
                    print(f"Attempt {attempt} ")
                    x = input('')
                else:
                    if len(x) == 4:
                        p4 = 0
                        for i in range(4):
                            if x[i] in code1:
                                p4 += 1
                        if p4 == 4:
                            break
                        else:
                            print("You can only use ['1', '2', '3', '4', '5', '6'] as colors. Try again!")
                            print(f"Attempt {attempt} ")
                            x = input('')
                    else:
                        print('The secret code has exactly four colors. Try again!')
                        print(f"Attempt {attempt} ")
                        x = input('')

            p = 0
            theseis = []
            for i in range(4):
                if x[i] == code[i]:
                    theseis.append(x[i])
                    p += 1

            p1 = 0
            for i in range(4):
                if len(theseis) != 0:
                    if x[i] not in theseis:
                        for j in range(4):
                            if x[i] == code[j]:
                                p1 += 1
                else:
                    for j in range(4):
                        if x[i] == code[j]:
                            p1 += 1
            p3 = 0
            for i in range(4):
                for j in range(i + 1, 4):
                    if code[i] == code[j]:
                        p3 += 1
            p1 = p1 - p3
            print(str('o' * p) + str('x' * p1))
            if p == 4:
                flag = True
                break

            attempt += 1

            if attempt == 9:
                break

        if flag==False:
            print(f"You failed to guess within 8 attempts")
            print(f"The secret code was {code}")
            print('CPU WINS!')
        else:
            print(f"Congratulations! You found it in {attempt} attempts!")

    #play against another player
    else:
        print('You play against another player')
        print('Player 2 enter the secret code (4 colors).')
        print("You can use any combination of 4 symbols in ['1', '2', '3', '4', '5', '6'] as colors.")
        code1 = ['1', '2', '3', '4', '5', '6']

        code= input('')
        while True:
            if code.isdigit() == False:
                print("You can only use ['1', '2', '3', '4', '5', '6'] as colors. Try again!")
                code = input('')
            elif len(code) > 4:
                print('The secret code has exactly four colors. Try again!')
                code= input('')
            else:
                if len(code) == 4:
                    p4 = 0
                    for i in range(4):
                        if code[i] in code1:
                            p4 += 1
                    if p4 == 4:
                        break
                    else:
                        print("You can only use ['1', '2', '3', '4', '5', '6'] as colors. Try again!")
                        code = input('')
                else:
                    print('The secret code has exactly four colors. Try again!')
                    code = input('')


        flag = False
        attempt = 1
        print('Player 1 please, enter your color code.')
        print("You can use any combination of 4 symbols in ['1','2','3','4','5','6'] as colors: ")
        code1 = ['1', '2', '3', '4', '5', '6']
        while True:
            print(f"Attempt {attempt} ")
            x = input('')
            while True:
                if x.isdigit() == False:
                    print("You can only use ['1', '2', '3', '4', '5', '6'] as colors. Try again!")
                    print(f"Attempt {attempt} ")
                    x = input('')
                elif len(x) > 4:
                    print('The secret code has exactly four colors. Try again!')
                    print(f"Attempt {attempt} ")
                    x = input('')
                else:
                    if len(x) == 4:
                        p4 = 0
                        for i in range(4):
                            if x[i] in code1:
                                p4 += 1
                        if p4 == 4:
                            break
                        else:
                            print("You can only use ['1', '2', '3', '4', '5', '6'] as colors. Try again!")
                            print(f"Attempt {attempt} ")
                            x = input('')
                    else:
                        print('The secret code has exactly four colors. Try again!')
                        print(f"Attempt {attempt} ")
                        x = input('')

            p = 0
            theseis = []
            for i in range(4):
                if x[i] == code[i]:
                    theseis.append(x[i])
                    p += 1

            p1 = 0
            for i in range(4):
                if len(theseis) != 0:
                    if x[i] not in theseis:
                        for j in range(4):
                            if x[i] == code[j]:
                                p1 += 1
                else:
                    for j in range(4):
                        if x[i] == code[j]:
                            p1 += 1
            p3 = 0
            for i in range(4):
                for j in range(i + 1, 4):
                    if code[i] == code[j]:
                        p3 += 1
            p1 = p1 - p3
            print(str('o' * p) + str('x' * p1))
            if p == 4:
                flag = True
                break

            attempt += 1

            if attempt == 9:
                break

        if flag==False:
            print(f"You failed to guess within 8 attempts")
            print(f"The secret code was {code}")
        else:
            print(f"Congratulations! You found it in {attempt} attempts!")



main()