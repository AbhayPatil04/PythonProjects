# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Abhay Patil
# Section:      522
# Assignment:   7.28 Kaoprekars constant
# Date:         10/16/22
#
#
# YOUR CODE HERE
#
from math import *
def Ascend(arrange):
    asc = []
    i = 0
    arrange.sort()
    while i < len(arrange):
        asc.append(arrange[i])
        i += 1
def Decend(arrange):
    dec = []
    i = 0
    arrange.sort(reverse=1)
    while i < len(arrange):
        dec.append(arrange[i])
        i += 1
def KepsConstant(number):
    number = str(number)
    tron = number
    arrange = []
    i = 0
    while i < len(number):
        arrange.append(int(number[i]))
        i += 1

    if len(arrange) < 4:
        while len(arrange) < 4:
            arrange.insert(0, int(0))

    A = ''
    Ascend(arrange)
    while len(A) < 4:
        A += str(arrange[len(A)])
    D = ''
    Decend(arrange)
    while len(D) < 4:
        D += str(arrange[len(D)])

    x = 0
    ctr = 0
    pog = []
    while int(number) != 6174:
        if int(number) == 0:
            break
        if int(A) > int(D):
            number = str(int(A) - int(D))
            if int(number) != 6174 and int(number) != 0:
                pog.append(f'{number} >')
            else:
                pog.append(f'{number}')
        else:
            number = str(int(D) - int(A))
            if int(number) != 6174 and int(number) != 0:
                pog.append(f'{number} >')
            else:
                pog.append(f'{number}')
        arrange = []
        while x < len(number):
            arrange.append(int(number[x]))
            x += 1

        if len(arrange) < 4:
            while len(arrange) < 4:
                arrange.insert(0, int(0))

        A = ''
        Ascend(arrange)
        while len(A) < 4:
            A += str(arrange[len(A)])
        D = ''
        Decend(arrange)
        while len(D) < 4:
            D += str(arrange[len(D)])
        x = 0
        ctr += 1
    return ctr

i = 0
count = 0
while i < 10000:
    count += KepsConstant(i)
    i += 1
print(f'Kaprekar\'s routine takes {count} total iterations for all four-digit numbers')
