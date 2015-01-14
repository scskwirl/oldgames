#--------------#
# Hack Attack! #
# By: Santo C. #
#--------------#

# Created January 15, 2008 (c) Santo C.


# Import the modules needed.
import random
random.seed()
from time import sleep


# Rules Document
Rules = """==========
Rules of the game:
------------------
A random set of 4 numbers (0-9) will be chosen, but hidden
from the player. This is the 'passcode'. The player must
take the limited amount of turns (10 turns) to try and
find the passcode.

For each guess made, the program will tell you if your
answer had a correct number, and if it was correctly placed.
The player wins when the code is entered correctly.

Get crackin'!
==========
"""

#
# -The Game Begins!-
#            

print """--------------------------------------
           +--------------+
           | Hack Attack! |
           | By: Santo C. |
           +--------------+
             How to play:
          Find the passcode!
--------------------------------------
    Hack Attack! (c) 2006 Santo C.
--------------------------------------
"""
# Game Constants & Functions
def NEW_PASSCODE():
    newpasscode = []
    for newnum in range(1, 5):
        newnum = str(random.randint(0, 9))
        newpasscode.append(newnum)
    return newpasscode

def Evaluate(passcode, answer):
    # Break the player's answer down into a list.
    player_eval = []
    for digit in answer:
        player_eval.append(digit)
    # See if the player has any correct numbers.
    Correct_Nums = 0
    for x in player_eval:
        for y in passcode:
            if x is y:
                Correct_Nums += 1
    print Correct_Nums, "of your numbers are in the passcode!"
    # See if the player has any in the right spot.
    Correct_Spot = 0
    for z in range(0, 4):
        if player_eval[z] is passcode[z]:
            Correct_Spot += 1
    print Correct_Spot, "of your numbers are in the right spot!"

    return Correct_Nums, Correct_Spot

#Game Loop
while True:
    print "-=MAIN MENU=-"
    print "1) Game Rules"
    print "2) Play"
    print "3) Quit Game"
    SLCT = raw_input("Select Choice: ")
    print

    if SLCT == '1': # List rules here.
        print Rules

    elif SLCT == '2':
        print "Alright let's begin!"
        print
        sleep(2)
        while True:
            print "Accessing random security database..."
            print
            PASSCODE = NEW_PASSCODE()
            sleep(2)
            print "Security database found! Connecting uplink to passcode..."
            print
            Progress = []
            for x in range(0,10):
                Progress.append([])
            sleep(2)
            print "Uplink established! Prepare for task..."
            print
            sleep(2)
            # Interface Begin
            turns = 0
            while turns < 10:
                print str(turns+1)+"/10 tries left."
                print "Type 'progress' to see your progress, or 'quit' to exit..."
                ANSWER = raw_input('PASSCODE: ')
                if int(ANSWER):
                    try:
                        c_n, c_s = Evaluate(PASSCODE, ANSWER)
                        Progress[turn] = (ANSWER, c_n+" Correct Numbers", c_s+" Correct Spots")
                        turns += 1
                    except:
                        if ANSWER == 'progress':
                            for x in range(0, 10):
                                print
                                print Progress[x]
                                print
                        elif ANSWER == 'quit':
                            print "Canceling Interface..."
                            print
                            sleep(2)
                            break
                        else:
                            print "Please write a 4-digit number, 'progress', or 'quit'!"
                            print
            break

    elif SLCT == '3':
        print "Goodbye! :)"
        sleep(2)
        break
    
    else:
        print "Please select an option!"
        print
