#!/usr/bin/env python3
"""
Script Name: read_multiple_lines.py
Description: 
    This script reads multiple lines of input from the user until EOF (Ctrl + D) is pressed.
Usage:
    Input string mode
        $ python3 read_multiple_lines.py                # Read function: input()
        $ python3 read_multiple_lines.py --sys          # Read function: sys.stdin.read()
    Fixed string mode
        $ python3 read_multiple_lines.py --fixed        # Read function: input()
        $ python3 read_multiple_lines.py --fixed --sys  # Read function: sys.stdin.read()

Author: tatsujin
Date: 2024-07-20
"""

import sys

FIXED_LINES_STR = 'Dog barks "woof!".\nCat jumps high.\nPenguin dives into the sea.'


def show_usage_with_sys_func():
    print("\n[Usage]")
    print('Input "string1" + Press Enter')
    print('Input "string2" + Press Enter')
    print("...")
    print('Finally, Press "Ctrl + D" (EOF)')
    print("\n[Input]")
    print("Please input lines:")


def show_usage_with_input_func():
    print("\n[Usage]")
    print('Input "string1" + Press Enter')
    print('Input "string2" + Press Enter')
    print("...")
    print("Finally, No input + Press Enter")
    print("\n[Input]")
    print("Please input lines:")


def read_lines_with_sys_func(fixed_mode):
    print("\nSet read function: sys.stdin.read()")
    if fixed_mode:
        input_lines_str = FIXED_LINES_STR
    else:
        show_usage_with_sys_func()
        # Read multiple lines up to the EOF delimiter, and trim whitespace from both ends
        input_lines_str = sys.stdin.read().strip()

    # Get each line up to the LF delimiter as list type
    lines_list = input_lines_str.split("\n")
    return lines_list


def read_lines_with_input_func(fixed_mode):
    print("\nSet read function: input()")
    if fixed_mode:
        lines_list = FIXED_LINES_STR.split("\n")
    else:
        show_usage_with_input_func()
        lines_list = []
        while True:
            # Read a single line and trim whitespace from both ends
            line = input().strip()
            if line == "":  # Break on empty line
                break
            lines_list.append(line)
    return lines_list


def show_lines(lines_list):
    print("\n[Result]")
    print(type(lines_list), lines_list)
    print(f"Number of input lines: {len(lines_list)}\n")

    # Print each line string with line number
    for i, line_str in enumerate(lines_list, start=1):
        print(f"line{i}: {line_str}")


if __name__ == "__main__":
    # Parse command arguments
    fixed_mode = "--fixed" in sys.argv
    sys_func_enabled = "--sys" in sys.argv
    if sys_func_enabled:
        # Read lines with sys.stdin.read()
        lines_list = read_lines_with_sys_func(fixed_mode)
    else:
        # Read lines with input()
        lines_list = read_lines_with_input_func(fixed_mode)
    # Show lines
    show_lines(lines_list)
