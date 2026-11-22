"""Exact rational sign certificate for a planar disk-autocorrelation spherical transfer example."""
from fractions import Fraction as F
from math import factorial

RADII = (F(1, 2), F(3, 2))
COEFFICIENTS = (3, 2)
TERMS = 28


def bessel_coefficients(n=TERMS):
    return [sum(F(c) * r ** (2*k + 2) for c, r in zip(COEFFICIENTS, RADII)) /
            (2 ** (2*k + 1) * factorial(k) * factorial(k + 1)) for k in range(n)]


def terms_and_tail(a, n=TERMS):
    """S(a)=integral G(a sin u)^2 sin u du. Return rational series sum and rigorous error."""
    b = bessel_coefficients(n)
    total = F(0)
    for m in range(n):
        c = sum(b[k] * b[m-k] for k in range(m+1))
        h = F(4**m * factorial(m)**2, factorial(2*m+1))
        total += (-1)**m * a**(2*m) * c * h
    # |C_m H_m| <= (21/8)^2 (9/4)^m/(m!)^2, since H_m <= 1.
    x = F(9*a*a, 4)
    assert x < (n+1)**2
    tail = F(21, 8)**2 * x**n / factorial(n)**2 / (1 - F(x, (n+1)**2))
    return total, tail


def check():
    assert F(57, 4) == 3**2 * F(1, 4) + 4 * F(9, 4) + 2*3*2*F(1, 4)
    a = {j: terms_and_tail(j) for j in (1, 2, 3, 4)}
    for j, (v, err) in a.items():
        assert v - err > 0, ('positive A', j)
    # sin(t)P_2(cos t) = (-sin(t)+3sin(3t))/8.
    second = 9*a[3][0] - a[1][0]
    second_err = 9*a[3][1] + a[1][1]
    assert second - second_err > F(1, 1)
    # sin(t)P_3(cos t) = (-2sin(2t)+5sin(4t))/16.
    third = 5*a[4][0] - a[2][0]
    third_err = 5*a[4][1] + a[2][1]
    assert third + third_err < -F(1, 200)
    assert third_err < F(1, 10**11)
    # A_1,A_2>0, 9A_3-A_1>0, 5A_4-A_2<0,
    # so Legendre degrees 0,1,2 pass and degree 3 fails.
    print('PASS exact rational signs, degrees 0,1,2 positive; degree 3 negative')
    print('5A4-A2 rational-series sum:', float(third))
    print('rigorous absolute error:', float(third_err))
    print('9A3-A1 lower bound:', float(second-second_err))
    print('normalization F(0)/pi = 57/4')


if __name__ == '__main__':
    check()
