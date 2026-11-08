#!/usr/bin/env python3
"""Exact checks for two- and three-primary fourth-power Pell sliding sums.
This script is finite verification; the accompanying mathematical proof is infinite.
"""
from math import comb, gcd
from functools import reduce


def valuation(n, p):
    assert n > 0
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def quartic_form_coeffs(forms):
    # coefficient of x^(4-i) y^i, i=0,...,4
    return [sum(comb(4, i) * a ** (4 - i) * b ** i for a, b in forms)
            for i in range(5)]


def test_form():
    # Four successive Pell terms from initial pair (x,y).
    forms = [(0, 1), (1, 2), (2, 5), (5, 12)]
    assert quartic_form_coeffs(forms) == [642, 6168, 22224, 35592, 21378]
    assert all(c % 6 == 0 for c in quartic_form_coeffs(forms))
    # Four-step vector map, (X_(n+4), X_(n+5)) = M (X_n,X_(n+1)).
    # Starting from (x,y), four successive recurrence updates:
    pair = ((1, 0), (0, 1))
    for _ in range(4):
        x, y = pair
        pair = (y, (x[0] + 2*y[0], x[1] + 2*y[1]))
    assert pair == ((5, 12), (12, 29))
    return quartic_form_coeffs(forms)


def test_sequences():
    seqs = {}
    for name, initial in [('P', [0, 1]), ('Q', [1, 1])]:
        seq = initial[:]
        for _ in range(625):
            seq.append(2 * seq[-1] + seq[-2])
        seqs[name] = seq
    ntests = 0
    for name, seq in seqs.items():
        # prefix fourth-power sums give exact window sums.
        prefix = [0]
        for value in seq:
            prefix.append(prefix[-1] + value ** 4)
        for k in range(1, 301):
            windows = [prefix[n + k + 1] - prefix[n + 1] for n in range(12)]
            observed = reduce(gcd, windows)
            e2 = (valuation(k, 2) - 1 if k % 4 == 0 else 0) if name == 'P' else valuation(k, 2)
            e3 = 1 + valuation(k, 3) if k % 4 == 0 else 0
            assert (valuation(observed, 2), valuation(observed, 3)) == (e2, e3), (name, k, observed)
            ntests += 1
        for m in range(1, 151):
            for n in range(7):
                window = prefix[n + 4*m + 1] - prefix[n + 1]
                one_block = prefix[n + 5] - prefix[n + 1]
                assert (window - m * one_block) % (2 ** (valuation(m, 2) + 3)) == 0
                assert (window - m * one_block) % (3 ** (valuation(m, 3) + 2)) == 0
                ntests += 1
    return ntests


if __name__ == '__main__':
    coeffs = test_form()
    count = test_sequences()
    print('FORM_COEFFICIENTS', coeffs)
    print('CHECKED_CASES', count)
    print('TWO_THREE_ADIC_CHECKS_PASS')
