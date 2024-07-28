#!/usr/bin/env python3
"""
Script Name: calc_level.py
Description: 
    This script calculates final my level.
Usage:
    $ python3 calc_level.py

Author: tatsujin
Date: 2024-07-28
"""

import sys
import math
from enum import Enum, auto


class BattleResult(Enum):
    WIN = "win"
    LOSE = "lose"
    DRAW = "draw"


def read_input_levels():
    # My level
    print("Enter my level:")
    print("ex) 30 + Press Enter")
    my_level = int(input().strip())
    # Enemies level
    print("\nEnter enemies level:")
    print("ex) 10\\n20\\n... + Press Ctl+D")
    level_list_str = sys.stdin.read().strip()
    level_list = [int(lv) for lv in level_list_str.split("\n")]
    return my_level, level_list


def calc_final_level(my_level, level_list):
    for level in level_list:
        if my_level > level:
            my_level = my_level + math.floor(level / 2)
            result = BattleResult.WIN
        elif my_level == level:
            result = BattleResult.DRAW
        else:
            my_level = max(math.floor(my_level / 2), 1)
            result = BattleResult.LOSE
        print(f"Result: {result.value}, my level: {my_level}")
    return my_level


if __name__ == "__main__":
    my_level, level_list = read_input_levels()
    print("\nInitial my level:", my_level)
    print("Enemies level list:", level_list)
    my_level = calc_final_level(my_level, level_list)
    print("\nFinal my level:", my_level)
