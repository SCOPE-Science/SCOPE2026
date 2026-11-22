"""Independent exact finite-state checks for the critical SIS importation law.

Usage: python VERIFY.py
Only the Python standard library is required.
"""
from fractions import Fraction
from math import comb, exp, log


def rising(a, k):
    z = Fraction(1)
    for j in range(k):
        z *= a + j
    return z


def weights_count(n, a):
    # Stationary weights from the one-dimensional birth/death recurrence.
    w = [Fraction(1)]
    for k in range(n):
        w.append(w[-1] * Fraction(n-k, n*(k+1)) * (k+a))
    return w


def weights_configs(n, a):
    # Independently constructed weights on every spin configuration.
    raw = {}
    for mask in range(1 << n):
        k = mask.bit_count()
        raw[mask] = rising(a, k) / (n ** k)
    return raw


def verify_exact():
    for n in range(2, 8):
        for a in (Fraction(1, 3), Fraction(2, 3), Fraction(3, 2)):
            w = weights_count(n, a)
            wc = weights_configs(n, a)
            for k in range(n+1):
                assert w[k] == sum(v for mask, v in wc.items() if mask.bit_count() == k)
            # Every individual transition satisfies the stationary flow identity.
            for mask, val in wc.items():
                k = mask.bit_count()
                for i in range(n):
                    bit = 1 << i
                    if not mask & bit:
                        birth_rate = (k+a) / n
                        reverse_val = wc[mask | bit]
                        assert val * birth_rate == reverse_val
    for a in (Fraction(1, 4), Fraction(2, 3), Fraction(5, 2)):
        partial = Fraction(0)
        for m in range(1, 40):
            if m == 1:
                partial = 1
            partial += rising(a, m) / rising(Fraction(1), m)
            exact = rising(1+a, m) / rising(Fraction(1), m)
            assert partial == exact
    return 'exact finite-state checks: PASS'


def numerical_distribution(n, c):
    a = c / log(n)
    w = 1.0
    z = 1.0
    cutoff = int(n**0.25)
    low = 1.0
    for k in range(n):
        w *= ((n-k)/n)*((k+a)/(k+1))
        z += w
        if k+1 <= cutoff:
            low += w
    return 1/z, low/z


def verify_asymptotic_sanity():
    # Numerical confirmation only; the proof controls all n and is separate.
    for c in (0.5, 2.0):
        expected0, expectedquarter = exp(-c/2), exp(-c/4)
        e = []
        for n in (1_000, 10_000, 200_000):
            p0, fq = numerical_distribution(n, c)
            e.append((abs(p0-expected0), abs(fq-expectedquarter)))
        assert e[-1][0] < e[0][0]
        assert e[-1][0] < 0.04
        assert e[-1][1] < 0.015
    return 'asymptotic finite-size sanity checks: PASS (not a proof)'


if __name__ == '__main__':
    print(verify_exact())
    print(verify_asymptotic_sanity())
