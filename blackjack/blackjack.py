#Simple BlackJack game

import random
bankroll = 50
bet = 0
dealerUpCard = 0
dealerDownCard = 0
dealerCardTotal = 0
userOneCard = 0
userTwoCard = 0
userCardTotal = 0


def betting():
    print("New hand! How much would you like to bet?")
    print("Current Bankroll: "+ str(bankroll))
    bet = 0
    bet = input()
    print("You have bet: $"+bet)
    print("Ready to be dealt?")
    dealt = input()
    if dealt == "yes" or "y":
        userOneCard = random.randint(1,11)
        userTwoCard = random.randint(1,11)
        userCardTotal = userOneCard + userTwoCard
        print("You have been dealt a " + str(userOneCard) + " and a " + str(userTwoCard))
        print("Your hand total is: " + str(userCardTotal))
        
    else:
        exit
    
    if userCardTotal >= 21:
        print("BUST!")
        exit
    else:
        dealerUpCard = random.randint(1,11)
        dealerDownCard = random.randint(1,11)
        dealerCardTotal = dealerUpCard + dealerDownCard
        print("The dealer has been dealt a " + str(dealerUpCard) + " for their face-up card")

    print("Hit or stay?")
    choice = input()

    if choice == "hit" or "h":
        newCard = random.randint(1,11)
        userCardTotal = userCardTotal + newCard
        print("You have been dealt a " + str(newCard) + ". Your hand total is: " + str(userCardTotal))
    else:  
        exit

print("Welcome to Blackjack, ready to play?")   
play = input()

if play == 'y' or play =='yes':
    betting()
else:
        print("Sorry you don't want to have fun")
        exit


