"""Supplementary finite and numerical checks for a spatial invasion theorem.

Usage: python verification_checker.py
Only the Python standard library is required. The analytic PDE proof is separate.
"""
from fractions import Fraction as F
from math import cos, sin, pi


def simpson(fn, n=4096):
    assert n > 0 and n % 2 == 0
    h = 1.0 / n
    total = fn(0.0) + fn(1.0)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * fn(i * h)
    return total * h / 3


def continuum_example():
    def u(x):
        return 1 + cos(pi*x)/5

    def m(x):
        return u(x) + pi*pi*cos(pi*x)/(50*u(x))

    def z(x):
        return 1 + cos(pi*x)

    def num(x):
        dz = -pi*sin(pi*x)
        return -dz*dz/100 + u(x)*(F(19,20)*m(x)-u(x))*z(x)**2

    den = simpson(lambda x: u(x)*z(x)**2)
    numer = simpson(num)
    expected_numer = (56*pi*pi-387)/4000
    expected_quotient = (56*pi*pi-387)/6800
    assert min(m(i/4096) for i in range(4097)) > 0.5
    assert abs(numer - expected_numer) < 2e-9
    assert abs(den - 1.7) < 2e-9
    assert abs(numer/den - expected_quotient) < 2e-9
    assert expected_quotient > 0
    return numer/den


def two_site_analogue():
    """Exact rational patch analogue; NOT a proof of the PDE assertion."""
    u = (F(1), F(2))
    p = (F(1,2), F(1,2))
    q = (F(1,3), F(2,3))
    m = (F(4,5), F(21,10))
    d_res, d_inv = F(1,10), F(1,10)
    for i in (0, 1):
        j = 1-i
        flux = d_res*(u[j]/p[j] - u[i]/p[i])
        assert flux+u[i]*(m[i]-u[i]) == 0
    assert q[0]+q[1] == 1
    a11 = d_inv + q[0]*u[0]
    a22 = d_inv + q[1]*u[1]
    b11, b22 = q[0]*m[0], q[1]*m[1]
    # det(A-k B)=const*(k - 55/56)*(k-5/3)
    for k in (F(0), F(1,2), F(55,56), F(1), F(5,3), F(2)):
        det = (a11-k*b11)*(a22-k*b22)-d_inv*d_inv
        assert det == (3*k-5)*(56*k-55)/450
    assert F(0) < F(55,56) < F(1)
    return F(55,56)


if __name__ == '__main__':
    value = continuum_example()
    threshold = two_site_analogue()
    print('PASS: smooth 1D lower bound = %.12f' % value)
    print('PASS: independent exact two-patch threshold = %s' % threshold)
    print('These checks supplement but do not establish the general PDE theorem.')
