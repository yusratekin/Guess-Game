import random

class StringGuessGame:
    def __init__(self):
        self.words = ["apple", "banana", "orange", "strawberry", "watermelon", "pineapple", "grapefruit"]
        self.secret_word = random.choice(self.words)
        self.guesses = []
        self.max_attempts = 6
        self.remaining_attempts = self.max_attempts
        self.play_game()

    def display_word(self):
        display = ""
        for letter in self.secret_word:
            if letter.lower() in self.guesses:
                display += letter + " "
            else:
                display += "_ "
        return display

    def play_game(self):
        print("Welcome to the String Guess Game!")
        print("Try to guess the secret word. It is a fruit name.")
        print("You have 6 attempts to guess the word.")

        while self.remaining_attempts > 0:
            print("\nSecret word:", self.display_word())
            print("Remaining attempts:", self.remaining_attempts)

            if "_" not in self.display_word():  # Eğer tüm harfler tahmin edildiyse
                print("Congratulations! You guessed the word correctly: '{}'".format(self.secret_word))
                break

            guess = input("Enter a letter or guess the whole word: ").lower()

            if guess == self.secret_word.lower():
                print("Congratulations! You guessed the word correctly: '{}'".format(self.secret_word))
                break
            elif guess in self.guesses:
                print("You already guessed that letter. Try again.")
                continue
            elif len(guess) == 1 and guess.isalpha():
                self.guesses.append(guess)
                if guess not in self.secret_word:
                    self.remaining_attempts -= 1
                    print("Incorrect guess!")
            else:
                print("Invalid input. Please enter a single letter or guess the whole word.")

        if "_" in self.display_word():  # Eğer tüm harfler tahmin edilmediyse
            print("\nOut of attempts! The secret word was '{}'".format(self.secret_word))

if __name__ == "__main__":
    game = StringGuessGame()



