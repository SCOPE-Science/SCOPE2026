#!/usr/bin/env python3
"""Exact-arithmetic checks for fourth-order Gauss heat steps on Cartesian clique products.

Run: python3 artifacts/verify.py (standard library only).
The all-parameter theorem is proved symbolically in RESULT.md; these tests
reconstruct the finite certificates and check their algebraic specializations.
"""
from fractions import Fraction
from itertools import product, combinations
from math import prod


def pad(a, n):
    return list(a) + [0] * (n - len(a))


def padd(a, b):
    n = max(len(a), len(b))
    return [x + y for x, y in zip(pad(a, n), pad(b, n))]


def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def pscale(a, x):
    return [x * v for v in a]


def pprod(*xs):
    a = [1]
    for x in xs:
        a = pmul(a, x)
    return a


def denominator(n):
    return [12, 6*n, n*n]


def numerator(n):
    return [12, -6*n, n*n]


def polynomial_certificates(p, q):
    dp, dq, dpq = map(denominator, (p, q, p+q))
    np, nq, npq = map(numerator, (p, q, p+q))
    base = pprod(dp, dq, dpq)
    x = pprod(np, dq, dpq)
    y = pprod(dp, nq, dpq)
    z = pprod(dp, dq, npq)
    return (
        padd(padd(base, pscale(x, -1)), pscale(padd(y, pscale(z, -1)), q-1)),
        padd(padd(base, pscale(y, -1)), pscale(padd(x, pscale(z, -1)), p-1)),
        padd(padd(padd(base, pscale(x, -1)), pscale(y, -1)), z)
    )


def F(x):
    x = Fraction(x)
    return (x*x - 6*x + 12)/(x*x + 6*x + 12)


def kernel(qs, differing, h):
    # Orthogonal spectral projectors of Cartesian products of complete graphs.
    d = len(qs)
    n = prod(qs)
    v = Fraction(0)
    for mask in range(1 << d):
        eigen = sum(qs[i] for i in range(d) if mask & (1 << i))
        coeff = prod((-1 if i in differing else qs[i]-1)
                     for i in range(d) if mask & (1 << i))
        v += coeff * F(Fraction(h) * eigen)
    return v/n


def green_adj(qs, k):
    # Pseudoinverse of the combinatorial Laplacian at nearest neighbors.
    total = Fraction(0)
    n = prod(qs)
    d = len(qs)
    for mask in range(1, 1 << d):
        eig = sum(qs[i] for i in range(d) if mask & (1 << i))
        coeff = prod((-1 if i == k else qs[i] - 1)
                     for i in range(d) if mask & (1 << i))
        total += Fraction(coeff, eig)
    return total/n


def green_adj_heat_formula(qs, k):
    Q = qs[k]
    other = [v for i,v in enumerate(qs) if i != k]
    s = -Fraction(1, Q)
    for mask in range(1, 1 << len(other)):
        ssum = sum(other[i] for i in range(len(other)) if mask & (1 << i))
        weight = prod(other[i] - 1 for i in range(len(other)) if mask & (1 << i))
        s += Fraction(Q * weight, ssum * (ssum + Q))
    return s / prod(qs)


def main():
    cases = [(2,2), (2,3), (3,3)]
    count_polynomial = 0
    for p,q in cases:
        for j, poly in enumerate(polynomial_certificates(p,q)):
            assert all(c >= 0 for c in poly), (p,q,j,poly)
            assert poly[0] == 0
            assert poly[1] > 0 if j < 2 else poly[1] == 0
            assert poly[2] > 0
            count_polynomial += 1
    # Completeness of exact rational spectral kernels and mass conservation.
    count_ker = 0
    count_row = 0
    for qs in [(2,), (7,), (2,2), (2,3), (3,3),
               (2,4), (3,4), (2,2,2), (2,2,5), (2,3,4), (2,2,2,2)]:
        for h in [Fraction(1,20), Fraction(1,2), Fraction(7,3), 9, 1000]:
            d = len(qs)
            row = Fraction(0)
            for mask in range(1 << d):
                J = {i for i in range(d) if mask & (1 << i)}
                k = kernel(qs, J, h)
                row += prod(qs[i]-1 for i in J)*k
                count_ker += 1
                if d == 1 or (d == 2 and max(qs) <= 3):
                    assert k > 0, (qs, J, h, k)
            assert row == 1, (qs, h, row)
            count_row += 1
    # Independent rational derivations of the nearest-neighbor Green formula.
    count_green = 0
    count_sign = 0
    for d in range(2, 6):
        for qs in product(range(2, 7), repeat=d):
            if sorted(qs) != list(qs):
                continue
            k = d-1  # the coordinate with largest clique order
            gv = green_adj(qs, k)
            assert gv == green_adj_heat_formula(qs, k), qs
            if d >= 3 or max(qs) >= 4:
                assert gv > 0, (qs, gv)
                count_sign += 1
            count_green += 1
    # Large-step Padé asymptotic: h * offdiagonal -> -12 * Green.
    # This exact finite-rational inequality checks the witness mechanism.
    count_witness = 0
    for qs in [(2,4), (3,4), (3,8), (2,2,2), (2,2,3), (2,3,4)]:
        k = len(qs)-1
        g = green_adj(qs, k)
        assert g > 0
        for h in [100000, 1000000]:
            val = kernel(qs, {k}, h)
            assert val < 0, (qs, h, val)
            # error decays as h^-1, with a generous exact bound
            assert abs(Fraction(h)*val + 12*g) < Fraction(1, 100), (qs, h)
            count_witness += 1
    print("VERIFY_OK", "polynomial_certificates", count_polynomial,
          "rational_kernels", count_ker, "row_sums", count_row,
          "green_identities", count_green, "positive_green", count_sign,
          "large_step_witnesses", count_witness)

if __name__ == "__main__":
    main()
