
import random
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from nnf import config

from functions import modelAccuracyTester
config.sat_backend = "kissat"
E = Encoding()
from functions import playOrFold, handRanking,determineWinner, dealCards, example_theory, playOrFold2,playOrFold3,modelAccuracyTester, home
from classes import Card, Hand
from Num_Suits import SUITS, NUMBERS


def main():


    userCorrect = 0
    totalGames = 0 
    modelCorrect = 0
    playAgain = True
    modelTest = False

    print("-------------------------------")
    print("Welcome")
    print()


    print("You have two options to explore this model:")

    home()




if __name__ == "__main__":
    main()

        
    

    


