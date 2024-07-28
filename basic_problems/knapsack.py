#!/usr/bin/env python3
"""
Script Name: knapsack.py
Description: 
    This script solves the knapsack problem using both dynamic programming and brute force methods,
    and compares their execution times.
Usage:
    $ python3 knapsack.py

Author: tatsujin
Date: 2024-07-28
"""

import time
from itertools import combinations
import random


def knapsack_dp(weights_list, values_list, max_weight):
    n = len(weights_list)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    dp_count = 0

    for i in range(1, n + 1):
        for w in range(max_weight + 1):
            dp_count += 1
            if weights_list[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights_list[i - 1]] + values_list[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    best_value = dp[n][max_weight]
    best_weight = 0
    for w in range(max_weight + 1):
        if dp[n][w] == best_value:
            best_weight = w
            break

    return best_value, best_weight, dp_count


def knapsack_brute_force(weights_list, values_list, max_weight):
    n = len(weights_list)
    max_value = 0
    best_weight = 0
    bf_count = 0

    for i in range(n + 1):
        for comb in combinations(range(n), i):
            bf_count += 1
            total_weight = sum(weights_list[j] for j in comb)
            total_value = sum(values_list[j] for j in comb)
            if total_weight <= max_weight and total_value > max_value:
                max_value = total_value
                best_weight = total_weight

    return max_value, best_weight, bf_count


if __name__ == "__main__":
    num_items = 20
    item_max_weight = 10
    item_max_value = 1000
    # Fixed random numbers by seed value
    # random.seed(0)

    # Generate items list
    weights_list = [random.randint(1, item_max_weight) for _ in range(num_items)]
    values_list = [random.randint(1, item_max_value) for _ in range(num_items)]
    max_weight = 50

    print("[Input]")
    print(f"Number of items: {num_items}")
    print(f"Weights[kg]: {weights_list}")
    print(f"Values[yen]: {values_list}")
    print(f"Max weight: {max_weight} kg")

    start_time = time.time()
    result_dp, best_weight_dp, dp_count = knapsack_dp(weights_list, values_list, max_weight)
    end_time = time.time()
    print("\n[Result: Dynamic Programming]")
    print(f"Max value: {result_dp} yen")
    print(f"Total weight: {best_weight_dp} kg")
    print(f"Time: {end_time - start_time:.6f} seconds")
    print(f"Count: {dp_count} times")

    start_time = time.time()
    result_brute_force, best_weight_bf, bf_count = knapsack_brute_force(
        weights_list, values_list, max_weight
    )
    end_time = time.time()
    print("\n[Result: Brute Force]")
    print(f"Max value: {result_brute_force} yen")
    print(f"Total weight: {best_weight_bf} kg")
    print(f"Time: {end_time - start_time:.6f} seconds")
    print(f"Count: {bf_count} times")
