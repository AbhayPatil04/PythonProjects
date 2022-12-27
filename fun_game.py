# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:    	Abhay Patil
#           	Aiden Guido
#           	Shikhar rai
#           	Riley Reid
# Section:  	102-522
# Assignment:   13
# Date:     	12/7/22

############################################################################
import turtle
import time
import random
import webbrowser
name = input('Enter your name - ')
try:
    with open('pog.txt','r') as f: #tries to read a file to read the instructions
        o = f.readlines()
        for line in o:
            print(line)

except: #if the file isnt there (we dont know how to submit it, too) this triggers and it just reads from here

    print('Rules of the game:')
    print('In bingo you have a 5x5 board with the word Bingo across the top for each column. ')
    print('Typically a random number is called and if you have that number on your board then you place a marker of some sort. ')
    print('Once you have five in a row, straight across, vertically, or diagonally, you win.')
    print('The very center of the board is a free space.')
    print('If a number is on the board twice and it is called, you have to choose which one to mark. Its strategy.')
    print('Just follow the keyboard input instructions on screen when each command is displayed.')




def rand(): #defined as its own function so that you can debug by just changing the values here
    """Creates a random number for the program to test against the board"""
    num = random.randint(10, 99)
    return num

binglist = [[rand(),rand(),rand(),rand(),rand()], [rand(),rand(),rand(),rand(),rand()], [rand(),rand(),"XX",rand(),rand()], [rand(),rand(),rand(),rand(),rand()], [rand(),rand(),rand(),rand(),rand()]]

#truelist stores if the number has been marked as gotten by the player or not
truelist = [[False, False, False, False, False], [False, False, False, False, False], [False, False, True, False, False], [False, False, False, False, False], [False, False, False, False, False]]

check = 0

def bingo():
    check = rand() #generates a new random number.
    print(f'Do any of your numbers match this: {check}')
    tru = input("Enter Y/N")
    if tru == 'Y':
        i = 0
        while i == 0:
            try: #the try and excepts following are about error catching with bad user inputs
                row = int(input("What row is it in: "))-1
                column = int(input("What column is it in: "))-1
            except:
                print("Bad input, Only numbers")
            try:
                binglist[row][column]
                break
            except: #usually for range errors
                print("Enter proper values")
        if binglist[row][column] == check: #this triggers if the row and column the user pointed out isnt a lie and the numbers do match
            print("Nice")
            binglist[row][column] = 'XX'
            truelist[row][column] = True

        else: #Trigggers if the user lied
            print('you lied or typed it wrong')

    else:
        print('rip') #triggers if they say no to having a matching number


def check():
    pog = False
    che = input("DO you have Bingo? Y/N: ")
    if che == 'Y':
        which = input("Diagonal Row or Column D/R/C?: ") #to make it easier for program checking
        if which == 'D':
            pog = checkdiagonal() #calls checkdiagonal
        elif which == 'R':
            i = 0
            while i == 0:
                try:                                #many try and excepts follow, all about  bad inputs
                    a = int(input("Which Row: "))
                    break
                except:
                    print("Bad input, Only numbers")
            pog = checkrow(a) #calls checkrow
        else:
            i = 0
            while i == 0:
                try:
                    a = int(input("Which Column: "))
                    break
                except:
                    print("Bad input, Only numbers")
            pog = checkcolumn(a) #calls check column
    return pog

def checkdiagonal():
    """Checks if there is a diagonal bingo"""
    i = 0
    ctr = 0
    lol = False #lol stores if there was actually a bingo found
    while i < 5: #checks the whole board and makes sure there are at least 5 trues before checking if they are in the diagonals
        j = 0
        while j < 5:
            if truelist[i][j] == True:
                ctr += 1
            j += 1
        i+= 1
    if ctr >= 5:
        pog = 0
        ctrr = 0
        while pog < 5:
            if truelist[pog][pog] ==  True: #checks the topleft-bottomright diagonal
                ctrr += 1
            pog += 1
        if ctrr == 5: #if all 5 are counted and thus there is all 5 in the diagonal, then lol is true
            lol = True
        else:
            pog = 4
            pog1 = 0
            ctrr = 0
            while pog > -1:
                if truelist[pog][pog1] == True: #checks the other diagonal (thus pog starts at 4 insteadof 0)
                    ctrr += 1
                pog -= 1
                pog1 += 1
            if ctrr == 5:
                lol = True
    return lol

def checkrow(a):
    """Check if there is a fully finished row"""
    i = 0
    ctr = 0
    lol = False
    while i < 5:
        j = 0
        while j < 5:
            if truelist[i][j] == True: #checks to see if theres at least 5 on the board at all first of all
                ctr += 1
            j += 1
        i+= 1

    if ctr >= 5: #triggers if 5 are detected in the board over all
        pog = a-1 #pog stores the row to check since a is what the user entered
        pog1 = 0
        ctrr = 0
        while pog1 < 5:
             if truelist[pog][pog1] == True: #checks the row
                ctrr += 1
             pog1 += 1
        if ctrr == 5: #if 5 are detected then lol is true and the row does have a bingo
            lol = True
    return lol

def checkcolumn(a):
    """Check if there is a fully finished column"""
    i = 0
    ctr = 0
    lol = False
    while i < 5:
        j = 0
        while j < 5:
            if truelist[i][j] == True: #makes sure theres at least 5 things checked to be true
                ctr += 1
            j += 1
        i+= 1

    if ctr >= 5:
        pog = a-1 #pog is the column that the user said the bingo is in
        pog1 = 0
        ctrr = 0
        while pog1 < 5:
             if truelist[pog1][pog] == True: #checks the column basically the same way that checkrow works
                ctrr += 1
             pog1 += 1
        if ctrr == 5:
            lol = True

    return lol

pog = turtle.Turtle() #tons of code for turtle found below
pog.speed(0)
arm_length = 100
leg_length = 120
def reset():
    pog.pu()
    pog.setpos(0, 0)
    pog.pd()

def eye(col, rad):
    pog.down()
    pog.fillcolor(col)
    pog.begin_fill()
    pog.circle(rad)
    pog.end_fill()
    pog.up()

def human(win): #triggers if win
    if win == True:
        # draw face
        pog.fillcolor('yellow')
        pog.begin_fill()
        pog.circle(100)
        pog.end_fill()
        pog.up()

        # draw eyes
        pog.goto(-40, 120)
        eye('white', 15)
        pog.goto(-37, 125)
        eye('black', 5)
        pog.goto(40, 120)
        eye('white', 15)
        pog.goto(40, 125)
        eye('black', 5)

        # draw mouth
        pog.goto(-40, 85)
        pog.down()
        pog.right(90)
        pog.circle(40, 180)
        pog.up()


        reset()
        # arm 1
        pog.seth(160)
        pog.fd(arm_length / 2)
        pog.rt(40)
        pog.fd(arm_length / 2)

        reset()
        # arm 2
        pog.seth(20)
        pog.fd(arm_length / 2)
        pog.lt(40)
        pog.fd(arm_length / 2)

        reset()
        # leg 1
        pog.seth(270)
        pog.fd(50)
        pog.seth(230)
        pog.fd(leg_length / 2)
        pog.lt(40)
        pog.fd(leg_length / 2)

        reset()
        # leg 2
        pog.seth(270)
        pog.fd(50)
        pog.seth(310)
        pog.fd(leg_length / 2)
        pog.rt(40)
        pog.fd(leg_length / 2)
        turtle.exitonclick()


i = 0
win = False
while i <= 20:
    x = 0
    while x < 5: #prints each row one at a time, 5 times
       print(binglist[x][0], end=' ')
       print(binglist[x][1], end=' ')
       print(binglist[x][2], end=' ')
       print(binglist[x][3], end=' ')
       print(binglist[x][4])
       x += 1
    bingo() #runs the bingofunction, which handles most of the turn by turn of the game including asking for moves and calling other functions
    if check() == True: #this is the win condition
        print('You win!')
        win = True
        with open('namesofwinners.txt', 'a') as f:
            f.write(name)
            f.write(' ')
        break
    i += 1 #after the move it adds to the loop. board is porinted again, bingo is called again, and then the player is asked if they have a bingo with check()

if i > 20: #triggers if 20 turns have passed
    print("Sorry, you lost so you deserve this")
    time.sleep(1.5)
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=oHg5SJYRHA0') #lol



human(win)


