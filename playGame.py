
import random
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from nnf import config
config.sat_backend = "kissat"
E = Encoding()
from functions import playOrFold, handRanking,determineWinner, dealCards, example_theory
from classes import Card, Hand
from Num_Suits import SUITS, NUMBERS





def main():
    print('playGame')
    correctDecisions = 0
    incorrectDecisions = 0 
    playAgain = True

    while(playAgain == True):

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
    
        handRanking(hand1)
        handRanking(hand2)

        print("You have a:", hand1.rank)
        playOrFold(hand1)

        if (hand1.SP):
            print("Recommendation: strong play")

        elif (hand1.MP):
         print("Recommendation: moderate play")

        elif (hand1.WP):
            print("Recommendation: weak play")

        playDecision = input("Enter 'P' to play, 'F' to fold: ").upper()
        while ((playDecision != 'P') and (playDecision != 'F')):
            playDecision = input("Enter 'P' to play, 'F' to fold: ").upper()
    
        print()
        print("The dealer had: ", hand2.cards, "which results in a", hand2.rank)

        determineWinner(hand1,hand2)


        if ((hand1.win == True) and (playDecision == 'P')):
            print("The user wins the round and the dealer loses!")
            print('You made the right decision :)')
            correctDecisions += 1
        elif ((hand1.win == False) and (playDecision == 'P')):
            print("The user loses the round and the dealer wins!")
            print("You made the wrong decision :(")
            incorrectDecisions += 1
        elif((hand1.win == True) and (playDecision == "F")):
            print("You folded so the dealer won, if you played you would have won!")
            print("You made the wrong decision :(")
            incorrectDecisions += 1
        else:
            print("You folded so the dealer won, if you played you would have lost!")
            print("You made the right decision :)")
            correctDecisions += 1
        
        print()
        totalGames = correctDecisions + incorrectDecisions
        print("You have played ", totalGames, "games")
        accuracy = correctDecisions / totalGames

        print("Your accuracy is", round(accuracy, 2), "%")
        print()
        qplay = (input("Enter 'y' to play again, any other key to exit: "))
        if (qplay == 'y'):
            print()
            print()
            playAgain = True
        else:
            playAgain = False



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