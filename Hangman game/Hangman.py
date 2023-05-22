from random import randrange, seed

def printhanger(player_try, maxtries):
    if player_try==5:
        print('+','-','-','-','-','+')
        print('|')
        print('|')
        print('|')
    elif player_try==4:
        print('+','-', '-', '-', '-', '+')
        print('|','       ','o')
        print('|')
        print('|')
    elif player_try==3:
        print('+','-', '-', '-', '-', '+')
        print('|','       ','o')
        print('|','   ','-','-','+')
        print('|')
    elif player_try==2:
        print('+','-', '-', '-', '-', '+')
        print('|','       ','o')
        print('|','   ','-','-','+','-','-')
        print('|')
    elif player_try==1:
        print('+','-', '-', '-', '-', '+')
        print('|','       ','o')
        print('|','   ','-','-','+','-','-')
        print('|','      ','/')
    else:
        print('+', '-', '-', '-', '-', '+')
        print('|', '       ', 'o')
        print('|', '   ', '-', '-', '+', '-', '-')
        print('|', '      ', '/','\\')


def letsplay(word):
    player_try = 5
    printhanger(player_try, 5)
    print(f"{player_try} tries left")
    print('-' * len(word))

    choosen_letters = []

    while True and player_try >= 1:

        print(f"choosen_letters: {choosen_letters} ")
        letter = input('Guess letter: ').upper()
        while True:
            if letter in choosen_letters:
                letter = input("You've chosen this letter already: ").upper()
            elif letter == ' ':
                letter = input('Wrong, please give another letter: ').upper()
            else:
                break

        choosen_letters.append(letter)

        flag = False
        pl = word.count(letter)
        for char in word:
            if char in choosen_letters:
                print(char, end=' ')
            else:
                print('_', end=' ')
                flag = True

        print(' ')

        if pl == 0:
            player_try -= 1

        if flag==False:
            print(f"Congratulations! You've found word {word} !")
            break

        printhanger(player_try, 5)
        print(f"{player_try} tries left")
    else:
        print(f"Sorry! You lost! The word was {word}")


def main():

    with open('words.txt','r') as f:
        lista=f.readlines()

    for i in range(len(lista)):
        if lista[i][len(lista[i])-1]== '\n':
            lista[i]=lista[i][:len(lista[i])-1]

    while True:
        print('Welcome to KREMALA!')
        choice = input('Type g<ENTER> or G<Enter> if world will be given by another player: ')

        if choice=='g' or choice=='G':
            print("Player don't look! 2nd player, type in word, must be in English and at least 3 letters long: ")
            x = input('Write a word:')
            while True:
                if x in lista:
                    break
                else:
                    x = input("WRONG word, try again:")

            word=x.upper()
            letsplay(word)

        else:
            choice= input('Type r < Enter > or R < Enter > for word of random length, else give length of random word (between 3 and 20): ')
            if choice=='r' or choice=='R':
                word= lista[randrange(len(lista))].upper()
                print(word)
            else:
                choice=int(choice)
                while True:
                    if choice<3 or choice>20:
                        choice=int(input('Wrong, give length of random word (between 3 and 20): '))
                    else:
                        break

                word = lista[randrange(len(lista))].upper()
                while True:
                    if len(word)==int(choice):
                        break
                    else:
                        word = lista[randrange(len(lista))].upper()

                print(word)

            letsplay(word)

        choice_again=input('Type P<Enter> or p<Enter> to play again: ')

        if choice_again=='P' or choice_again=='p':
            pass
        else:
            break

main()


"""
ekremmotita me to clear tis othonis
"""