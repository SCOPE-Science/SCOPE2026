#!/usr/bin/env python3
"""Independent finite-state and exact-binomial checks for sandpile burst laws."""
from collections import Counter
from itertools import product
from math import comb


def stabilize(chips, n):
    """Legal topplings in K_{2,n}, with one leaf as sink."""
    chips = list(chips)
    odometer = [0] * len(chips)
    while True:
        site = next((j for j, height in enumerate(chips)
                     if height >= (n if j < 2 else 2)), None)
        if site is None:
            break
        odometer[site] += 1
        assert sum(odometer) <= 4 * (n + 1), "unexpected stabilization"
        if site < 2:
            chips[site] -= n
            for j in range(2, n + 1):
                chips[j] += 1
        else:
            chips[site] -= 2
            chips[0] += 1
            chips[1] += 1
    return tuple(chips), tuple(odometer)


def burning_recurrent(chips, n):
    trial = list(chips)
    trial[0] += 1
    trial[1] += 1
    stabilized, odometer = stabilize(trial, n)
    return (stabilized == tuple(chips)
            and odometer == (1,) * (n + 1))


def criterion_recurrent(chips, n):
    a, b = chips[:2]
    k = sum(chips[2:])
    return ((a == n - 1 and b >= n - 1 - k)
            or (b == n - 1 and a >= n - 1 - k))


def theoretical_hub(n):
    z = Counter({0: (n - 1) * 2 ** (n - 2), n + 1: (n - 1) * 2 ** (n - 2)})
    for k in range(n):
        z[k + 1] += comb(n - 1, k)
    return z


def theoretical_leaf(n):
    z = Counter({0: (n - 1) * 2 ** (n - 2), n + 2: (n - 1) * 2 ** (n - 2)})
    for k in range(n - 1):
        z[k + 2] += 2 * comb(n - 2, k)
    return z


def run():
    for n in range(2, 11):
        total = 0
        hub_counts = Counter()
        leaf_counts = Counter()
        for a in range(n):
            for b in range(n):
                for heights in product((0, 1), repeat=n - 1):
                    chips = (a, b, *heights)
                    formula = criterion_recurrent(chips, n)
                    independently_burnt = burning_recurrent(chips, n)
                    assert formula == independently_burnt, (n, chips, 'burning')
                    if not formula:
                        continue
                    total += 1
                    for drive, counts in ((0, hub_counts), (2, leaf_counts)):
                        perturb = list(chips)
                        perturb[drive] += 1
                        _, odometer = stabilize(perturb, n)
                        counts[sum(odometer)] += 1
        assert total == n * 2 ** (n - 1), (n, total)
        assert hub_counts == theoretical_hub(n), (n, 'hub', hub_counts)
        assert leaf_counts == theoretical_leaf(n), (n, 'leaf', leaf_counts)
    for n in range(2, 513):
        h, l = theoretical_hub(n), theoretical_leaf(n)
        expected = n * 2 ** (n - 1)
        assert sum(h.values()) == sum(l.values()) == expected
        assert sum(t * amount for t, amount in h.items()) * 2 == (n + 1) * expected
        assert sum(t * amount for t, amount in l.items()) * 2 == (n + 2) * expected
        assert h[n + 1] == l[n + 2] == h[0] == l[0]
    print('SANDPILE_TWO_HUB_CHECKS_PASSED finite_n=2..10 formulas_n=2..512')

if __name__ == '__main__':
    run()
