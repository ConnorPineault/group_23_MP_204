import random
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# These two lines make sure a faster SAT solver is used.
from nnf import config
config.sat_backend = "kissat"

# Encoding that will store all of your constraints
E = Encoding()

SUITS = ['S', 'C', 'D', 'H']  # Spades, Clubs, Diamonds, Hearts
NUMBERS = list(range(2, 15))  # 2 to 14, where 11=Jack, 12=Queen, 13=King, 14=Ace





""" DEAL CARDS(): CREATES DECK | SHUFFLES | DEALS | AND PUTS CARDS BACK | """

"""ABILITY TO INITIATE A SECOND PLAYER IF NEEDED"""
def dealCards():


    deck = [Card(player,num,suit) for player in ['U', 'D','CPU']for num in NUMBERS for suit in SUITS]
    
    random.shuffle(deck)
    u_hand = set()
    d_hand = set()
    # cpu_hand = set()

    while len(u_hand) < 3 and deck:
        card = deck.pop()
        if card.player == 'U' and card not in d_hand and card not in u_hand and card not in cpu_hand: 
            u_hand.add(card)

    while len(d_hand) < 3 and deck:
        card = deck.pop()
        if card.player == 'D' and card not in d_hand and card not in u_hand and card not in cpu_hand: 
            d_hand.add(card)

   # while len(cpu_hand) < 3 and deck:
        # card = deck.pop()
        # if card.player == 'CPU' and card not in d_hand and card not in u_hand and card not in cpu_hand: 
            # cpu_hand.add(card)
        

    u_hand_sorted = sorted(u_hand, key=lambda card: (card.number, card.suit)) #SORTED!!
    d_hand_sorted = sorted(d_hand, key=lambda card: (card.number, card.suit))
    # cpu_hand_sorted = sorted(cpu_hand, key=lambda card: (card.number, card.suit))


    print("USER:")
    for card in u_hand_sorted:
        print(f"{card.number}, Of {card.suit}")
    print("DEAL:")
    for card in d_hand_sorted:
        print(f"{card.number}, Of {card.suit}")
    # print("CPU:")
    # for card in cpu_hand_sorted:
        # print(f"{card.number}, Of {card.suit}")

    
    """option to put cards back into deck when/if playing multiple rounds"""
    #put cards back
    # for card in u_hand:
        # deck.append(card)
    # for card in d_hand:
        # deck.append(card)
    # for card in cpu_hand:
        # deck.append(card)
    




# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class Card:

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __repr__(self):
        return f"{self.player}.{self.number}.{self.suit}" #in english 8 of hearts, not heart 8: changed for readability
    






# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
#@constraint.at_least_one(E)
#@proposition(E)
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

# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
##DETERMINE HAND RANKINGS

    #Straight Flush for user
    for i in range(2, 13):  # Loop through numbers 2 to 12 for the start of a straight
        for suit in SUITS:
            E.add_constraint(
                Card( i, suit) & Card(i+1, suit) & Card(i+2, suit)
            )

    #Straight for user
    for i in range(2, 13):  # Loop through numbers 2 to 12 for the start of a straight
        straight_conditions = []
        for suit1 in SUITS:
            for suit2 in SUITS:
                for suit3 in SUITS:
                    straight_conditions.append(
                        Card(i, suit1) & Card(i+1, suit2) & Card(i+2, suit3)
                    )
        # Add a constraint that at least one of the straight conditions must be met
        # Bauhaus encoding means that sum checks through each proposition in the list
        # So if one proposition in list is correct it returns as true
        E.add_constraint(sum(straight_conditions))

    #High card for user
    high_card_constraints = []
    #We iterate over the numbers starting from the highest (Ace)
    #Then go down to the lowest to find the high card for the user and dealer.
    for num in reversed(NUMBERS):
        user_high_card_conditions = []
        dealer_not_higher_card_conditions = []

        for suit in SUITS:
            # User high card condition for a specific suit
            user_high_card_conditions.append(Card(num, suit))

            # Dealer not having this card or any higher card for all suits
            for any_suit in SUITS:
                dealer_not_higher_card_conditions.append(~Card(num, any_suit))
            for higher in NUMBERS:
                if higher > num:  # Only consider cards that are of higher rank
                    for any_suit in SUITS:
                        dealer_not_higher_card_conditions.append(~Card(higher, any_suit))

    # The user has a high card, and the dealer does not have this or any higher card
    high_card_constraint = sum(user_high_card_conditions) & sum(dealer_not_higher_card_conditions)
    high_card_constraints.append(high_card_constraint)
    
    # If no better hand we then compare high cards
    # Need to add the constraints for pair then high card if pair is same, same for straight, flush and straight flush, and if they have same high card (different suit)
    # Also need to account for ties depending on what cards they have
    if_no_better_hand = (...)  # We need to add a condition that ensures no better hand is present for either user or the dealer
    E.add_constraint(if_no_better_hand >> sum(high_card_constraints))


    


 #Three of a kind
    for num in NUMBERS:
        E.add_constraint(                               #ADD ~SF AND ONCE HAND RANKINGS HAVE PROPOSITION
            Card(14, suit) & Card(14, suit) & Card(14, suit) |
            Card(13, suit) & Card(13, suit) & Card(13, suit) |
            Card(12, suit) & Card(12, suit) & Card(12, suit) |
            Card(11, suit) & Card(11, suit) & Card(11, suit) |
            Card(10, suit) & Card(10, suit) & Card(10, suit) |
            Card(9, suit) & Card(9, suit) & Card(9, suit) |
            Card(8, suit) & Card(8, suit) & Card(8, suit) |
            Card(7, suit) & Card(7, suit) & Card(7, suit) |
            Card(6, suit) & Card(6, suit) & Card(6, suit) |
            Card(5, suit) & Card(5, suit) & Card(5, suit) |
            Card(4, suit) & Card(4, suit) & Card(4, suit) |
            Card(3, suit) & Card(3, suit) & Card(3, suit) |
            Card(2, suit) & Card(2, suit) & Card(2, suit)
        )

    #Flush
    for suit in SUITS:
        E.add_constraint(                               #ADD ~SF AND ~T ONCE HAND RANKINGS HAVE PROPOSITION
            Card(num, 'S') & Card(num, 'S') & Card(num, 'S') |         #Three spades
            Card(num, 'C') & Card(num, 'C') & Card(num,'C') |         #Three clubs
            Card(num, 'D') & Card(num, 'D') & Card(num, 'D') |         #Three diamonds
            Card(num, 'H') & Card(num, 'H') & Card(num, 'H')           #Three hearts
        )

    

    #Pair       
    for num in NUMBERS:                 #ORDER THE CARDS, SO MIDDLE IS ALWAYS PAIR, CHECK NOT ANY HIGEHR RANKINGS
        E.add_constraint(
            Card(num, suit) & Card(num, suit) & ~Card(num, suit) |    #NOT SURE WHERE TO PUT NEGATION
            ~Card(num, suit) & Card(num, suit) & Card(num, suit)
        )



    ##PLAY OR FOLD RECOMMENDATIONS

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
  #          q64_conditions.append(condition)
   # E.add_constraint(sum(q64_conditions))

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


if __name__ == "__main__":

    dealCards()

    


        
    

    



   # T = example_theory()
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
