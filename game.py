"""A number-guessing game."""

import random

name = raw_input("Hey! What's your name? ")
print "%s, I'm thinking of a number between 1 and 100.\nTry to guess my number." % (name)

random_number = random.randint(1, 100)

while True:
    number_guess = int(raw_input("Your guess? "))
