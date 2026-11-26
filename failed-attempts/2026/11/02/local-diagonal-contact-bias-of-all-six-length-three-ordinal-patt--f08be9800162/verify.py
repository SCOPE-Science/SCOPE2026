"""Exact finite checks for fixed-point / length-three ordinal-pattern identities."""
from math import comb, factorial
from fractions import Fraction
from itertools import permutations

PATTERNS = tuple(permutations((1, 2, 3)))


def rank_pattern(a):
    return tuple(1 + sum(b < x for b in a) for x in a)


def pattern_covariance_numerator(n, i, ranks):
    a = {
        (1, 2, 3): (n - 1),
        (1, 3, 2): (-3 * i + 2 * n - 3),
        (2, 1, 3): (3 * i - n),
        (2, 3, 1): (3 * i - 2 * n + 2),
        (3, 1, 2): (-3 * i + n - 1),
        (3, 2, 1): (-n + 3),
    }
    return a[ranks]


def local_rank_count(n, j, r):
    # Number of admissible ordered assignments to the two other sites.
    return comb(j - 1, r - 1) * comb(n - j, 3 - r)


def check():
    assertions = 0
    # Check the complete fixed-location covariance matrix, beyond direct enumeration.
    for n in range(3, 51):
        denominator = n * (n - 1) * (n - 2)
        for i in range(1, n - 1):
            for ranks in PATTERNS:
                local_sum = Fraction(0)
                for t, r in enumerate(ranks):
                    j = i + t
                    # E[1_{pi(j)=j} 1_{pattern}]-E[1_{pi(j)=j}]E[1_{pattern}].
                    actual = Fraction(local_rank_count(n, j, r), denominator) - Fraction(1, 6 * n)
                    local_sum += actual
                    assertions += 1
                expected = Fraction(pattern_covariance_numerator(n, i, ranks), denominator)
                assert local_sum == expected, (n, i, ranks, local_sum, expected)
                assertions += 1
            assert sum(pattern_covariance_numerator(n, i, r) for r in PATTERNS) == 0
            assertions += 1
            assert pattern_covariance_numerator(n, i, (1, 3, 2)) + pattern_covariance_numerator(n, i, (2, 3, 1)) == -1
            assertions += 1
            assert pattern_covariance_numerator(n, i, (2, 1, 3)) + pattern_covariance_numerator(n, i, (3, 1, 2)) == -1
            assertions += 1
    # Direct independent brute-force enumeration of uniform permutations.
    for n in range(3, 9):
        observed = {}
        for p in permutations(range(1, n + 1)):
            fixed_sites = {j for j, v in enumerate(p, 1) if j == v}
            fixed_count = len(fixed_sites)
            for i in range(1, n - 1):
                ranks = rank_pattern(p[i-1:i+2])
                key = (i, ranks)
                cell = observed.setdefault(key, [0, 0, [0] * n])
                cell[0] += 1
                cell[1] += fixed_count
                for j in fixed_sites:
                    cell[2][j-1] += 1
        denom = factorial(n)
        for i in range(1, n - 1):
            for ranks in PATTERNS:
                count, fixed_sum, fixed_cells = observed[(i, ranks)]
                assert count == denom // 6
                assertions += 1
                actual = Fraction(fixed_sum, denom) - Fraction(1, 6)
                expected = Fraction(pattern_covariance_numerator(n, i, ranks), n*(n-1)*(n-2))
                assert actual == expected, (n, i, ranks, actual, expected)
                assertions += 1
                for j in range(1, n + 1):
                    actual_cell = Fraction(fixed_cells[j - 1], denom) - Fraction(1, 6*n)
                    if not i <= j <= i+2:
                        expected_cell = Fraction(0)
                    else:
                        r = ranks[j-i]
                        expected_cell = (Fraction(local_rank_count(n, j, r), n*(n-1)*(n-2)) - Fraction(1,6*n))
                    assert actual_cell == expected_cell, (n, i, ranks, j, actual_cell, expected_cell)
                    assertions += 1
        print(f"n={n}: complete enumeration checked")
    return assertions


if __name__ == '__main__':
    print(f"PASS: {check():,} exact assertions")
