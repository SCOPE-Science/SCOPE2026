"""Bounded diagnostics for the capture bound; requires only Python 3."""
from fractions import Fraction as Q
from math import erfc, exp, sqrt


def contraction_delta(s):
    a = s * (sqrt(2 - s*s) - s)
    return a / (2 + a)


def quadrature(s):
    # Integrate over the square root of dimensionless alarm time.
    a, b = 1 - s*s, s/sqrt(2)
    def f(z):
        return 2*z*exp(-a*z*z)*erfc(b*z)
    n, h = 20000, 0.001
    return h*(f(0) + f(n*h) + sum((4 if j % 2 else 2)*f(j*h)
                                  for j in range(1, n)))/3


for s in (0.0625, 0.25, 0.5, 0.875, 0.98, 0.999):
    assert abs(quadrature(s) - (1-contraction_delta(s))) < 1e-9

for k in range(1, 200):
    s = Q(k, 200)
    # Certify rational bounds on the square root by comparing squares.
    assert 1 <= 2-s*s
    assert s*s*(2-s*s) <= 1
    assert s*s < 2-s*s
    # The analytical inequalities imply delta(s) >= s(1-s)/3.
    assert contraction_delta(float(s)) >= float(s*(1-s)/3)

for k in range(0, 1001):
    y = Q(k, 10)
    s = 1-1/(y+2)
    assert s >= Q(1, 2) and (1-s)*y < 1
    assert s*(1-s)/3 >= 1/(6*(y+2))

assert abs(contraction_delta(0.5) - (4/sqrt(7)-1)/3) < 1e-15
print('PASS: six transform quadratures, sampled contraction bounds, and rational prefactor checks.')
print('The exact logarithmic asymptotic is proved analytically, not by these diagnostics.')
