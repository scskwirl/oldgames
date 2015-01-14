#--------------#
#  Look Away!  #
# By: Santo C. #
#--------------#

# Created October 26, 2006 (c) Santo C.


# Import the modules needed.
import random
from time import sleep


# Rules Document
Rules = """==========
Rules of the game:
------------------
Standing in front of you is your game host.

He will point in one direction, and you have to
face the other direction by selecting the direction.

For example, he will point left, which means you will
have to look right, and it's done at the split of the
moment, so you never know...

Bonne Chance!
==========
"""

#
# -The Game Begins!-
#            

print """--------------------------------------
           +--------------+
           |  Look Away!  |
           | By: Santo C. |
           +--------------+
             How to play:
Look the other way from the game host!
--------------------------------------
     Look Away! (c) 2006 Santo C.
--------------------------------------
"""

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
        print "Alright, let's play!"
        print
        sleep(2)
        print "(The game host approaches you for the game...)"
        print
        sleep(2)
        print "Host: Hello there! Let's play some Look Away!"
        print
        sleep(2)
        print "Host: Right... When you're ready..."
        print "... You can look to the Left, or the Right, or quit at any time."
        print
        sleep(2)
        
        while True:
            print "(Which way will you look?)"
            Direction = raw_input('(1) Left / (2) Right / (3) Quit : ')
            print
            if Direction == '1':
                sleep(2)
                print "(You will look to the left...)"
                print
                sleep(2)
                print "Host: Ready? And..."
                print
                sleep(2)
                
                HostDirection = str(random.randrange(1,3))
                print "GO!"
                print "You: ", '<='
                if HostDirection == '1': print "Host:", '<='
                elif HostDirection == '2': print "Host:", '=>'
                print
                sleep(2)
                if HostDirection != Direction:
                    print "Host: Good, you looked the other way! You win!"
                    print
                elif HostDirection == Direction:
                    print "Host: Hah, you looked my direction! You lose!"
                    print
            elif Direction == '2':
                sleep(2)
                print "(You will look to the right...)"
                print
                sleep(2)
                print "Host: Ready? And..."
                print
                sleep(2)
                
                HostDirection = str(random.randrange(1,3))
                print "GO!"
                print "You: ", '=>'
                if HostDirection == '1': print "Host:", '<='
                elif HostDirection == '2': print "Host:", '=>'
                print
                sleep(2)
                if HostDirection != Direction:
                    print "Host: Good, you looked the other way! You win!"
                    print
                elif HostDirection == Direction:
                    print "Host: Hah, you looked my direction! You lose!"
                    print
                sleep(2)
            elif Direction == '3':
                break
            else:
                print
                print "Please select an option!"
                print
            

    elif SLCT == '3':
        print "Alright then. About face, and goodbye! :)"
        sleep(2)
        break
    
    else:
        print "Please select an option!"
        print
