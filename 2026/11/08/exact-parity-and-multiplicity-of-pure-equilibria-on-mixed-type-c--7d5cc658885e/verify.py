"""Independent finite checks for the exact mixed-type bipartite equilibrium formula.

Uses direct payoff inequalities, not the four-case proof, to count pure equilibria.
"""
from fractions import Fraction
from itertools import product
from math import comb


def central(n):
    return comb(n, n // 2) if n % 2 == 0 else 0


def closed_count(a, b, c, d):
    za, zb = central(a), central(b)
    da, db = 2 * c - a, 2 * d - b
    return (za * zb + (2 ** b - zb) * (da == 0)
            + (2 ** a - za) * (db == 0) + 2 * (da * db > 0))


def direct_count(a, b, c, d):
    types = (+1,) * c + (-1,) * (a - c) + (+1,) * d + (-1,) * (b - d)
    accepted = 0
    for actions in product((-1, +1), repeat=a + b):
        u = sum(actions[:a])
        v = sum(actions[a:])
        good = all(types[i] * actions[i] * v >= 0 for i in range(a))
        good &= all(types[i] * actions[i] * u >= 0 for i in range(a, a + b))
        if good:
            accepted += 1
    return accepted


def random_types_failure(a, b):
    bad = sum(comb(a, c) * comb(b, d) for c in range(a + 1)
              for d in range(b + 1) if closed_count(a, b, c, d) == 0)
    return Fraction(bad, 2 ** (a + b))


def predicted_failure(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return Fraction(0)
    return Fraction(1, 2) * (1 - Fraction(central(a), 2 ** a)) * (1 - Fraction(central(b), 2 ** b))


def main():
    cases = 0
    direct_profiles = 0
    for a in range(1, 6):
        for b in range(1, 6):
            for c in range(a + 1):
                for d in range(b + 1):
                    expected = closed_count(a, b, c, d)
                    actual = direct_count(a, b, c, d)
                    assert actual == expected, (a, b, c, d, actual, expected)
                    cases += 1
                    direct_profiles += 2 ** (a + b)
    for a in range(1, 9):
        for b in range(1, 9):
            assert random_types_failure(a, b) == predicted_failure(a, b), (a, b)
    assert closed_count(2, 2, 1, 1) == 8
    assert closed_count(3, 3, 2, 1) == 0
    assert closed_count(4, 4, 4, 0) == 36
    print('VERIFIED exact direct-payoff cases:', cases)
    print('VERIFIED action profiles:', direct_profiles)
    print('VERIFIED random-type probability pairs: 64')
    print('VERIFIED sample equilibrium counts: 8, 0, 36')


if __name__ == '__main__':
    main()
