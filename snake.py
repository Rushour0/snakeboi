import time
import os
import random
from pynput import keyboard
def ran(a,b,v):
    r = random.randint(1,a-1)
    c = random.randint(2,b-1)
    if [r,c] in v.values():
        return ran(a,b,v)
    else:
        return [r,c]
def t(s):
    return time.sleep(s)
def clr():
        os.system('cls||clear')
body = '\u25CF'
head = 'o'
n = 21
l = [['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#'],['#']+[' ']*(2*n-2)+['#']]
snake = ['\u25CF','\u25CF',head]
l[10] = ['#']+snake+[' ']*(2*n-5)+['#']
d = {1:[10,3],2:[10,2],3:[10,1]}
border = ['#']*(2*n)
counter = 0
def output():
    print(counter)
    print(*border)
    for i in l:
        print(*i)
    print(*border)
ipos = [10,10]
l[ipos[0]][ipos[1]] = '.' 
def update():
    pos = {}
    tpos = ran(n-1,2*n-2,d)
    l[tpos[0]][tpos[1]] = '.'
    pos[tuple(tpos)] = 1
    pos[(-n+tpos[0],tpos[1])] = 2
    return pos
def chk(t):
    if t == 0:
        l[d[len(snake)][0]][d[len(snake)][1]] = ' '
    else:
        l[d[len(snake)][0]][d[len(snake)][1]] = body
        d[len(snake)+1] = d[len(snake)]
    for i in range(len(snake)-1):
        a = len(snake)-i
        d[a] = d[a-1].copy()
        l[d[a][0]][d[a][1]] = body
def up(t):
    chk(t)
    if d[1][0] == 0:
            d[1][0] = n
    d[1] = [d[1][0]-1,d[1][1]]
    l[d[1][0]][d[1][1]] = head
def down(t):
    chk(t)
    if d[1][0] == n-1:
            d[1][0] = -1
    d[1] = [d[1][0]+1,d[1][1]]
    l[d[1][0]][d[1][1]] = head
def right(t):
    chk(t)
    if d[1][1] == 2*n-2:
            d[1][1] = 0
    d[1] = [d[1][0],d[1][1]+1]
    l[d[1][0]][d[1][1]] = head
def left(t):
    chk(t)
    if d[1][1] == 1:
        d[1][1] = 2*n-1       
    d[1] = [d[1][0],d[1][1]-1]
    l[d[1][0]][d[1][1]] = head    
def end():
    clr()
    ded = [[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55,[' ']*55]
    for i in range(2):
        ded[3+i][12:20] = '\u25CF'*7
        ded[13+i][12:20] = '\u25CF'*7
        ded[8+i][12:20] = '\u25CF'*4
    for i in range(12):
        ded[3+i][1] = '\u25CF'
        ded[3+i][2] = '\u25CF'
        ded[3+i][10] = '\u25CF'
        ded[3+i][11] = '\u25CF'
        ded[3+i][21] = '\u25CF'
        ded[3+i][22] = '\u25CF'
    for z in range(5):
        for i in range(3):
            ded[3+i+z][23+z] = '\u25CF'
            ded[14-i-z][23+z] = '\u25CF'
    for z in range(5):
        for i in range(3):
            ded[3+i+z][3+z] = '\u25CF'
            ded[14-i-z][3+z] = '\u25CF'
    for i in ded:
        print(''.join(i))
    print('Ded, lol NOOB') 
    t(20)    
inp = ''
di = 'r'
fpos = {(10,10):1}
while 1:
    with keyboard.Events() as events:
        st = time.time()
        event = events.get(0.5)
        en = time.time()
        if float(en-st)<= float(0.5):
            time.sleep(0.5  -en+st)
        if event is None:
            t(0)
        else:
            val = str(event)[11]
            if val in 'wasd':
                inp = val
    dchk = d.copy()
    del dchk[1]
    clr()
    if [d[1][0],d[1][1]] not in dchk.values():
        if inp == 'w':
            if di != 'd':
                di = 'u'
                if (d[1][0]-1,d[1][1]) in fpos:
                    counter +=1
                    up(1)
                    fpos = update()
                    snake+=['O']
                else:
                    up(0)
            else:
                end()
                print('Went reverse, LOL dumb')
                break
        elif inp == 's':
            if di != 'u':
                di = 'd'
                if (d[1][0]+1,d[1][1])in fpos:
                    counter +=1
                    down(1)
                    fpos = update()
                    snake+=['O']
                else:
                    down(0)
            else:
                end()
                print('Went reverse, LOL dumb')
                break
        elif inp == 'd':
            if di != 'l':
                di = 'r'
                if (d[1][0],d[1][1]+1) in fpos:
                    counter +=1
                    right(1)
                    fpos = update()
                    snake+=['O']
                else:
                    right(0)
            else:
                end()
                print('Went reverse, LOL dumb')
                break
        elif inp == 'a':
            if di!='r':
                di = 'l'
                if (d[1][0],d[1][1]-1) in fpos:
                    counter +=1
                    left(1)
                    fpos = update()
                    snake+=['O']
                else:
                    left(0)
            else:
                end()
                print('Went reverse, LOL dumb')
                break
    else:
        end()
        break
    output()
t(20)

    
