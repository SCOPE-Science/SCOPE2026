"""Finite consistency checks for the regular-polygon Ehrlich–Aberth theorem.

Standard-library only. These checks are not a proof for arbitrary degree;
see RESULT.md for the exact algebraic argument.
"""
from fractions import Fraction
from math import pi, sqrt
import cmath

COUNT = 0


def check(test):
    global COUNT
    assert test
    COUNT += 1


def add(*polys):
    size = max(map(len, polys))
    return [sum(p[i] if i < len(p) else 0 for p in polys) for i in range(size)]


def scale(p, c):
    return [c * a for a in p]


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def deriv(p):
    return [i * p[i] for i in range(1, len(p))]


def same(a, b):
    n = max(len(a), len(b))
    return add(a, scale(b, -1)) == [0] * n


for n in range(2, 41):
    B = [n - 1] + [0] * (n - 1) + [n + 1]
    numerator = [0, n + 1] + [0] * (n - 1) + [n - 1]
    Q = [(j + 1) * (n - 1 - j) for j in range(n - 1)]
    cube = [-1, 3, -3, 1]
    check(same(add(numerator, scale(B, -1)), mul(cube, Q)))
    check(same(add(numerator, scale(mul([0, 1], B), -1)),
               [0, 2] + [0] * (n - 1) + [-2]))
    derivative_num = add(mul(deriv(numerator), B),
                         scale(mul(numerator, deriv(B)), -1))
    root_diff = [-1] + [0] * (n - 1) + [1]
    check(same(derivative_num, scale(mul(root_diff, root_diff), n*n-1)))
    check(all((j + 1) * (n - 1 - j) > 0 for j in range(n - 1)))
    coeffs = [n*n - 1 - 2 * (k-1) * (n+1-k) for k in range(1, n+1)]
    check(all(c > 0 for c in coeffs))
    check(coeffs[0] == max(coeffs) and coeffs[0] > max(coeffs[1:]))
    tau = (sqrt(n*n-1) - (n-1)) / (sqrt(n*n-1) + n+1)
    norm = lambda t: sqrt(n*n-1) * abs(t-1) / ((n+1)*t+n-1)
    check(0 < tau < 1)
    check(abs(norm(tau) - 1) < 2e-13)
    check(norm(tau / 2) > 1 and norm((tau + 1) / 2) < 1)
    check(norm(2) < 1)


def direct_jacobian(n, r):
    roots = [cmath.exp(2j*pi*i/n) for i in range(n)]
    z = [r*root for root in roots]
    out = [[0j] * n for _ in range(n)]
    for i in range(n):
        p = z[i]**n - 1
        p1 = n * z[i]**(n-1)
        p2 = n * (n-1) * z[i]**(n-2)
        S = sum(1/(z[i]-z[j]) for j in range(n) if j != i)
        S2 = sum(1/(z[i]-z[j])**2 for j in range(n) if j != i)
        D = p1 - p*S
        Dprime = p2 - p1*S + p*S2
        out[i][i] = 1-p1/D+p*Dprime/D**2
        for j in range(n):
            if i != j:
                out[i][j] = -(p/D)**2/(z[i]-z[j])**2
    return out


for n in range(2, 13):
    roots = [cmath.exp(2j*pi*i/n) for i in range(n)]
    for r in (0.41, 0.77, 1.25):
        J = direct_jacobian(n, r)
        t = r**n
        B = (n+1)*t+n-1
        for k in range(1, n+1):
            expected = (n*n-1-2*(k-1)*(n+1-k)) * ((t-1)/B)**2
            vec = [v**k for v in roots]
            norm_err = max(abs(sum(J[i][j]*vec[j] for j in range(n)) - expected*vec[i])
                           for i in range(n))
            check(norm_err < 2e-8 * (1 + expected))
        S = [sum(roots[j]**k/(1-roots[j])**2 for j in range(1, n))
             for k in range(1, n+1)]
        for k in range(1, n+1):
            check(abs(S[k-1]-S[0]-(k-1)*(n+1-k)/2) < 2e-8)

print(f'VERIFY_OK {COUNT}')
