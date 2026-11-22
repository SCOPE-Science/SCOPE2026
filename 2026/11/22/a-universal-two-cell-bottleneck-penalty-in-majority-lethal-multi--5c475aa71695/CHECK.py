"""Exact, self-contained one-split calculation for majority-lethal daughters.

Standard-library only. All arithmetic is rational. Finite checks corroborate,
but do not replace, the symbolic proof in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def direct(m, a):
    n = 2 * m
    den = comb(n, a)
    expected_i = expected_c = expected_n = Fraction(0)
    for j in range(a + 1):
        probability = Fraction(comb(m, j) * comb(m, a - j), den)
        infected_small, healthy_small = j, a - j
        infected_large, healthy_large = m - j, m - a + j
        live_small = 2 * infected_small <= a
        live_large = 2 * infected_large <= n - a
        expected_i += probability * (
            live_small * infected_small + live_large * infected_large
        )
        expected_c += probability * (
            live_small * infected_small * healthy_small
            + live_large * infected_large * healthy_large
        )
        expected_n += probability * (
            live_small * a + live_large * (n - a)
        )
    return expected_i, expected_c, expected_n


def formula(m, a):
    if a == 1:
        return Fraction(m - 1, 2), Fraction(m * (m - 1), 2), Fraction(m)
    if a == 2:
        return (
            Fraction(3*m*m - 3*m + 2, 2 * (2*m - 1)),
            Fraction(m * (3*m*m - 7*m + 6), 2 * (2*m - 1)),
            Fraction(m * (3*m - 1), 2*m - 1),
        )
    if a == 3:
        return (
            Fraction(2*m*m - 4*m + 3, 2 * (2*m - 1)),
            Fraction(m * (2*m*m - 7*m + 9), 2 * (2*m - 1)),
            Fraction(m),
        )
    raise ValueError(a)


def microstate_check():
    # Unlike direct(), this enumerates labeled three-infected sets in six cells.
    m, n = 3, 6
    infected = {0, 1, 2}
    for a in (1, 2, 3):
        total = [0, 0, 0]
        for subset in combinations(range(n), a):
            smaller = set(subset)
            larger = set(range(n)) - smaller
            for daughter in (smaller, larger):
                count_i = len(daughter & infected)
                count_h = len(daughter) - count_i
                if 2 * count_i <= len(daughter):
                    total[0] += count_i
                    total[1] += count_i * count_h
                    total[2] += len(daughter)
        actual = tuple(Fraction(x, comb(n, a)) for x in total)
        assert actual == formula(m, a), (a, actual, formula(m, a))


def main():
    microstate_check()
    for m in range(3, 150):
        rows = [direct(m, a) for a in (1, 2, 3)]
        for a, row in zip((1, 2, 3), rows):
            assert row == formula(m, a), (m, a, row)
        i1, i2, i3 = (row[0] for row in rows)
        c1, c2, c3 = (row[1] for row in rows)
        n1, n2, n3 = (row[2] for row in rows)
        assert i2 > i1 > i3
        assert c2 > c1 > c3
        assert Fraction(i2, n2) > Fraction(i1, n1) > Fraction(i3, n3)
        assert i2 - i1 == Fraction(m*m + 1, 2*(2*m-1))
        assert i1 - i3 == Fraction(m-2, 2*(2*m-1))
        assert c2 - c1 == Fraction(m*((m-2)**2+1), 2*(2*m-1))
        assert c1 - c3 == Fraction(2*m*(m-2), 2*m-1)
        assert Fraction(i2, n2) - Fraction(i1, n1) == Fraction(m+1, 2*m*(3*m-1))
        assert Fraction(i1, n1) - Fraction(i3, n3) == Fraction(m-2, 2*m*(2*m-1))
    print('PASS: exact hypergeometric and assignment checks')


if __name__ == '__main__':
    main()
