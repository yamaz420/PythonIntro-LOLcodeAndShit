from utils import Utils


class VocabularyTrainingProgram:
    words = [
        Word("hus", "house")
        Word("bil", "car")
    ]

    def show_menu(self):
        choice = None
        while choice !=5:
        print(
            ''' 
            1. Add a new word
            2. Shuffle the words in the list
            3. Take the test
            4. show all the words
            5. Exit
            '''
        )

        choice = Utils.get_int_input("Enter your menu choice: ")

        if choice < 1 or choice > 5:
            print("Error: not a valid menu choice")
        elif choice != 5:
            # print(self.menu_switcher(str(choice)))
            # pass # invoke the corresponding method
            self.menu_switcher(str(choice))()
        else:
            print("Closing the game...")

    def menu_switcher(self, choice):
        switch = {
            "1": self.add_new_word, 
            "2": self.shuffle_words,
            "3": self.take_the_test,
            "4": self.show_all_words
        }
    return switch[choice]

    def add_new_word(self):
        swedish_word = Utils.get_string_input("Enter the swedish word: ")
        english_word = Utils.get_string_input("Enter english word: ")
        self.words.append(word(swedish_word, english_word))
        print()
        print("The new word has been added")

    def show_all_words(self):
        for word in self.words:
            print(word.to_string())

    def shuffle_words(self):
        shuffle(self.words)
        print("the words have been shuffeled")

    def take_the_test(self):
        points = 0
        max_failures = 3
        misses = 0
        for word in self.words:
            print()
            answer = Utils.get_string_input(f"What is the translation for {word.get_english_word()}?")
            if word.verify_answer(answer):
                points += len(word.get_english_word())
                print("CORRECT!")
            else:
                misses += 1
                print(f"WronG! The Correct answer is {word.get_english_word()}.")
                if misses = max_failures:
                    print()
                    print("GAME OVAH BIATCH, go practice nooooob")
    print()
    print(f"the test is ovah matey u focken focker fuuuuuuuuuuuuuuuuuuuck you got {points}")
