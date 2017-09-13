"""A number-guessing game."""

import random

def play_game(): 
    random_number = random.randint(1, 100)
    count = 0
    print "I'm thinking of a number between 1 and 100.\nTry to guess my number." 

    while True:
        count += 1

        try:
            number_guess = int(raw_input("Your guess? "))

        except ValueError:
            print "Please enter a valid interger."
            continue

        if number_guess < 0 or number_guess > 100:
            print "That is not a valid number. Please guess between 1 and 100."
        elif number_guess < random_number:
            print "Your guess is too low, try again."
        elif number_guess > random_number:
            print "Your guess is too high, try again."
        else:
            print "Congrats! You guessed correctly, after %d guesses." % (count)
            break


name = raw_input("Hey! What's your name? ")
print "Hello {}, Want to play a guessing game? ".format(name)
user_input = raw_input("Enter Y for yes or N for no: ")

while user_input != "N": 
    play_game()
    print "Do you want to play another game?"
    user_input = raw_input("Enter Y for yes or N for no: ")

print "GOODBYE FOR NOw"