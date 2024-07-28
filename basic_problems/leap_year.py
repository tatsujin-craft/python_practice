#!/usr/bin/env python3
"""
Script Name: leap_year.py
Description: 
    This script checks if a given year is a leap year based on the Gregorian calendar rules.
    Leap year definitions:
        - A year is a leap year if it is divisible by 4.
        - However, year divisible by 100 are not leap year.
        - However, year divisible by 400 are leap year.
Usage:
    $ python3 leap_year.py

Input:
    Enter a year as an integer.

Author: tatsujin
Date: 2024-07-27
"""

from colorama import Fore, Style


def is_leap_year(year):
    """
    Check if a given year is a leap year.

    Formula:
        - Leap year: year % 4 == 0
        - Not leap year: if year % 100 == 0, unless year % 400 == 0

    Args:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    year = int(input("Input a year and press Enter: "))
    if is_leap_year(year):
        print(Fore.GREEN + Style.BRIGHT + f"{year} is a leap year")
    else:
        print(Fore.RED + Style.BRIGHT + f"{year} is not a leap year")
