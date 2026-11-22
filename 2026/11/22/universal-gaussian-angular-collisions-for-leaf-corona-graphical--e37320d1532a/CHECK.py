"""Exact finite checks for Gaussian collisions in leaf-corona graphical zonotopes.

Run with Python 3, standard library only: python CHECK.py
The all-dimensional limit is justified by the analytic proof, not this test.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial


def orientation_agreement(k, edges):
    """Two independent uniform orders induce identical orientations on edges."""
    tally = Counter()
    for order in permutations(range(k)):
        rank = [0] * k
        for place, vertex in enumerate(order):
            rank[vertex] = place
        signature = tuple(rank[i] < rank[j] for i, j in edges)
        tally[signature] += 1
    return Fraction(sum(c * c for c in tally.values()), factorial(k) ** 2)


def core_constant(k, edges):
    """Independent computation of the two-corner limiting coefficient."""
    ans = Fraction(0)
    for bits in product((0, 1), repeat=k):
        term = Fraction(1)
        for b in (0, 1):
            members = [v for v in range(k) if bits[v] == b]
            new_index = {vertex: j for j, vertex in enumerate(members)}
            sub_edges = [(new_index[i], new_index[j]) for i, j in edges
                         if i in new_index and j in new_index]
            term *= orientation_agreement(len(members), sub_edges)
        ans += term
    return ans


def full_permutation_collision(k, edges, n):
    """Exact finite collision probability, independently enumerating all rank orders."""
    N = k * (n + 1)
    full_edges = list(edges) + [(i, k + i * n + j)
                                for i in range(k) for j in range(n)]
    tally = Counter()
    for order in permutations(range(N)):
        rank = [0] * N
        for place, vertex in enumerate(order):
            rank[vertex] = place
        signature = tuple(rank[i] < rank[j] for i, j in full_edges)
        tally[signature] += 1
    return Fraction(sum(c * c for c in tally.values()), factorial(N) ** 2)


def run():
    assert orientation_agreement(0, []) == 1
    assert orientation_agreement(3, [(0, 1), (1, 2)]) == Fraction(5, 18)
    assert core_constant(1, []) == 2
    assert core_constant(2, [(0, 1)]) == 3
    assert core_constant(3, [(0, 1), (1, 2)]) == Fraction(41, 9)
    assert core_constant(3, [(0, 1), (1, 2), (0, 2)]) == Fraction(10, 3)
    assert core_constant(4, [(0, 1), (1, 2), (2, 3)]) == Fraction(83, 12)
    for k in range(1, 5):
        possible = list(combinations(range(k), 2))
        values = {}
        for mask in range(1 << len(possible)):
            edges = [e for j, e in enumerate(possible) if mask & (1 << j)]
            val = core_constant(k, edges)
            values[mask] = val
            assert Fraction(comb(2*k, k), factorial(k)) <= val <= 2**k
            for j in range(len(possible)):
                if not mask & (1 << j):
                    extended = [e for r, e in enumerate(possible) if mask & (1 << r) or r == j]
                    assert core_constant(k, extended) < val
        assert values[0] == 2**k
        assert values[(1 << len(possible)) - 1] == Fraction(comb(2*k, k), factorial(k))
    expected = [
        (2, [(0,1)], 1, Fraction(11,72)),
        (2, [(0,1)], 2, Fraction(859,16200)),
        (3, [(0,1),(1,2)], 1, Fraction(89,1800)),
        (3, [(0,1),(1,2),(0,2)], 1, Fraction(13,400)),
    ]
    for k, edges, n, value in expected:
        assert full_permutation_collision(k, edges, n) == value
    print('CORE_LEAF_CORONA_EXACT_PASS: graph_mono_k<=4, finite_cases=4')


if __name__ == '__main__':
    run()
