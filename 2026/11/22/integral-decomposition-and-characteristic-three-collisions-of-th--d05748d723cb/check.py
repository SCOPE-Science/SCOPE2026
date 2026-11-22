"""Finite-field consistency checks for the integral Penrose quartic model.

This checks finite examples and monomial length counts; the universal proof is
by local equations and finite-flat descent, not by this enumeration.
Run with Python 3, no external packages required.
"""
from itertools import product
from math import gcd


def quartics(point, p):
    x, y, z, w = point
    return (
        x*y*z*w,
        w*(x**3-y**3+z**3),
        z*(x**3+y**3+w**3),
        y*(-x**3+z**3+w**3),
        x*(y**3+z**3-w**3),
    )


def projective_points(p):
    for first in range(4):
        for tail in product(range(p), repeat=3-first):
            yield (0,)*first+(1,)+tail


def check_prime(p):
    points = [v for v in projective_points(p)
              if all(t%p == 0 for t in quartics(v, p))]
    expected = 4+4*gcd(3,p-1)**2
    assert len(points)==expected, (p,len(points),expected)
    assert len(points)==len(set(points))
    assert sum(sum(c!=0 for c in v)==1 for v in points)==4
    assert sum(sum(c!=0 for c in v)==3 for v in points)==expected-4
    return len(points)


def check_special_fiber_monomials():
    basis = [(i,j) for i in range(3) for j in range(3)]
    h = [sum(i+j==degree for i,j in basis) for degree in range(5)]
    assert h==[1,2,3,2,1]
    assert len(basis)==9
    # Local Artin algebra k[u,v]/(u^3,v^3) has m^5=0, m^4!=0.
    assert max(i+j for i,j in basis)==4
    # Four reduced coordinate points and four length-nine local rings.
    assert 4+4*len(basis)==40
    return h


if __name__ == '__main__':
    for p in [2,3,5,7,11,13,17,19]:
        print('F_%s rational points: %s' % (p, check_prime(p)))
    print('F_3 nonreduced local Hilbert function:',check_special_fiber_monomials())
    print('Checks passed; finite experiments are not an infinite proof.')
