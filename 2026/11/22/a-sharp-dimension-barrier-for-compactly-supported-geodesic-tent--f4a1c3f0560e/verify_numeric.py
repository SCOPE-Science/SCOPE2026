"""Supplementary numerical checks for geodesic tent Legendre coefficients.

Standard-library only. Finite quadrature checks are not proofs of asymptotic
sign changes or of positive definiteness in every spherical dimension.
"""
from math import cos, sin


def legendre(n, x):
    if n == 0:
        return 1.0
    a, b = 1.0, x
    for k in range(1, n):
        a, b = b, ((2*k + 1)*x*b - k*a)/(k+1)
    return b


def simpson(fun, upper, intervals=8000):
    assert intervals % 2 == 0
    h = upper / intervals
    total = fun(0.0) + fun(upper)
    for j in range(1, intervals):
        total += (4 if j % 2 else 2)*fun(j*h)
    return total*h/3


def main():
    test_count = 0
    for c, negative_n, positive_n in [
        (0.7, 35, 30), (1.5, 30, 31), (2.7, 30, 31)
    ]:
        for n in (3, 10, 20, negative_n, positive_n):
            first = simpson(
                lambda t: (c-t)*legendre(n, cos(t))*sin(t), c
            )
            jval = simpson(lambda t: cos(t)*legendre(n, cos(t)), c)
            second = (jval-sin(c)*legendre(n, cos(c)))/(n*(n+1))
            assert abs(first-second) < 2e-8, (c, n, first, second)
            test_count += 1
        neg = simpson(lambda t:(c-t)*legendre(negative_n,cos(t))*sin(t),c)
        pos = simpson(lambda t:(c-t)*legendre(positive_n,cos(t))*sin(t),c)
        assert neg < -1e-7 and pos > 1e-7, (c, neg, pos)
        test_count += 2
    print(f"Passed {test_count} supplementary integral/sign assertions.")


if __name__ == '__main__':
    main()
