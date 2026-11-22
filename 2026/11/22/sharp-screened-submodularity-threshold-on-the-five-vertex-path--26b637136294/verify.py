#!/usr/bin/env python3
"""Exact finite certificate for screened edge-addition submodularity on P5.

Requires only the Python standard library.  Polynomials use coefficient lists
in ascending powers of the indeterminate.  All arithmetic is integer or
rational; no floating-point sign decision is used.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb

N = 5
BASE = ((0, 1), (1, 2), (2, 3), (3, 4))
CHOICES = ((0, 2), (0, 3), (0, 4), (1, 3), (1, 4), (2, 4))
EXCEPTION = (0, 0, 5)  # S empty, (1,3), (3,5)


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, z in enumerate(a):
        c[i] += z
    for i, z in enumerate(b):
        c[i] += z
    return trim(c)


def scale(a, k):
    return trim([k * z for z in a])


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                c[i + j] += x * y
    return trim(c)


def deriv(a):
    return trim([i * a[i] for i in range(1, len(a))] or [0])


def shift_coefficients(a, shift):
    """Return coefficients of a(v+shift), using exact fractions."""
    out = [Fraction(0)] * len(a)
    for k, x in enumerate(a):
        for j in range(k + 1):
            out[j] += x * comb(k, j) * shift ** (k - j)
    return trim(out)


def determinant_polynomial(mask):
    # Laplacian L(P5) plus selected unit-weight nonedges.
    M = [[0 for j in range(N)] for i in range(N)]
    for i, j in BASE + tuple(CHOICES[k] for k in range(6) if mask & (1 << k)):
        M[i][i] += 1
        M[j][j] += 1
        M[i][j] -= 1
        M[j][i] -= 1
    # det(uI+L), by the entire 5! Leibniz expansion (not numerical samples).
    result = [0]
    for perm in permutations(range(N)):
        inv = sum(perm[i] > perm[j] for i in range(N) for j in range(i + 1, N))
        term = [1]
        for i, j in enumerate(perm):
            entry = [M[i][j], 1] if i == j else [M[i][j]]
            term = mul(term, entry)
        result = add(result, scale(term, -1 if inv % 2 else 1))
    # Connected graphs have exactly one zero Laplacian eigenvalue.
    assert len(result) == 6 and result[0] == 0 and result[-1] == 1
    p = result[1:]
    assert p[0] > 0 and all(coef > 0 for coef in p)
    return p


def numerator_of_negative_second_difference(polys, mask, i, j):
    # -Delta = T(S)+T(S+ef)-T(S+e)-T(S+f),
    # T=tr((uI+L)^{-1}) = 1/u + p'/p.
    ids = [mask, mask | 1 << i, mask | 1 << j, mask | 1 << i | 1 << j]
    p = [polys[k] for k in ids]
    d = [deriv(x) for x in p]
    out = [0]
    for k, sign in enumerate((1, -1, -1, 1)):
        term = d[k]
        for ell in range(4):
            if ell != k:
                term = mul(term, p[ell])
        out = add(out, scale(term, sign))
    return out


def main():
    p = [determinant_polynomial(mask) for mask in range(64)]
    q = [-15, -10, 8, 6, 1]
    # Exception polynomial from a direct, exact determinant identity.
    expected = scale(mul(mul(mul([0, 1], [3, 1]), [3, 1]), [3, 1]), 2)
    expected = mul(mul(expected, mul([3, 1], [3, 1])), mul([5, 13, 7, 1], q))
    # 2*u*(u+3)^5*(u^3+7u^2+13u+5)*q(u).
    zero = positive = total = 0
    for i, j in combinations(range(6), 2):
        for mask in range(64):
            if mask & ((1 << i) | (1 << j)):
                continue
            total += 1
            nu = numerator_of_negative_second_difference(p, mask, i, j)
            if (mask, i, j) == EXCEPTION:
                assert nu == expected, (nu, expected)
                continue
            if nu == [0]:
                zero += 1
                continue
            # All coefficients must be >=0 after u=v+5/4, for v>=0.
            coefs = shift_coefficients(nu, Fraction(5, 4))
            assert all(c >= 0 for c in coefs), (mask, i, j, coefs)
            assert coefs[0] > 0, (mask, i, j)
            positive += 1
    assert (total, zero, positive) == (240, 29, 210)
    # q has a unique positive root by Descartes: (+,+,+,-,-) in
    # descending powers.  It lies strictly above 5/4 and below 13/10.
    def evaluate(a, x):
        return sum(c * x ** i for i, c in enumerate(a))
    assert evaluate(q, Fraction(5, 4)) == Fraction(-215, 256)
    assert evaluate(q, Fraction(13, 10)) == Fraction(15581, 10000)
    # The canonical zero-screening counterexample has exact defect 3/70.
    mask, i, j = (1 << 3, 0, 5)
    ids = [mask, mask | 1 << i, mask | 1 << j, mask | 1 << i | 1 << j]
    vals = [Fraction(p[k][1], p[k][0]) for k in ids]
    delta0 = vals[1] + vals[2] - vals[3] - vals[0]
    assert delta0 == Fraction(3, 70)
    print('PASS: 64 determinant polynomials and 240 exhaustive elemental inequalities')
    print('PASS: 210 strictly positive shifted certificates, 29 identities, one quartic witness')
    print('PASS: quartic isolating interval (5/4,13/10), unscreened witness 3/70')


if __name__ == '__main__':
    main()
