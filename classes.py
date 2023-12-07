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
        self.SP = False
        self.MP = False
        self.HCR = 0    #Variable to keep track of rank of high card of hand (no shared)
        self.rank = ""

    