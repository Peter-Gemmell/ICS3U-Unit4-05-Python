#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on March 2022
# This program calculates is a sum of all positive integers


def main():
    # This is a sum of all positive integers
    integer = 0
    total = 0

    # input
    user_number = input("Enter number of times looped : ")

    # process & output
    try:
        user_input = int(user_number)
        if user_input < 0:
            print("Invalid Input, please try again")
        else:
            for integer in range(user_input):
                user_number = input("Enter another number!: ")
                user_input = int(user_number)
                if user_input < 0:
                    continue
                total = total + user_input
                print("The sum is {0}.".format(total))
    except Exception:
        print("\nThat was not an integer.")


if __name__ == "__main__":
    main()
