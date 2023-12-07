


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

    pass














""" FUNCTION: HANDRANKING
    PARAMETER: HAND (FOUND IN MAIN)
    RETURNS: TRUE (FOR FOUND RANK)
    """
def handRanking(hand): 

    # Add a constraint that at least one of the straight conditions must be met
    # Bauhaus encoding means that sum checks through each proposition in the list
    # So if one proposition in list is correct it returns as true
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
        print('straight flush')
        hand.SF = True
        return True
    

#THREE OF A KIND
    TK = [
    ((cards[0].number == num) & (cards[1].number == num) & (cards[2].number == num)) |
     ((cards[1].number == num) & (cards[2].number == num) & (cards[3].number == num)) |
      ((cards[2].number == num) & (cards[3].number == num) & (cards[4].number == num)) 

    for num in NUMBERS
    ]

    if any(TK):
        print('three of a kind')
        hand.TK = True
        return True


#Straight | with 4 in a row | subject to change
    S = [
    ((cards[0].number == cards[1].number - 1) & (cards[1].number == cards[2].number - 1) &  (cards[2].number == cards[3].number - 1))|
    (cards[1].number == cards[2].number - 1) & (cards[2].number == cards[3].number - 1) &  (cards[3].number == cards[4].number - 1)
    ]

    if any(S):
        print('straight')
        hand.S = True
        return True

#FLUSH
    FL = [
    (cards[0].suit == cards[1].suit == cards[2].suit == cards[3].suit)
     ]

    if any(FL):
        print('flush')
        hand.FL = True
        return True


# Two - Pair
    TP = [
    ((cards[0].number == cards[1].number) & (cards[2].number == cards[3].number)) |
    ((cards[0].number == cards[1].number) & (cards[3].number == cards[4].number)) |
    ((cards[1].number == cards[2].number) & (cards[3].number == cards[4].number)) |
    ((cards[2].number == cards[3].number) & (cards[4].number == cards[0].number))
    ]

    if any(TP):
        print('two pair')
        hand.TP = True
        return True




#Pair       
    P = [
    ((cards[0].number == cards[1].number) | (cards[1].number == cards[2].number) | 
     (cards[2].number == cards[3].number) | (cards[3].number == cards[4].number))
    ]
    if any(P):
        print('pair')
        hand.P = True
        return True
    
#High card
    HC = [
        not hand.SF and not hand.TK and not hand.S and not hand.FL and not hand.TP and not hand.P
    ]
    if any(HC):
        print("high card", cards[4].number)
        hand.HC = True
        return True

    

















""" FUNCTION: PLAY OR FOLD
    PARAMETER: HAND (FOUND IN MAIN)
    RETURNS: ...
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



















""" FUNCTION: DETERMINE WINNER
    PARAMETER: HAND1, HAND2 (FOUND IN MAIN)
    RETURNS: TRUE (FOR WINNING RANK)
    """   



def determineWinner(hand1, hand2):

    #HCC (High card comparator) will evaluate to true for the hand with the better high card
    cards1 = hand1.cards
    cards2 = hand2.cards
    print(hand1.cards[2].number)
    print(hand2.cards[2].number)
    #hc1 = cards1[2]
   # hc2 = cards2[2]
    if (hand1.cards[2].number > hand2.cards[2].number):
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
    













""" FUNCTION: DETERMINE WINNER
    PARAMETER: HAND1, HAND2 (FOUND IN MAIN)
    RETURNS: TRUE (FOR WINNING RANK)
    """
def main():





    # order should go as follows: 

    # user sees cards. 
    # user sees table cards
    # play or fold function runs. 
    # user decides 
    # user sees dealers cards
    # win determined
    # result shown

    deck = [Card(num,suit) for num in NUMBERS for suit in SUITS]
    shared_cards = dealCards(deck)
    shared_cards.pop(0) #burn first card



    cards1 = dealCards(deck)    
    hand1 = Hand(cards1,shared_cards)
    cards2 = dealCards(deck)
    hand2 = Hand(cards2,shared_cards)



    print("User Cards: ", cards1)
    # playOrFold()



    print("TABLE CARDS", shared_cards)
    
    print("Dealer Cards: ",cards2)
    handRanking(hand1)
    handRanking(hand2)

    
    determineWinner(hand1,hand2)

    if hand1.win == True:
        print("USER: WIN")
        print('DEALER: LOSE')
    else:
        print("USER: LOSE")
        print("DEALER: WIN")
        


    #print("USER: ", hand1.win)
    #print("DEALER: ", hand2.win)






    #print("Test!    Straight Flush: ", hand1.SF, ", Flush:", hand1.FL, ", Pair:", hand1.P, ", Three of:", hand1.TK, ", Straight:", hand1.S)
   # print("Test!    Straight Flush: ", hand1.SF, ", Flush:", hand2.FL, ", Pair:", hand2.P, ", Three of:", hand2.TK, ", Straight:", hand2.S)

    
    


   


























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