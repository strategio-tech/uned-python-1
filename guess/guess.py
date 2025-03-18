import random

def main():
    guess_the_number()

def guess_the_number():
    # have a random number to guess
    number_to_guess = random.randint(1,100)
    # only allow 3 guesses (0,1,2)
    attempt = 0
    #Introduce the game
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    # track playing the game = true
    playing_game = True
    while playing_game:
        # get a guess
        guess = int(input("Enter your guess: "))
        if attempt == 2:
            # check to see if they have used all their guess, provide answer, end
            print(f"You ran out of guesses! The number was {number_to_guess}")
            break
        if guess < number_to_guess:
            # give hint if too low, number of attempts left
            print("Too low. Try again.")
            print(f"You have {2-attempt} left!")
        elif guess > number_to_guess:
            # give hint if too high, number of attempts left
            print("Too high. Try again.")
            print(f"You have {2-attempt} left!")
        else:
            # congratulate if guessed
            print(f"Congratulations! You guessed the number in {attempt} attempts!")
            break
        attempt += 1

main()
