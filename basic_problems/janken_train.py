#!/usr/bin/env python3

import sys


def simulate_janken_trains():
    input = sys.stdin.read().strip()
    if not input:
        print("No input provided.")
        return

    rounds = input.split("\n")
    trains = {}

    for round in rounds:
        x, y = map(int, round.split())
        if x not in trains:
            trains[x] = [x]
        if y not in trains:
            trains[y] = [y]

        trains[x] += trains.pop(y)

    max_length = max(len(train) for train in trains.values())
    winners = [train[0] for train in trains.values() if len(train) == max_length]

    for winner in winners:
        print(winner)


if __name__ == "__main__":
    simulate_janken_trains()
