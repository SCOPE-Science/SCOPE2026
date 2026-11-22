"""Reproduce the finite tests for squarefree square-product triples.

This program supplies finite checks only; the asymptotic theorem requires the
proof from geometry of numbers and a local sieve.
"""
from math import gcd, isqrt


def squarefree_flags(bound):
    good = [True] * (bound + 1)
    good[0] = False
    for d in range(2, isqrt(bound) + 1):
        sq = d * d
        for j in range(sq, bound + 1, sq):
            good[j] = False
    return good


def count_by_factors(bound):
    """Unique factorization a=uv, b=uw, c=vw with u<v<w."""
    sf = squarefree_flags(bound)
    total = 0
    for v in range(2, isqrt(bound) + 1):
        if not sf[v]:
            continue
        us = [u for u in range(1, v) if sf[u] and gcd(u, v) == 1]
        for w in range(v + 1, bound // v + 1):
            if sf[w] and gcd(v, w) == 1:
                total += sum(gcd(u, w) == 1 for u in us)
    return total


def count_by_numbers(bound):
    """Independently test every increasing triple of squarefree numbers."""
    sf = squarefree_flags(bound)
    vals = [a for a in range(2, bound + 1) if sf[a]]
    total = 0
    for i, a in enumerate(vals):
        for j in range(i + 1, len(vals)):
            b = vals[j]
            ab = a * b
            for c in vals[j + 1:]:
                z = ab * c
                if isqrt(z) ** 2 == z:
                    total += 1
    return total


def prime_sieve(bound):
    ok = [True] * (bound + 1)
    ok[0] = ok[1] = False
    for p in range(2, isqrt(bound) + 1):
        if ok[p]:
            for a in range(p*p, bound + 1, p):
                ok[a] = False
    return [p for p in range(2, bound + 1) if ok[p]]


def local_constant(prime_limit=100000):
    density = 1.0
    for p in prime_sieve(prime_limit):
        density *= (1-1/p)**3 * (1+3/p)
    return 2*density/3


if __name__ == '__main__':
    small = (30, 100, 200, 300)
    large = (1000, 3000, 10000)
    for n in small:
        a, b = count_by_factors(n), count_by_numbers(n)
        assert a == b, (n, a, b)
        print(f'crosscheck N={n}: factor={a}, direct={b} PASS')
    k = local_constant()
    print(f'approximate leading constant at primes <= 100000: {k:.12f}')
    for n in large:
        a = count_by_factors(n)
        print(f'N={n}: count={a}, count/N^(3/2)={a/n**1.5:.9f}')
