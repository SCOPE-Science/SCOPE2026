#!/usr/bin/env python3
"""Finite independent tests for a polarized house-allocation theorem.

No use of analytic characterization in the brute-force objective computation.
"""
from itertools import permutations
from math import factorial


def objectives_by_assignments(third):
    m = len(third)
    ranks = []
    for ranking in (tuple(range(m)), tuple(range(m - 1, -1, -1)), third):
        pos = [0] * m
        for rank, house in enumerate(ranking):
            pos[house] = rank
        ranks.append(pos)
    best = (10, 10, 10)
    for houses in permutations(range(m), 3):
        loads = [sum(ranks[i][houses[j]] < ranks[i][houses[i]]
                     for j in range(3) if i != j) for i in range(3)]
        val = (sum(x > 0 for x in loads), sum(loads), max(loads))
        best = tuple(min(a, b) for a, b in zip(best, val))
        if best == (0, 0, 0):
            break
    return best


def endpoint_deletion(third):
    lo, hi = 0, len(third) - 1
    for house in third:
        if house == lo:
            lo += 1
        elif house == hi:
            hi -= 1
        else:
            return False
    return True


def main():
    for m in range(3, 9):
        failure = arrival_first = 0
        for ranking in permutations(range(m)):
            obs = objectives_by_assignments(ranking)
            theoretical = int(endpoint_deletion(ranking))
            assert obs == (theoretical,) * 3, (m, ranking, obs)
            failure += theoretical
            if (theoretical == 0 and endpoint_deletion(tuple(
                    h for h in ranking if h != m - 1))):
                arrival_first += 1
        assert failure == 2 ** (m - 1), (m, failure)
        assert arrival_first == 2 ** (m - 2) * (m - 2), (m, arrival_first)
        print(f"m={m}, checked {factorial(m)} complete third-agent orders: "
              f"failure={failure}; first success={arrival_first}; "
              f"all three envy objectives verified")


if __name__ == '__main__':
    main()
