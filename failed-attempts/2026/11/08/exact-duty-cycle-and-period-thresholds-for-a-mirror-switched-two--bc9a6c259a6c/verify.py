#!/usr/bin/env python3
"""Finite checks of a two-community SIS switching phase diagram.

Run: python3 verify.py .  Uses the Python standard library only.
This is a finite verification aid; all-parameter conclusions require the proof.
"""

import math
from itertools import product


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def expm_by_taylor(a):
    # Independent scaling-and-squaring Taylor matrix exponential.
    norm = max(sum(abs(x) for x in row) for row in a)
    squarings = max(0, math.ceil(math.log2(norm / 0.25))) if norm > 0.25 else 0
    scale = 2 ** squarings
    x = [[v / scale for v in row] for row in a]
    ans = [[1.0, 0.0], [0.0, 1.0]]
    term = [[1.0, 0.0], [0.0, 1.0]]
    for k in range(1, 65):
        term = multiply(term, x)
        for i in range(2):
            for j in range(2):
                term[i][j] /= k
                ans[i][j] += term[i][j]
        if max(abs(v) for row in term for v in row) < 1e-17:
            break
    for _ in range(squarings):
        ans = multiply(ans, ans)
    return ans


def direct_growth(a, c, b, beta, mu, T, theta):
    Lplus = [[beta * a - mu, beta * b], [beta * b, beta * c - mu]]
    Lminus = [[beta * c - mu, beta * b], [beta * b, beta * a - mu]]
    eplus = expm_by_taylor([[x * theta * T for x in row] for row in Lplus])
    eminus = expm_by_taylor([[x * (1-theta) * T for x in row] for row in Lminus])
    mat = multiply(eminus, eplus)
    trace = mat[0][0] + mat[1][1]
    determinant = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    assert determinant > 0.0
    discr = max(0.0, trace * trace - 4.0 * determinant)
    return math.log((trace + math.sqrt(discr)) / 2.0) / T


def formula(a, c, b, beta, mu, T, theta):
    h = beta * (a+c) / 2 - mu
    u = beta * b
    v = beta * (a-c) / 2
    q = math.hypot(u, v)
    Xi = (u / q)**2 * math.cosh(q*T) + (v/q)**2 * math.cosh(q*T*(2*theta-1))
    return h + math.acosh(max(1, Xi)) / T


def optimal(a, c, b, beta, mu, T):
    h = beta*(a+c)/2 - mu
    u = beta*b
    v = beta*(a-c)/2
    q = math.hypot(u, v)
    return h + 2*math.asinh(u/q * math.sinh(q*T/2)) / T


def bisect_zero(f, lo, hi):
    flo = f(lo)
    fhi = f(hi)
    assert flo < 0 and fhi > 0
    for _ in range(100):
        mid = (lo+hi)/2
        if f(mid) > 0: hi = mid
        else: lo = mid
    return (lo+hi)/2


checks = 0
cases = [
    (2.0, 0.0, 0.5, 1.0, 1.75),
    (3.0, 0.0, 0.2, 0.5, 1.2),
    (1.5, 0.25, 0.7, 1.0, 0.9),
    (6.0, 2.0, 0.4, 0.25, 1.0),
    (1.0, 0.8, 0.9, 1.2, 1.5),
    (5.0, 1.0, 1.5, 0.7, 2.6),
    (1.2, 0.1, 0.75, 0.9, 1.0),
    (2.5, 0.5, 0.4, 0.8, 1.0),
    (4.0, 0.0, 1.0, 0.6, 1.2),
    (0.4, 0.0, 0.025, 3.0, 0.7),
]
periods = (0.12, 0.5, 1.0, 1.7, 2.0, 3.5, 4.0)
duties = (0, 0.01, 0.10, 0.2, 0.35, 0.5, 0.65, 0.8, 0.9, 0.99, 1)
for case, T, duty in product(cases, periods, duties):
    analytic = formula(*case, T, duty)
    direct = direct_growth(*case, T, duty)
    if abs(analytic-direct) > 2.0e-10:
        raise AssertionError((case, T, duty, analytic, direct))
    checks += 1

for case, T in product(cases, periods):
    f = optimal(*case, T)
    assert abs(f-formula(*case, T, 0.5)) < 2.0e-11
    for duty in duties:
        assert formula(*case, T, duty) >= f-2.0e-11
    checks += 12

for case in cases:
    fvals = [optimal(*case, T) for T in periods]
    assert all(y > x for x,y in zip(fvals, fvals[1:]))
    checks += len(fvals)-1

case = (2.0, 0.0, 0.5, 1.0, 1.75)
Tc = bisect_zero(lambda T: optimal(*case, T), 1, 10)
assert abs(Tc - 4.182730782489124) < 3e-13
assert abs(optimal(*case, 2) - (-0.17187290456102275)) < 2e-14
h, u, v, q = -0.75, 0.5, 1.0, math.sqrt(1.25)
T = 2.0
Z = (q*q*math.cosh(-h*T)-u*u*math.cosh(q*T)) / (v*v)
half_width = math.acosh(Z) / (2*q*T)
left, right = 0.5-half_width, 0.5+half_width
assert abs(left-0.23970358622398983)<3e-14
assert abs(right-0.7602964137760102)<3e-14
assert abs(formula(*case, T, left)) < 2e-14
assert abs(formula(*case, T, right)) < 2e-14
assert formula(*case, T, 0.5)<0
assert formula(*case, T, left-0.03)>0
assert formula(*case, T, right+0.03)>0
assert optimal(*case, Tc-0.005) < 0 < optimal(*case, Tc+0.005)
checks += 9

print(f'PASS: {checks} finite direct matrix/duty/period checks')
print(f'Example: critical period {Tc:.15f}; duty range at T=2: ({left:.15f}, {right:.15f})')
