import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:
    def __init__(self):
        self.deck = []
        
        for suit in suits:
            for rank in ranks:
                # Create the Card object
                createdCard = Card(suit,rank)
                
                self.deck.append(createdCard)
    
    def __str__(self):
        return f'This deck has {len(self.deck)} cards'
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand():
    def __init__(self):
            self.cards = []  # start with an empty list as we did in the Deck class
            self.value = 0   # start with zero value
            self.aces = 0    # add an attribute to keep track of aces
        
    def addCard(self,card):
        self.cards.append(card)
        self.value += card.value
        if card.value == 11:
            self.aces += 1
        
    def adjustForAce(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
    
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def winBet(self):
        self.total += self.bet     
        
    def loseBet(self):
        self.total -= self.bet
    
def takeBet():
    playerBet = 0
    
    while True:
        try:
            playerBet = int(input('Enter an amount to bet: '))
        except ValueError:
            print('Enter a number!')
            continue
        else:
            return playerBet

def hit(deck,hand):
    
    hand.addCard(deck.deal())


def hitOrStand(deck,hand):
    global playing  # to control an upcoming while loop
    
    playerInput = ''
    
    while playerInput != 'hit' and playerInput != 'stand':
        playerInput = input('Hit or stand: ').lower()

        if playerInput != 'hit' and playerInput != 'stand':
            print('Please type "hit" or "stand"')
    
    if playerInput == 'stand':
        playing = False

    else:
        hit(deck,hand)

def showSome(player,dealer):
    print(f"Dealer's second card:\n{dealer.cards[1]}")
    
    print("Your cards:")
    for i in range(0,len(player.cards)):
        print(player.cards[i])
        i += 1
    
def showAll(player,dealer):
    print("Dealer's cards:")
    for i in range(0,len(dealer.cards)):
        print(dealer.cards[i])
        i += 1
        
    print("Your cards:")
    for i in range(0,len(player.cards)):
        print(player.cards[i])
        i += 1

def playerBusts():
    print("You have busted!")

def playerWins():
    print("You have won!")

def dealerBusts():
    print("Dealer has busted! You win!")
    
def dealerWins():
    print("Dealer has won!")
    
def push():
    print("It's a tie!")

def game():
    playerChips = Chips()

    global playing

    while True:
    
        print("Welcome to Blackjack!")

        print("Initializing deck...")
        newDeck = Deck()
        newDeck.shuffle()
        print("Deck initialized...")
        
        while True:
            if playerChips.total > 0:
                playerChips.bet = takeBet()
                if playerChips.total >= playerChips.bet:
                    break
                else:
                    print(f'Please enter a bet less than or equal to {playerChips.total}')
            else:
                print("You do not have enough money!")
                return
            
        print("Initializing player's hand...")
        player = Hand()
        print("Initializing dealer's hand...")
        dealer = Hand()
        
        
        print("Dealing 2 cards to player and dealer...")
        for i in range (0, 2):
            dealer.addCard(newDeck.deal())
            player.addCard(newDeck.deal())
            i += 1
        print("Cards have been dealt...")
            
        showSome(player,dealer)
        print(f"Your current card values: {player.value}")

        while playing:
            print(f"Your current card values: {player.value}")
            hitOrStand(newDeck,player)
            showSome(player,dealer)    
            if player.value > 21:
                if player.aces != 0:
                    player.adjustForAce()
                else:
                    playerBusts()
                    playerChips.loseBet()
                    break
            elif player.value == 21:
                break
        
        while dealer.value < 17:
            dealer.addCard(newDeck.deal())

        showAll(player,dealer)
        print(f"Your value: {player.value}, dealer value {dealer.value}")

        if dealer.value > player.value and dealer.value < 21:
            dealerWins()
            playerChips.loseBet()
        elif player.value > dealer.value and player.value < 21:
            playerWins()
            playerChips.winBet()
        elif player.value == 21:
            playerWins()
            playerChips.winBet()
        elif dealer.value > 21 and player.value < 21:
            dealerBusts()
            playerChips.winBet()
        elif player.value == 21 and dealer.value == 21:
            push()
        
        print(f"You have ${playerChips.total} left")
        playAgain = ''
        while playAgain.lower() != 'yes' and playAgain.lower() != 'no':
            playAgain = input("Play again? ")
            
        if playAgain.lower() == 'no':
            break
        else:
            playing = True
    
game()

