class Word:
    def __init__(self, swedish_word, english_word):
        self.swedish_word = swedish_word.lower()
        self.english_word = english_word.lower()

    def get_swedish_word(self):
        return self.swedish_word

    def get_english_word(self):
        return self.english_word

    def to_string(self):
        return f"{self.swedish_word}, {self.english_word}"

    def verify_answer(self, english_guess):
        return self.english_word == english_guess.lower()

word = Word("bil", "car")
print(word.to_string())

