from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Othello Game')

bt = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

lb1 = Label(root,text='Othello Game', font=('Comic Sans',18))
lb1.grid(row=0, column=0, columnspan=3)

frm = Frame(root)
frm.grid(row=1, column=0, columnspan=3)

frm1 = Frame(root)
frm1.grid(row=2, column=0, columnspan=3)

def move_up(x, y, color):
    line = x - 1
    if color == 'black':
        upp = []
        p = 0
        thesi = -1
        for i in range(line, -1, -1):
            if bt[i][y]['bg'] == 'black':
                p += 1

        if p >= 1:
            while True:
                if bt[line][y]['bg'] == 'black':
                    thesi = line
                    break
                line -= 1

        if p >= 1:
            p1 = 0
            line1 = x - 1
            for i in range(line1, thesi, -1):
                if bt[i][y]['bg'] == 'white':
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
            if bt[i][y]['bg'] == 'white':
                p += 1

        if p >= 1:
            while True:
                if bt[line][y]['bg'] == 'white':
                    thesi = line
                    break
                line -= 1

        if p >= 1:
            p1 = 0
            line1 = x - 1
            for i in range(line1, thesi, -1):
                if bt[i][y]['bg'] == 'black':
                    p1 += 1

            plithos = (x - 1) - thesi

            if p1 == plithos:
                for i in range(line1, thesi, -1):
                    upp.append((i, y))

    return upp


def move_down(x, y, color):
    line = x + 1
    if color == 'black':
        upd = []
        p = 0
        thesi = -1
        for i in range(line, 8):
            if bt[i][y]['bg'] == 'black':
                p += 1

        if p >= 1:
            while True:
                if bt[line][y]['bg'] == 'black':
                    thesi = line
                    break
                line += 1
        if p >= 1:
            p1 = 0
            line1 = x + 1
            for i in range(line1, thesi):
                if bt[i][y]['bg'] == 'white':
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
            if bt[i][y]['bg'] == 'white':
                p += 1

        if p >= 1:
            while True:
                if bt[line][y]['bg'] == 'white':
                    thesi = line
                    break
                line += 1
        if p >= 1:
            p1 = 0
            line1 = x + 1
            for i in range(line1, thesi):
                if bt[i][y]['bg'] == 'black':
                    p1 += 1

            plithos = thesi - (x + 1)

            if p1 == plithos:
                for i in range(line1, thesi):
                    upd.append((i, y))

    return upd


def move_right(x, y, color):
    col = y + 1
    if color == 'black':
        right = []
        p = 0
        thesi = -1
        for j in range(col, 8):
            if bt[x][j]['bg'] == 'black':
                p += 1

        if p >= 1:
            while True:
                if bt[x][col]['bg'] == 'black':
                    thesi = col
                    break
                col += 1
        if p >= 1:
            p1 = 0
            col1 = y + 1
            for j in range(col1, thesi):
                if bt[x][j]['bg'] == 'white':
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
            if bt[x][j]['bg'] == 'white':
                p += 1

        if p >= 1:
            while True:
                if bt[x][col]['bg'] == 'white':
                    thesi = col
                    break
                col += 1
        if p >= 1:
            p1 = 0
            col1 = y + 1
            for j in range(col1, thesi):
                if bt[x][j]['bg'] == 'black':
                    p1 += 1

            plithos = thesi - (y + 1)

            if p1 == plithos:
                for j in range(col1, thesi):
                    right.append((x, j))
    return right


def move_left(x, y, color):
    col = y - 1
    if color == 'black':
        left = []
        p = 0
        thesi = -1
        for j in range(col, -1, -1):
            if bt[x][j]['bg'] == 'black':
                p += 1

        if p >= 1:
            while True:
                if bt[x][col]['bg'] == 'black':
                    thesi = col
                    break
                col -= 1
        if p >= 1:
            p1 = 0
            col1 = y - 1
            for j in range(col1, thesi - 1, -1):
                if bt[x][j]['bg'] == 'white':
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
            if bt[x][j]['bg'] == 'white':
                p += 1

        if p >= 1:
            while True:
                if bt[x][col]['bg'] == 'white':
                    thesi = col
                    break
                col -= 1
        if p >= 1:
            p1 = 0
            col1 = y - 1
            for j in range(col1, thesi - 1, -1):
                if bt[x][j]['bg'] == 'black':
                    p1 += 1

            plithos = (y - 1) - thesi

            if p1 == plithos:
                for j in range(col1, thesi, -1):
                    left.append((x, j))
    return left


def move_up_right(x, y, color):
    line = x - 1
    col = y + 1
    if color == 'black':
        upright = []
        p = 0
        thesi_i = -1
        thesi_j = -1
        for i in range(line, -1, -1):
            for j in range(col, 8):
                if i + j == x + y:
                    if bt[i][j]['bg'] == 'black':
                        p += 1

        if p >= 1:
            p2 = 1
            for i in range(line, -1, -1):
                for j in range(col, 8):
                    if i + j == x + y:
                        if bt[i][j]['bg'] == 'black':
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
                        if bt[i][j]['bg'] == 'white':
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
                    if bt[i][j]['bg'] == 'white':
                        p += 1

        if p >= 1:
            p2 = 1
            for i in range(line, -1, -1):
                for j in range(col, 8):
                    if i + j == x + y:
                        if bt[i][j]['bg'] == 'white':
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
                        if bt[i][j]['bg'] == 'black':
                            p1 += 1

            plithos = x - thesi_i - 1

            if p1 == plithos:
                for i in range(line1, thesi_i, -1):
                    for j in range(col1, thesi_j):
                        if i + j == x + y:
                            upright.append((i, j))
    return upright


def move_down_right(x, y, color):
    line = x + 1
    col = y + 1
    if color == 'black':
        downright = []
        p = 0
        thesi_i = -1
        thesi_j = -1
        sum = x + y
        for i in range(line, 8):
            for j in range(col, 8):
                if i + j == sum + 2:
                    if bt[i][j]['bg'] == 'black':
                        p += 1
            sum += 2

        if p >= 1:
            p2 = 1
            sum = x + y
            for i in range(line, 8):
                for j in range(col, 8):
                    if i + j == sum + 2:
                        if bt[i][j]['bg'] == 'black':
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
                        if bt[i][j]['bg'] == 'white':
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
                    if bt[i][j]['bg'] == 'white':
                        p += 1
            sum += 2

        if p >= 1:
            p2 = 1
            sum = x + y
            for i in range(line, 8):
                for j in range(col, 8):
                    if i + j == sum + 2:
                        if bt[i][j]['bg'] == 'white':
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
                        if bt[i][j]['bg'] == 'black':
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


def move_up_left(x, y, color):
    line = x - 1
    col = y - 1
    if color == 'black':
        upleft = []
        p = 0
        thesi_i = -1
        thesi_j = -1
        sum = x+y
        for i in range(line, -1, -1):
            for j in range(col, -1, -1):
                if i + j == sum -2:
                    if bt[i][j]['bg'] == 'black':
                        p += 1
            sum -=2

        if p >= 1:
            p2 = 1
            sum =x+y
            for i in range(line, -1, -1):
                for j in range(col, -1, -1):
                    if i+j==sum-2:
                        if bt[i][j]['bg'] == 'black':
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
                        if bt[i][j]['bg'] == 'white':
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
                    if bt[i][j]['bg'] == 'white':
                        p += 1
            sum -= 2

        if p >= 1:
            p2 = 1
            sum = x + y
            for i in range(line, -1, -1):
                for j in range(col, -1, -1):
                    if i + j == sum - 2:
                        if bt[i][j]['bg'] == 'white':
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
                        if bt[i][j]['bg'] == 'black':
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


def move_down_left(x, y, color):
    line = x + 1
    col = y - 1
    if color == 'black':
        downleft = []
        p = 0
        thesi_i = -1
        thesi_j = -1
        for i in range(line, 8):
            for j in range(col, -1, -1):
                if i + j == x + y:
                    if bt[i][j]['bg'] == 'black':
                        p += 1

        if p >= 1:
            p2 = 1
            for i in range(line, 8):
                for j in range(col, -1, -1):
                    if i + j == x + y:
                        if bt[i][j]['bg'] == 'black':
                            if p2 == 1:
                                thesi_i = i
                                thesi_j = j
                                p2 += 1

        p1 = 0
        line1 = x + 1
        col1 = y - 1
        for i in range(line1, thesi_i):
            for j in range(col1, thesi_j, -1):
                if i + j == x + y:
                    if bt[i][j]['bg'] == 'white':
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
                    if bt[i][j]['bg'] == 'white':
                        p += 1

        if p >= 1:
            p2 = 1
            for i in range(line, 8):
                for j in range(col, -1, -1):
                    if i + j == x + y:
                        if bt[i][j]['bg'] == 'white':
                            if p2 == 1:
                                thesi_i = i
                                thesi_j = j
                                p2 += 1

        p1 = 0
        line1 = x + 1
        col1 = y - 1
        for i in range(line1, thesi_i):
            for j in range(col1, thesi_j, -1):
                if i + j == x + y:
                    if bt[i][j]['bg'] == 'black':
                        p1 += 1

        plithos = thesi_i - x - 1

        if p1 == plithos:
            for i in range(line1, thesi_i):
                for j in range(col1, thesi_j, -1):
                    if i + j == x + y:
                        downleft.append((i, j))
    return downleft


def reverse_count(i, j, color):
    if bt[i][j]['bg'] == 'darkcyan' :
        upp_list = move_up(i, j, color)
        # print(f" upp_list {upp_list}")
        down_list = move_down(i, j, color)
        # print(f" down_list {down_list}")
        right_list = move_right(i, j, color)
        # print(f" right_list {right_list}")
        left_list = move_left(i, j, color)
        # print(f" left_list {left_list}")
        upright_list = move_up_right(i, j, color)
        # print(f" upright_list {upright_list}")
        downright_list = move_down_right(i, j, color)
        # print(f" downright_list {downright_list}")
        upleft = move_up_left(i, j, color)
        # print(f" upleft {upleft}")
        downleft = move_down_left(i, j, color)
        # print(f" downleft {downleft}")
        sum = len(upp_list) + len(down_list) + len(right_list) + len(left_list) + len(upright_list) + len(downright_list) + \
              len(upleft) + len(downleft)
        return sum
    else:
        return 0


def add_checker(i, j, color):
    bt[i][j]['bg'] = color
    upp_list = move_up(i, j, color)
    if upp_list != []:
        for c in upp_list:
            bt[c[0]][c[1]]['bg'] = color

    down_list = move_down(i, j, color)
    if down_list != []:
        for c in down_list:
            bt[c[0]][c[1]]['bg'] = color

    right_list = move_right(i, j, color)
    if right_list != []:
        for c in right_list:
            bt[c[0]][c[1]]['bg'] = color

    left_list = move_left(i, j, color)
    if left_list != []:
        for c in left_list:
            bt[c[0]][c[1]]['bg'] = color

    upright_list = move_up_right(i, j, color)
    if upright_list != []:
        for c in upright_list:
            bt[c[0]][c[1]]['bg'] = color

    downright_list = move_down_right(i, j, color)
    if downright_list != []:
        for c in downright_list:
            bt[c[0]][c[1]]['bg'] = color

    downleft = move_down_left(i, j, color)
    if downleft != []:
        for c in downleft:
            bt[c[0]][c[1]]['bg'] = color

    upleft = move_up_left(i, j, color)
    if upleft != []:
        for c in upleft:
            bt[c[0]][c[1]]['bg'] = color


def human_play(color):
    flag1 = False
    for i in range(8):
        for j in range(8):
            x = reverse_count(i, j, color)
            if x != 0:
                flag1 = True
    return flag1

def score():
    global p1, p2
    p1 = 0
    p2 = 0
    for i in range(8):
        for j in range(8):
            if bt[i][j]['bg'] == 'black':
                p1 +=1
            if bt[i][j]['bg'] == 'white':
                p2 +=1

    lblack_point['text'] = p1
    lwhite_point['text'] = p2

    p3 = 0
    for i in range(8):
        for j in range(8):
            if bt[i][j]['bg'] == 'black' or bt[i][j]['bg'] == 'white':
                p3 += 1

    if p3 == 64:
        if p1 > p2:
            messagebox.showinfo(title='message', message='Black Wins!')
        else:
            messagebox.showinfo(title='message', message='White Wins!')

    if flag_no==True:
        if p1 > p2:
            messagebox.showinfo(title='message', message='Black Wins!')
        else:
            messagebox.showinfo(title='message', message='White Wins!')



def click(r,c):
    global flag,color, flag_no
    flag_no = False
    if flag == True:
        color = 'black'
        x = human_play(color)
        if x == True:
            result = reverse_count(r, c, color)
            if result != 0:
                add_checker(r, c, color)
                score()
                flag = False
        else:
            flag_no = True
            messagebox.showinfo(title='Message', message='No move')
            score()
    else:
        color = 'white'
        x = human_play(color)
        if x == True:
            result = reverse_count(r, c, color)
            if result != 0:
                add_checker(r, c, color)
                score()
                flag = True
        else:
            flag_no = True
            messagebox.showinfo(title='Message', message='No move')
            score()


def reset():
    global flag
    flag = True

    for r in range(8):
        for c in range(8):
            if r ==3 and c ==3:
                bt[r][c] = Button(frm, bg='black', width=5, height=3, command= lambda row=r,column=c: click(row,column))
                bt[r][c].grid(row=r, column=c)
            elif r ==3 and c ==4:
                bt[r][c] = Button(frm, bg='white', width=5, height=3, command= lambda row=r,column=c: click(row,column))
                bt[r][c].grid(row=r, column=c)
            elif r==4 and c ==3:
                bt[r][c] = Button(frm, bg='white', width=5, height=3, command= lambda row=r, column=c: click(row,column))
                bt[r][c].grid(row=r, column=c)
            elif r ==4 and c ==4:
                bt[r][c] = Button(frm, bg='black', width=5, height=3, command= lambda row=r, column=c: click(row,column))
                bt[r][c].grid(row=r, column=c)
            else:
                bt[r][c] = Button(frm, bg='darkcyan', width=5, height=3, command= lambda row=r, column=c: click(row,column))
                bt[r][c].grid(row=r, column=c)

    lblack_point['text'] = 2
    lwhite_point['text'] = 2


lblack = Label(frm1,bg='Black', padx=20,pady=10, relief=RAISED)
lblack.grid(row=0, column=0)
lblack_point = Label(frm1, text=0, padx=20,pady=10, font=('Comic Sans',15))
lblack_point.grid(row=1, column=0)

lvs = Label(frm1, text='Vs', font=('Comic Sans',18))
lvs.grid(row=0,column=1)

lwhite = Label(frm1, bg='white', padx=20,pady=10, relief=RAISED)
lwhite.grid(row=0, column=2)
lwhite_point = Label(frm1, text=0, padx=20,pady=10, font=('Comic Sans',15))
lwhite_point.grid(row=1, column=2)

lvs_point = Label(frm1, text='-', font=('Comic Sans',18))
lvs_point.grid(row=1, column=1)



    #messagebox.showinfo(title='Othello', message="Let's play Othello Game!")


button_reset = Button(root, text='New Game', command=reset, font=('Comic Sans',15))
button_reset.grid(row=4, column=1)

reset()
root.mainloop()