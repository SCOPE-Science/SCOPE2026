#!/usr/bin/env python3
"""Reconstruct the invariant golden-mean rotation on sequential bi-threshold sunlets.
Standard-library only. No external data or services.
"""
from math import isqrt
from collections import Counter


def independent_words(L):
    for w in range(1 << L):
        if all(not ((w >> i & 1) and (w >> ((i+1) % L) & 1)) for i in range(L)):
            yield w


def encode(n, w):
    L = n - 1
    x = 0
    for i in range(n):
        j = i % L
        C = (w >> j) & 1
        B = (w >> ((j - 1) % L)) & 1
        x |= (C | B) << i
        x |= C << (n + i)
    return x


def rotate(w, L):
    return (w >> 1) | ((w & 1) << (L - 1))


def F(n, x):
    # Rim positions 0...n-1; attached leaf at n+i. Sweep rim then leaves.
    for i in range(n):
        old = (x >> i) & 1
        count = old + ((x >> ((i - 1) % n)) & 1) + ((x >> ((i + 1) % n)) & 1) + ((x >> (n + i)) & 1)
        new = int(count >= (3 if old else 1))
        x = (x & ~(1 << i)) | (new << i)
    for i in range(n):
        j = n + i
        old = (x >> j) & 1
        count = old + ((x >> i) & 1)
        new = int(count >= (3 if old else 1))
        x = (x & ~(1 << j)) | (new << j)
    return x


def lucas(k):
    a, b = 2, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def mobius(k):
    primes = 0
    p = 2
    while p * p <= k:
        if k % p == 0:
            k //= p
            if k % p == 0:
                return 0
            primes += 1
        p += 1
    if k > 1:
        primes += 1
    return -1 if primes % 2 else 1


def primitive_states(d):
    return sum(mobius(d // e) * lucas(e) for e in range(1, d+1) if d % e == 0)


def check(n):
    L = n - 1
    wlist = list(independent_words(L))
    assert len(wlist) == lucas(L)
    E = set()
    periods = Counter()
    for w in wlist:
        x = encode(n, w)
        assert x not in E
        E.add(x)
        assert F(n, x) == encode(n, rotate(w, L)), (n,w)
        u = w
        for t in range(1, L+1):
            u = rotate(u, L)
            if u == w:
                periods[t] += 1
                break
        else:
            raise AssertionError((n, w))
    assert len(E) == lucas(L)
    for d in range(1, L+1):
        if L % d == 0:
            assert periods[d] == primitive_states(d), (n,d,periods[d],primitive_states(d))
    U = {((1 << n) - 1) | (b << n) for b in range(1 << n)}
    for x in U:
        assert F(n, x) == x ^ (((1 << n) - 1) << n)
    intersection = E & U
    assert len(intersection) == (2 if L % 2 == 0 else 0)
    union = E | U
    assert len(union) == (1 << n) + lucas(L) - len(intersection)
    assert all(F(n, x) in union for x in union)
    return len(E), len(U), len(union), dict(sorted(periods.items()))


def main():
    for n in range(3, 18):
        e, u, total, pd = check(n)
        print(f'n={n}: embedded={e}; leaf-flipping={u}; distinct={total}; rotation_period_states={pd}')
    print('PASS: exact coding, bijectivity, leaf involution, overlap, rotation-period census on n=3..17')

if __name__ == '__main__':
    main()
