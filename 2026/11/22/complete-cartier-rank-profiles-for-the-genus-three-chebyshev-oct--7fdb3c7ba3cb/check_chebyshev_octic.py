#!/usr/bin/env python3
"""Exact finite checks for the genus-three Chebyshev octic Cartier profile.

The proof for all primes uses a tame-involution quotient and modular-residue
sparsity. This script independently tests characteristic-p Hasse-Witt matrices
at every prime from 5 to 199, without floating point arithmetic.
"""
from math import comb

COEFFICIENTS = [2, 0, -16, 0, 20, 0, -8, 0, 1]
EXPECTED = {
    1: (3, 3, 3, 0),
    3: (2, 1, 1, 1),
    5: (1, 0, 0, 2),
    7: (2, 2, 2, 1),
    9: (1, 1, 1, 2),
    11: (2, 1, 1, 1),
    13: (1, 0, 0, 2),
    15: (0, 0, 0, 3),
}


def prime(p):
    return p > 1 and all(p % d for d in range(2, int(p ** .5) + 1))


def coeff_power(p):
    a = [1]
    for _ in range((p - 1) // 2):
        b = [0] * (len(a) + 8)
        for i, v in enumerate(a):
            for j in (0, 2, 4, 6, 8):
                b[i + j] = (b[i + j] + v * COEFFICIENTS[j]) % p
        a = b
    return a


def mul(A, B, p):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) % p
             for j in range(3)] for i in range(3)]


def rank(A, p):
    A = [[x % p for x in row] for row in A]
    r = 0
    for j in range(3):
        z = next((i for i in range(r, 3) if A[i][j]), None)
        if z is None:
            continue
        A[r], A[z] = A[z], A[r]
        inv = pow(A[r][j], -1, p)
        A[r] = [inv * v % p for v in A[r]]
        for i in range(3):
            if i == r:
                continue
            t = A[i][j]
            A[i] = [(v - t * w) % p for v, w in zip(A[i], A[r])]
        r += 1
    return r


def arrows(residue):
    out = {}
    for n in (1, 2, 3):
        j = (residue * n) % 16
        if j in (1, 2, 3, 5, 6, 7):
            out[n] = min(j, 8 - j)
    return out


def graph_ranks(residue):
    d = arrows(residue)
    live = set(d)
    result = []
    for _ in range(3):
        result.append(len(live))
        live = {n for n in live if d[n] in live}
    return tuple(result)


def main():
    classes = {r: graph_ranks(r) for r in EXPECTED}
    for r, vals in classes.items():
        assert vals == EXPECTED[r][:3], (r, vals, EXPECTED[r])
    primes = [p for p in range(5, 200) if prime(p)]
    for p in primes:
        c = coeff_power(p)
        H = [[c[p * (i + 1) - (j + 1)] for j in range(3)]
             for i in range(3)]
        R1 = rank(H, p)
        H2 = mul(H, H, p)
        R2 = rank(H2, p)
        H3 = mul(H2, H, p)
        R3 = rank(H3, p)
        target = EXPECTED[p % 16]
        assert (R1, R2, R3, 3 - R1) == target, (p, (R1, R2, R3), target)
    print('PASS: eight residue classes; {} primes; exact Hasse-Witt ranks and a-numbers'.format(len(primes)))
    for r in sorted(EXPECTED):
        print('p mod 16 = {:2d}: arrows={}, rank profiles={}, p-rank={}, a={}'.format(
            r, arrows(r), EXPECTED[r][:3], EXPECTED[r][2], EXPECTED[r][3]))


if __name__ == '__main__':
    main()
