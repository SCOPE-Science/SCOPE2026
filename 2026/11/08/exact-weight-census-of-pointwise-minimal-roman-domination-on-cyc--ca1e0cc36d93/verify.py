#!/usr/bin/env python3
"""Exact independent checks of pointwise-minimal Roman functions on cycles."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def roman_ok(a):
    n = len(a)
    for i in range(n):
        if a[i] == 0 and a[(i - 1) % n] != 2 and a[(i + 1) % n] != 2:
            return False
    return True


def minimal_roman_ok(a):
    if not roman_ok(a):
        return False
    for i in range(len(a)):
        if a[i] == 0:
            continue
        b = list(a)
        b[i] -= 1
        if roman_ok(b):
            return False
    return True


def direct_labeling(n):
    ans = Counter()
    for a in product(range(3), repeat=n):
        if minimal_roman_ok(a):
            ans[sum(a)] += 1
    return ans


def from_defender_subsets(n):
    """Second graph-level method: select defender positions, test private neighbors."""
    ans = Counter()
    for mask in range(1 << n):
        S = {i for i in range(n) if (mask >> i) & 1}
        if any(not any(j not in S and sum(v in S for v in ((j - 1) % n, (j + 1) % n)) == 1
                       for j in ((i - 1) % n, (i + 1) % n)) for i in S):
            continue
        w = [2 if i in S else
             0 if ((i - 1) % n in S or (i + 1) % n in S) else 1
             for i in range(n)]
        assert minimal_roman_ok(w)
        ans[sum(w)] += 1
    return ans


def coefficient_formula(n, w):
    """Independent explicit cyclic-gap binomial sum, with rational intermediates."""
    result = Fraction(int(w == n), 1)
    for ell in range(1, n // 3 + 1):
        for s in range(ell + 1):
            b = n - w - ell + s
            excess = w - 2 * (ell + s)
            if 0 <= b <= s and excess >= 0:
                result += (Fraction(n, ell) * comb(ell, s)
                           * comb(s, b) * comb(excess + ell - 1, ell - 1))
    assert result.denominator == 1
    return result.numerator


def rational_recurrence(N):
    """Coefficient recurrence of the stated bivariate rational function."""
    initial_numerator = {
        3: {2: 3, 3: 1},
        4: {3: 1, 4: 4},
        5: {4: 6, 5: 1},
        6: {5: 1, 6: 1},
        7: {6: 1},
    }
    p = [Counter() for _ in range(N + 1)]
    for n in range(3, N + 1):
        p[n].update(initial_numerator.get(n, {}))
        for shift, wz in ((1, 1), (3, 2), (4, 4), (5, 4)):
            if n >= shift:
                for w, count in p[n - shift].items():
                    p[n][w + wz] += count
    return p


def run():
    p = rational_recurrence(65)
    labeling_cases = 0
    subset_cases = 0
    for n in range(3, 12):
        direct = direct_labeling(n)
        assert direct == p[n], (n, direct, p[n])
        labeling_cases += 3 ** n
    for n in range(3, 19):
        by_subsets = from_defender_subsets(n)
        assert by_subsets == p[n], (n, by_subsets, p[n])
        subset_cases += 2 ** n
    coefficient_cases = 0
    for n in range(3, 46):
        assert sorted(p[n]) == list(range((2 * n + 2) // 3, n + 1))
        for w in range(n + 1):
            assert coefficient_formula(n, w) == p[n].get(w, 0), (n, w)
            coefficient_cases += 1
    totals = [sum(x.values()) for x in p]
    assert totals[3:12] == [4, 9, 16, 22, 36, 65, 112, 186, 309]
    for n in range(8, 66):
        assert totals[n] == totals[n - 1] + totals[n - 3] + totals[n - 4] + totals[n - 5]
    print('VERIFY_OK',
          'bruteforce_labelings_n=3..11', labeling_cases,
          'independent_defender_subsets_n=3..18', subset_cases,
          'explicit_coefficients_n=3..45', coefficient_cases,
          'recurrence_and_support_n=3..65', 'PASS')


if __name__ == '__main__':
    run()
