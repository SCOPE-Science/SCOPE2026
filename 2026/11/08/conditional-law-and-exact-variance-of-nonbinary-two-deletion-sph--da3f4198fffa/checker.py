"""Reproduce exact two-deletion sphere law over finite q-ary words.

Run with python3 checker.py; Python standard library only.
The script tests finite instances; the accompanying mathematical proof covers all n,q.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def observed(word):
    n = len(word)
    return len({word[:i] + word[i + 1:j] + word[j + 1:]
                for i in range(n) for j in range(i + 1, n)})


def pointwise(word):
    n = len(word)
    if n == 2:
        return 1
    ts = [int(word[i] != word[i - 1]) for i in range(1, n)]
    s = sum(ts)
    j = sum(a * b for a, b in zip(ts, ts[1:]))
    rev = sum(int(word[i - 1] == word[i + 1] != word[i])
              for i in range(1, n - 1))
    return 1 + s * (s + 3) // 2 - ts[0] - ts[-1] - j - rev


def predicted_distribution(q, n):
    if n == 2:
        return {1: Fraction(1)}
    p = Fraction(q - 1, q)
    a = Fraction(1, q - 1)
    result = Counter()
    for ts in product((0, 1), repeat=n - 1):
        s = sum(ts)
        j = sum(u * v for u, v in zip(ts, ts[1:]))
        base = 1 + s * (s + 3) // 2 - ts[0] - ts[-1] - j
        weight = p ** s * (1 - p) ** (n - 1 - s)
        for r in range(j + 1):
            result[base - r] += weight * comb(j, r) * a ** r * (1 - a) ** (j - r)
    return {k: v for k, v in result.items() if v}


def moments(q, n):
    m = n - 2
    p = Fraction(q - 1, q)
    expected = 1 + m * p + Fraction((n - 1) * m, 2) * p * p
    variance = Fraction(m * ((n - 1) * m * (q - 1) ** 3
                              + Fraction(n - 3, 2) * (q - 1) ** 2
                              + 1 + (q - 2) * q * q), q ** 4)
    return expected, variance


def check():
    pointwise_cases = 0
    distribution_cases = 0
    for q, max_n in ((2, 8), (3, 7), (4, 6)):
        for n in range(2, max_n + 1):
            empirical = Counter()
            for w in product(range(q), repeat=n):
                observed_count = observed(w)
                calculated = pointwise(w)
                assert observed_count == calculated, (q, n, w, observed_count, calculated)
                empirical[observed_count] += 1
                pointwise_cases += 1
            empirical = {k: Fraction(c, q ** n) for k, c in empirical.items()}
            theoretical = predicted_distribution(q, n)
            assert empirical == theoretical, (q, n, empirical, theoretical)
            expectation = sum(Fraction(k) * v for k, v in empirical.items())
            variance = sum((k - expectation) ** 2 * v for k, v in empirical.items())
            assert (expectation, variance) == moments(q, n), (q, n, expectation, variance, moments(q,n))
            distribution_cases += 1
    for n in range(2, 40):
        assert moments(2, n)[1] == Fraction((n-1)*(n-2)*(2*n-3), 32)
    print(f"PASS: {pointwise_cases} exhaustive pointwise cases; {distribution_cases} exact finite-distribution and moment comparisons; 38 binary specialization comparisons.")


if __name__ == '__main__':
    check()
