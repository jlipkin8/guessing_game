"""A number-guessing game."""

import random

name = raw_input("Hey! What's your name? ")
print "%s, I'm thinking of a number between 1 and 100.\nTry to guess my number." % (name)

random_number = random.randint(1, 100)
count = 0

while True:
    try:    
        number_guess = int(raw_input("Your guess? "))
        if number_guess != random_number:
            count += 1
            if number_guess < random_number:
                if number_guess < 0:
                    print "That is not a valid number. Please guess between 1 and 100."
                else:
                    print "Your guess is too low, try again."
            else:
                if number_guess > 100:
                    print "That is not a valid number. Please guess between 1 and 100."
                else:
                    print "Your guess is too high, try again."
        else:
            count += 1
            print "Congrats! You guessed correctly, after %d guesses." % (count)
            break
    except ValueError:
        print "Please enter a valid interger."
