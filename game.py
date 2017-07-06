"""A number-guessing game."""

import random

name = raw_input("Hey! What's your name? ")
print "%s, I'm thinking of a number between 1 and 100.\nTry to guess my number." % (name)

random_number = random.randint(1, 100)
count = 0

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
