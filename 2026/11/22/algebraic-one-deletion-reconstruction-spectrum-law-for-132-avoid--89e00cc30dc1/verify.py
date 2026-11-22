#!/usr/bin/env python3
"""Independent finite checks of a polynomial sphere enumerator for Av(132).
Run with: python3 verify.py. Requires Python standard library only.
The proofs of all-length identities and asymptotics are in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb


def is_132_avoiding(p):
    n = len(p)
    return not any(p[i] < p[k] < p[j]
                   for i in range(n)
                   for j in range(i + 1, n)
                   for k in range(j + 1, n))


def standardized(p):
    ranks = {x: i + 1 for i, x in enumerate(sorted(p))}
    return tuple(ranks[x] for x in p)


def deletion_ball(p):
    return {standardized(p[:i] + p[i + 1:]) for i in range(len(p))}


def bond_count(p):
    return sum(abs(p[i] - p[i + 1]) == 1 for i in range(len(p) - 1))


def polynomial_add(a, b, sign=1):
    c = Counter(a)
    for k, v in b.items():
        c[k] += sign * v
    return Counter({k: v for k, v in c.items() if v})


def polynomial_shift(a, shift):
    return Counter({k + shift: v for k, v in a.items()})


def polynomial_mul(a, b):
    result = Counter()
    for i, x in a.items():
        for j, y in b.items():
            result[i + j] += x * y
    return result


def generating_function_coefficients(max_n):
    # A=z + z(1+u)A + z A^2 + z^2(u-1)(1+A).
    f = [Counter()]
    for n in range(1, max_n + 1):
        new = Counter({0: 1}) if n == 1 else Counter()
        new = polynomial_add(new, f[n - 1])
        new = polynomial_add(new, polynomial_shift(f[n - 1], 1))
        if n == 2:
            new = polynomial_add(new, {1: 1, 0: -1})
        elif n > 2:
            new = polynomial_add(new, polynomial_shift(f[n - 2], 1))
            new = polynomial_add(new, f[n - 2], -1)
        for left in range(1, n - 1):
            new = polynomial_add(new, polynomial_mul(f[left], f[n - 1 - left]))
        f.append(new)
    return f


def run():
    fs = generating_function_coefficients(12)
    expected = {1: {0: 1}, 2: {1: 2}, 3: {1: 3, 2: 2},
                4: {1: 5, 2: 7, 3: 2},
                5: {1: 8, 2: 21, 3: 11, 4: 2},
                6: {1: 13, 2: 53, 3: 49, 4: 15, 5: 2},
                7: {1: 21, 2: 124, 3: 174, 4: 89, 5: 19, 6: 2},
                8: {1: 34, 2: 273, 3: 546, 4: 411, 5: 141, 6: 23, 7: 2}}
    for n, poly in expected.items():
        assert fs[n] == Counter(poly), (n, fs[n], poly)
    print('Series coefficients: n=1..8 match explicit expected rows')

    for n in range(1, 9):
        brute = Counter()
        sources = 0
        for p in permutations(range(1, n + 1)):
            if not is_132_avoiding(p):
                continue
            sources += 1
            b = bond_count(p)
            assert len(deletion_ball(p)) == n - b, (n, p)
            brute[b] += 1
        assert brute == fs[n], (n, brute, fs[n])
        assert sources == comb(2 * n, n) // (n + 1), (n, sources)
        if n >= 2:
            observed = Fraction(sum(k * v for k, v in brute.items()), sources)
            predicted = Fraction((n + 1) * (3 * n - 2), 4 * (2 * n - 1))
            assert observed == predicted, (n, observed, predicted)
        print(f'n={n}: {sources} sources; deletion spheres, bond row and mean verified')
    for n in range(9, 13):
        assert sum(fs[n].values()) == comb(2 * n, n) // (n + 1)
        expected_mean = Fraction((n + 1) * (3 * n - 2), 4 * (2 * n - 1))
        actual = Fraction(sum(k * v for k, v in fs[n].items()), sum(fs[n].values()))
        assert expected_mean == actual
    print('Polynomial recurrence and exact expectation: n=1..12 verified')
    print('PASS (finite verification, not an infinite proof)')


if __name__ == '__main__':
    run()
