#--------------#
#   Blue Cat   #
# By: Santo C. #
#--------------#

# Created October 8, 2005 (c) Santo C.


# Import the modules needed.
import random
from time import sleep

# Create the Deck suits and values
Suits = ['Spades','Clubs','Hearts','Diamonds']
SuitsID = ['s','c','h','d']
Values = ['Ace',
          'Two',
          'Three',
          'Four',
          'Five',
          'Six',
          'Seven',
          'Eight',
          'Nine',
          'Ten',
          'Jack',
          'Queen',
          'King']
ValuesID = ['a','2','3','4','5','6','7','8','9','10','j','q','k']

# Create the Card Object
class GameCard:
    def __init__(self,Suit,Value):
        self.Name = Value + ' of ' + Suit
        self.Suit = Suit
        self.Value = Value


# Create the List that is the deck
Deck = []

# Build the deck
for a in range(0,len(Suits)):
    for b in range(0,len(Values)):
        Card = GameCard(Suits[a],Values[b])
        Card.Iden = (ValuesID[b]+SuitsID[a])
        Card.CoreVal = b+1
        Deck.append(Card)


# The Rules Document.
Rules = """==========
Rules of the game:
------------------
You will be dealt a hand of three cards, two of
which are face-up. The middle card has to be of
value between the two other cards by chance.

To win:
The card must be any of the values in between the
two side cards.

If the two side cards are the same, the third must
also tie for a three in a row win.

If the two side cards are adjacent in value,
you must get either of those values to win.

Good luck!
==========
"""

#
# -The Game Begins!-
#            

print """----------------------------------------
            +--------------+
            |   Blue Cat   |
            | By: Santo C. |
            +--------------+
              How to play:
Get the middle value on the middle card!
----------------------------------------
       Blue Cat (c) 2005 Santo C.
----------------------------------------
"""
while True:
    print "-=MAIN MENU=-"
    print "1) Game Rules"
    print "2) Play Game"
    print "3) Quit Game"
    SLCT = raw_input("Select Choice: ")
    print
    if SLCT == '1': # Print the rules
        print Rules
    elif SLCT == '3': # Exit the game
        print "Come again soon! :)"
        sleep(2)
        break
    elif SLCT == '2': # The Game loop
        print "Let's play some Blue Cat!"
        print
        while True:
            # Shuffle the deck and deal the cards, sides first.
            random.shuffle(Deck)
            print "Here is your hand..."
            print
            Hand1 = Deck[0]
            Hand2 = Deck[2]
            Hand3 = Deck[1]
            print '['+Hand1.Name+']', '[???]', '['+Hand3.Name+']'
            print
            
            if Hand1.CoreVal == Hand3.CoreVal: # If you get tied side cards...
                print "You must land",Hand1.CoreVal,"to win!"
                print
                raw_input("Press [ENTER] to check!")
                print
                print '['+Hand1.Name+']', '   [[['+Hand2.Name+']]]   ', '['+Hand3.Name+']'
                print
                if Hand2.CoreVal == Hand1.CoreVal and Hand2.CoreVal == Hand3.CoreVal:
                    print "You won!"
                    print
                else:
                    print "You lost!"
                    print
            elif Hand1.CoreVal == Hand3.CoreVal-1 or Hand1.CoreVal == Hand3.CoreVal+1\
                 or Hand3.CoreVal == Hand1.CoreVal-1 or Hand3.CoreVal == Hand1.CoreVal+1:
                # Side Cards are adjacent in value.
                print "You must get either",Hand1.CoreVal,"or",Hand3.CoreVal,"to win!"
                print
                raw_input("Press [ENTER] to check!")
                print
                print '['+Hand1.Name+']', '   [[['+Hand2.Name+']]]   ', '['+Hand3.Name+']'
                print
                if Hand2.CoreVal == Hand1.CoreVal or Hand2.CoreVal == Hand3.CoreVal:
                    print "You won!"
                    print
                else:
                    print "You lost!"
                    print
                
            else: # Any other give.
                if Hand1.CoreVal < Hand3.CoreVal:
                    WinCards = range(Hand1.CoreVal+1, Hand3.CoreVal)
                elif Hand3.CoreVal < Hand1.CoreVal:
                    WinCards = range(Hand3.CoreVal+1, Hand1.CoreVal)
                print "Anything between",Hand1.CoreVal,"and",Hand3.CoreVal,\
                "will land you a win!"
                print "Winning Cards:", str(WinCards)
                print
                raw_input("Press [ENTER] to check!")
                print
                print '['+Hand1.Name+']', '   [[['+Hand2.Name+']]]   ', '['+Hand3.Name+']'
                print
                if Hand2.CoreVal in WinCards:
                    print "You won!"
                    print
                elif Hand2.CoreVal not in WinCards:
                    print "You lost!"
                    print

            while True: # Try Again prompt
                Choice = raw_input("Would you like to try again? (y/n): ")
                if Choice == 'y':
                    print
                    print '-' * 20
                    print
                    break
                elif Choice == 'n':
                    print
                    break
                else:
                    print
                    print "Please select an option!"
                    print
            if Choice == 'n':
                break
    else:
        print "Please select an option!"
        print
