#!/usr/bin/env python3
"""Independent finite checks for a theorem on longest unbordered factors.

Run: python3 verify.py
Standard library only. Finite checks supplement, but do not replace, proofs.
"""
from collections import Counter
from fractions import Fraction


def slow_longest_unbordered(word):
    best = 0
    for left in range(len(word)):
        for right in range(left + 1, len(word) + 1):
            factor = word[left:right]
            if not any(factor[:k] == factor[-k:] for k in range(1, len(factor))):
                best = max(best, len(factor))
    return best


def gap_formula(a, b, c):
    maximum_outer = max(a, c)
    return maximum_outer + b + 2 if maximum_outer > b else b + 1


def full_count_by_length(max_n):
    result = Counter()
    for n in range(2, max_n + 1):
        for a in range(n - 1):
            for b in range(n - a - 1):
                c = n - a - b - 2
                result[(n, gap_formula(a, b, c))] += 1
    return result


def rational_coefficient_table(limit):
    # Bivariate generating function is a sum of six rational terms.
    # Each denominator factor is (1 - z^p*t^q), expanded exactly.
    terms = [
        (1, 2, 1, [(1, 0), (1, 0), (1, 1)]),
        (-2, 3, 1, [(1, 0), (1, 0), (2, 1)]),
        (1, 4, 1, [(1, 0), (1, 0), (3, 1)]),
        (2, 3, 3, [(1, 0), (1, 1), (2, 2)]),
        (-1, 4, 3, [(1, 0), (2, 1), (3, 2)]),
        (-1, 5, 3, [(1, 0), (2, 1), (3, 2)]),
    ]
    table = [[0] * (limit + 1) for _ in range(limit + 1)]
    for sign, zn, tu, factors in terms:
        arr = [[0] * (limit + 1) for _ in range(limit + 1)]
        arr[zn][tu] = sign
        for p, q in factors:
            for n in range(p, limit + 1):
                for u in range(q, limit + 1):
                    arr[n][u] += arr[n - p][u - q]
        for n in range(limit + 1):
            for u in range(limit + 1):
                table[n][u] += arr[n][u]
    return table


def limiting_cdf(x):
    x = Fraction(x)
    if x <= Fraction(1, 3):
        return Fraction(0)
    if x <= Fraction(1, 2):
        return (3*x - 1)**2 / 3
    if x <= Fraction(2, 3):
        return 3*(x - Fraction(1, 3))**2
    if x <= 1:
        return 2*x - 1
    return Fraction(1)


def main():
    checked_words = 0
    for n in range(2, 24):
        for a in range(n-1):
            for b in range(n-a-1):
                c = n-a-b-2
                word = '0'*a + '1' + '0'*b + '1' + '0'*c
                assert slow_longest_unbordered(word) == gap_formula(a,b,c), (a,b,c)
                checked_words += 1
    print('Direct factor/border enumeration PASS:', checked_words, 'words (lengths 2..23)')

    limit = 48
    table = rational_coefficient_table(limit)
    counts = full_count_by_length(limit)
    for n in range(limit+1):
        for u in range(limit+1):
            assert table[n][u] == counts.get((n,u), 0), (n,u,table[n][u],counts.get((n,u),0))
    print('Independent rational-series coefficient check PASS: all bidegrees to',limit)

    # The asserted univariate first-moment rational function has numerator
    # z^2*(1+8*z+16*z^2+22*z^3+19*z^4+11*z^5+3*z^6)
    # and denominator (1-z^2)^2*(1-z^3)^2.
    moments = [0] * (limit + 1)
    for exponent, coefficient in enumerate((1,8,16,22,19,11,3), start=2):
        moments[exponent] = coefficient
    for step in (2,2,3,3):
        for degree in range(step,limit+1):
            moments[degree] += moments[degree-step]
    for n in range(2,limit+1):
        direct = sum(u * counts.get((n,u), 0) for u in range(n+1))
        assert moments[n] == direct, (n,moments[n],direct)
    print('Independent first-moment rational-series check PASS: degrees 2..',limit)

    n = 500
    vals = []
    for a in range(n-1):
        for b in range(n-a-1):
            c = n-a-b-2
            vals.append(gap_formula(a,b,c))
    for threshold in (Fraction(1,3), Fraction(1,2), Fraction(2,3), Fraction(3,4), Fraction(9,10)):
        empirical = Fraction(sum(v*threshold.denominator <= n*threshold.numerator for v in vals),len(vals))
        target = limiting_cdf(threshold)
        assert abs(empirical - target) < Fraction(1, 70), (threshold,empirical,target)
    mean_ratio = Fraction(sum(vals), n*len(vals))
    assert abs(mean_ratio - Fraction(20,27)) < Fraction(1, 100)
    print('Asymptotic CDF and mean numerical sanity checks PASS: length',n)
    print('CHECKS_OK')


if __name__ == '__main__':
    main()
