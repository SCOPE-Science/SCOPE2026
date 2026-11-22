#!/usr/bin/env python3
"""Exact-rational diagnostic checker for metric-star P1 mass preconditioning.

Requires Python 3 standard library only. Finite checks corroborate the
closed-form theorem; the proof for arbitrary star degree is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def mul(a, b):
    n, p, m = len(a), len(b), len(b[0])
    return [[sum((a[i][k] * b[k][j] for k in range(p)), F(0))
             for j in range(m)] for i in range(n)]


def characteristic(a):
    """Return descending coefficients of det(t I - A)."""
    n = len(a)
    b = eye(n)
    coeff = [F(1)]
    for k in range(1, n + 1):
        c = mul(a, b)
        ck = -sum((c[i][i] for i in range(n)), F(0)) / k
        coeff.append(ck)
        for i in range(n):
            c[i][i] += ck
        b = c
    return coeff


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def build(lengths):
    lengths = list(map(F, lengths))
    assert len(lengths) >= 3 and min(lengths) > 0
    k, n = len(lengths), len(lengths) + 1
    m = [[F(0) for _ in range(n)] for _ in range(n)]
    b = [[F(0) for _ in range(n)] for _ in range(n)]
    for j, h in enumerate(lengths, 1):
        m[0][0] += h / 3
        m[0][j] += h / 6
        m[j][0] += h / 6
        m[j][j] += h / 3
        b[0][0] += 4 / (k*k*h)
        b[0][j] -= 2 / (k*h)
        b[j][0] -= 2 / (k*h)
        b[j][j] += 4 / h
    return m, b


def test(lengths):
    lengths = list(map(F, lengths))
    k, n = len(lengths), len(lengths) + 1
    s = sum(lengths)
    t = sum((1 / x for x in lengths), F(0))
    mu = F(4)*s*t / (3*k*k)
    m,b = build(lengths)
    bm = mul(b,m)
    vec1 = [[F(0)]] + [[1 / h] for h in lengths]
    vec2 = [[F(1)]] + [[-2 + 2*s/(k*h)] for h in lengths]
    assert mul(bm,vec1) == vec1
    assert mul(bm,vec2) == vec2
    p = characteristic(bm)
    expect = [F(1)]
    for root, multiplicity in [(F(1),2),(F(4,3),k-2),(mu,1)]:
        for _ in range(multiplicity):
            expect = pmul(expect,[F(1),-root])
    assert p == expect, (lengths,p,expect)
    d = [m[i][i] for i in range(n)]
    inv_diag = [[(F(1)/d[i] if i==j else F(0)) for j in range(n)] for i in range(n)]
    jac_poly = characteristic(mul(inv_diag,m))
    jac_expect = [F(1)]
    for root,multiplicity in [(F(1),k-1),(F(1,2),1),(F(3,2),1)]:
        for _ in range(multiplicity):
            jac_expect = pmul(jac_expect,[F(1),-root])
    assert jac_poly == jac_expect
    assert mu >= F(4,3)
    if min(lengths)==max(lengths): assert mu == F(4,3)
    r = max(lengths) / min(lengths)
    assert mu <= (r+1)**2/(3*r)
    return mu


def main():
    cases = 0
    for k in (3,4,5,6,7):
        for a in (F(1), F(2), F(5,3)):
            for b in (F(1), F(3), F(7,4)):
                lengths = [a if j % 2 else b for j in range(k)]
                test(lengths)
                cases += 1
        lengths = [F(2*i+1, i+2) for i in range(k)]
        test(lengths)
        cases += 1
    assert test([1,1,1,1]) == F(4,3)
    assert test([1,1,10,10]) == F(121,30)
    assert test([1,10,1,10,1,10]) == F(121,30)
    print('PASS: %s exact-rational star instances, Jacobi and BRAS characteristic polynomials.' % (cases+3))
    print('PASS: equal-arm and sharp fixed-contrast constructions.')

if __name__=='__main__':
    main()
