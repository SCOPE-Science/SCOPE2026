#!/usr/bin/env python3
"""Exact rational arithmetic checks for the two specified stationary architecture variances."""
from fractions import Fraction as Q
from itertools import product


def laplace_first(lam):
    """Integral of exp(-t) exp(-lam*t), t >= 0."""
    return Q(1, lam + 1)


def laplace_double(lam):
    """Integral of exp(-t) times one unit-queue filtered covariance mode."""
    return Q(lam + 2, 2 * (lam + 1)**2)


def variances(a, b, c):
    s, m = a + b, (a + b) * c
    # X's covariance: s * (exp(-t) + (1+t)*exp(-t)/2).
    # Y's driver is X*C with independent process C; its covariance is
    # c*c*K_X + s*s*K_C + K_X*K_C.
    int_x = Q(1, 2) + laplace_double(1)  # 7/8
    int_cross = Q(1, 3) + Q(1, 2) * (Q(1, 3) + Q(1, 9))  # 5/9
    factor = m + c*c*s*int_x + s*s*c*laplace_first(1) + s*c*int_cross
    # U+V superposes to a single Cox queue driven by (A+B)*C.
    # Its intensity covariance has exp(-t) and exp(-2t) modes.
    distribute = m + m*laplace_first(1) + m*(s+c)*laplace_double(1) + m*laplace_double(2)
    return factor, distribute


assert laplace_double(1) == Q(3, 8)
assert laplace_double(2) == Q(2, 9)
assert laplace_first(1) + laplace_double(1) == Q(7, 8)
assert Q(1, 3) + Q(1, 2)*(Q(1, 3) + Q(1, 9)) == Q(5, 9)
checks = 0
values = (Q(1,100), Q(1,10), Q(2,9), Q(1,2), Q(3,2), Q(10))
for a, b, c in product(values, repeat=3):
    vf, vd = variances(a, b, c)
    s, m = a+b, (a+b)*c
    assert vf == m*(Q(14,9) + s/2 + Q(7,8)*c)
    assert vd == m*(Q(31,18) + Q(3,8)*(s+c))
    assert vd-vf == m*(4-3*s-12*c)/24
    assert (vd > vf) == (4 > 3*s+12*c)
    assert (vd < vf) == (4 < 3*s+12*c)
    checks += 5
for x in (Q(1,100), Q(2,9), Q(1,4), Q(1,3)):
    vf, vd = variances(x, x, x)
    assert (vf == vd) == (x == Q(2,9))
    checks += 1
assert variances(Q(9,20),Q(9,20),Q(1,10))[1] > variances(Q(9,20),Q(9,20),Q(1,10))[0]
assert variances(Q(7,20),Q(7,20),Q(3,10))[1] < variances(Q(7,20),Q(7,20),Q(3,10))[0]
checks += 2
print(f"PASS {checks} exact rational checks")
print("Equal-variance example:", variances(Q(2,9),Q(2,9),Q(2,9)))
