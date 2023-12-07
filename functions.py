import random
from classes import Hand, Card
from Num_Suits import NUMBERS, SUITS




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




def example_theory():







    



    """ FUNCTION: HANDRANKING
    PARAMETER: HAND (FOUND IN MAIN)
    RETURNS: TRUE (FOR FOUND RANK)
    """
def handRanking(hand): 

    # Add a constraint that at least one of the straight conditions must be met
    # Bauhaus encoding means that sum checks through each proposition in the list
    # So if one proposition in list is correct it returns as true

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

    hand.SP = not hand.HC
    if (hand.SP):
        return True
    
    hand.MP = ((not hand.SP) and (hand.HCR == 11 or hand.HCR == 12 or hand.HCR == 13 or hand.HCR == 14))
    if(hand.MP):
        return True
    
    hand.WP = (not hand.SP and not hand.MP)
    if(hand.WP):
        return True
    


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
    









