#!/usr/bin/env python
#queen8 algorithm

queen = [['*']*8 , ['*']*8, ['*']*8 , ['*']*8 , ['*']*8 , ['*']*8 , ['*']*8 , ['*']*8]
row = []
a = []
b = []
c = []
rowColumn = 8
diagonal = 15
i = 0
while i < rowColumn:
    a.append(1)
    i += 1
i = 0
while i < diagonal:
    b.append(1)
    c.append(1)
    i += 1
i = 0


def set_queen(num):
    global queen
    global a
    global b
    global c
    global i
    j = 0
    while j < rowColumn:
            if (a[j] == 1) and (b[num+j] == 1) and (c[num-j+7] == 1):
                a[j] = 0
                b[num+j] = 0
                c[num-j+7] = 0
                queen[num][j] = '@'
                if num != 7:
                    set_queen(num + 1)
                else:
                    i += 1
                    print(str(i) + '\n')
                    k = 0
                    while k < 8:
                        print(queen[k])
                        k += 1
                    print('\n')
                a[j] = 1
                queen[num][j] = '*'
                b[num+j] = 1
                c[num-j+7] = 1
            j += 1
set_queen(0)
myList = [([0] * 3) for io in range(4)]
print(myList)


