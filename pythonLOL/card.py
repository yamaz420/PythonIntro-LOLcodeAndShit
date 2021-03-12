class Card:
    def __init__(self, name, value, suite):
        self.name = name
        self.value = value
        self.suite = suite

    def to_string(self):
        return(f"{self.name} of {self.suite}")


card = Card("Jack", 11, "Spades")
card.to_string()