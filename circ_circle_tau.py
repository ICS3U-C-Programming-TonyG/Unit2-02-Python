#!/usr/bin/env python3

# Created By: Tony G

# Date: 2025-02-28

# Calculates the circumference of a circle

import constants
import math

    # User input
def main():
    radius = float(input("what is your radius(cm): "))

    print("")
    # Calculates circumference
    circumference = print("Your circumference is(cm): {}".format(radius * constants.TAU))


if __name__ == "__main__":
    main()
