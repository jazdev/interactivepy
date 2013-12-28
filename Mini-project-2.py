# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
number = 0
guesses = 7

# helper function to start and restart the game
def new_game():
    print("\nNEW GAME. \nRange is from 0 to " + str(num_range))
    print("Number of remaining guesses: " + str(guesses))
    print "Enter your guess."
    global number
    number = random.randrange(0, num_range)
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range, guesses
    num_range = 100
    guesses = 7
    new_game()   

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range, guesses
    num_range = 1000
    guesses = 10
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global guesses
    guesses -= 1
    print("\nPlayer guess was: " + guess)
    print("Number of remaining guesses: " + str(guesses))
    
    if int(guess) == number:
        print("Correct guess!")
        range100()
    elif int(guess) < number:
        print("Higher! Enter a higher number.")
    else:
        print("Lower! Enter a lower number.")
        
    if guesses == 0:
        print("\nYou ran out of guesses! The number was: " + str(number) + "\n")
        range100()
        pass
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess: ", input_guess , 200)

# call new_game and start frame
new_game()
f.start()

# always remember to check your completed program against the grading rubric
