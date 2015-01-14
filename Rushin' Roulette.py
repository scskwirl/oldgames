#------------------#
# Rushin' Roulette #
#   By: Santo C.   #
#------------------#

# Created October 25, 2006 (c) Santo C.


# Import the modules needed.
import random
from time import sleep

# Create self-made functions and classes.
def GameRound(ChamberCount):
    while True:
        Chamber = []
        for Round in range(ChamberCount):
            Chamber.append(False)
        print "You open up the %d-Chamber gun..." % (ChamberCount)
        sleep(2)
        Chamber[random.randrange(ChamberCount)] = True
        print "... To put in one bullet, and spin the clip HARD!"
        sleep(2)
        print "You then slap the clip back in..."
        sleep(2)
        print "... And you put the gun to your head..."
        sleep(2)

        print
        print "Are you ready?"
        print
        raw_input('Press [ENTER] to pull the trigger...')
        sleep(1)
        print
        print "You slowly pull the trigger, and..."
        sleep(3)

        if Chamber[0] == True:
            print
            print " /\\/\\/\\"
            print "< BANG > You're dead!"
            print " \\/\\/\\/"
            print
            sleep(2)
            print "Well, be glad this is only a text game..."
            sleep(2)

        elif Chamber[0] == False:
            print
            print "Click!"
            print
            sleep(2)
            print "... You're still alive! Good job!"
            sleep(2)

        print
        ContinuePlay = raw_input('Play again? (y/n) ')
        if ContinuePlay == 'y':
            print
            pass
        elif ContinuePlay == 'n':
            print
            break

# Rules Document
Rules = """==========
Rules of the game:
------------------
Play the world's most dangerous chance game,
in the safety of your own home!

Select how many chambers you want in the gun,
eight being easiest, two being hardest.
Then, the cartridge will be loaded with one bullet
and spun hard.

Then it's all in chance...

Good luck!
==========
"""

#
# -The Game Begins!-
#            

print """------------------------------------------
           +------------------+
           | Rushin' Roulette |
           |   By: Santo C.   |
           +------------------+
               How to play:
Spin the gun cartridge and don't get shot!
------------------------------------------
    Rushin' Roulette (c) 2006 Santo C.
------------------------------------------
"""

#Game Loop
while True:
    print "-=MAIN MENU=-"
    print "1) Game Rules"
    print "2) 8-Chamber Game (1/8 Chance)"
    print "3) 6-Chamber Game (1/6 Chance) [Standard]"
    print "4) 4-Chamber Game (1/4 Chance)"
    print "5) 2-Chamber Game (1/2 Chance)"
    print "6) Quit Game"
    SLCT = raw_input("Select Choice: ")
    print

    if SLCT == '1': # List rules here.
        print Rules

    elif SLCT == '2':
        print "You selected the 8-Chamber game, you wimp!"
        print
        sleep(2)
        GameRound(8)

    elif SLCT == '3':
        print "You selected the 6-Chamber game, the standard."
        print
        sleep(2)
        GameRound(6)

    elif SLCT == '4':
        print "You selected the 4-Chamber game... Sure you can do it?"
        print
        sleep(2)
        GameRound(4)

    elif SLCT == '5':
        print "You selected the 2-Chamber game... GODSPEED!!!"
        print
        sleep(2)
        GameRound(2)
        
    elif SLCT == '6': # Quit Application.
        print "Bite the bullet, for next time. See you! :)"
        sleep(3)
        break

    else:
        print "Please select an option!"
        print
