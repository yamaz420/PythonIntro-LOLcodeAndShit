import random
import re

# ----- START of variable declaration -----
# Tuple
words = (
    "boat",
    "car",
    "airplane",
    "bicycle",
    "scooter",
    "motorcycle",
    "train",
    "ship",
    "cruiser"
)

# Random.randint(start, stop), returns a random value between the start and end parameter, both are included.
secret_word = words[random.randint(0, len(words) - 1)] 
max_misses = 11
misses = 0
attempts = 0
public_word = re.sub("\D", "_", secret_word)
word_is_correct = False
used_letters = []
# ----- END of variable declaration -----


# ----- START of help function decl -----
def check_if_letter_is_already_guessed(letter):
    return letter in used_letters

def does_letter_exist(letter):
    return letter in secret_word

def get_indexes_of_letter(letter):
    indexes = []
    for index in range(len(secret_word)):
        if letter == secret_word[index]:
            indexes.append(index)
    return indexes

def replace_underscores_with_letter(letter):
    index = get_indexes_of_letter(letter)
    public_word_list = list(public_word)
    for index in indexes:
        public_word_list[index] = letter
    return "".join(public_word_list)

def guess_letter():
    guess = None
    regex = re.compile("[^a-zA-Z]")
    guess_again = True

    while guess_again:
        guess = input("type in your guess: ").lower()
        if check_if_letter_is_already_guessed(guess):
            print("the letter has already been guessed.")
        elif regex.search(guess) and len(guess) > 1:
            print("ERROR - you're only allowed to enter letters and ONE letter only")
        elif regex.search(guess):
            print("ERROR - only letters allowed.")
        elif len(guess) > 1:
            print("ERROR - only ONE letter allowed")
        else:
            guess_again = False
    used_letters.append(guess)
    return guess

def print_public_word():
    print(" ".join(list(public_word)))

def check_if_secret_word_is_complete():
    return secret_word == public_word
# ----- END of help function decl -----

# ----- START of program code ----------
print("Welcome to a game of hangman! The secret word has been set. Let's guess!")
print_public_word()

while not word_is_correct:
    if used_letters:
        print(f"Used letters: {used_letters}")
        print(f"{max_misses - misses} missed left til u are hung")

letter = guess_letter()
attempts += 1

if does_letter_exist(letter):
    print("HIT")
    public_word = replace_underscores_with_letter(letter)
    print_public_word()

    if check_if_secret_word_is_complete():
        print("GZ you have guessed the whole word")
        print(f"it took you {attempts} attempts to guess the secred word")
        word_is_correct = True

else:
    print("MISS")
    misses +=1
    if misses == max_misses:
        print("GAME OVER! you've been hanged")
        break


# ----- END of program code --------