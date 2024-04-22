import random
import time

game = 'да'
while game == 'да':
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
        prover = False
        while prover != True:
            prov = 0
            for i in x1:
                if i == '*' or i == ' ':
                    prov += 1
            if prov == len(x1):
                prover = True
            else:
                print('можно вводить только пробелы( ) и звездочки(*)')
                x1 = list(input())

    x2 = x1[:]
    while '*' in ''.join(x2) and ogr != 0:
        n = 0
        ogr -= 1
        for i in x2:
            if n == 0:
                sled = x2[n + 1]
                pred = x2[len(x2) - 1]
            elif n == len(x2) - 1:
                sled = x2[0]
                pred = x2[n - 1]
            else:
                sled = x2[n + 1]
                pred = x2[n - 1]
            if i == '*':
                if (sled == '*' and pred == '*') or (sled == ' ' and pred == ' '):
                    x1[n] = ' '
            elif i == ' ':
                if (sled == '*' and pred == ' ') or (sled == ' ' and pred == '*'):
                    x1[n] = '*'
            n += 1
        x2 = x1[:]
        print(*x1, sep='')
        time.sleep(0.5)
    game = input('Хочешь еще поиграть?(Если хочешь, то введи "да", иначе введи что-то другое)')