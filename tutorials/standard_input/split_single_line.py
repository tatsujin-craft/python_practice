#!/usr/bin/env python3
"""
Script Name: split_single_line.py
Description: 
    This script splits a line with a delimiter of comma or space.
Usage:
    Input string mode
        $ python3 read_multiple_lines.py                # Read function: input()
        $ python3 read_multiple_lines.py --sys          # Read function: sys.stdin.readline()
    Fixed string mode
        $ python3 read_multiple_lines.py --fixed        # Read function: input()
        $ python3 read_multiple_lines.py --fixed --sys  # Read function: sys.stdin.readline()

Author: tatsujin
Date: 2024-07-20
"""

import sys
from enum import Enum, auto

FIXED_LINE_STR = "penguin,dolphin,whale,orca"


class ReadFunction(Enum):
    SYS = auto()
    INPUT = auto()

    @property
    def reader(self):
        if self == ReadFunction.SYS:
            return sys.stdin.readline
        elif self == ReadFunction.INPUT:
            return input

    @property
    def name(self):
        if self == ReadFunction.SYS:
            return "sys.stdin.readline()"
        elif self == ReadFunction.INPUT:
            return "input()"


def show_usage(read_function):
    print("\n[Usage]")
    print("example1 (comma delimiter): lion,tiger,wolf,bear")
    print("example2 (space delimiter): apple banana orange")
    print("\nPlease input a line and press Enter:")


def read_single_line(fixed_mode, read_function):
    print(f"Set read function: {read_function.name}")
    if fixed_mode:
        input_line = FIXED_LINE_STR
    else:
        show_usage(read_function)
        # Read a single line and trim whitespace from both ends
        input_line = read_function.reader().strip()
    return input_line


def split_single_line(input_line):
    if "," in input_line:
        split_str = input_line.split(",")
    else:
        split_str = input_line.split()

    print("\n[Result]")
    print(type(split_str), split_str)
    for element in split_str:
        print(element)


if __name__ == "__main__":
    # Parse command arguments
    fixed_mode = "--fixed" in sys.argv
    # Set read function
    if "--sys" in sys.argv:
        read_function = ReadFunction.SYS
    else:
        read_function = ReadFunction.INPUT

    # Read single line
    input_line = read_single_line(fixed_mode, read_function)
    # Split single line
    split_single_line(input_line)
