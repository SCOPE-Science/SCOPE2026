#!/usr/bin/env python3
"""Independent finite checks of a laminar-support DR classification.

Requires only the Python 3 standard library. This is finite validation;
the theorem for arbitrary electorates is proved separately.
"""
import itertools
import math
import random
from collections import Counter


def laminar(supports):
    return all(not (a & b) or (a & b) == a or (a & b) == b
               for a, b in itertools.combinations(supports, 2))


def predicted(n, k, supports):
    q = (n + k - 1) // k
    eligible = [s for s in supports if s.bit_count() == q]
    groups = Counter(eligible)
    if len(eligible) < k:
        return 0
    union = 0
    for s in groups:
        union |= s
    if any((s & ~union).bit_count() >= q for s in supports):
        return 0
    coeff = [1] + [0] * k
    for multiplicity in groups.values():
        poly = [0] * (k + 1)
        for j in range(1, min(k, multiplicity) + 1):
            poly[j] = math.comb(multiplicity, j)
        coeff = [sum(coeff[t - j] * poly[j]
                     for j in range(t + 1))
                 for t in range(k + 1)]
    return coeff[k]


def brute(n, k, supports):
    q = (n + k - 1) // k
    answer = 0
    for chosen in itertools.combinations(range(len(supports)), k):
        if any(supports[c].bit_count() != q for c in chosen):
            continue
        represented = 0
        for c in chosen:
            represented |= supports[c]
        if all((s & ~represented).bit_count() < q for s in supports):
            answer += 1
    return answer


def random_laminar(n, m, rng):
    # Start from the full electorate and recursively split into random blocks.
    nodes = [(1 << n) - 1]
    pending = [tuple(range(n))]
    while pending:
        v = pending.pop()
        if len(v) <= 1:
            continue
        rng.shuffle(v := list(v))
        cut = rng.randrange(1, len(v))
        children = [tuple(v[:cut]), tuple(v[cut:])]
        for child in children:
            nodes.append(sum(1 << i for i in child))
            pending.append(child)
    # Include empty voter sets and arbitrary repeated candidate support sets.
    nodes.append(0)
    return tuple(rng.choice(nodes) for _ in range(m))


def run():
    checked = 0
    laminar_checked = 0
    for n in range(1, 5):
        values = range(1 << n)
        for m in range(1, 5):
            for supports in itertools.product(values, repeat=m):
                if not laminar(supports):
                    continue
                laminar_checked += 1
                for k in range(1, m + 1):
                    actual = brute(n, k, supports)
                    expected = predicted(n, k, supports)
                    assert actual == expected, (n, k, supports, actual, expected)
                    checked += 1
    rng = random.Random(20261102)
    for _ in range(30000):
        n = rng.randint(1, 10)
        m = rng.randint(1, 9)
        supports = random_laminar(n, m, rng)
        assert laminar(supports)
        k = rng.randint(1, m)
        actual = brute(n, k, supports)
        expected = predicted(n, k, supports)
        assert actual == expected, (n, k, supports, actual, expected)
        checked += 1
    # A feasible laminar instance with an omitted-voter buffer at the bound.
    n, k = 8, 3
    B1, B2 = 7, 56   # {0,1,2}, {3,4,5}
    supporters = (B1, B1, B2, B2, 255)
    assert predicted(n, k, supporters) == brute(n, k, supporters) == 4
    # The size-2 quota blocks can overlap outside the laminar domain.
    # Two distinct DR committees here have different coverage.
    n, k = 4, 2
    supports = (0b0011, 0b0110, 0b1100)
    assert not laminar(supports)
    assert brute(n, k, supports) == 3
    print('VERIFIED')
    print(f'exhaustive_laminar_candidate_tuples={laminar_checked}')
    print(f'committee_count_comparisons={checked}')
    print('nonlaminar_coverage_counterexample=passed')
    print('eight_voter_four_committee_example=passed')


if __name__ == '__main__':
    run()
