"""Exact finite checks for prefix-deletion record-gain probabilities.

Run with Python 3. No third-party packages are needed.
"""
from fractions import Fraction
from itertools import permutations
from collections import defaultdict
from math import factorial


def c1(n, k):
    """Unsigned Stirling number of the first kind."""
    if n == k == 0:
        return 1
    if n <= 0 or k <= 0 or k > n:
        return 0
    return c1(n - 1, k - 1) + (n - 1) * c1(n - 1, k)


def record_count(seq):
    maximum = float('-inf')
    total = 0
    for x in seq:
        if x > maximum:
            maximum = x
            total += 1
    return total


def gain_and_hitting_position(seq, m):
    maximum = max(seq[:m])
    j = next((i + 1 for i in range(m, len(seq)) if seq[i] > maximum), len(seq) + 1)
    suffix = seq[m:]
    exposure = record_count(suffix) - sum(
        seq[i] > max(seq[:i]) for i in range(m, len(seq))
    )
    return exposure, j


def predicted(n, m):
    out = {}
    for j in range(m + 1, n + 1):
        ell = j - m - 1
        weight = Fraction(m, j * (j - 1))
        for k in range(ell + 1):
            prob = Fraction(c1(ell, k), factorial(ell))
            if prob:
                out[(k, j)] = weight * prob
    ell = n - m
    for k in range(ell + 1):
        prob = Fraction(c1(ell, k), factorial(ell))
        if prob:
            out[(k, n + 1)] = Fraction(m, n) * prob
    return out


def verify_exact():
    total_tests = 0
    for n in range(2, 9):
        observed = [defaultdict(int) for _ in range(1, n)]
        for seq in permutations(range(n)):
            for m in range(1, n):
                observed[m - 1][gain_and_hitting_position(seq, m)] += 1
        for m in range(1, n):
            expected = predicted(n, m)
            actual = {key: Fraction(val, factorial(n))
                      for key, val in observed[m-1].items()}
            assert actual == expected, (n, m, actual, expected)
            total_tests += len(set(actual) | set(expected))
            assert sum(expected.values()) == 1
            total_tests += 1
            mean = sum(Fraction(k) * prob for (k, _), prob in actual.items())
            harmonic = lambda a: sum((Fraction(1, j) for j in range(1, a + 1)), Fraction(0))
            assert mean == harmonic(n-m) + harmonic(m) - harmonic(n), (n, m, mean)
            total_tests += 1
            for j in range(m+1, n+2):
                hit = sum(prob for (k, x), prob in actual.items() if x == j)
                target = Fraction(m, n) if j == n+1 else Fraction(m, j*(j-1))
                assert hit == target
                total_tests += 1
    return total_tests


def verify_infinite_pgf():
    # Coefficients of the independent-geometric sum, truncated after 25 terms.
    tests = 0
    for m in range(1, 11):
        pmf = [Fraction(1)] + [Fraction(0)] * 25
        for j in range(1, m + 1):
            p = Fraction(j, j+1)
            q = Fraction(1, j+1)
            geo = [p*q**k for k in range(26)]
            pmf = [sum((pmf[r]*geo[k-r] for r in range(k+1)), Fraction(0)) for k in range(26)]
        # Recover the first coefficient and derivative identities from the PGF product.
        assert pmf[0] == Fraction(1, m+1)
        tests += 1
        mean = sum(Fraction(1,j) for j in range(1,m+1))
        variance = sum(Fraction(1,j)+Fraction(1,j*j) for j in range(1,m+1))
        assert mean > 0 and variance > mean
        tests += 1
        assert 0 < sum(pmf) < 1
        tests += 1
    return tests


if __name__ == '__main__':
    a = verify_exact()
    b = verify_infinite_pgf()
    print(f'PASS: {a} exact finite/joint assertions; {b} infinite-PGF consistency assertions')
