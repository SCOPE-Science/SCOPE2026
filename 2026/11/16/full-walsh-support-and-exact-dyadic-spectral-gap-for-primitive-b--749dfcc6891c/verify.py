#!/usr/bin/env python3
"""Exact integer checks for primitive binary word Walsh multipliers.
The finite tests corroborate, but do not replace, the infinite proof.
"""
from math import prod


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def rad(n):
    d, r = 2, 1
    while d * d <= n:
        if n % d == 0:
            r *= d
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        r *= n
    return r


def mobius(n):
    d, sign = 2, 1
    while d * d <= n:
        if n % d == 0:
            n //= d
            sign = -sign
            if n % d == 0:
                return 0
        d += 1
    if n > 1:
        sign = -sign
    return sign


def periodic(x, n, d):
    return all(((x >> i) & 1) == ((x >> (i % d)) & 1) for i in range(n))


def parity_annihilator(b, n, d):
    return all(sum((b >> i) & 1 for i in range(j, n, d)) % 2 == 0
               for j in range(d))


def mobius_multiplier(b, n):
    return sum(mobius(n // d) * (1 << d)
               for d in divisors(n) if parity_annihilator(b, n, d))


def primitive_mask(n):
    proper = divisors(n)[:-1]
    return [int(not any(periodic(x, n, d) for d in proper))
            for x in range(1 << n)]


def fwht_inplace(v):
    N, h = len(v), 1
    while h < N:
        for i in range(0, N, h << 1):
            for j in range(i, i+h):
                a, b = v[j], v[j+h]
                v[j], v[j+h] = a+b, a-b
        h <<= 1


def main():
    for n in range(2, 17):
        m, r = n // rad(n), rad(n)
        f = primitive_mask(n)
        w = f[:]
        fwht_inplace(w)
        support = [b for b, x in enumerate(w) if x != 0]
        assert len(support) == (1 << (n - m))
        assert w[0] == sum(mobius(n // d)*(1 << d) for d in divisors(n))
        assert min(abs(t) for t in w if t) == (1 << m)
        assert w[(1 << 0) | (1 << m)] == mobius(r) * (1 << m)
        for b, val in enumerate(w):
            in_H = parity_annihilator(b, n, m)
            assert (val != 0) == in_H, (n,b,val)
            if val:
                assert val % (1 << (m+1)) == (1 << m)
            assert val == mobius_multiplier(b,n), (n,b,val)
        # Test every translation in the claimed stabilizer for n<=8.
        if n <= 8:
            for t in range(1 << n):
                translation_preserves = all(f[x] == f[x ^ t] for x in range(1 << n))
                is_periodic = periodic(t, n, m)
                assert translation_preserves == is_periodic, (n,t)
    print('PRIMITIVE_BINARY_WALSH_EXACT_PASS lengths=2..16; all frequencies and stabilizers<=8')

if __name__ == '__main__':
    main()
