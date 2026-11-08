#!/usr/bin/env python3
"""Exhaustive small-instance check of fixed-action equilibrium thresholds."""
from itertools import product, combinations
from math import comb


def equilibrium_exists(a, b, pinned, strict):
    n = a + b
    free = [i for i in range(n) if i not in pinned]
    for trial in product((0, 1), repeat=len(free)):
        actions = [0] * n
        for i, action in pinned.items():
            actions[i] = action
        for i, action in zip(free, trial):
            actions[i] = action
        left_ones = sum(actions[:a])
        right_ones = sum(actions[a:])
        success = True
        for i in free:
            # Gain from action 1 compared with action 0.
            advantage = ((2 * right_ones - b) if i < a else (a - 2 * left_ones))
            chosen_gain = advantage * (2 * actions[i] - 1)
            if chosen_gain < 0 or (strict and chosen_gain == 0):
                success = False
                break
        if success:
            return True
    return False


def expected(a, b, strict):
    if strict:
        ta, tb = a // 2 + 1, b // 2 + 1
        k = min(ta, tb)
    elif a % 2 == b % 2 == 0:
        return (0, 1)
    else:
        ta, tb = (a + 1) // 2, (b + 1) // 2
        k = min(ta, tb)
    count = 2 * ((comb(a, k) if ta == k else 0) +
                 (comb(b, k) if tb == k else 0))
    return k, count


def main():
    budgets = 0
    checked_interventions = 0
    for a in range(1, 6):
        for b in range(1, 6):
            for strict in (False, True):
                k, correct_count = expected(a, b, strict)
                for smaller in range(k):
                    for positions in combinations(range(a + b), smaller):
                        for choices in product((0, 1), repeat=smaller):
                            checked_interventions += 1
                            assert not equilibrium_exists(a, b, dict(zip(positions, choices)), strict), (a, b, strict, smaller, positions, choices)
                count = 0
                for positions in combinations(range(a + b), k):
                    for choices in product((0, 1), repeat=k):
                        checked_interventions += 1
                        count += equilibrium_exists(a, b, dict(zip(positions, choices)), strict)
                assert count == correct_count, (a, b, strict, count, correct_count)
                budgets += 1
    print(f'VERIFIED: {budgets} minimum-budget claims; {checked_interventions} interventions checked, including all lower-budget cases')

if __name__ == '__main__':
    main()
