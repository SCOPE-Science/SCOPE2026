#!/usr/bin/env python3
"""Exact stand-alone checks for all-weight enumerators of N_k and Z_k codes.

Use: python3 verify.py

No external dependencies. The defining codes are enumerated independently of the
closed-form coefficient computation. Finite checks supplement the symbolic proof.
"""
from itertools import product
from math import comb, gcd


def weight_enumerators(k, q):
    assert k >= 2 and q >= 2
    S = sum(comb(k, j) * gcd(q, j - 1) for j in range(k + 1))
    B = [0] * (2 * k + 1)
    H = [0] * (2 * k + 1)
    for r in range(k + 1):
        bnum = (q - 1)**r + (q - 1) * (-1)**r
        assert bnum % q == 0
        B[2*r] = comb(k, r) * (bnum // q)
        hnum = (q - 1) * 2**(k-r) * (q-2)**r + (-1)**r * (q*S - (2*q-1)*2**k)
        assert hnum % q == 0
        H[k+r] = comb(k, r) * (hnum // q)
    N = [B[i] + H[i] for i in range(2*k+1)]
    Z = [0] * (2*k+2)
    for i in range(2*k+1):
        Z[i] += B[i]
        Z[i+1] += H[i]
    return N, Z


def direct_enumerators(k, q):
    N = [0] * (2*k+1)
    Z = [0] * (2*k+2)
    for u in product(range(q), repeat=k):
        s = sum(u) % q
        w = sum(x != 0 for x in u) + sum((s-x) % q != 0 for x in u)
        N[w] += 1
        Z[w + (s != 0)] += 1
    return N, Z


def test():
    count = 0
    for q in range(2, 10):
        for k in range(2, 8):
            if q**k <= 100000:
                assert weight_enumerators(k, q) == direct_enumerators(k, q), (k, q)
                count += 1
    symbolic = 0
    for q in range(2, 31):
        for k in range(2, 51):
            n, z = weight_enumerators(k, q)
            assert all(isinstance(x, int) and x >= 0 for x in n+z)
            assert n[0] == z[0] == 1
            assert sum(n) == sum(z) == q**k
            S = sum(comb(k, j)*gcd(q, j-1) for j in range(k+1))
            # Theorem 5.3 in Imamura--Nakashima--Saito, full-support coefficient.
            full_z_num = (q-1)*(q-2)**k - (-2)**k*(2*q-1)
            assert full_z_num % q == 0
            full_z = full_z_num // q + (-1)**k * S
            assert z[2*k+1] == full_z
            full_n_num = (q-1)**k + (-1)**k*(q-1)
            assert full_n_num % q == 0
            assert n[2*k] == full_z + full_n_num//q
            assert min(i for i, x in enumerate(n) if i and x) == (k if k < 4 else 4)
            assert min(i for i, x in enumerate(z) if i and x) == (k+1 if k < 4 else 4)
            if k >= 5:
                assert n[4] == z[4] == comb(k, 2)*(q-1)
            symbolic += 1
    assert weight_enumerators(4, 2)[0] == [1,0,0,0,14,0,0,0,1]
    print(f"NZ_WEIGHT_ENUMERATORS_OK direct_pairs={count} structural_cases={symbolic}")


if __name__ == '__main__':
    test()
