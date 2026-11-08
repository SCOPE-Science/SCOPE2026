"""Exact finite checks for a two-layer path-collision variance identity.

Python 3 standard library only.  All expectations computed as exact fractions.
This script tests finite instances; the proof of the all-order theorem is separate.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
from random import Random


def circulant(d, offsets):
    offsets = set(offsets)
    return [[int((j - i) % d in offsets) for j in range(d)] for i in range(d)]


def verify_matrix(A):
    d = len(A)
    r = sum(A[0])
    assert d >= 4 and 2 <= r <= d - 2
    assert all(len(row) == d and all(x in (0, 1) for x in row) and sum(row) == r for row in A)
    assert all(sum(A[u][j] for u in range(d)) == r for j in range(d))
    c = {(u,v): sum(A[u][j] * A[v][j] for j in range(d))
         for u in range(d) for v in range(u + 1, d)}
    mean_c = Fraction(r * (r - 1), d - 1)
    predicted_mean = comb(r, 2) * mean_c
    kappa = Fraction(r * (r - 1) * (d - r) * (d - r - 1),
                     d * (d - 1) * (d - 2) * (d - 3))
    predicted_variance = kappa * sum((v - mean_c) ** 2 for v in c.values())
    collisions = []
    for S in combinations(range(d), r):
        counts = [sum(A[u][j] for u in S) for j in range(d)]
        direct = sum(comb(n, 2) for n in counts)
        alternative = sum(c[u, v] for u, v in combinations(S, 2))
        assert direct == alternative
        collisions.append(direct)
    actual_mean = Fraction(sum(collisions), len(collisions))
    actual_variance = Fraction(sum((x - actual_mean) ** 2 for x in collisions),
                               len(collisions))
    assert actual_mean == predicted_mean, (d, r, actual_mean, predicted_mean)
    assert actual_variance == predicted_variance, (d, r, actual_variance, predicted_variance)
    assert (actual_variance == 0) == (all(x == mean_c for x in c.values()))
    return actual_mean, actual_variance


def randomized_regular(d, r, rng, swaps=30):
    A = circulant(d, range(r))
    for _ in range(swaps):
        a, b = rng.sample(range(d), 2)
        left = [j for j in range(d) if A[a][j] == 1 and A[b][j] == 0]
        right = [j for j in range(d) if A[a][j] == 0 and A[b][j] == 1]
        if left and right:
            j, k = rng.choice(left), rng.choice(right)
            A[a][j], A[b][j] = 0, 1
            A[a][k], A[b][k] = 1, 0
    return A


def run():
    cases = 0
    for d in range(4, 10):
        for r in range(2, d - 1):
            for offsets in combinations(range(d), r):
                verify_matrix(circulant(d, offsets))
                cases += 1
    rng = Random(1729)
    for d in range(4, 10):
        for r in range(2, d - 1):
            for _ in range(30):
                verify_matrix(randomized_regular(d, r, rng))
                cases += 1
    fano = verify_matrix(circulant(7, (1, 2, 4)))
    consecutive = verify_matrix(circulant(7, (1, 2, 3)))
    assert fano == (Fraction(3), Fraction(0))
    assert consecutive == (Fraction(3), Fraction(6, 5))
    print(f"PASS: {cases} exact matrix/subset comparisons")
    print(f"7-vertex difference-set example: mean={fano[0]}, variance={fano[1]}")
    print(f"7-vertex interval example: mean={consecutive[0]}, variance={consecutive[1]}")


if __name__ == '__main__':
    run()
