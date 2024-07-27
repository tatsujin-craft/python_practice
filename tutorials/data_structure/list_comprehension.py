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


def get_num_list(input_enabled):
    """
    Get a list of numbers from standard input or a fixed string.
    list comprehension is [formura(element) for element in iterable_object]

    Args:
        input_enabled (bool): Whether to use standard input.

    Returns:
        list: A list of numbers.
    """
    if input_enabled:
        num_list_str = sys.stdin.read().strip()
    else:
        num_list_str = "10\n20\n30\n40\n50"

    # Create integer list from string by list comprehension
    num_list = [int(num) for num in num_list_str.split("\n")]
    return num_list


def get_min_val(num_list):
    """
    Get the minimum value from a list of numbers.

    Formula:
        min_val = min([a_1, a_2, a_3, ..., a_n])

    Args:
        num_list (list): A list of numbers.

    Returns:
        int: The minimum value.
    """
    min_val = min(num_list)
    return min_val


def get_sum(num_list):
    """
    Get the sum of a list of numbers.

    Formula:
        sum_val = a_1 + a_2 + a_3 + ... + a_n

    Args:
        num_list (list): A list of numbers.

    Returns:
        int: The sum of the numbers.
    """
    sum_val = sum(num_list)
    return sum_val


def get_product_sum(num_list):
    """
    Get the product of a list of numbers.

    Formula:
        product_sum = a_1 * a_2 * a_3 * ... * a_n

    Args:
        num_list (list): A list of numbers.

    Returns:
        int: The product of the numbers.
    """
    product_sum = 1
    for num in num_list:
        product_sum *= num
    return product_sum


def get_squared_list(num_list):
    """
    Get a list of each element is the squared from the input list.

    Formula:
        squared_list = [a_1^2, a_2^2, ..., a_n^2]

    Args:
        num_list (list): A list of numbers.

    Returns:
        list: A list of squared numbers.
    """
    squared_list = [num**2 for num in num_list]
    return squared_list


def get_cumulative_sum_list(num_list):
    """
    Get a list of cumulative sums from the input list.

    Formula:
        cumulative_sum_list = [a_1, a_1+a_2, a_1+a_2+a_3, ...]

    Args:
        num_list (list): A list of numbers.

    Returns:
        list: A list of cumulative sums.
    """

    cumulative_sum_list = []
    current_sum = 0
    for num in num_list:
        current_sum += num
        cumulative_sum_list.append(current_sum)
    return cumulative_sum_list


if __name__ == "__main__":
    input_enabled = False
    num_list = get_num_list(input_enabled)
    print("Input list:", num_list)

    min_val = get_min_val(num_list)
    print("min:", min_val)

    sum_val = get_sum(num_list)
    print("sum:", sum_val)

    product_sum = get_product_sum(num_list)
    print("product:", product_sum)

    squared_list = get_squared_list(num_list)
    print("squared list", squared_list)

    cumulative_sum_list = get_cumulative_sum_list(num_list)
    print("cumulative sum list", cumulative_sum_list)
