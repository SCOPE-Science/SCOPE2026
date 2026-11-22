#!/usr/bin/env python3
"""Reproduce golden-mean lexicographic width-three minimizer counts.

The finite exhaustive tests are checks, not substitutes for the all-length proof.
"""
from collections import Counter
from decimal import Decimal, getcontext
from itertools import product


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def admissible(n):
    for letters in product('01', repeat=n):
        s = ''.join(letters)
        if '11' not in s:
            yield s


def brute_charge(s, k):
    kmers = [s[i:i + k] for i in range(4)]
    before = min(range(3), key=lambda i: (kmers[i], i))
    after = min(range(1, 4), key=lambda i: (kmers[i], i))
    overall = min(range(4), key=lambda i: (kmers[i], i))
    assert (before != after) == (overall == 0 or overall == 3)
    return before != after


def structural_charge(s, k):
    if s[:2] == '00':
        return True
    if s[:3] == '100':
        return False
    if s[:3] == '010':
        return all(s[i] != s[i+1] for i in range(k+1))
    assert s[:4] == '1010'
    return not all(s[i] != s[i+1] for i in range(1, k+2))


def theoretical_end_counts(k):
    odd = k % 2
    return {
        ('0', '0'): fib(k + 2) + 1,
        ('0', '1'): fib(k + 1) + odd,
        ('1', '0'): fib(k) - odd,
        ('1', '1'): fib(k - 1) - (1 - odd),
    }


def run():
    getcontext().prec = 50
    phi = (Decimal(1) + Decimal(5).sqrt()) / 2
    total_examined = 0
    for k in range(1, 21):
        actual = Counter()
        endpoint_total = Counter()
        for s in admissible(k+3):
            endpoint_total[(s[0], s[-1])] += 1
            a = brute_charge(s, k)
            b = structural_charge(s, k)
            assert a == b, ('structural mismatch', k, s, a, b)
            if a:
                actual[(s[0], s[-1])] += 1
            total_examined += 1
        expected = theoretical_end_counts(k)
        assert dict(actual) == {key: value for key, value in expected.items() if value}, (k, actual, expected)
        assert sum(actual.values()) == 2*fib(k + 2) + fib(k - 1) + 1 - (k % 2 == 0), (k, actual)
        normalizer = (phi**2 * endpoint_total[('0', '0')]
                      + phi*(endpoint_total[('0', '1')] + endpoint_total[('1', '0')])
                      + endpoint_total[('1', '1')])
        assert abs(normalizer/((phi + 2)*phi**(k+2)) - 1) < Decimal('1e-45')
        weighted = (phi**2 * actual[('0', '0')]
                    + phi*(actual[('0', '1')] + actual[('1', '0')])
                    + actual[('1', '1')])
        density = weighted/((phi + 2)*phi**(k+2))
        formula = (2 + phi**(-(2*(k//2)+1)))/(phi+2)
        assert abs(density-formula) < Decimal('1e-45'), (k, density, formula)
    for k in range(2, 100):
        d = lambda j: (2+phi**(-(2*(j//2)+1)))/(phi+2)
        if k % 2 == 0:
            assert d(k) == d(k+1)
        else:
            assert d(k) > d(k+1)
    print('PASS: all admissible words at k=1..20; endpoint count, independent structural criterion, Parry weighted density; strict plateau through k=99')
    print('Examined:', total_examined, 'words')
    for k in (1,2,3,4,5,6,8,12,20):
        d=(2+phi**(-(2*(k//2)+1)))/(phi+2)
        print('k=',k,'density=',format(d,'.12f'),'endpoint_counts=',theoretical_end_counts(k))


if __name__ == '__main__':
    run()
