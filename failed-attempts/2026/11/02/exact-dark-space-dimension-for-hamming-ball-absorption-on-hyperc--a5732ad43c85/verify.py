#!/usr/bin/env python3
"""Exact finite-dimensional checks for the hypercube Hamming-ball sink theorem.
Run: python3 verify.py. Python standard library only. No network or external data.
These finite checks supplement, and do not replace, the infinite-dimensional-parameter proof.
"""
from math import comb

PRIME = 1000003

def rank_mod(rows, modulus=PRIME):
    """Rank over GF(modulus) by incremental exact elimination."""
    basis = {}
    for raw in rows:
        v = [int(q) % modulus for q in raw]
        for piv, b in sorted(basis.items()):
            if v[piv]:
                factor = v[piv]
                v = [(a - factor * c) % modulus for a, c in zip(v, b)]
        nextpivot = next((j for j, q in enumerate(v) if q), None)
        if nextpivot is not None:
            inv = pow(v[nextpivot], -1, modulus)
            basis[nextpivot] = [q * inv % modulus for q in v]
    return len(basis)

def predicted_sector(d, r, weight):
    return comb(d, min(r, weight, d - weight))

def predicted_bright(d, r):
    return sum(predicted_sector(d, r, w) for w in range(d + 1))

def direct_walsh_sector_rank(d, r, w):
    words = range(1 << d)
    xs = [x for x in words if x.bit_count() <= r]
    fs = [s for s in words if s.bit_count() == w]
    return rank_mod([[(-1 if ((x & s).bit_count() % 2) else 1) for s in fs] for x in xs])

def direct_krylov_rank(d, r):
    N = 1 << d
    out = []
    for x in range(N):
        if x.bit_count() > r: continue
        v = [int(y == x) for y in range(N)]
        for _ in range(d+1):
            out.append(v)
            v = [sum(v[y ^ (1 << bit)] for bit in range(d)) % PRIME for y in range(N)]
    return rank_mod(out)

def cat(k):
    return comb(2*k,k)//(k+1)

assert predicted_bright(8, 2) == 158
checks = 0
for d in range(2, 9):
    for r in range(0, d + 1):
        for w in range(d + 1):
            observed = direct_walsh_sector_rank(d, r, w)
            expected = predicted_sector(d, r, w)
            assert observed == expected, ('Walsh', d,r,w,observed,expected)
            checks += 1
print('EXACT_WALSH_SECTORS', checks)
for d in range(2, 7):
    for r in range(d+1):
        observed = direct_krylov_rank(d,r)
        expected = predicted_bright(d,r)
        assert observed == expected, ('Krylov',d,r,observed,expected)
        checks += 1
print('EXACT_KRYLOV_CASES', sum(d+1 for d in range(2,7)))
for t in range(1,20):
    d=2*t
    r=t-1
    assert (1<<d)-predicted_bright(d,r)==cat(t)
    d=2*t+1
    assert (1<<d)-predicted_bright(d,r)==2*cat(t+1)
    checks+=2
for d in range(2,39):
    for r in range(d//2, d+1):
        assert predicted_bright(d,r)==(1<<d), ('threshold',d,r)
        checks+=1
print('VERIFY_OK checks='+str(checks))
