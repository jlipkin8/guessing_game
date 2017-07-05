"""A number-guessing game."""

import random

name = raw_input("Hey! What's your name? ")
print "%s, I'm thinking of a number between 1 and 100.\nTry to guess my number." % (name)

random_number = random.randint(1, 100)
count = 0

while True:
    number_guess = int(raw_input("Your guess? "))
    if number_guess != random_number:
        count += 1
        if number_guess < random_number:
            print "Your guess is too low, try again."
        else:
            print "Your guess is too high, try again."
    else:
        count += 1
        print "Congrats! You guessed correctly, after %d guesses." % (count)
        break
