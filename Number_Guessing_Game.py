import random
import time

class GuessingGame:
    def __init__(self):
        self.description = """
This game is about trying to guess a randomly selected 4-digit number by the computer.
If a digit is in the correct position and has the correct value, it will receive a '+' sign,
If a digit has the correct value but is in the wrong position, it will receive a '-' sign.
For example, if the computer's number is 1234 and you guess 1352, the output will be +1, -1.
You win the game when you correctly guess all the digits in the number.
        """
        self.play_game()

    def generate_number(self):
        return ''.join(random.sample('0123456789', 4))

    def count_bulls(self, guess, secret_number):
        return sum(1 for i in range(4) if guess[i] == secret_number[i])

    def count_cows(self, guess, secret_number):
        return sum(min(guess.count(digit), secret_number.count(digit)) for digit in set(guess))

    def play_game(self):
        secret_number = self.generate_number()
        attempts = 0

        print("4-Digit Number Guessing Game")
        print("-" * 30)
        print(self.description)
        print("-" * 30)

        while True:
            try:
                attempts += 1
                guess = input("Enter Your Guess (4-Digit Number): ")

                if not guess.isdigit() or len(guess) != 4:
                    raise ValueError("Invalid input! Please enter a 4-digit number.")

                bulls = self.count_bulls(guess, secret_number)
                cows = self.count_cows(guess, secret_number)

                if bulls == 4:
                    print(f"Congratulations! You found the correct number in {attempts} attempts: {secret_number}")
                    break
                else:
                    print(f"{bulls} +, {cows - bulls} -\n")
            except ValueError as ve:
                print(ve)

if __name__ == "__main__":
    game = GuessingGame()
    print("Closing the Program. Please Wait...")
    time.sleep(1)
