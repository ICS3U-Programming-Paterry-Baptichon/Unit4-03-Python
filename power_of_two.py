#!/usr/bin/env python3

# created by: Paterry Baptichon
# created on: 2022-04-26
# this program calculates the square of each integer from 0 to the
# number entered


def main():
    # this program calculates the square of each integer from 0 to the
    # number entered
    counter = 0
    integer_squared = 0

    # input of the user
    positive_number = input("Enter any positive integer please: ")
    print("\n", end="")

    # switching string to integer
    try:
        positive_number_int = int(positive_number)
    # calculation of the square of each number
        if positive_number_int > 0:
            print("The square of each number from 0 to {0} is:"
                  .format(positive_number))
            for counter in range(positive_number_int + 1):
                integer_squared = counter**2
                print("{0}²= {1}"
                      .format(counter, integer_squared))
    # tell user the input is negative
        else:
            print("{0} was not a positive integer. Enter an integer"
                  " above 0.".format(positive_number))
            print("\n", end="")
    # tell the user the input is invalid
    except Exception:
        print("{0} is not an integer. Please enter an integer."
              .format(positive_number))


if __name__ == "__main__":
    main()