import random
#from bauhaus import Encoding, proposition, constraint
#from bauhaus.utils import count_solutions, likelihood

# These two lines make sure a faster SAT solver is used.
#from nnf import config
#config.sat_backend = "kissat"

# Encoding that will store all of your constraints
#E = Encoding()

SUITS = ['S', 'C', 'D', 'H']  # Spades, Clubs, Diamonds, Hearts
NUMBERS = list(range(2, 15))  # 2 to 14, where 11=Jack, 12=Queen, 13=King, 14=Ace





""" DEAL CARDS(): CREATES DECK | SHUFFLES | DEALS | AND PUTS CARDS BACK | """
def dealCards():


    deck = [Card(player,num,suit) for player in ['U', 'D']for num in NUMBERS for suit in SUITS]
    
    random.shuffle(deck)
    u_hand = set()
    d_hand = set()

    while len(u_hand) < 3 and deck:
        card = deck.pop()
        if card.player == 'U' and card not in d_hand and card not in u_hand: 
            u_hand.add(card)

    while len(d_hand) < 3 and deck:
        card = deck.pop()
        if card.player == 'D' and card not in d_hand and card not in u_hand: 
            d_hand.add(card)
        

    u_hand_sorted = sorted(u_hand, key=lambda card: (card.number, card.suit)) #SORTED!!
    d_hand_sorted = sorted(d_hand, key=lambda card: (card.number, card.suit))


    print("USER:")
    for card in u_hand_sorted:
        print(f"{card.number}, Of {card.suit}")
    print("DEAL:")
    for card in d_hand_sorted:
        print(f"{card.number}, Of {card.suit}")

    
    """option to put cards back into deck when/if playing multiple rounds"""
    #put cards back
    # for card in u_hand:
        # deck.append(card)
    # for card in d_hand:
        # deck.append(card)
    




# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
#@proposition(E)
class Card:

    def __init__(self, player, number, suit):
        self.player = player
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
    #Straight Flush for user
    for i in range(2, 13):  # Loop through numbers 2 to 12 for the start of a straight
        for suit in SUITS:
            E.add_constraint(
                Card('U', i, suit) & Card('U', i+1, suit) & Card('U', i+2, suit)
            )

    #Straight for user
    for i in range(2, 13):  # Loop through numbers 2 to 12 for the start of a straight
        straight_conditions = []
        for suit1 in SUITS:
            for suit2 in SUITS:
                for suit3 in SUITS:
                    straight_conditions.append(
                        Card('U', i, suit1) & Card('U', i+1, suit2) & Card('U', i+2, suit3)
                    )
        # Add a constraint that at least one of the straight conditions must be met
        # Bauhaus encoding means that sum checks through each proposition in the list
        # So if one proposition in list is correct it returns as true
        E.add_constraint(sum(straight_conditions))

##DETERMINE HAND RANKINGS
 #Three of a kind
    for num in NUMBERS:
        E.add_constraint(                               #ADD ~SF AND ONCE HAND RANKINGS HAVE PROPOSITION
            Card('U', 14, suit) & Card('U', 14, suit) & Card('U', 14, suit) |
            Card('U', 13, suit) & Card('U', 13, suit) & Card('U', 13, suit) |
            Card('U', 12, suit) & Card('U', 12, suit) & Card('U', 12, suit) |
            Card('U', 11, suit) & Card('U', 11, suit) & Card('U', 11, suit) |
            Card('U', 10, suit) & Card('U', 10, suit) & Card('U', 10, suit) |
            Card('U', 9, suit) & Card('U', 9, suit) & Card('U', 9, suit) |
            Card('U', 8, suit) & Card('U', 8, suit) & Card('U', 8, suit) |
            Card('U', 7, suit) & Card('U', 7, suit) & Card('U', 7, suit) |
            Card('U', 6, suit) & Card('U', 6, suit) & Card('U', 6, suit) |
            Card('U', 5, suit) & Card('U', 5, suit) & Card('U', 5, suit) |
            Card('U', 4, suit) & Card('U', 4, suit) & Card('U', 4, suit) |
            Card('U', 3, suit) & Card('U', 3, suit) & Card('U', 3, suit) |
            Card('U', 2, suit) & Card('U', 2, suit) & Card('U', 2, suit)
        )

    #Flush
    for suit in SUITS:
        E.add_constraint(                               #ADD ~SF AND ~T ONCE HAND RANKINGS HAVE PROPOSITION
            Card('U', num, S) & Card('U', num, S) & Card('U', num, S) |         #Three spades
            Card('U', num, C) & Card('U', num, C) & Card('U', num, C) |         #Three clubs
            Card('U', num, D) & Card('U', num, D) & Card('U', num, D) |         #Three diamonds
            Card('U', num, H) & Card('U', num, H) & Card('U', num, H)           #Three hearts
        )

    

    #Pair       
    for num in NUMBERS:                 #ORDER THE CARDS, SO MIDDLE IS ALWAYS PAIR, CHECK NOT ANY HIGEHR RANKINGS
        E.add_constraint(
            Card('U', num, suit) & Card('U', num, suit) & ~Card('U', num, suit) |    #NOT SURE WHERE TO PUT NEGATION
            ~Card('U', num, suit) & Card('U', num, suit) & Card('U', num, suit)
        )



    ##PLAY OR FOLD RECOMMENDATIONS

    # High card is Ace or King for user
    for suit in SUITS:
        E.add_constraint(Card('U', 14, suit) | Card('U', 13, suit))

    #Hand is Queen-7 or better for user
    for suit in SUITS:
        for suit2 in SUITS:
            #condition = (
            E.add_constraint((Card('U', 14, suit) | Card('U', 13, suit) | Card('U', 12, suit))
                &
                (Card('U', 14, suit) | Card('U', 13, suit) | Card('U', 12, suit) |
                Card('U', 11, suit) | Card('U', 10, suit) | Card('U', 9, suit) |
                Card('U', 8, suit) | Card('U', 7, suit)) 
            )
  #          q64_conditions.append(condition)
   # E.add_constraint(sum(q64_conditions))

    # Hand is Queen-6-4 or better for user
    q64_conditions = []
    for suit1 in SUITS:
        for suit2 in SUITS:
            for suit3 in SUITS:
                condition = (
                Card('U', 12, suit1) &  # Queen
                (Card('U', 6, suit2) | Card('U', 7, suit2) | Card('U', 8, suit2) |
                    Card('U', 9, suit2) | Card('U', 10, suit2) | Card('U', 11, suit2) |
                    Card('U', 12, suit2) | Card('U', 13, suit2) | Card('U', 14, suit2)) 
                    &
                (Card('U', 4, suit3) | Card('U', 5, suit3) | Card('U', 6, suit3) |
                    Card('U', 7, suit3) | Card('U', 8, suit3) | Card('U', 9, suit3) |
                    Card('U', 10, suit3) | Card('U', 11, suit3) | Card('U', 12, suit3) |
                    Card('U', 13, suit3) | Card('U', 14, suit3))
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
