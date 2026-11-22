#!/usr/bin/env python3
"""Exact rational sign certificate for a four-node Gaussian kernel quadrature.

Requires only Python 3's standard library. All assertions are exact fractions.
"""
from fractions import Fraction as Q
from math import factorial

A = Q(9, 16)
B = Q(4, 5)
SHAPE = Q(2)
ORDER = 80


def taylor_exp(z, order):
    """Return rational polynomial and a rigorous error radius for exp(-z)."""
    assert z >= 0
    term = Q(1)
    value = term
    for k in range(1, order + 1):
        term *= -z / k
        value += term
    return value, z**(order + 1) / factorial(order + 1)


def taylor_mass(v, shape, order):
    """Half-integral of a Gaussian translate over [-1,1], with bound."""
    assert 0 <= v < 1 and shape > 0
    result = Q(0)
    term = Q(1)
    for k in range(order + 1):
        moment = ((1-v)**(2*k+1) + (1+v)**(2*k+1)) / (2*(2*k+1))
        result += term*moment
        term *= -shape / (k+1)
    err = (shape*(1+v)**2)**(order+1) / factorial(order+1)
    return result, err


def add(items):
    return (sum((v for v,e in items), Q(0)), sum((e for v,e in items), Q(0)))


def product(u, v):
    """Interval enclosure for product, expressed as center and error."""
    x,ex=u
    y,ey=v
    return x*y, ex*abs(y) + ey*abs(x) + ex*ey


def negate(u):
    return -u[0], u[1]


def cert():
    a, b, lam, n=A,B,SHAPE,ORDER
    AA = add([(Q(1),Q(0)),taylor_exp(4*lam*a*a,n)])
    BB = add([(Q(1),Q(0)),taylor_exp(4*lam*b*b,n)])
    CC = add([taylor_exp(lam*(b-a)**2,n),taylor_exp(lam*(b+a)**2,n)])
    FA = taylor_mass(a,lam,n)
    FB = taylor_mass(b,lam,n)
    outer = add([product(AA,FB),negate(product(CC,FA))])
    inner = add([product(BB,FA),negate(product(CC,FB))])
    det = add([product(AA,BB),negate(product(CC,CC))])
    assert outer[0] + outer[1] < -Q(1,100), 'Outer sign not certified'
    assert inner[0] - inner[1] > Q(1,100), 'Inner sign not certified'
    assert det[0] - det[1] > Q(1,100), 'Determinant sign not certified'
    assert abs(outer[1]) < Q(1,10**8), 'Interval too coarse'
    print('CERTIFIED at lambda=2, a=9/16, b=4/5; Taylor order=80')
    for name, pair in [('outer numerator',outer),('inner numerator',inner),('determinant',det)]:
        c,e=pair
        print(f'{name}: center={float(c):.14f}; uncertainty <= {float(e):.3e}')
    print('Both outer weights strictly negative; both inner weights strictly positive.')
    print('All inequalities use exact rational arithmetic; no floating-point comparison.')

if __name__=='__main__':
    cert()
