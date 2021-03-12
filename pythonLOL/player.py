class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return f"{self.name}: {self.hand}. Points: {self.calculate_hand()}"

    def reveal_hand(self):
        hand = [card for card in self.hand]
        print(f"{self.name}: {hand}. Points: {self.calculate_hand()}")

    def calculate_hand(self):
        total_value = 0
        for card in self.hand:
            total_value += card.value
        return total_value

    def throw_card(self):
        return self.hand.pop()