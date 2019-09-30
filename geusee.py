#!usr/bin/env python

# Created by: Cameron Teed
# Created On: September 2019
# this program gets you to guess my number

import constant


def main():
    # this program gets you to guess my number

    # input
    secret_number = int(input("Guess my number:"))

    # process
    if secret_number == constant.NUMBER:

        # output
        print("you got it")


if __name__ == "__main__":
    main()
