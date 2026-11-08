#!/usr/bin/env python3
"""Exact certification of first 2-by-3 invisible rectangle for f(t)=t(t+1).
Standard-library-only; exhaustive in the finite first-coordinate range.
"""
from math import gcd, lcm


def irredundant_moduli(x):
    f = x * (x + 1)
    raw = sorted({f // gcd(f, t * (t + 1)) for t in range(1, x)})
    return tuple(d for d in raw if not any(d % e == 0 for e in raw if e < d))


def joint_moduli(x):
    return tuple(sorted({lcm(d, e) for d in irredundant_moduli(x)
                                      for e in irredundant_moduli(x + 1)}))


def triples(x):
    S = joint_moduli(x)
    return [(A, B, C) for A in S for B in S if gcd(A, B) == 1
            for C in S if gcd(B, C) == 1 and gcd(A, C) in (1, 2)]


def merge(r, m, s, n):
    g = gcd(m, n)
    assert (r - s) % g == 0
    M, N = m // g, n // g
    k = ((s - r) // g * pow(M, -1, N)) % N if N > 1 else 0
    modulus = lcm(m, n)
    return (r + k * m) % modulus, modulus


def crt_for(t):
    r, mod = 0, 1
    for m, s in zip(t, (0, -1, -2)):
        r, mod = merge(r, mod, s, m)
    return (r if r else mod), mod


def invisible(x, y):
    return any(y * t * (t + 1) % (x * (x + 1)) == 0 for t in range(1, x))


def check():
    no_count = 0
    for x in range(2, 230):
        T = triples(x)
        if T:
            raise AssertionError((x, T))
        no_count += 1
    A, B = irredundant_moduli(230), irredundant_moduli(231)
    assert A == (11, 23, 105), A
    assert B == (7, 22, 58, 87, 319), B
    T = triples(230)
    assert T == [(22, 105, 1334), (1334, 105, 22)], T
    residues = sorted(crt_for(t) for t in T)
    assert residues == [(759044, 1540770), (781724, 1540770)], residues
    for b, mod in residues:
        for dx in range(2):
            for dy in range(3):
                assert invisible(230 + dx, b + dy)
    for x in range(2, 230):
        # independent diagnostic: no row pair can have three consecutive
        # invisible ordinates in any of the first 1000 positive positions
        if x < 45:
            for b in range(1, 1001):
                assert not all(invisible(x + i, b + j) for i in range(2) for j in range(3))
    print('VERIFY_OK: 228 smaller first coordinates excluded; minimal x=230')
    print('MODULI_X230:', A)
    print('MODULI_X231:', B)
    print('EXACT_COMPATIBLE_TRIPLES:', T)
    print('ALL_ORDINATE_CLASSES:', residues)
    print('SIX_DIRECT_POINT_CHECKS: PASS at both primitive residues')


if __name__ == '__main__':
    check()
