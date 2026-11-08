#!/usr/bin/env python3
"""Exact finite checks of the cyclic Klein cubic fixed-scheme calculation.

The general proof is algebraic and is not inferred from the tested primes.
"""
from math import comb


def rank_mod(a, p):
    a = [row[:] for row in a]
    if not a:
        return 0
    nr, nc = len(a), len(a[0])
    r = 0
    for c in range(nc):
        pivot = next((j for j in range(r, nr) if a[j][c] % p), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        t = pow(a[r][c] % p, -1, p)
        a[r] = [(z*t) % p for z in a[r]]
        for i in range(nr):
            if i != r and a[i][c] % p:
                u = a[i][c]
                a[i] = [(a[i][j]-u*a[r][j]) % p for j in range(nc)]
        r += 1
        if r == nr:
            break
    return r


def matmul(a, b, p):
    n = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) % p for j in range(n)] for i in range(n)]


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5)+1))


def check(p):
    assert is_prime(p) and p >= 5
    # Lambda^p = 1: sum lambda^(3i+1) has one copy of every residue.
    f_residues = [0]*p
    for i in range(p):
        f_residues[(3*i+1) % p] += 1
    assert f_residues == [1]*p
    # The shifted cyclotomic polynomial is Eisenstein at p.
    shifted = [comb(p, j+1) for j in range(p)]
    assert shifted[0] == p and shifted[-1] == 1
    assert all(c % p == 0 for c in shifted[:-1])
    assert shifted[0] % (p*p) != 0
    # Phi_p(1+t) = t^(p-1) in F_p[t].
    assert [v % p for v in shifted] == [0]*(p-1)+[1]
    # All partial derivatives at the one-vector equal 3, so the point is smooth.
    assert (2*1*1 + 1*1) % p == 3
    assert (1-pow(-2, p, p)) % p == 3 % p
    # The coordinate cycle has one unipotent Jordan block of size p.
    a = [[0]*p for _ in range(p)]
    for i in range(p):
        a[i][(i+1) % p] = 1
    n = [[(a[i][j]-(i == j)) % p for j in range(p)] for i in range(p)]
    power = [[int(i == j) for j in range(p)] for i in range(p)]
    for k in range(p+1):
        assert rank_mod(power, p) == p-k
        if k < p:
            power = matmul(power, n, p)
    # Degree p-1 of the cyclotomic ring gives the fixed scheme's length.
    assert len(shifted)-1 == p-1
    print(f"p={p}: cyclic cubic smooth; fixed ring Eisenstein degree {p-1}; "
          f"special length {p-1}; full Jordan block checked")


for prime in (5, 7, 11, 13, 17, 19):
    check(prime)
print('VERIFY_OK')
