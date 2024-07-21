#!/usr/bin/env python3
"""
Script Name: trim_string.py
Description: 
    This script demonstrates how to trim whitespace and specific characters from strings.
    It includes functions of strip(), rstrip(), lstrip(), replace(), repr()
Usage:
    $ python3 trim_string.py

Author: tatsujin
Date: 2024-07-20
"""


def trim_whitespace(text):
    """Trim whitespace from the strings."""
    print("\nOriginal text:", repr(text))

    # Trim whitespace from both ends
    trimmed_both = text.strip()
    print("Both trimmed whitespace:", repr(trimmed_both))

    # Trim all whitespace
    trimmed_all = text.replace(" ", "")
    print("All trimmed whitespace:", repr(trimmed_all))


def trim_target_character(text, trim_target):
    """Trim target character from the strings."""
    print("\nOriginal text:", repr(text))

    # Trim target character from both ends
    trimmed_both = text.strip(trim_target)
    print("Both trimmed:", repr(trimmed_both))

    # Trim target character from the right ends
    trimmed_right = text.rstrip(trim_target)
    print("Right trimmed:", repr(trimmed_right))

    # Trim target character from the left ends
    trimmed_left = text.lstrip(trim_target)
    print("Left trimmed:", repr(trimmed_left))


if __name__ == "__main__":
    text1 = "  Hello, World!  "
    trim_whitespace(text1)

    text2 = "xxHello, World!xx"
    trim_target_character(text2, "x")

    text3 = "\r\nHello, World!\r\n"
    trim_target_character(text3, "\r\n")
