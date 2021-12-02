import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}

# Card class - suit, rank, value
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:
    def __init__(self):
        self.allCards = []
        
        for suit in suits:
            for rank in ranks:
                # Create the Card object
                createdCard = Card(suit,rank)
                
                self.allCards.append(createdCard)
    
    def shuffle(self):
        random.shuffle(self.allCards)

    def dealOne(self):
        return self.allCards.pop()
                
class Player():

    def __init__(self,name):
        self.name = name
        self.allCards = []
        
    def removeOne(self):
        return self.allCards.pop(0)

    def addCard(self,newCards):
       if type(newCards) == type([]):
           self.allCards.extend(newCards)
       else:
           self.allCards.append(newCards) 
    
    def __str__(self):
        return f'Player {self.name} has {len(self.allCards)} cards.'

def game():
    player1 = Player('One')
    player2 = Player('Two')

    newDeck = Deck()
    newDeck.shuffle()

    for x in range(26):
        player1.addCard(newDeck.dealOne())
        player2.addCard(newDeck.dealOne())

    gameOn = True

    roundNo = 0

    while gameOn:
        roundNo += 1
        print(f'Currently on round {roundNo}')
        
        if len(player1.allCards) == 0:
            print(f'Player {player1.name} is out of cards! Player {player2.name} wins!')
            gameOn = False
            break
        
        if len(player2.allCards) == 0:
            print(f'Player {player2.name} is out of cards! Player {player1.name} wins!')
            gameOn = False
            break

        # Start a new round
        playerOneCards = []
        playerOneCards.append(player1.removeOne())

        playerTwoCards = []
        playerTwoCards.append(player2.removeOne())
        
        atWar = True
        
        while atWar:
            if playerOneCards[-1].value > playerTwoCards[-1].value:
                player1.addCard(playerOneCards)
                player1.addCard(playerTwoCards)

                atWar = False
                
            if playerOneCards[-1].value < playerTwoCards[-1].value:
                player2.addCard(playerOneCards)
                player2.addCard(playerTwoCards)

                atWar = False

            else:
                print('War!')
                
                if len(player1.allCards) < 5:
                    print(f'Player {player1.name} is unable to declare war')
                    print(f'Player {player2.name} wins!')
                    gameOn = False
                    break

                elif len(player2.allCards) < 5:
                    print(f'Player {player2.name} is unable to declare war')
                    print(f'Player {player1.name} wins!')
                    gameOn = False
                    break
                else:
                    for num in range(5):
                        playerOneCards.append(player1.removeOne())
                        playerTwoCards.append(player2.removeOne())

game()