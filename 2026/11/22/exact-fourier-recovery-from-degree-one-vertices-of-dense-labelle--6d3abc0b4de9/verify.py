#!/usr/bin/env python3
"""Exact checks of the degree-one-vertex Walsh spectrum for labelled simple graphs.

Requires only Python 3 standard library. Graphs are unweighted and have no loops.
Use: python3 verify.py
"""
from math import comb, factorial
from fractions import Fraction


def hermite_matching(j, m):
    """Number of assignments of incident edges giving degree 1 on j fixed vertices."""
    return sum(factorial(j) // (2 ** r * factorial(r) * factorial(j - 2 * r))
               * m ** (j - 2 * r) for r in range(j // 2 + 1))


def fixed_degree_one(n, j):
    return 2 ** comb(n - j, 2) * hermite_matching(j, n - j)


def multipliers(n):
    return [sum(comb(k, j) * (-2) ** j * fixed_degree_one(n, j)
                for j in range(k + 1)) for k in range(n + 1)]


def independent_gray_histogram(n):
    """Count degree-one vertex sets by a Gray-code walk over every simple graph."""
    edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
    deg = [0] * n
    hist = [0] * (1 << n)
    indicator = 0
    hist[indicator] += 1
    for step in range(1, 1 << len(edges)):
        bit = (step & -step).bit_length() - 1
        u, v = edges[bit]
        for w in (u, v):
            if deg[w] == 1:
                indicator ^= (1 << w)
        if ((step ^ (step >> 1)) >> bit) & 1:
            deg[u] += 1
            deg[v] += 1
        else:
            deg[u] -= 1
            deg[v] -= 1
        for w in (u, v):
            if deg[w] == 1:
                indicator ^= (1 << w)
        hist[indicator] += 1
    assert sum(hist) == 1 << len(edges)
    assert min(hist) >= 0
    return hist


def hadamard_transform(hist):
    vals = list(hist)
    n = len(vals)
    width = 1
    while width < n:
        for start in range(0, n, 2 * width):
            for j in range(width):
                a, b = vals[start + j], vals[start + width + j]
                vals[start + j] = a + b
                vals[start + width + j] = a - b
        width *= 2
    return vals


EXPECTED = {
    1: [1, 1],
    2: [2, 0, 2],
    3: [8, 0, 0, 8],
    4: [64, 16, 8, 8, 32],
    5: [1024, 512, 320, 224, 160, 224],
    6: [32768, 22528, 16640, 12800, 10080, 8096, 7136],
    7: [2097152, 1703936, 1417216, 1198080, 1025280,
        886144, 772352, 680576],
    8: [268435456, 239075328, 214564864, 193757184,
        175868928, 160337408, 146741632, 134757504, 124144384],
}


def main():
    tests = 0
    for n in range(1, 9):
        l = multipliers(n)
        assert l == EXPECTED[n]
        tests += 1
        assert l[0] == 2 ** comb(n, 2)
        tests += 1
        if n in (2, 3):
            assert [k for k, x in enumerate(l) if x == 0] == list(range(1, n))
        elif n >= 4:
            assert min(l) > 0
        else:
            assert l == [1, 1]
        tests += 1
        if n >= 4:
            if n == 4:
                assert [k for k, x in enumerate(l) if x == min(l)] == [2, 3]
            elif n == 5:
                assert [k for k, x in enumerate(l) if x == min(l)] == [4]
            else:
                assert [k for k, x in enumerate(l) if x == min(l)] == [n]
            tests += 1
    assert Fraction(2 ** comb(4, 2), min(multipliers(4))) == 8
    tests += 1
    for n in range(5, 9):
        assert Fraction(2 ** comb(n, 2), min(multipliers(n))) < 8
        tests += 1
    for n in range(6, 9):
        a = multipliers(n)
        assert all(a[k] > a[k + 1] for k in range(n))
        tests += n
    # Distinct direct enumeration: full Walsh transform of degree-one profiles,
    # not just all-one frequencies or a graph count by degree.
    for n in range(1, 8):
        actual = hadamard_transform(independent_gray_histogram(n))
        a = multipliers(n)
        for char in range(1 << n):
            assert actual[char] == a[char.bit_count()]
            tests += 1
    # These finite checks accompany, but do not replace, the all-order proof.
    for n in range(9, 150):
        assert 2 * n * (n - 1) < 2 ** (n - 1)
        assert 2 * (1 + (n - 2) ** 2) < 2 ** (n - 2)
        tests += 2
    print(f"PASS: {tests} exact assertions; direct graph enumeration through n=7; "
          "full small-order spectrum through n=8; all-order bounds proved in RESULT.md")


if __name__ == '__main__':
    main()
