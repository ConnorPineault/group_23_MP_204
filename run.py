


import random
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# These two lines make sure a faster SAT solver is used.
from nnf import config
config.sat_backend = "kissat"

# Encoding that will store all of your constraints
E = Encoding()

SUITS = ['S', 'C', 'D', 'H']  # Spades, Clubs, Diamonds, Hearts
NUMBERS = list(range(2, 15))
  # 2 to 14, where 11=Jack, 12=Queen, 13=King, 14=Ace


#test_case
#SUITS = ['S','H'] 
#NUMBERS = list(range(2, 6))





""" FUNCTION: DEAL CARDS
    PARAMETER: DECK (FOUND IN MAIN)
    RETURNS: SORTED LIST OF 3 CARDS
    """

def dealCards(deck):

    random.shuffle(deck)
    u_hand = set()

    while len(u_hand) < 3 and deck:
        card = deck.pop()
        u_hand.add(card)

    u_hand_sorted = sorted(u_hand, key=lambda card: (card.number, card.suit)) #SORTED!!


    

    
    

    return u_hand_sorted



# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class Card:

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __repr__(self):
        return f"{self.number}.{self.suit}" 
    

class Hand:
    def __init__(self, cards):        #CARD 1,2,3 ???
        self.cards = cards
      #  self.card2 = card2
      #  self.card3 = card3
        self.SF = False
        self.TK = False
        self.S = False
        self.FL = False
       # self.P = handRanking()
        self.P = False
        self.HC = False
        self.win = False
        




# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
@constraint.at_least_one(E)
@proposition(E)


class FancyPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"

# Call your variables whatever you want
"""
a = BasicPropositions("a")
b = BasicPropositions("b")   
c = BasicPropositions("c")
d = BasicPropositions("d")
e = BasicPropositions("e")
# At least one of these will be true
x = FancyPropositions("x")
y = FancyPropositions("y")
z = FancyPropositions("z")


"""

"""
SF = BasicPropositions("SF")
FL = BasicPropositions("F")
S =  BasicPropositions("S")
TK = BasicPropositions("TK")
P =  BasicPropositions("P")
HC = BasicPropositions("HC")
"""
# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():

    pass



""" HANDRANK
    PARAMETER: HAND 
    RETURNS: 
"""
def handRanking(hand): 

    # Add a constraint that at least one of the straight conditions must be met
    # Bauhaus encoding means that sum checks through each proposition in the list
    # So if one proposition in list is correct it returns as true
    cards = hand.cards


    
#STRAIGHT FLUSH
    SF = [
    ((cards[0].suit == suit) & (cards[1].suit == suit) & (cards[2].suit == suit) & 
    (cards[0].number == cards[1].number - 1) & (cards[1].number == cards[2].number - 1))
    for suit in SUITS
]

    if any(SF):
        print('straight flush')
        hand.SF = True
        return True
    """BROKEN SF
SF = [
    ((cards[0].suit == suit) & (cards[1].suit == suit) & (cards[2].suit == suit) & 
    (cards[0].number == cards[1].number + 1) & (cards[1].number == cards[2].number + 1))
    for suit in SUITS
    ]
    if any(SF):
        print('straight flush')
        return True
    """

    
#THREE OF A KIND
    TK = [
    ((cards[0].number == num) & (cards[1].number == num) & (cards[2].number == num))
    for num in NUMBERS
    ]

#Straight
    S = (cards[0].number + 1 == cards[1].number) and (cards[1].number + 1 == cards[2].number)

    if S:
        print("Straight")
        hand.S = True
        return True

#FLUSH
    FL = [
    ((cards[0].suit == suit) & (cards[1].suit == suit) & (cards[2].suit == suit))
    for suit in SUITS
    ]

    if any(FL):
        print('flush')
        hand.FL = True
        return True

#Pair       
    P = [
        ((cards[0].number == num) & (cards[1].number == num) & (cards[2].number != num)) or ((cards[0].number != num) & (cards[1].number == num) & (cards[2].number == num))
        for num in NUMBERS
    ]
    if any(P):
        print('pair')
        hand.P = True
        return True
    
    """"

        #Pair           #Not sure if cards P works
    cards.P = [
        ((cards.card1.number == num) & (cards.card2.number == num) & (cards.cards3.number != num)) or ((cards.card1.number != num) & (cards[1].number == num) & (cards[2].number == num))
        for num in NUMBERS
    ]
    if any(P):
        print('pair')
    
        return True

    """

"""FUNCTION: PLAY OR FOLD
   PARAMETER: 
   RETURNS: 
"""
def playOrFold(): ##PLAY OR FOLD RECOMMENDATIONS

    # High card is Ace or King for user
    for suit in SUITS:
        E.add_constraint(Card(14, suit) | Card(13, suit))

    #Hand is Queen-7 or better for user
    for suit in SUITS:
        for suit2 in SUITS:
            #condition = (
            E.add_constraint((Card(14, suit) | Card(13, suit) | Card(12, suit))
                &
                (Card(14, suit) | Card(13, suit) | Card(12, suit) |
                Card(11, suit) | Card(10, suit) | Card(9, suit) |
                Card(8, suit) | Card(7, suit)) 
            )
    q64_conditions.append(condition)
    E.add_constraint(sum(q64_conditions))

    # Hand is Queen-6-4 or better for user
    q64_conditions = []
    for suit1 in SUITS:
        for suit2 in SUITS:
            for suit3 in SUITS:
                condition = (
                Card(12, suit1) &  # Queen
                (Card(6, suit2) | Card(7, suit2) | Card(8, suit2) |
                    Card(9, suit2) | Card(10, suit2) | Card(11, suit2) |
                    Card(12, suit2) | Card(13, suit2) | Card(14, suit2)) 
                    &
                (Card(4, suit3) | Card(5, suit3) | Card(6, suit3) |
                    Card(7, suit3) | Card(8, suit3) | Card(9, suit3) |
                    Card(10, suit3) | Card(11, suit3) | Card(12, suit3) |
                    Card(13, suit3) | Card(14, suit3))
                )

                q64_conditions.append(condition)
    E.add_constraint(sum(q64_conditions))

    return E



#THIS FUNCTION DETERMINES WHICH HAND IS BETTER      STILL NEED TO ADD TIES!!!
def determineWinner(hand1, hand2):

    #USER HAS A STRAIGHT FLUSH, DEALER DOES NOT
    win = (hand1.SF and not hand2.SF)
    if (win):
        hand1.win = True
        return True

    
    hand1.win = hand1.SF and not hand2.SF  
    #USER HAS THREE OF A KIND
    win = (hand1.TK and not hand2.SF and not hand2.TK)
    if (win):
        hand1.win = True
        return True

    #USER HAS A STRAIGHT
    win = (hand1.S and not hand2.SF and not hand2.TK and not hand2.S)
    if (win):
        hand1.win = True
        return True

    #USER HAS A PAIR
    win = (hand1.P and not hand2.SF and not hand2.TK and not hand2.S and not hand2.P)
    if (win):
        hand1.win = True
        return True
    hand1.win = (hand1.S and not hand2.SF and not hand2.TK and not hand2.S) 

    #USER HAS A PAIR
    hand1.win = (hand1.S and not hand2.SF and not hand2.TK and not hand2.S and not hand2.P) 

    cards1 = hand1.cards
    cards2 = hand2.cards
    hc1 = cards1[2]
    hc2 = cards2[2]

    #USER HAS A HIGH CARD
    if (hand1.HC & hand2.HC):
        if (hc1 > hc2):
            hand1.win = True
            return True
        else:
            hand2.win = True
            return True
            
    if (hand1.win == False):
        hand2.win = True
        return True
    
    
def main():
    deck = [Card(num,suit) for num in NUMBERS for suit in SUITS]


    cards1 = dealCards(deck)    
    print(cards1)
    hand1 = Hand(cards1)

    cards2 = dealCards(deck)
    print(cards2)
    hand2 = Hand(cards2)


    handRanking(hand1)

    handRanking(hand2)

    print("Test!    Straight Flush: ", hand1.SF, ", Flush:", hand1.FL, ", Pair:", hand1.P, ", Three of:", hand1.TK, ", Straight:", hand1.S)
    print("Test!    Straight Flush: ", hand1.SF, ", Flush:", hand2.FL, ", Pair:", hand2.P, ", Three of:", hand2.TK, ", Straight:", hand2.S)


    determineWinner(hand1, hand2)
    print("Hand1: ", hand1.win)
    print("Hand2: ", hand2.win)
    


   


























if __name__ == "__main__":
    main()

        
    

    



    #T = example_theory()
    # Don't compile until you're finished adding all your constraints!
   # T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
   # print("\nSatisfiable: %s" % T.satisfiable())
   # print("# Solutions: %d" % count_solutions(T))
   # print("   Solution: %s" % T.solve())

 #   print("\nVariable likelihoods:")
  #  for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
  #      print(" %s: %.2f" % (vn, likelihood(T, v)))
 #   print()