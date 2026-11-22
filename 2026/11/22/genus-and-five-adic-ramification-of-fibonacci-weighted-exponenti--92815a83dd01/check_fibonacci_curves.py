#!/usr/bin/env python3
"""Exact integer consistency checks for Fibonacci-weighted Kummer curves.

Run with Python 3. No dependencies beyond the standard library.
Finite checks complement, and do not replace, Riemann--Hurwitz and Lucas proofs.
"""
from math import comb, gcd, prod


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def luc(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def ord5(m):
    if m == 0:
        raise ValueError('valuation of zero not used')
    e = 0
    while m % 5 == 0:
        m //= 5
        e += 1
    return e


def digits5(n):
    ds = []
    while n:
        ds.append(n % 5)
        n //= 5
    return ds or [0]


def full_ramification_criterion(k):
    n = 2*k + 1
    while n % 5 == 0:
        n //= 5
    return n in (1, 3)


def counts(k):
    n = 2*k
    N = 5 ** (k-1)
    val = [comb(n, j) for j in range(n+1)]
    gcds = [gcd(N, c) for c in val]
    s = sum(gcds)
    numerator = (n-1)*N - s
    assert numerator % 2 == 0
    g = 1+numerator//2
    total = sum(v == 1 for v in gcds)
    digit_count = prod(d+1 for d in digits5(n))
    assert total == digit_count
    assert (total == n+1) == full_ramification_criterion(k)
    assert all(v < N for v in gcds)
    return g, s, total


def check_log_identity():
    trials = 0
    for k in range(1, 13):
        for n in range(1, 17):
            lhs = 5 ** k * fib(n) ** (2*k)
            rhs = (-1)**(k+k*n) * comb(2*k, k)
            rhs += sum((-1)**(j+j*n) * comb(2*k, j)
                       * luc(2*(k-j)*n) for j in range(k))
            assert lhs == rhs, (k, n, lhs, rhs)
            trials += 1
    return trials


def check_symmetry():
    trials = 0
    for k in range(1, 101):
        n = 2*k
        val = [(-1)**(j+1)*comb(n, j) for j in range(k)]
        center = (-1)**(k+1)*comb(n, k)
        assert 2*sum(val)+center == 0  # infinity valuation zero
        trials += 1
    return trials


def check_genus():
    trials = 0
    for k in range(2, 100):
        g, s, total = counts(k)
        N = 5**(k-1)
        assert g >= 0
        assert g <= (2*k-1)*(N-1)//2
        assert g == 1 + ((2*k-1)*N - sum(5**ord5(comb(2*k,j))
                                            for j in range(2*k+1)))//2
        assert (g == (2*k-1)*(N-1)//2) == full_ramification_criterion(k)
        trials += 1
    return trials


def main():
    total1 = check_log_identity()
    total2 = check_symmetry()
    total3 = check_genus()
    expected = {2:(6,5,5), 3:(54,19,4), 4:(432,13,8),
                5:(2792,43,3), 7:(101556,15,15),
                12:(561523426,25,25)}
    for k, result in expected.items():
        assert counts(k) == result, (k, counts(k), result)
    print('PASS: %d independent Fibonacci-Lucas weight identities' % total1)
    print('PASS: %d rational-divisor infinity cancellations' % total2)
    print('PASS: %d genus, Lucas-digit and full-inertia comparisons' % total3)
    print('PASS: %d exact genus/branch-count fixtures' % len(expected))
    for k in range(2, 9):
        g, s, full = counts(k)
        print('k=%d: degree=%d genus=%d gcd_sum=%d fully_ramified=%d/%d' %
              (k, 5**(k-1), g, s, full, 2*k+1))


if __name__ == '__main__':
    main()
