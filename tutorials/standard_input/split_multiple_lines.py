#!/usr/bin/env python3
"""
Script Name: split_multiple_lines.py
Description: 
    This script splits lines with a delimiter of comma or space.
Usage:
    Input mode
        $ python3 split_multiple_lines.py
    Fixed mode
        $ python3 split_multiple_lines.py --fixed

Author: tatsujin
Date: 2024-07-20
"""

import sys

FIXED_LINES_STR = "penguin,dolphin,whale,orca\nlion,tiger,wolf,bear\napple,banana,orange"


def show_usage():
    print("[Usage]")
    print("example1 (comma delimiter): lion,tiger,wolf,bear")
    print("example2 (space delimiter): apple banana orange")
    print("\nPlease input a line and press Enter. Press Ctrl+D to end input lines.")


def read_multiple_lines(fixed_mode):
    if fixed_mode:
        input_lines_str = FIXED_LINES_STR
    else:
        show_usage()
        # Read multiple lines up to the EOF delimiter, and trim whitespace from both ends
        input_lines_str = sys.stdin.read().strip()
    return input_lines_str.split("\n")


def split_multiple_lines(input_lines):
    print("\n[Result]")
    for line in input_lines:
        if "," in line:
            split_str = line.split(",")
        else:
            split_str = line.split()
        print(type(split_str), split_str)
        for element in split_str:
            print(element)


if __name__ == "__main__":
    # Parse command arguments
    fixed_mode = len(sys.argv) > 1 and sys.argv[1] == "--fixed"
    # Read lines
    input_lines = read_multiple_lines(fixed_mode)
    # Split lines
    split_multiple_lines(input_lines)
