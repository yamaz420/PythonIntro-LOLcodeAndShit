from deck import Deck
from player import Player

#del1
##1
deck = Deck()

##2
slim = Player("Slim")
Luke = Player("Luke")
print(slim)

##5
for i in range(5):
    slim.hand.append(deck.give_card())
    Luke.hand.append(deck.give_card())

##6
deck.cards_left()
print(slim)
print(Luke)

#del 3
trashpile = []
for i in range(2):
    trashpile.append(slim.throw_card())
    trashpile.append(Luke.throw_card())

##8
for i in range(2):
    slim.hand.append(deck.give_card())
    Luke.hand.append(deck.give_card())

##9
print()
deck.cards_left()
slim.reveal_hand()
Luke.reveal_hand()

#del 4
##10
def throw_all(self):
    thrown_cards = []
    thrown_cards += self.hand
    self.cards.clear()
    return thrown_cards

trashpile += slim.throw_all()
trashpile += Luke.throw_all()

##11
deck += trashpile
trashpile.clear()
slim.reveal_hand()
Luke.reveal_hand()
print("trashpile: ", len(trashpile))
deck.cards_left()

##12
deck.shuffle()
deck.reveal()
