"""A number-guessing game."""

import random

def play_game(): 
    start_range = int(user_input("Add a start range: "))
    end_range = int(user_input("Pick an end range: "))
    random_number = random.randint(start_range, end_range)
    count = 0
    print "I'm thinking of a number between {} and {}.\nTry to guess my number.".format(start_range, end_range) 

    while True:
        MAX_GUESS = 5
        count += 1

        if count >= 5: 
            print "Too many guess. This game will end."
            break

        try:
            number_guess = int(raw_input("Your guess? "))

        except ValueError:
            print "Please enter a valid interger."
            continue

        if number_guess < start_range or number_guess > end_range:
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