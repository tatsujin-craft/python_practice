#!/usr/bin/env python3
"""
Thousand Barrels Problem Solver

Script Name: thousand_barrels.py
Description: 
    This script solves the "Thousand Barrel" problem where 1000 barrels 
    each contain either whiskey, wine, or beer with random amounts between 0 and 100 liters. 
    The goal is to find the subset of barrels for each type of liquor that most closely matches a 
    target amount.

Usage:
    $ python3 thousand_barrels.py
    Run the script to generate a random set of barrels 
    and find the best subsets of barrels for given target amounts.

Functions:
    - generate_barrels(num_barrels=1000, max_capacity=100): 
        Generates a list of barrels with random liquor types and amounts.
    - find_best_subset(barrels, target, liquor_type): 
        Finds the subset of barrels of a specified liquor type that most closely matches 
        the target amount using dynamic programming.

Arguments:
    - num_barrels (int): Number of barrels to generate. Default is 1000.
    - max_capacity (int): Maximum capacity of each barrel in liters. Default is 100 liters.
    - barrels (list): List of Barrel objects.
    - target (int): Target total amount of liquor in liters.
    - liquor_type (str): Type of liquor ('whiskey', 'wine', 'beer').

Returns:
    - List of indices for the best subset of barrels and the closest amount.

Author: tatsujin
Date: 2024-07-27
"""

import random


class Barrel:
    def __init__(self, type_of_liquor, amount):
        self.type_of_liquor = type_of_liquor
        self.amount = amount


def generate_barrels(num_barrels=1000, max_capacity=100):
    """
    Generate a list of barrels, each with a random type of liquor and random amount.

    Args:
    num_barrels (int): Number of barrels. Default is 1000.
    max_capacity (int): Maximum capacity of each barrel. Default is 100 liters.

    Returns:
    list: List of barrels.
    """
    types_of_liquor = ["whiskey", "wine", "beer"]
    barrels = []
    for _ in range(num_barrels):
        type_of_liquor = random.choice(types_of_liquor)
        amount = random.randint(0, max_capacity)
        barrels.append(Barrel(type_of_liquor, amount))
    return barrels


def find_best_subset(barrels, target, liquor_type):
    """
    Find the subset of barrels with a specified type of liquor
    that most closely matches the target amount using dynamic programming.

    Args:
    barrels (list): List of barrels.
    target (int): Target total amount of liquor.
    liquor_type (str): Type of liquor in the barrels (whiskey, wine, beer).

    Returns:
    tuple: List of indices for the best subset of barrels and the closest amount.
    """
    filtered_barrels = [
        (i, barrel.amount)
        for i, barrel in enumerate(barrels)
        if barrel.type_of_liquor == liquor_type
    ]
    n = len(filtered_barrels)

    # Dynamic programming table
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    keep = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        index, amount = filtered_barrels[i - 1]
        for j in range(target + 1):
            if j >= amount and dp[i - 1][j - amount] + amount > dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j - amount] + amount
                keep[i][j] = True
            else:
                dp[i][j] = dp[i - 1][j]

    # Backtracking to find the best subset
    best_subset = []
    j = target
    for i in range(n, 0, -1):
        if keep[i][j]:
            index, amount = filtered_barrels[i - 1]
            best_subset.append(index)
            j -= amount

    closest_amount = dp[n][target]
    return best_subset, closest_amount


def main():
    # Generate the list of barrels
    barrels = generate_barrels()

    # Log the number of barrels of each type and their capacities
    whiskey_count = sum(1 for barrel in barrels if barrel.type_of_liquor == "whiskey")
    wine_count = sum(1 for barrel in barrels if barrel.type_of_liquor == "wine")
    beer_count = sum(1 for barrel in barrels if barrel.type_of_liquor == "beer")

    print(
        f"Generated {whiskey_count} whiskey barrels, "
        f"{wine_count} wine barrels, {beer_count} beer barrels."
    )

    for i, barrel in enumerate(barrels):
        print(f"Barrel {i}: Type={barrel.type_of_liquor}, Amount={barrel.amount}L")

    # Set target amounts
    whiskey_target = 12007
    wine_target = 15013
    beer_target = 17011

    # Find the best subsets
    best_whiskey_subset, whiskey_amount = find_best_subset(barrels, whiskey_target, "whiskey")
    best_wine_subset, wine_amount = find_best_subset(barrels, wine_target, "wine")
    best_beer_subset, beer_amount = find_best_subset(barrels, beer_target, "beer")

    # Display the indices of the best subsets and the closest amounts
    print(
        f"\nBest subset of whiskey barrels close to target {whiskey_target} L"
        f"\nBarrels ID list: {best_whiskey_subset}"
        f"\nNumber of whiskey barrels: {len(best_whiskey_subset)}"
        f"\nClosest amount: {whiskey_amount} L"
    )
    print(
        f"\nBest subset of wine barrels close to target {wine_target} L"
        f"\nBarrels ID list: {best_wine_subset}"
        f"\nNumber of wine barrels: {len(best_wine_subset)}"
        f"\nClosest amount: {wine_amount} L"
    )
    print(
        f"\nBest subset of beer barrels close to target {beer_target} L"
        f"\nBarrels ID list: {best_beer_subset}"
        f"\nNumber of beer barrels: {len(best_beer_subset)}"
        f"\nClosest amount: {beer_amount} L"
    )

    # Calculate the sum of the amounts in the best subsets
    whiskey_sum = sum(barrels[i].amount for i in best_whiskey_subset)
    wine_sum = sum(barrels[i].amount for i in best_wine_subset)
    beer_sum = sum(barrels[i].amount for i in best_beer_subset)

    # Display the calculated sums
    print(f"\nCalculated sum of the best subset of whiskey barrels: {whiskey_sum} L")
    print(f"Calculated sum of the best subset of wine barrels: {wine_sum} L")
    print(f"Calculated sum of the best subset of beer barrels: {beer_sum} L")


if __name__ == "__main__":
    main()
