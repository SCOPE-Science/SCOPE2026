#!/usr/bin/env python3
"""Independent finite checks for cyclic fibers of the difference sliding-block code.

Run: python3 checker.py   (Python standard library only).
The checker confirms finite cases; the all-parameter result has a separate proof.
"""
import itertools
import math
from collections import Counter


def mobius(n):
    p = 2
    mu = 1
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            mu = -mu
        p += 1
    return -mu if n > 1 else mu


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def fixed_fibers(k, n, d, y, t):
    g = math.gcd(n, d)
    h = math.gcd(t, d // g)
    S = [sum(y[i] for i in range(r, n, g)) for r in range(g)]
    m = k // math.gcd(k, *S)
    return k ** (g * h) if (t // h) % m == 0 else 0


def minimum_inflation(k, n, d, y):
    g = math.gcd(n, d)
    S = [sum(y[i] for i in range(r, n, g)) for r in range(g)]
    m = k // math.gcd(k, *S)
    b = d // g
    v = m
    for p in range(2, m + 1):
        if m % p == 0 and all(p % u for u in range(2, math.isqrt(p) + 1)):
            while b % p == 0:
                b //= p
                v *= p
    return v


def enumerate_periods(k, n, d, y):
    counts = Counter()
    for prefix in itertools.product(range(k), repeat=d):
        sequence = list(prefix)
        for i in range(k * d * n + d):
            sequence.append((sequence[i] + y[i % n]) % k)
        for t in range(1, k * d + 1):
            N = n * t
            if all(sequence[i + N] == sequence[i] for i in range(d)):
                counts[t] += 1
                break
        else:
            raise AssertionError((k, n, d, y, prefix))
    return counts


def jordan(g, m):
    answer = m ** g
    for p in range(2, m + 1):
        if m % p == 0 and all(p % u for u in range(2, math.isqrt(p) + 1)):
            answer = answer // (p ** g) * (p ** g - 1)
    return answer


def main():
    cases = 0
    fibers = 0
    mixed = 0
    for k in (2, 3, 4):
        for d in range(1, 6):
            if k ** d > 400:
                continue
            for n in range(1, 7):
                for y in itertools.product((0, 1), repeat=n):
                    if any(n % p == 0 and y == y[:p] * (n // p)
                           for p in range(1, n)):
                        continue
                    counts = enumerate_periods(k, n, d, y)
                    fibers += k ** d
                    for t in range(1, k * d + 1):
                        exact_fixed = fixed_fibers(k, n, d, y, t)
                        brute_fixed = sum(c for p, c in counts.items() if t % p == 0)
                        assert exact_fixed == brute_fixed, (k, n, d, y, t)
                        mobius_count = sum(mobius(t // u) * fixed_fibers(k, n, d, y, u)
                                           for u in divisors(t))
                        assert mobius_count == counts[t], (k, n, d, y, t)
                    assert min(counts) == minimum_inflation(k, n, d, y)
                    if len(counts) > 1:
                        mixed += 1
                    cases += 1
    distributions = 0
    for k in range(2, 6):
        for n in range(1, 6):
            for d in range(1, 6):
                if k ** n > 2000:
                    continue
                g = math.gcd(n, d)
                empirical = Counter()
                b = d // g
                for y in itertools.product(range(k), repeat=n):
                    S = [sum(y[i] for i in range(r, n, g)) for r in range(g)]
                    m = k // math.gcd(k, *S)
                    empirical[m] += 1
                for m in divisors(k):
                    expected = k ** (n - g) * jordan(g, m)
                    assert empirical[m] == expected, (k, n, d, m, empirical[m], expected)
                distributions += 1
    print(f'PASS: {cases} primitive-target cases; {fibers} complete enumerated fibers; '
          f'{mixed} multi-period spectra; {distributions} all-output distributions')
    for k, n, d, y in [(3, 1, 4, (1,)), (2, 1, 4, (1,))]:
        print('Example', (k,n,d,y), sorted(enumerate_periods(k,n,d,y).items()))


if __name__ == '__main__':
    main()
