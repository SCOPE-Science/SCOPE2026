#!/usr/bin/env python3
"""Exact, dependency-free finite checks for affine three-tap convolution.

Runs modular-rank tests of integer regular-representation matrices and
cyclotomic divisibility tests of the induced-block determinants.
These finite tests corroborate, but do not replace, the general proof.
"""
from math import gcd


def order(a, p):
    v = 1
    for n in range(1, p):
        v = (v * a) % p
        if v == 1:
            return n
    raise AssertionError((a, p))


def multiplicative_subgroup(a, p):
    h = [1]
    v = a % p
    while v != 1:
        h.append(v)
        v = v * a % p
    return h


def is_prime(n):
    return n > 1 and all(n % k for k in range(2, int(n ** 0.5) + 1))


def cyclic_product_coefficients(p, residues):
    """Coefficient vector for product (1+X**r), modulo X**p-1."""
    c = [0] * p
    c[0] = 1
    for r in residues:
        c = [c[j] + c[(j - r) % p] for j in range(p)]
    return c


def cyclotomic_zero(p, residues):
    """Whether product(1+zeta**r)=(-1)**len(residues), exactly.

    In Z[X]/Phi_p, a polynomial with cyclic coefficients is zero
    precisely when all coefficients are equal.
    """
    c = cyclic_product_coefficients(p, residues)
    c[0] -= (-1) ** len(residues)
    return len(set(c)) == 1


def convolution_matrix(p, a, u=1, b=0):
    """Entries of right convolution by identity,(u,1),(b,a)."""
    H = multiplicative_subgroup(a, p)
    G = [(x, h) for h in H for x in range(p)]
    lookup = {g: i for i, g in enumerate(G)}
    n = len(G)
    M = [[0] * n for _ in range(n)]
    for i, (x, h) in enumerate(G):
        for dest in ((x, h), ((x + h * u) % p, h),
                     ((x + h * b) % p, (h * a) % p)):
            M[i][lookup[dest]] += 1
    return M


def rank_mod(mat, ell=65537):
    """Exact Gaussian elimination over F_ell; ell must be prime."""
    rows = [list(map(lambda x: x % ell, row)) for row in mat]
    n = len(rows)
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, n) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        lead = pow(rows[rank][col], -1, ell)
        rr = rows[rank]
        for k in range(col, n):
            rr[k] = rr[k] * lead % ell
        for i in range(rank + 1, n):
            factor = rows[i][col]
            if factor:
                row = rows[i]
                for k in range(col + 1, n):
                    row[k] = (row[k] - factor * rr[k]) % ell
                row[col] = 0
        rank += 1
        if rank == n:
            break
    return rank


def main():
    num_blocks = 0
    num_rank_cases = 0
    for p in (5, 7, 11, 13, 17, 19, 23, 31):
        assert is_prime(p)
        for a in range(2, p):
            H = multiplicative_subgroup(a, p)
            m = len(H)
            predicted = (-2) % p in H
            assert (pow(-2, m, p) == 1) == predicted
            # Verify every orbit's exact cyclotomic block criterion.
            orbits = set(range(1, p))
            while orbits:
                k = min(orbits)
                C = {k * h % p for h in H}
                assert C <= orbits
                orbits -= C
                assert cyclotomic_zero(p, C) == predicted, (p, a, k)
                num_blocks += 1
            # Small integer regular convolution matrices, exact mod 65537.
            if p * m <= 120:
                for u, b in ((1, 0), (p - 1, 2 % p)):
                    M = convolution_matrix(p, a, u=u, b=b)
                    nullity = len(M) - rank_mod(M)
                    expected = p - 1 if predicted else 0
                    assert nullity == expected, (p, a, u, b, nullity, expected)
                    num_rank_cases += 1
    print('AFFINE_THREE_TAP_CHECKS_PASS',
          'cyclotomic_orbits='+str(num_blocks),
          'modular_rank_cases='+str(num_rank_cases))


if __name__ == '__main__':
    main()
