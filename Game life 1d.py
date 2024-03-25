import random
import time

lenn = int(input('Введите длину мира: '))
ogr = int(input('Введите ограничение по поколениям: '))
aorb = int(input('Вы хотите сделать мир сами(введи - 1) или сгенироровать рандомно(введи - 2)?: '))
if aorb == 2:
    x1 = []
    for i in range(lenn):
        if random.randint(0, 1) == 0:
            x1.append('*')
        else:
            x1.append(' ')
else:
    x1 = list(input())
while '*' in ''.join(x1) and ogr != 0:
    n = -1
    ogr -= 1
    for i in x1:
        n += 1
        if n == 0:
            sled = x1[n + 1]
            pred = x1[len(x1) - 1]
        elif n == len(x1) - 1:
            sled = x1[0]
            pred = x1[n - 1]
        else:
            sled = x1[n + 1]
            pred = x1[n - 1]
        if i == '*':
            if (sled == '*' and pred == '*') or (sled == ' ' and pred == ' '):
                x1[n] = ' '
        elif i == ' ':
            if (sled == '*' and pred == ' ') or (sled == ' ' and pred == '*'):
                x1[n] = '*'
    print(x1)
    time.sleep(0.5)