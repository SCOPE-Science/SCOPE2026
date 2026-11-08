"""Exact checks for even moments of real degree-two harmonics on the 2-sphere.

Only Python 3 standard library is required. This verifies finite rational
instances, not the general theorem.
"""
from fractions import Fraction as F
from math import factorial, comb
from itertools import product


def double_odd(n):
    v = 1
    for k in range(1, n + 1):
        v *= 2 * k - 1
    return v


def radial_moment(p):
    ans = 1
    for j in range(p):
        ans *= 3 + 2 * j
    return ans


def poch_half(j):
    v = F(1)
    for k in range(j):
        v *= F(2 * k + 1, 2)
    return v


def gaussian_formula(eigs, m):
    s2 = sum(x * x for x in eigs)
    s3 = sum(x ** 3 for x in eigs)
    assert sum(eigs) == 0 and s2 > 0
    z = F(0)
    for ell in range(m // 3 + 1):
        j = m - 3 * ell
        k = 2 * ell
        z += (poch_half(j+k) / (factorial(j)*factorial(k))
              * (2*s2)**j * (F(8,3)*s3)**k)
    return F(factorial(2*m))*z / radial_moment(2*m)


def direct_sphere(eigs, m):
    # On the uniform 2-sphere, U_i^2 have Dirichlet(1/2,1/2,1/2) law.
    p = 2 * m
    ans = F(0)
    for a in range(p+1):
        for b in range(p-a+1):
            c = p-a-b
            coeff = F(factorial(p),factorial(a)*factorial(b)*factorial(c))
            moment = F(double_odd(a)*double_odd(b)*double_odd(c),radial_moment(p))
            ans += coeff * eigs[0]**a * eigs[1]**b * eigs[2]**c * moment
    return ans


def ratio(eigs,m):
    s2 = sum(x*x for x in eigs)
    return gaussian_formula(eigs,m) / F(2*s2,15)**m


def run():
    tests = 0
    for a,b in product(range(-4,5),repeat=2):
        eigs=tuple(F(t) for t in (a,b,-a-b))
        if eigs==(F(0),)*3:
            continue
        for m in range(1,9):
            assert gaussian_formula(eigs,m) == direct_sphere(eigs,m),(eigs,m)
            tests += 1
    print('EXACT_SPHERE_MOMENT_EXPANSIONS_OK',tests)
    # The sixth-moment extremizers and fourth-moment flatness are exact.
    amin = (F(1),F(0),F(-1))
    amax = (F(2),F(-1),F(-1))
    assert ratio(amin,2)==ratio(amax,2)==F(15,7)
    assert ratio(amin,3)==F(5625,1001)
    assert ratio(amax,3)==F(6625,1001)
    print('FOURTH_MOMENT_FLAT_AND_SIXTH_MOMENT_ENDPOINTS_OK',F(5625,1001),F(6625,1001))
    # For higher even moments: coefficients of the spectral discriminant are positive.
    for m in range(3,21):
        for ell in range(1,m//3+1):
            j=m-3*ell
            c=poch_half(m-ell)/ (factorial(j)*factorial(2*ell)) * F(2)**j * F(8,3)**(2*ell)
            assert c>0
    print('STRICT_POSITIVE_DISCRIMINANT_COEFFICIENTS_OK',18)
    # Exact minimizer/maximizer profile for many algebraic rational spectra.
    for a,b in product(range(-8,9),repeat=2):
        vals=tuple(F(t) for t in (a,b,-a-b))
        s2=sum(t*t for t in vals)
        if not s2:continue
        s3=sum(t**3 for t in vals)
        d=s3*s3/s2**3
        assert 0<=d<=F(1,6)
        for m in range(3,11):
            assert ratio(amin,m)<=ratio(vals,m)<=ratio(amax,m)
    print('EXACT_MOMENT_EXTREMA_IN_RATIONAL_GRID_OK',17*17-1)
    print('ALL_EVEN_SPHERICAL_HARMONIC_CHECKS_OK')


if __name__=='__main__':
    run()
