#!/usr/bin/env python3
"""
Script Name: fizz_buzz.py
Description: 
    This script output "FizzBuzz" if divisible by both 3 and 5, "Fizz" if divisible by 3 only, 
    "Buzz" if divisible by 5 only, for integers from 1 to 100,
Usage:
    $ python3 fizz_buzz.py

Author: tatsujin
Date: 2024-07-21
"""


def output_fizz_buzz():
    for i in range(1, 101):
        if ((i % 3) == 0) and ((i % 5) == 0):
            print("FizzBuzz")
        elif (i % 3) == 0:
            print("Fizz")
        elif (i % 5) == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    output_fizz_buzz()
