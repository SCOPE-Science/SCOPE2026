"""Exact finite-matrix checks for a rational copula covariance kernel.
Run with Python 3 standard library: python3 CHECKER.py
The infinite-dimensional statements are proved analytically in RESULT.md.
"""
from fractions import Fraction as Q
from math import exp, sqrt


def det(a):
    """Exact Gaussian elimination over rational numbers."""
    n = len(a)
    m = [[Q(x) for x in row] for row in a]
    sign, product = 1, Q(1)
    for j in range(n):
        k = next((i for i in range(j, n) if m[i][j] != 0), None)
        if k is None:
            return Q(0)
        if k != j:
            m[k], m[j] = m[j], m[k]
            sign = -sign
        pivot = m[j][j]
        product *= pivot
        for i in range(j + 1, n):
            q = m[i][j] / pivot
            for k in range(j + 1, n):
                m[i][k] -= q * m[j][k]
            m[i][j] = 0
    return sign * product


def negative_gram(xs, us, a):
    ws = [u * x for u, x in zip(us, xs)]
    return [[-a * ws[i] * ws[j] / (1 + a * xs[i] * xs[j])
             for j in range(len(xs))] for i in range(len(xs))]


def determinant_formula(xs, us, a):
    n = len(xs)
    ws = [u * x for u, x in zip(us, xs)]
    out = Q(-1) ** (n * (n + 1) // 2) * a ** (n * (n + 1) // 2)
    for wi in ws:
        out *= wi ** 2
    for i in range(n):
        for j in range(i + 1, n):
            out *= (xs[i] - xs[j]) ** 2
    for i in range(n):
        for j in range(n):
            out /= 1 + a * xs[i] * xs[j]
    return out


for n in range(1, 7):
    a = Q(7, 3)
    xs = [Q(i + 1, n + 3) for i in range(n)]
    us = [Q(i + 1, n + 7) for i in range(n)]
    gram = negative_gram(xs, us, a)
    assert det(gram) == determinant_formula(xs, us, a)
    leading = [Q(1)] + [det([row[:j] for row in gram[:j]])
                         for j in range(1, n + 1)]
    assert all(leading[j] != 0 for j in range(n + 1))
    pivots = [leading[j] / leading[j-1] for j in range(1, n+1)]
    assert [p > 0 for p in pivots] == [j % 2 == 0 for j in range(1, n+1)]
    assert sum(p > 0 for p in pivots) == n // 2
    assert sum(p < 0 for p in pivots) == (n + 1) // 2
    print('Negative parameter, size', n, ': inertia (+,-) =',
          (n // 2, (n + 1) // 2))

for n in range(1, 7):
    theta = Q(1, 2)
    xs = [Q(i + 1, n + 4) for i in range(n)]
    us = [Q(i + 1, n + 5) for i in range(n)]
    ws = [u * x for u, x in zip(us, xs)]
    gram = [[theta * ws[i] * ws[j] / (1 - theta * xs[i] * xs[j])
             for j in range(n)] for i in range(n)]
    for j in range(1, n + 1):
        assert det([row[:j] for row in gram[:j]]) > 0
    print('Positive parameter, size', n, ': positive definite')

# Evaluate the 2024 exponential-ratio example at two distinct points.
f = lambda u: (1-u)*exp(-u)
u, v = 0.25, 0.75
x, y = f(u), f(v)
p = lambda s,t: -s*f(s)*t*f(t)/(1+f(s)*f(t))
a, b, d = p(u,u), p(u,v), p(v,v)
assert a*d-b*b < 0 and a < 0
tr = a+d
rad = sqrt((a-d)*(a-d)+4*b*b)
lam1, lam2 = (tr-rad)/2,(tr+rad)/2
assert lam1 < 0 < lam2
print('Two-node exponential-ratio kernel eigenvalues:',lam1,lam2)
print('ALL EXACT CHECKS PASSED. The analytic proof covers every matrix size.')
