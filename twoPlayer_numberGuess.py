import random


def guessGame(a, b, actual):
    guess = int(input(f"Guess the number beetween {a} and {b} \n"))
    nguess = 1
    while guess != actual:

        if guess < actual:
            guess = int(input("Enter a Bigger number\n"))
            nguess += 1
        else:
            guess = int(input("Enter a Smaller number\n"))
            nguess += 1

    print(f"You guessed the number in {nguess} guesses\n")

    return nguess

try:
    if __name__ == "__main__":
        a = int(input("Enter the value of 1st number\n"))
        b = int(input("Enter the value of 2nd number\n"))

        actual1 = random.randint(a, b)
        print("Player 1's turn\n")
        g1 = guessGame(a, b, actual1)

        actual2 = random.randint(a, b)
        print("Player 2's turn\n")
        g2 = guessGame(a, b, actual2)

        if g1 < g2:
            print("Player 1 wins\n")
        elif g1 > g2:
            print("Player 2 wins\n")
        else:
            print("Its a tie!!\n")

        print(f"The number for player 1 was {actual1} and for player 2 was {actual2}")

except Exception as f:
    print("Please enter numbers only")
