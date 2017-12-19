import random

print("\n ^^ -_-_-_-_-_-_-_ Welcome to Guess a Number _-_-_-_-_-_-_- ^^ ")


def game():
    # Generate random number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        try:
            # User guesses a number
            guess = int(input("\n               Guess a number between 1 and 10  "))
        except ValueError:
            print("{} isn't a number".format(guess))

        else:
            # Compare user guess to random module's guess
            if guess == secret_num:
                print("You got it! My the number was {} ".format(secret_num))
                break
            elif guess < secret_num:
                print("The secret number is higher than {}".format(guess))

            else:
                print("The secret number is lower than {}".format(guess))
            guesses.append(guess)

    else:
        print("You didn't get it! The secret number was {}".format(secret_num))
    play_again = input("\n Do you want to play again? Y/n ")
    if play_again.lower() != 'n':
            game()
    else:
        print("\n Goodbye!")
        break

game()


