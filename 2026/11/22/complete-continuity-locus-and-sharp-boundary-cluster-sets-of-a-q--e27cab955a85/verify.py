#!/usr/bin/env python3
"""Exact rational checks for box/halfspace quadratic-projection sensitivity.

No floating-point operations or third-party dependencies are used.
The analytic continuity and cluster-set proofs are in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

count = 0


def check(condition):
    global count
    assert condition
    count += 1


def clip(v, upper):
    return min(upper, max(F(0), v))


def value(a, x):
    return sum((v * y for v, y in zip(a, x)), F(0))


def certificate(a, b, u, q, lam):
    """KKT sufficient certificate, with the active halfspace at equality."""
    check(all(t > 0 for t in u))
    check(all(F(0) <= z <= t for z, t in zip(q, u)))
    check(value(a, q) == b)
    for ai, ui, qi in zip(a, u, q):
        check(qi == clip(lam * ai, ui))
    # The strictly convex Lagrangian minimizer is the unique primal optimum.


def maxbox(a, u):
    return sum((ai*ui for ai, ui in zip(a, u) if ai > 0), F(0))

# Fixed right-hand side: the smallest nontrivial discontinuity.
for den in range(3, 101):
    eps = F(1, den)
    a = (1-eps, eps)
    b = F(1)
    u = (F(1), F(1))
    q = (F(1), F(1))
    check(maxbox(a, u) == b)
    certificate(a, b, u, q, F(1, 1)/eps)
    a = (1-eps/2, eps)
    q = (F(1), F(1, 2))
    check(maxbox(a, u) > b)
    certificate(a, b, u, q, F(1, 2)/eps)

# Every rational value in the limiting face is realized by explicit data.
# Base has two positive, two zero, and one negative component.
u = (F(2), F(3), F(3, 2), F(4), F(5))
a0 = (F(3), F(1, 2), F(0), F(-2), F(0))
b0 = maxbox(a0, u)
for r, s, den in product(range(6), range(6), (8, 13, 23, 41)):
    q = (u[0], u[1], F(r, 5)*u[2], F(0), F(s, 5)*u[4])
    S = q[2]**2 + q[4]**2
    eps = F(1, den * 100)
    aa = list(a0)
    aa[0] -= eps*S/u[0]
    aa[2] = eps*q[2]
    aa[4] = eps*q[4]
    check(aa[0] > 0)
    check(maxbox(aa, u) >= b0)
    certificate(tuple(aa), b0, u, q, F(1)/eps)

# At the zero-margin origin, changing the RHS is sometimes indispensable.
a0 = (F(-3), F(0), F(-1), F(0))
u = (F(2), F(3), F(4), F(5))
for r, s, den in product(range(6), range(6), (11, 17, 31)):
    q = (F(0), F(r,5)*u[1], F(0), F(s,5)*u[3])
    eps = F(1, den)
    aa = (a0[0], eps*q[1], a0[2], eps*q[3])
    bb = eps*(q[1]**2+q[3]**2)
    check(maxbox(aa, u) >= bb)
    certificate(aa, bb, u, q, F(1)/eps)

# A zero-coefficient coordinate gives the sharp attainable jump.
a = (F(2), F(0), F(-1), F(0))
u = (F(1), F(3), F(2), F(4))
base = (F(1), F(0), F(0), F(0))
q = (F(1), u[1], F(0), u[3])
S = u[1]**2 + u[3]**2
for den in (40, 100, 200, 400):
    eps = F(1, den)
    aa = (a[0]-eps*S, eps*u[1], a[2], eps*u[3])
    certificate(aa, F(2), u, q, F(1)/eps)
    check(sum((v-w)**2 for v, w in zip(q,base)) == S)

print(f"VERIFY_OK {count} exact_rational_checks")
