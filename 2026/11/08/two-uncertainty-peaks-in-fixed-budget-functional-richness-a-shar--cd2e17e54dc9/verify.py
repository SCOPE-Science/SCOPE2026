#!/usr/bin/env python3
"""Exact checks for fixed-budget functional-richness variance.

Run: python3 verify.py
Requires only the Python 3 standard library.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def partitions(n, lower=1):
    """All nondecreasing positive-integer partitions of n, exactly once."""
    if n == 0:
        yield ()
        return
    for first in range(lower, n + 1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def omit_ratio(remaining, population, taken):
    if taken < 0 or taken > remaining:
        return Fraction(0)
    return Fraction(comb(remaining, taken), comb(population, taken))


def variance_formula(profile, taken):
    population = sum(profile)
    absences = [omit_ratio(population - size, population, taken)
                for size in profile]
    answer = sum((p * (1 - p) for p in absences), Fraction(0))
    for i in range(len(profile)):
        for j in range(i):
            joint = omit_ratio(population - profile[i] - profile[j],
                               population, taken)
            answer += 2 * (joint - absences[i] * absences[j])
    return answer


def variance_direct(profile, taken):
    population = sum(profile)
    group_of = []
    for i, size in enumerate(profile):
        group_of.extend([i] * size)
    totals = [len({group_of[x] for x in subset})
              for subset in combinations(range(population), taken)]
    first = Fraction(sum(totals), len(totals))
    second = Fraction(sum(t * t for t in totals), len(totals))
    return second - first * first


def has_valley(sequence):
    slopes = [int(b > a) - int(b < a)
              for a, b in zip(sequence, sequence[1:])]
    nonzero = [direction for direction in slopes if direction]
    return any(a == -1 and b == 1
               for a, b in zip(nonzero, nonzero[1:]))


def family_formula(m, k):
    """Independent absent-group derivation for (1,m,m), k>=2."""
    n = 2*m + 1
    q0 = Fraction(n-k, n)
    big = omit_ratio(m+1, n, k)
    singleton_big = omit_ratio(m, n, k)
    return q0 * (1-q0) + 2*big - 4*big*big + 4*singleton_big - 4*q0*big


def family_polynomial(m):
    return 5*m**4 - 42*m**3 + 123*m**2 - 94*m + 24


def family_peak_numerator(m):
    t = comb(2*m+1, m)
    return (2*t*t - t*(10*m**3 + 15*m**2 + 5*m)
            + 4*m**6 + 28*m**5 + 61*m**4
            + 58*m**3 + 25*m**2 + 4*m)


def main():
    examined = 0
    for n in range(2, 13):
        for profile in partitions(n):
            if len(profile) < 2:
                continue
            examined += 1
            values = [variance_formula(profile, k) for k in range(n + 1)]
            assert not has_valley(values), (n, profile)
    assert examined == 259, examined
    exceptions = []
    total_profiles = 0
    for profile in partitions(13):
        if len(profile) < 2:
            continue
        total_profiles += 1
        values = [variance_formula(profile, k) for k in range(14)]
        if has_valley(values):
            exceptions.append(profile)
    assert total_profiles == 100 and exceptions == [(1, 6, 6)]

    witness = (1, 6, 6)
    exact = [variance_formula(witness, k) for k in range(14)]
    assert exact == [variance_direct(witness, k) for k in range(14)]
    assert exact[3] == Fraction(5430, 20449)
    assert exact[4] == Fraction(5106, 20449)
    assert exact[5] == Fraction(45410, 184041)
    assert exact[6] == Fraction(184157, 736164)
    assert exact[7] == Fraction(183017, 736164)
    assert exact[2] < exact[3] > exact[4] > exact[5] < exact[6] > exact[7]

    direct_comparisons = 0
    for n in range(2, 9):
        for profile in partitions(n):
            if len(profile) < 2:
                continue
            for k in range(n + 1):
                assert variance_formula(profile, k) == variance_direct(profile, k)
                direct_comparisons += 1

    family_checks = 0
    for m in range(6, 101):
        n = 2*m + 1
        a = variance_formula((1, m, m), 3)
        b = variance_formula((1, m, m), 4)
        c = variance_formula((1, m, m), m-1)
        d = variance_formula((1, m, m), m)
        assert a == family_formula(m, 3) and b == family_formula(m, 4)
        assert c == family_formula(m, m-1) and d == family_formula(m, m)
        assert a-b == Fraction(family_polynomial(m), 4*(2*m-1)**2*n**2)
        t = comb(n, m)
        assert d-c == Fraction(family_peak_numerator(m), t*t*n*n)
        assert a > b and d > c
        assert t > Fraction(10*m**3+15*m**2+5*m, 2)
        family_checks += 1

    print('PASS: 259 nontrivial partitions of n<=12 (all unimodal)')
    print('PASS: exactly one exception among 100 nontrivial partitions of n=13: (1,6,6)')
    print('PASS: direct exact survivor-state count at all 14 witness budgets')
    print('PASS: {} further independent direct-enumeration variance comparisons'.format(direct_comparisons))
    print('PASS: {} exact family formula and sign checks, m=6..100'.format(family_checks))
    print('NOTE: universal m>=6 statements use analytic inequalities in RESULT.md, not finite testing')


if __name__ == '__main__':
    main()
