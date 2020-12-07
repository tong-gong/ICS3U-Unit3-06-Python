#!/usr/bin/env python3

# Created by Tong Gong
# Created time November 2020
# This is a  "Number Guessing Game" program.

import random


def main():
    # This is the function to play the "Number Guessing Game" program.

    random_number = random.randint(1, 10)   # a number between 1 and 10

    # Input
    userinput = input("Enter the number you guess:")
    print("")

    # Process & output
    try:
        userinput = int(userinput)
        if userinput == random_number:
            print("You guessed right")
        elif userinput > 10:
            print("You do not enter a number between 1-10")
        else:
            print("You are not right!")
    except Exception:
        print("It is not an integer")


if __name__ == "__main__":
    main()
