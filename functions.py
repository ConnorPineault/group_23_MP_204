import random
from classes import Hand, Card
from Num_Suits import NUMBERS, SUITS




""" 
FUNCTION: DEAL CARDS
PARAMETER: DECK (FOUND IN MAIN)
RETURNS: U_HAND_SORTED (SORTED LIST OF 3 CARDS)
"""
def dealCards(deck):

    # Shuffle deck to randomize the order of cards
    random.shuffle(deck)
     # Initialize an empty set to hold the cards for user's hand
    u_hand = set()

    # Keep drawing cards from the deck until we have 3 unique cards then pop it out and add to user's hand
    while len(u_hand) < 3 and deck:
        card = deck.pop()
        u_hand.add(card)

    # Sort cards by number then suit
    u_hand_sorted = sorted(u_hand, key=lambda card: (card.number, card.suit)) #SORTED!!

    # Returns sorted hand
    return u_hand_sorted




def example_theory():




    pass


    



    """ FUNCTION: HANDRANKING
    PARAMETER: HAND (FOUND IN MAIN)
    RETURNS: TRUE (FOR FOUND RANK)
    """
def handRanking(hand): 

    # Assign the highest card rank (HCR) from the user's own cards to the hand.
    hand.HCR = hand.cards[2].number

    # Combine the user's cards and shared cards into one list
    cards = hand.cards + hand.shared_cards
    cards.sort(key=lambda card: (card.number, card.suit))

    
#STRAIGHT FLUSH
    # Check if all cards are of the same suit and in order.
    SF = [
            (cards[0].suit == cards[1].suit == cards[2].suit == cards[3].suit == cards[4].suit) &
            ((cards[0].number == cards[1].number - 1) & (cards[1].number == cards[2].number - 1) & (cards[2].number == cards[3].number - 1)) | 
            (cards[1].number == cards[2].number - 1) & (cards[2].number == cards[3].number - 1) & (cards[3].number == cards[4].number - 1) 
    ]
    # If the condition for SF is met, set hand.SF to True and update hand.rank
    if any(SF):
       # print('straight flush')
        hand.SF = True
        hand.rank = ("Straight flush")
        return True
    

#THREE OF A KIND
    # Iterate over each number in NUMBERS and check if there are any three consecutive cards with that number.
    TK = [
    ((cards[0].number == num) & (cards[1].number == num) & (cards[2].number == num)) |
     ((cards[1].number == num) & (cards[2].number == num) & (cards[3].number == num)) |
      ((cards[2].number == num) & (cards[3].number == num) & (cards[4].number == num)) 

    for num in NUMBERS
    ]
    # If the condition for TK is met, set hand.TK to True and update hand.rank
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
    # If the condition for S is met, set hand.S to True and update hand.rank
    if any(S):
      #  print('straight')
        hand.S = True
        hand.rank = "Straight"
        return True

#FLUSH
    FL = [
    (cards[0].suit == cards[1].suit == cards[2].suit == cards[3].suit)
     ]
    # If the condition for FL is met, set hand.FL to True and update hand.rank
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
    # If the condition for TP is met, set hand.TP to True and update hand.rank
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
    # If the condition for P is met, set hand.P to True and update hand.rank
    if any(P):
       # print('pair')
        hand.P = True
        hand.rank = "Pair"
        return True
    
#High card
    HC = [
        not hand.SF and not hand.TK and not hand.S and not hand.FL and not hand.TP and not hand.P
    ]
    # If the condition for HC is met, set hand.HC to True and update hand.rank
    if any(HC):
        #print("high card", hand.HCR)
        hand.HC = True
        hand.rank = ("high card of " + str(hand.HCR))
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
""" FUNCTION: PLAY OR FOLD 3
    PARAMETER: HAND (FOUND IN MAIN)
    RETURNS: ...
    """
def playOrFold3(hand, shared_cards): ##PLAY OR FOLD RECOMMENDATIONS

    hc5OrHigher = (hand.HCR == 14 or hand.HCR == 13 or hand.HCR == 12 or hand.HCR == 11 or hand.HCR == 10 or hand.HCR == 9 or hand.HCR == 8 or hand.HCR == 7 or hand.HCR == 6 or hand.HCR == 5)
    sharedDangerTK = shared_cards[0].number == shared_cards[1].number and not hand.TK
    sharedDangerS = (shared_cards[0].number == shared_cards[1].number + 1) and not hand.S             
    sharedDangerFL = (shared_cards[0].suit == shared_cards[1].suit) and not hand.FL

    hand.RP = (not hand.HC) and (hc5OrHigher) and (not sharedDangerTK or not hand.P) and (not sharedDangerS or not hand.P) and (not sharedDangerFL or not hand.P)

    if (hand.RP):
        return True
    else:
        hand.RP = False
        return True
""" FUNCTION: PLAY OR FOLD 2
    PARAMETER: HAND (FOUND IN MAIN)
    RETURNS: ...
    """
def playOrFold2(hand): ##PLAY OR FOLD RECOMMENDATIONS

    hand.RP = ((not hand.HC) and (hand.HCR == 14 or hand.HCR == 13
                or hand.HCR == 12 or hand.HCR == 11 or hand.HCR == 10
                or hand.HCR == 9 or hand.HCR == 8 or hand.HCR == 7
                or hand.HCR == 6 or hand.HCR == 5))
   
    if (hand.RP):
        return True
    else:
        hand.RP = False
        return True
""" FUNCTION: PLAY OR FOLD 1
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

def modelAccuracyTester(modelChoice):


    userCorrect = 0
    totalGames = 0 
    modelCorrect = 0
    playAgain = True

    print()
    print("Calculating accuracy... Please wait a few seconds")

    for int in range(100000):



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

     
        if (modelChoice == 1):
            playOrFold(hand1)
        elif (modelChoice == 2):
            playOrFold2(hand1)
        else:
            playOrFold3(hand1, shared_cards)

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

def home():
    

        userCorrect = 0
        totalGames = 0 
        modelCorrect = 0
        playAgain = True
        modelTest = False
        print()
        print()
        print("(1) Hand by Hand")
        print("(2) Model Runs 100,000 game instances.")
        print()
        print('-Reccomended to explore model with enlarged terminal for best expierence-')
        print()

        print("Select: 1 or 2: ")
        answer = int(input(": "))

        if answer == 1:
            playAgain = True
        else:
            playAgain = False
            modelTest = True




        while(playAgain == True):


        


            totalGames += 1

            deck = [Card(num,suit) for num in NUMBERS for suit in SUITS]
            shared_cards = dealCards(deck)
            shared_cards.pop(0) #burn first card



            cards1 = dealCards(deck)    
            hand1 = Hand(cards1,shared_cards)
            cards2 = dealCards(deck)
            hand2 = Hand(cards2,shared_cards)






            print("User Cards: ", cards1)




            print("TABLE CARDS", shared_cards)
        
            handRanking(hand1)
            handRanking(hand2)
            

            print("You have a:", hand1.rank)
            playOrFold(hand1)

            if (hand1.RP):
                print("Recommendation: Play")

            elif (not hand1.RP):
                print("Recommendation: Fold")
            print()

            playDecision = input("Enter 'P' to play, 'F' to fold: ").upper()
            while ((playDecision != 'P') and (playDecision != 'F')):
                playDecision = input("Enter 'P' to play, 'F' to fold: ").upper()
        
            print()
            print("The dealer had: ", hand2.cards, "which results in a", hand2.rank)

            determineWinner(hand1,hand2)

            print()
            print("Your decision:")
            if (hand1.win == True and playDecision == "P"):
                print("You decided to play and you won the round!")
                userCorrect += 1
            elif ((hand1.win == False) and (hand1.RP)):
                print("You decided to play and you lost the round!")
            elif ((hand1.win == True) and (not hand1.RP)):
                print("You decided to fold, but you would have won the round!")
            else:
                print("You decided to fold, and would have lost the round!")
                userCorrect += 1

            print()
            print("Our model:")
            if ((hand1.win == True) and (hand1.RP)):
                print("We recommended to play, the user would have won!")
                print('Our model made the right decision :)')
                modelCorrect += 1
            elif ((hand1.win == False) and (hand1.RP)):
                print("We recommended to play, the user would have lost!")
                print("Our model made the wrong decision :(")
            elif((hand1.win == True) and (not hand1.RP)):
                print("We recommended to fold, but your hand would have won.")
                print("Our model made the wrong decision :(")
            else:
                print("You folded so the dealer won, if you played you would have lost!")
                print("You made the right decision :)")
                modelCorrect += 1
            
            print()
            print("You have played", totalGames, "games")
            userAccuracy = userCorrect / totalGames
            modelAccuracy = modelCorrect / totalGames

            print("Your decision accuracy is", round(userAccuracy, 2), "%")
            print("Our models decision accuracy is", round(modelAccuracy, 2), "%")
            print()
            qplay = (input("Enter 'y' to play again, any other key to go home: ")).upper()
            if (qplay != 'Y'):
                print()
                print()
                playAgain = False
                home()
            else:
                playAgain = True



        
        while (modelTest == True):
            print("1: is the pair + model")
            print("2: is the pair + with high card 5 + model")
            print("3: is the pair plus + high card 5 + (avoids dangerous shared cards) model")
            modelNum = 0 
            while (modelNum != 1 and modelNum != 2 and modelNum != 3):
                modelNum = int(input("Enter model: (1|2|3): "))
    
            modelAccuracyTester(modelNum)

            testAgain = input("Enter 'y' to test again, any other key to exit: ").upper()
            if (testAgain != "Y"):
                modelTest = False
                home()
            else:
                modelTest = True







