#--------------#
# High Roller! #
# By: Santo C. #
#--------------#

# Created June 1, 2005 (c) Santo C.


# Import the modules needed.
import random
from time import sleep

# Create self-made functions and classes.
def PlayerRoll(player,dice):
    raw_input(player.Name + ", press [ENTER] to roll!")
    dice.Roll()
    player.Value = dice.n + dice.n2
    print player.Name,"has",player.Value,"points!"
    print

class Player: # Player class
    def __init__(self):
        self.Name = ''
        self.Value = None
        
class Dice: # One Die
    def __init__(self):
        self.n = None
        self.n2 = None
    def Roll(self):
        self.n = random.randrange(1,7)
        self.n2 = random.randrange(1,7)
        print "+---++---+"
        print "|",self.n,"||",self.n2,"|"
        print "+---++---+"
        return self.n
        return self.n2

# Rules Document.
Rules = """==========
Rules of the game:
------------------
Select how many players will play.
Then, name each player that will play.
Each player gets only one roll at a time.
Press [ENTER] when prompted to roll the dice.
Player with the highest roll is the winner.
Ties draw the game, unless a player rolls higher than the tie.
You can replay with the same players, or play a different game after.

And of course, best of luck!
==========
"""

#
# -The Game Begins!-
#            

print """--------------------------------------------
              +--------------+
              | High Roller! |
              | By: Santo C. |
              +--------------+
                How to play:
Roll higher than the other player(s) to win!
--------------------------------------------
       High Roller! (c) 2005 Santo C.
--------------------------------------------
"""

#Game Loop
while True:
    print "-=MAIN MENU=-"
    print "1) Game Rules"
    print "2) 2 Players"
    print "3) 3 Players"
    print "4) 4 Players"
    print "5) Quit Game"
    SLCT = raw_input("Select Choice: ")
    print

    if SLCT == '1': # List rules here.
        print Rules
        
    elif SLCT == '2': # Start the 2-Player Game.
        print "2-Player game selected!"
        print
        while True:
            Player1 = Player()
            Player1.Name = raw_input("Player 1's Name: ")
            P1_Dice = Dice()
            
            Player2 = Player()
            Player2.Name = raw_input("Player 2's Name: ")
            P2_Dice = Dice()
            
            print
            print Player1.Name,'and',Player2.Name,'are ready to play!'
            print
            
            while True:
                print "---ROUND READY!---"
                print

                # This resets the scores.
                Player1.Value = 0
                Player2.Value = 0

                # This has the players roll their dice.
                PlayerRoll(Player1,P1_Dice)
                PlayerRoll(Player2,P2_Dice)
                sleep(2)

                # This displays the player results.
                print "+-Player Results-+"
                print '1. '+Player1.Name+':', Player1.Value
                print '2. '+Player2.Name+':', Player2.Value
                print "+----------------+"
                print
                sleep(2)

                # An algorithm that determines the winner.
                if Player1.Value > Player2.Value:
                    print Player1.Name, "is the winner!"
                    print
                elif Player1.Value < Player2.Value:
                    print Player2.Name, "is the winner!"
                    print
                elif Player1.Value == Player2.Value:
                    print Player1.Name,"and",Player2.Name,"tie this round!"
                    print

                # Ask to play again.                
                while True:
                    TryAgain = raw_input("Try again? (y/n) ")
                    if TryAgain == 'y':
                        print
                        print "Resetting Round..."
                        print
                        break
                    elif TryAgain == 'n':
                        print
                        print "Exiting round..."
                        del Player1
                        del P1_Dice
                        del Player2
                        del P2_Dice
                        print
                        break
                    else:
                        print
                        print "Please select 'y' or 'n'!"
                        print

                if TryAgain == 'n':
                    break
                elif TryAgain == 'y':
                    continue
            break

        # The following steps are all repeated for 3- and 4-Player games.
        # Exception: Snippets are modified to work with the player numbers.

    elif SLCT == '3': # Start the 3-Player Game.
        print "3-Player game selected!"
        print
        while True:
            Player1 = Player()
            Player1.Name = raw_input("Player 1's Name: ")
            P1_Dice = Dice()
            
            Player2 = Player()
            Player2.Name = raw_input("Player 2's Name: ")
            P2_Dice = Dice()

            Player3 = Player()
            Player3.Name = raw_input("Player 3's Name: ")
            P3_Dice = Dice()
            
            print
            print Player1.Name+',',Player2.Name+',','and',Player3.Name,'are ready to play!'
            print
            
            while True:
                print "---ROUND READY!---"
                print
                Player1.Value = 0
                Player2.Value = 0
                Player3.Value = 0
                
                PlayerRoll(Player1,P1_Dice)
                PlayerRoll(Player2,P2_Dice)
                PlayerRoll(Player3,P3_Dice)
                sleep(2)

                print "+-Player Results-+"
                print '1. '+Player1.Name+':', Player1.Value
                print '2. '+Player2.Name+':', Player2.Value
                print '3. '+Player3.Name+':', Player3.Value
                print "+----------------+"
                print
                sleep(2)

                if Player1.Value > Player2.Value and Player1.Value > Player3.Value:
                    print Player1.Name, "is the winner!"
                    print
                elif Player2.Value > Player1.Value and Player2.Value > Player3.Value:
                    print Player2.Name, "is the winner!"
                    print
                elif Player3.Value > Player1.Value and Player3.Value > Player2.Value:
                    print Player3.Name, "is the winner!"
                    print
                elif Player1.Value == Player2.Value or Player1.Value == Player3.Value\
                     or Player2.Value == Player1.Value or Player2.Value == Player3.Value\
                     or Player3.Value == Player1.Value or Player3.Value == Player2.Value\
                     or Player1.Value == Player2.Value == Player3.Value:
                    print "There is a tie!"
                    print

                while True:
                    TryAgain = raw_input("Try again? (y/n) ")
                    if TryAgain == 'y':
                        print
                        print "Resetting Round..."
                        print
                        break
                    elif TryAgain == 'n':
                        print
                        print "Exiting round..."
                        del Player1
                        del P1_Dice
                        del Player2
                        del P2_Dice
                        del Player3
                        del P3_Dice
                        print
                        break
                    else:
                        print
                        print "Please select 'y' or 'n'!"
                        print

                if TryAgain == 'n':
                    break
                elif TryAgain == 'y':
                    continue
            break

    elif SLCT == '4': # Start the 4-Player Game.
        print "4-Player game selected!"
        print
        while True:
            Player1 = Player()
            Player1.Name = raw_input("Player 1's Name: ")
            P1_Dice = Dice()
            
            Player2 = Player()
            Player2.Name = raw_input("Player 2's Name: ")
            P2_Dice = Dice()

            Player3 = Player()
            Player3.Name = raw_input("Player 3's Name: ")
            P3_Dice = Dice()

            Player4 = Player()
            Player4.Name = raw_input("Player 4's Name: ")
            P4_Dice = Dice()
            
            print
            print Player1.Name+',',Player2.Name+',',Player3.Name+',',\
            'and',Player4.Name,'are ready to play!'
            print
            
            while True:
                print "---ROUND READY!---"
                print
                Player1.Value = 0
                Player2.Value = 0
                Player3.Value = 0
                Player4.Value = 0
                
                PlayerRoll(Player1,P1_Dice)
                PlayerRoll(Player2,P2_Dice)
                PlayerRoll(Player3,P3_Dice)
                PlayerRoll(Player4,P4_Dice)
                sleep(2)

                print "+-Player Results-+"
                print '1. '+Player1.Name+':', Player1.Value
                print '2. '+Player2.Name+':', Player2.Value
                print '3. '+Player3.Name+':', Player3.Value
                print '4. '+Player4.Name+':', Player4.Value
                print "+----------------+"
                print
                sleep(2)

                if Player1.Value > Player2.Value\
                   and Player1.Value > Player3.Value\
                   and Player1.Value > Player4.Value:
                    print Player1.Name, "is the winner!"
                    print
                elif Player2.Value > Player1.Value\
                   and Player2.Value > Player3.Value\
                   and Player2.Value > Player4.Value:
                    print Player2.Name, "is the winner!"
                    print
                elif Player3.Value > Player1.Value\
                   and Player3.Value > Player2.Value\
                   and Player3.Value > Player4.Value:
                    print Player3.Name, "is the winner!"
                    print
                elif Player4.Value > Player1.Value\
                   and Player4.Value > Player2.Value\
                   and Player4.Value > Player3.Value:
                    print Player4.Name, "is the winner!"
                    print
                elif Player1.Value == Player2.Value\
                     or Player1.Value == Player3.Value\
                     or Player1.Value == Player4.Value\
                     or Player2.Value == Player1.Value\
                     or Player2.Value == Player3.Value\
                     or Player2.Value == Player4.Value\
                     or Player3.Value == Player1.Value\
                     or Player3.Value == Player2.Value\
                     or Player3.Value == Player4.Value\
                     or Player4.Value == Player1.Value\
                     or Player4.Value == Player2.Value\
                     or Player4.Value == Player3.Value\
                     or Player1.Value == Player2.Value == Player3.Value == Player4.Value:
                    print "There is a tie!"
                    print

                while True:
                    TryAgain = raw_input("Try again? (y/n) ")
                    if TryAgain == 'y':
                        print
                        print "Resetting Round..."
                        print
                        break
                    elif TryAgain == 'n':
                        print
                        print "Exiting round..."
                        del Player1
                        del P1_Dice
                        del Player2
                        del P2_Dice
                        del Player3
                        del P3_Dice
                        del Player4
                        del P4_Dice
                        print
                        break
                    else:
                        print
                        print "Please select 'y' or 'n'!"
                        print

                if TryAgain == 'n':
                    break
                elif TryAgain == 'y':
                    continue
            break
                    
    elif SLCT == '5': # Quit Application.
        print "Play again, sometime! Goodbye! :)"
        sleep(3)
        break

    else:
        print "Please select an option!"
        print
