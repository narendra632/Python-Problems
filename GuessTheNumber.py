
import pyttsx3
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

pyttsx3.speak("Welcome to the Number Game. Please enter, your name")

def Hello():
    user = input("Please enter your name\n")
    if user=="":
        Hello()
    else:
        print(f"Hello {user} - Guess the Number in 8 chances")
        pyttsx3.speak(f"hello {user}, Guess the number in 8 chances")


def letsGuess():
    number = random.randint(0,100)
    guess = 1
    while (guess <= 8):
        try:
            inputnumber = int(input("Guess between 1 to 100\n"))
            if inputnumber not in range(0,101):
                print("Your Guess is out of range")
                pyttsx3.speak("Your Guess is, out of range")
            elif inputnumber < number:
                print("you guessed low")
                pyttsx3.speak("you guessed low")
            elif inputnumber > number:
                print("you guessed high")    
                pyttsx3.speak("you guessed high")
            else:
                print("Hurray!!  You, won the game")
                pyttsx3.speak("Excellent work!! You won the game")
                print("you took ", guess, " number of guesses to Win")
                pyttsx3.speak(f"you took, {guess}, number of guesses to win")
                break
        except Exception as f:
            if guess<=7:
                print("Please enter numbers only.")
                pyttsx3.speak("Please enter numbers only.")
        print(8-guess, " number of guesses left\n")
        guess = guess+1

    if guess > 8:
        print("GAME OVER")
        pyttsx3.speak("You lost the game")
        print(f"The number was {number}\n")
        pyttsx3.speak(f"The number was {number}")

    print("Do you want to play again?")
    pyttsx3.speak("Do you want to play again?")
    PlayAgain()
        
def PlayAgain():
    again=input("Yes or no\n").lower()
    if again=="yes":
        pyttsx3.speak("Again guess the number in 8 chances")
        letsGuess()
    elif again=="no":
        print("THANKS FOR PLAYING")
        pyttsx3.speak("Thanks for playing, Hope you enjoyed.")
        exit()
    else:
        pyttsx3.speak("Type yes or no.")
        PlayAgain()

 
Hello()
letsGuess()

