#!/usr/bin/env python3
"""Independent checks for the minimal-Roman cycle bivariate enumerator.

Run: python3 verify.py
Uses only the Python standard library.
"""
from collections import Counter
from itertools import product


def roman_valid(labels):
    n = len(labels)
    for i, value in enumerate(labels):
        if value == 0 and labels[(i - 1) % n] != 2 and labels[(i + 1) % n] != 2:
            return False
    return True


def pointwise_minimal(labels):
    if not roman_valid(labels):
        return False
    n = len(labels)
    for i, value in enumerate(labels):
        if value:
            lower = list(labels)
            lower[i] -= 1
            if roman_valid(lower):
                return False
    return True


def algebraic_coefficients(limit):
    """Compute [-x dD/dx / D] coefficients as maps (twos, weight)->count."""
    c = [Counter() for _ in range(limit + 1)]
    shifts = [(1, 0, 1, 1), (3, 1, 2, 1), (4, 2, 4, 1), (5, 2, 4, 1)]
    for n in range(1, limit + 1):
        out = Counter()
        for step, twos, weight, coefficient in shifts:
            if n >= step:
                for (k, w), amount in c[n-step].items():
                    out[(k+twos, w+weight)] += coefficient * amount
            if n == step:
                out[(twos, weight)] += step * coefficient
        c[n] = out
    return c


def gap_characterization(n):
    counts = Counter()
    for mask in range(1 << n):
        used = [(mask >> i) & 1 for i in range(n)]
        if any(used[i] and not (
            (not used[(i-1)%n] and not used[(i-2)%n]) or
            (not used[(i+1)%n] and not used[(i+2)%n])
        ) for i in range(n)):
            continue
        twos = sum(used)
        weight = 2 * twos + sum(
            not used[i] and not used[(i-1)%n] and not used[(i+1)%n]
            for i in range(n)
        )
        counts[(twos, weight)] += 1
    return counts


def main():
    coeff = algebraic_coefficients(22)
    # This enumerates the original three-label definitions, not the gap rule.
    for n in range(3, 13):
        direct = Counter()
        for labels in product(range(3), repeat=n):
            if pointwise_minimal(labels):
                direct[(labels.count(2), sum(labels))] += 1
        assert direct == coeff[n], (n, direct, coeff[n])
        assert direct == gap_characterization(n), (n, 'gap characterization')
        print('definition n=%d configurations=%d weight_classes=%d OK' %
              (n, sum(direct.values()), len(direct)))
    for n in range(13, 18):
        assert gap_characterization(n) == coeff[n], n
        print('gap n=%d configurations=%d OK' % (n, sum(coeff[n].values())))
    assert sum(coeff[5].values()) == 16
    assert [sum(coeff[n].values()) for n in range(3, 13)] == [4, 9, 16, 22, 36, 65, 112, 186, 309, 522]
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
