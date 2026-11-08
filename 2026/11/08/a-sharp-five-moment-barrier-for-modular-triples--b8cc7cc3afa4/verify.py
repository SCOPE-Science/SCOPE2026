#!/usr/bin/env python3
"""Reproducible finite checks of the modular three-summand moment threshold."""
from itertools import combinations_with_replacement

def expected(n):
    if n == 2: return 1
    if n in (3, 6): return 2
    if n % 9 == 0: return 5
    return 3

def signature(t, n, depth=11):
    return tuple(sum(pow(x, j, n) for x in t) % n for j in range(1, depth + 1))

def brute_threshold(n):
    sigs = [signature(t, n) for t in combinations_with_replacement(range(n), 3)]
    for m in range(1, 6):
        d = {}
        if all(d.setdefault(s[:m], s) == s for s in sigs):
            return m, len(sigs)
    raise AssertionError(('missing-bound', n))

def roots_hensel(k):
    n = 3**k
    u = 3**(k-1)
    roots = []
    for residue in (0,1,2):
        r = residue
        for t in range(1,k):
            modulus = 3**(t+1)
            r = next(r + digit*3**t for digit in range(3) if ((r + digit*3**t)**3 -(r + digit*3**t) +u) % modulus == 0)
        roots.append(r % n)
    return roots

def main():
    total = 0
    for n in range(2, 61):
        m, checked = brute_threshold(n)
        assert m == expected(n), (n, m, expected(n))
        total += checked
    for k in range(2, 8):
        n = 3**k
        a=(0,1,n-1)
        b=roots_hensel(k)
        assert len(set(b)) == 3
        assert all(sum(pow(x, j, n) for x in a)%n == sum(pow(x,j,n) for x in b)%n for j in range(1,5))
        assert sum(pow(x,5,n) for x in a)%n != sum(pow(x,5,n) for x in b)%n
    for k in range(2, 14):
        n=2**k
        u=n//2
        a=(0,0,1+u)
        b=(0,1,u)
        assert all(sum(pow(x,j,n) for x in a)%n == sum(pow(x,j,n) for x in b)%n for j in (1,2))
        assert sum(pow(x,3,n) for x in a)%n != sum(pow(x,3,n) for x in b)%n
    for p in (5,7,11,13,17,19):
        for k in range(1,5):
            n=p**k
            inv3=pow(3,-1,n)
            a=(0,0,1)
            b=(2*inv3 % n,2*inv3 % n,-inv3 % n)
            assert all(sum(pow(x,j,n) for x in a)%n == sum(pow(x,j,n) for x in b)%n for j in (1,2))
            assert sum(pow(x,3,n) for x in a)%n != sum(pow(x,3,n) for x in b)%n
    print(f'VERIFY_OK moduli=2..60 unordered_triples={total} tested_powers=1..11 hensel_levels_3adic=2..7 dyadic_levels=2..13 large_prime_witnesses=24')
if __name__ == '__main__': main()
