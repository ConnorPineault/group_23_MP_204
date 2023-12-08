


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






""" FUNCTION: DEAL CARDS
    PARAMETER: DECK (FOUND IN MAIN)
    RETURNS: U_HAND_SORTED (SORTED LIST OF 3 CARDS)
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
#@proposition(E)

    


""" CLASS: CARD
    ATTRIBUTES: NUMBER, SUIT
    METHODS: __init__, __repr__  
    """
class Card:

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __repr__(self):
        return f"{self.number}.{self.suit}" 
    


""" CLASS: HAND
    ATTRIBUTES: CARDS, SHARED_CARDS, HAND RANKS
    METHODS: N/A
    """
class Hand:
    def __init__(self, cards, shared_cards):        #CARD 1,2,3 ???
        self.cards = cards
        self.shared_cards = shared_cards
      #  self.card2 = card2
      #  self.card3 = card3
        self.SF = False
        self.TK = False
        self.S = False
        self.FL = False
      # self.P = handRanking()
        self.P = False
        self.TP = False
        self.HC = False
        self.HCC = False    #Compares high card with high card of other deck
        self.win = False
        #Hand recommendations
        self.RP = False     #Recommend play or fold the hand
        self.HCR = 0    #Variable to keep track of rank of high card of hand (no shared)
        self.rank = ""

        




# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html


"""CONSTRAINTS"""
###    @constraint.at_least_one(E)



"""PROPOSITIONS"""
@proposition(E)
class SF:
    def __init__(self):
        pass
@proposition(E)
class TK:
    def __init__(self):
        pass
@proposition(E)
class S:
    def __init__(self):
        pass 
@proposition(E)
class FL:
    def __init__(self):
         pass
@proposition(E)
class TP:
    def __init__(self):
         pass
@proposition(E)
class P:
    def __init__(self):
        pass 
@proposition(E)
class HC:
    def __init__(self):
        pass








""" CLASS: FANCY PROPOSITIONS
    ATTRIBUTES: N/A
    METHODS: __init__, __repr__  
    """
class FancyPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"





#  Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():





    @constraint.add_implies_all(E, SF)
    def straight_flush_constraint(hand):
        cards = hand.cards + hand.shared_cards
        cards.sort(key=lambda card: (card.number, card.suit))
        return (
            (cards[0].suit == cards[1].suit == cards[2].suit == cards[3].suit == cards[4].suit) and
            ((cards[0].number == cards[1].number - 1) & (cards[1].number == cards[2].number - 1) & (cards[2].number == cards[3].number - 1)) |
            (cards[1].number == cards[2].number - 1) & (cards[2].number == cards[3].number - 1) & (cards[3].number == cards[4].number - 1)
        )
    @constraint.add_implies_all(E, TK)
    def three_of_a_kind_constraint(hand):
        cards = hand.cards + hand.shared_cards
        cards.sort(key=lambda card: (card.number, card.suit))
        return (   
            ((cards[0].number == num) & (cards[1].number == num) & (cards[2].number == num)) |
            ((cards[1].number == num) & (cards[2].number == num) & (cards[3].number == num)) |
            ((cards[2].number == num) & (cards[3].number == num) & (cards[4].number == num)) 
        )
    @constraint.add_implies_all(E, S)
    def straight_constraint(hand):
        cards = hand.cards + hand.shared_cards
        cards.sort(key=lambda card: (card.number, card.suit))
        return (   
        ((cards[0].number == cards[1].number - 1) & (cards[1].number == cards[2].number - 1) &  (cards[2].number == cards[3].number - 1))|
        (cards[1].number == cards[2].number - 1) & (cards[2].number == cards[3].number - 1) &  (cards[3].number == cards[4].number - 1) 
        )
    @constraint.add_implies_all(E, FL)
    def flush_constraint(hand):
        cards = hand.cards + hand.shared_cards
        cards.sort(key=lambda card: (card.number, card.suit))
        return (
           
        (cards[0].suit == cards[1].suit == cards[2].suit == cards[3].suit)
        )
    @constraint.add_implies_all(E, TP)
    def two_pair_constraint(hand):
        cards = hand.cards + hand.shared_cards
        cards.sort(key=lambda card: (card.number, card.suit))
        return (
           
        ((cards[0].number == cards[1].number) & (cards[2].number == cards[3].number)) |
        ((cards[0].number == cards[1].number) & (cards[3].number == cards[4].number)) |
        ((cards[1].number == cards[2].number) & (cards[3].number == cards[4].number)) |
        ((cards[2].number == cards[3].number) & (cards[4].number == cards[0].number))

        )
    @constraint.add_implies_all(E, P)
    def pair_constraint(hand):
        cards = hand.cards + hand.shared_cards
        cards.sort(key=lambda card: (card.number, card.suit))
        return (  
        ((cards[0].number == cards[1].number) | (cards[1].number == cards[2].number) | 
        (cards[2].number == cards[3].number) | (cards[3].number == cards[4].number))
        )
    @constraint.add_implies_all(E, HC)
    def high_card_constraint(hand):
        cards = hand.cards + hand.shared_cards
        cards.sort(key=lambda card: (card.number, card.suit))
        return (
           
        (not hand.SF and not hand.TK and not hand.S and not hand.FL and not hand.TP and not hand.P)

        )





    from bauhaus import solve


    def handRanking2(hand):
     
        E.reset()  

        cards = hand.cards + hand.shared_cards
        cards.sort(key=lambda card: (card.number, card.suit))


        straight_flush_constraint(E, hand)
        three_of_a_kind_constraint(E, hand)
        straight_constraint(E, hand)
        flush_constraint(E, hand)
        two_pair_constraint(E, hand)
        pair_constraint(E, hand)
        high_card_constraint(E, hand)

 
        solution = solve(E)

        if SF in solution:
            hand.SF = True
            hand.rank = "Straight flush"
            return True
        elif TK in solution:
            hand.TK = True
            hand.rank = "Three of a kind"
            return True
        elif S in solution:
            hand.S = True
            hand.rank = "Straight"
            return True
        elif FL in solution:
            hand.SF = True
            hand.rank = "Flush"
            return True
        elif TP in solution:
            hand.TK = True
            hand.rank = "Two-Pair"
            return True
        elif P in solution:
            hand.S = True
            hand.rank = "Pair"
            return True
        elif HC in solution:
            hand.S = True
            hand.rank = "High-Card"
            return True
 

        return False  


    handRanking2()











""" FUNCTION: HANDRANKING
    PARAMETER: HAND (FOUND IN MAIN)
    RETURNS: TRUE (FOR FOUND RANK)
    """
def handRanking(hand): 

    hand.HCR = hand.cards[2].number

    cards = hand.cards + hand.shared_cards
    cards.sort(key=lambda card: (card.number, card.suit))
    #print(cards)


    
#STRAIGHT FLUSH
    SF = [
            (cards[0].suit == cards[1].suit == cards[2].suit == cards[3].suit == cards[4].suit) &
            ((cards[0].number == cards[1].number - 1) & (cards[1].number == cards[2].number - 1) & (cards[2].number == cards[3].number - 1)) | 
            (cards[1].number == cards[2].number - 1) & (cards[2].number == cards[3].number - 1) & (cards[3].number == cards[4].number - 1) 
    ]
    if any(SF):
       # print('straight flush')
        hand.SF = True
        hand.rank = ("Straight flush")
        return True
    

#THREE OF A KIND
    TK = [
    ((cards[0].number == num) & (cards[1].number == num) & (cards[2].number == num)) |
     ((cards[1].number == num) & (cards[2].number == num) & (cards[3].number == num)) |
      ((cards[2].number == num) & (cards[3].number == num) & (cards[4].number == num)) 

    for num in NUMBERS
    ]

    if any(TK):
      #  print('three of a kind')
        hand.TK = True
        hand.rank = "Three of a kind"
        return True


#Straight | with 4 in a row | subject to change
    S = [
    ((cards[0].number == cards[1].number - 1) & (cards[1].number == cards[2].number - 1) &  (cards[2].number == cards[3].number - 1))|
    (cards[1].number == cards[2].number - 1) & (cards[2].number == cards[3].number - 1) &  (cards[3].number == cards[4].number - 1)
    ]

    if any(S):
      #  print('straight')
        hand.S = True
        hand.rank = "Straight"
        return True

#FLUSH
    FL = [
    (cards[0].suit == cards[1].suit == cards[2].suit == cards[3].suit)
     ]

    if any(FL):
       # print('flush')
        hand.FL = True
        hand.rank = "Flush"
        return True


# Two - Pair
    TP = [
    ((cards[0].number == cards[1].number) & (cards[2].number == cards[3].number)) |
    ((cards[0].number == cards[1].number) & (cards[3].number == cards[4].number)) |
    ((cards[1].number == cards[2].number) & (cards[3].number == cards[4].number)) |
    ((cards[2].number == cards[3].number) & (cards[4].number == cards[0].number))
    ]

    if any(TP):
       # print('two pair')
        hand.TP = True
        hand.rank = "Two pair"
        return True




#Pair       
    P = [
    ((cards[0].number == cards[1].number) | (cards[1].number == cards[2].number) | 
     (cards[2].number == cards[3].number) | (cards[3].number == cards[4].number))
    ]
    if any(P):
       # print('pair')
        hand.P = True
        hand.rank = "Pair"
        return True
    
#High card
    HC = [
        not hand.SF and not hand.TK and not hand.S and not hand.FL and not hand.TP and not hand.P
    ]
    if any(HC):
        #print("high card", hand.HCR)
        hand.HC = True
        hand.rank = ("high card of " + str(hand.HCR))
        return True

    

















""" FUNCTION: PLAY OR FOLD
    PARAMETER: HAND (FOUND IN MAIN)
    RETURNS: ...
    """
def playOrFold(hand): ##PLAY OR FOLD RECOMMENDATIONS

    hand.RP = not hand.HC
    if (hand.RP):
        return True
    
    hand.RP = not((not hand.SF and not hand.FL and not hand.TK and not hand.S and not hand.TP and not hand.P))
    if(not hand.RP):
        return True
    
    
    
   
"""" FUNCTION: MODEL ACCURACY TESTER
     PARAMETER: 
"""
"""
def modelAccuracyTester():
    userCorrect = 0
    totalGames = 0 
    modelCorrect = 0
    playAgain = True

    print()
    print("Calculating accuracy... Please wait a few seconds")

    for int in range(100000):

        # order should go as follows: 

        # user sees cards. 
        # user sees table cards
        # play or fold function runs. 
        # user decides 
        # user sees dealers cards
        # win determined
        # result shown

        totalGames += 1

        deck = [Card(num,suit) for num in NUMBERS for suit in SUITS]
        shared_cards = dealCards(deck)
        shared_cards.pop(0) #burn first card



        cards1 = dealCards(deck)    
        hand1 = Hand(cards1,shared_cards)
        cards2 = dealCards(deck)
        hand2 = Hand(cards2,shared_cards)

        handRanking(hand1)
        handRanking(hand2)

     
        playOrFold(hand1)


        determineWinner(hand1,hand2)



        if ((hand1.win == True) and (hand1.RP)):
            modelCorrect += 1
        elif ((hand1.win == False) and (hand1.RP)):
            pass
        elif((hand1.win == True) and (not hand1.RP)):
            pass
        else:
            modelCorrect += 1
    

    modelAccuracy = (modelCorrect / totalGames) * 100
    print("Our models decision accuracy is", round(modelAccuracy, 2), "%, for 100,000 rounds")

    """










""" FUNCTION: DETERMINE WINNER
    PARAMETER: HAND1, HAND2 (FOUND IN MAIN)
    RETURNS: TRUE (FOR WINNING RANK)
    """   
def determineWinner(hand1, hand2):

    #HCC (High card comparator) will evaluate to true for the hand with the better high card
    cards1 = hand1.cards
    cards2 = hand2.cards

    if (hand1.HCR > hand2.HCR):
        hand1.HCC = True
    else:       
        hand2.HCC = True
        

    
    #USER HAS A STRAIGHT FLUSH, DEALER DOES NOT
    win = (hand1.SF and not hand2.SF)
    if (win):
        hand1.win = True
        return True
    
    #USER AND DEALER HAVE A STRAIGHT FLUSH
    win = (hand1.SF and hand2.SF and hand1.HCC)
    if (win):
        hand1.win = True
        return True
        
    
    #hand1.win = hand1.SF and not hand2.SF  
   
    #USER HAS THREE OF A KIND
    win = (hand1.TK and not hand2.SF and not hand2.TK)
    if (win):
        hand1.win = True
        return True
  
    #USER AND DEALER HAVE THREE OF A KIND
    win = (hand1.TK and hand2.TK and hand1.HCC)
    if (win):
        hand1.win = True
        return True
  


    #USER HAS A STRAIGHT
    win = (hand1.S and not hand2.SF and not hand2.TK and not hand2.S)
    if (win):
        hand1.win = True
        return True
    
    #USER AND DEALER HAVE A STRAIGHT
    win = (hand1.S and hand2.S and hand1.HCC)
    if (win):
        hand1.win = True
        return True



    #USER HAS FLUSH
    win = (hand1.FL and not hand2.SF and not hand2.TK)
    if (win):
        hand1.win = True
        return True

    #USER AND DEALER HAVE A FLUSH
    win = (hand1.FL and hand2.FL and hand1.HCC)
    if (win):
        hand1.win = True
        return True
    

    #USER HAS 2-PAIR    
    win = (hand1.TP and not hand2.SF and not hand2.TK and not hand2.S and not hand2.FL and not hand2.TP)
    if (win):
        hand1.win = True
        return True
    #hand1.win = (hand1.S and not hand2.SF and not hand2.TK and not hand2.S) 

    #BOTH PLAYERS HAVE A 2 PAIR
    win = (hand1.TP and hand2.TP and hand1.HCC)
    if (win):
        hand1.win = True
        return True
   

    #USER HAS A PAIR
    win = (hand1.P and not hand2.SF and not hand2.TK and not hand2.S and not hand2.P and not hand2.FL and not hand2.TP)
    if (win):
        hand1.win = True
        return True
    
    #BOTH PLAYERS HAVE A PAIR
    win = (hand1.P and hand2.P and hand1.HCC)
    if (win):
        hand1.win = True
        return True
    
    #HIGH CARD AND FIRST PLAYER HAS BETTER HIGHCARD
    win = (hand1.HC and hand2.HC and hand1.HCC)
    if (win):
        hand1.win = True
        return True
    
    #HIGH CARD AND SECOND PLAYER HAS BETTER HIGHCARD
    win = (hand1.HC and hand2.HC and not hand1.HCC)
    if (win):
        hand1.win = False


    #HC = (not hand1.P and not hand2.SF and not hand2.TK and not hand2.S and not hand2.P and not hand2.FL and not hand2.TP)
    #if (HC):
    #    hand1.HC = True #setting hand HC to true 
    #    cards1 = hand1.cards
    #    cards2 = hand2.cards
    #    hc1 = cards1[2]
    #    hc2 = cards2[2]
    #    print(hc1)
    #    print(hc2)
    #    if (hand1.cards[2].number > hand2.cards[2].number):
    #            hand1.win = True
    #            return True
    #    else:
    #           hand2.win = True
    #            return True


    #If the first player does not win, then this implies that the second player wins
    if (hand1.win == False):
        hand2.win = True
        return True
    













def test_hand_ranking():
    deck = [Card(num, suit) for num in NUMBERS for suit in SUITS]
    shared_cards = dealCards(deck)
    shared_cards.pop(0)  # burn first card

    cards = dealCards(deck)
    hand = Hand(cards, shared_cards)

    print("User Cards:", hand.cards)
    print("Table Cards:", shared_cards)

    handRanking(hand)

    print("Hand Category:", hand.rank)
    print("SF:", hand.SF, "TK:", hand.TK, "S:", hand.S, "FL:", hand.FL, "TP:", hand.TP, "P:", hand.P, "HC:", hand.HC)

test_hand_ranking()

    
    


   
def main():
    example_theory
    test_hand_ranking()


























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