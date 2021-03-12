from card import Card
import random import shuffle

class Deck:
    values = (2,3,4,5,6,7,8,9,10,11,12,13,14)
    suites = ("Hearts", "Spades", "Diamonds", "Clubs" )
    names = ("Deuce", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

    def __init__(self):
        self.cards = []
        for suite in self.suites:
            for i  in range(len(self.values)):
                self.cards.append(Card(self.names[i], self.values[i], suite))

        self.shuffle()

    def shuffle(self):
        shuffle(seld.cards)

    def reveal(self):
        for card in self.cards:
            print(card)

    def give_card(self):
        return self.cards.pop()

    def cards_left(self):
        print(f"Cards left: {len(self.cards)}")

        
