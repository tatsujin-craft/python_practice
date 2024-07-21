#!/usr/bin/env python3
"""
Script Name: list_comprehension.py
Description: 
    This script calculates minimum value with list comprehension.
Usage:
    $ python3 list_comprehension.py

Input:
    n_1 + Enter
    n_2 + Enter
    ...
    Ctrl + D

Author: tatsujin
Date: 2024-07-21
"""

import sys


def get_min_value(input_enabled):
    if input_enabled:
        num_list_str = sys.stdin.read().strip()
    else:
        num_list_str = "10\n20\n30\n40\n50"

    # Create integer list from string
    num_list = [int(num) for num in num_list_str.split("\n")]
    print(num_list)
    min_val = min(num_list)
    print(min_val)


if __name__ == "__main__":
    input_enabled = False
    get_min_value(input_enabled)
