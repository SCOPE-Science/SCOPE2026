#!/usr/bin/env python3
"""Independent exact-arithmetic checks for fourth-power Franel recurrence rigidity."""
from fractions import Fraction
from math import comb, factorial


def f4(n):
    return sum(comb(n, k) ** 4 for k in range(n + 1))


def solution(u, v, N):
    a = [Fraction(u), Fraction(v)]
    for n in range(1, N):
        coeff = 2 * (6 * n**3 + 9 * n**2 + 5 * n + 1)
        back = 4 * n * (4 * n - 1) * (4 * n + 1)
        a.append((coeff * a[n] + back * a[n-1]) / (n+1)**3)
    return a


def p_valuation(z, p):
    if not z:
        raise ValueError('valuation of zero')
    v = 0
    while z % p == 0:
        z //= p
        v += 1
    return v


def primes_through(n):
    return [p for p in range(5, n+1)
            if all(p % d for d in range(2, int(p**0.5) + 1))]


def run():
    N = 96
    H = [f4(n) for n in range(N+1)]
    assert H[:6] == [1, 2, 18, 164, 1810, 21252]
    assert solution(1, 2, N) == H
    pairs = [(0, 1), (2, 5), (1, 2), (-3, 7), (24, 23), (0, 5), (3, 3)]
    for u, v in pairs:
        a = solution(u, v, N)
        W = Fraction(v-2*u)
        for n in range(N):
            assert H[n]*a[n+1] - H[n+1]*a[n] == W, (u, v, n)
            if v == 2*u:
                assert a[n] == u*H[n]
            if n+1 < N:
                j = n+1
                W *= Fraction(-4*j*(4*j-1)*(4*j+1), (j+1)**3)
    primes = primes_through(89)
    for p in primes:
        P = 1
        for j in range(1, p):
            P *= j*(4*j-1)*(4*j+1)
        assert p_valuation(P,p) == 2
        assert 3*p_valuation(factorial(p),p) == 3
        # At the first obstructing prime, the Wronskian has denominator p.
        u, v = 0, 1
        a = solution(u, v, p)
        w = H[p-1]*a[p] - H[p]*a[p-1]
        assert p_valuation(w.denominator, p) - p_valuation(w.numerator, p) == 1
    print('VERIFY_OK recurrence_depth=96 initial_pairs=7 Wronskian_checks=672')
    print('PRIME_OBSTRUCTIONS_OK primes=%d largest_prime=%d' % (len(primes),primes[-1]))

if __name__ == '__main__':
    run()
