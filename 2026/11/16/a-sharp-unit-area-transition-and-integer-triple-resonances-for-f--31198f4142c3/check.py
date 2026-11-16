"""Standalone checks of the first-Hermite disk localization identities.

Run with Python 3, SymPy and mpmath installed. Finite tests corroborate
but do not prove the infinite-index and all-area statements.
"""
from math import exp, factorial
from fractions import Fraction
import sympy as sp
import mpmath as mp

s = sp.symbols('s', positive=True)


def closed_sym(j):
    if j == 0:
        return 1-(1+s)*sp.exp(-s)
    return 1-sp.exp(-s)*sum(s**i/sp.factorial(i) for i in range(j)) \
        +(j-1-s)*sp.exp(-s)*s**j/sp.factorial(j)


def coefficient(j, x):
    """The polynomial multiplied by exp(-x) in lambda_j(x)."""
    if j == 0:
        return -(1+x)
    return -sum(x**i/sp.factorial(i) for i in range(j)) \
           +(j-1-x)*x**j/sp.factorial(j)


def lam(j, area):
    x = mp.mpf(area)
    if j == 0:
        return 1-(1+x)*mp.exp(-x)
    return mp.quad(lambda t: mp.exp(-t)*t**(j-1)*(j-t)**2/mp.factorial(j),[0,x])


def lam_closed(j, area):
    x = mp.mpf(area)
    if j == 0:
        return 1-(1+x)*mp.exp(-x)
    term = mp.fsum(x**i/mp.factorial(i) for i in range(j))
    return 1-mp.exp(-x)*term+(j-1-x)*mp.exp(-x)*x**j/mp.factorial(j)


def main():
    mp.mp.dps = 55
    for j in range(35):
        diff = sp.factor(sp.exp(s)*(closed_sym(j+1)-closed_sym(j))
                         +s**j*(s-j)*(s-j-1)/sp.factorial(j+1))
        assert diff == 0, (j,diff)

    # Integer-area triple collisions are checked as exact rational
    # equality of the polynomial coefficients of the common exp(-area).
    for m in range(1,36):
        a = [sp.cancel(coefficient(j, sp.Integer(m))) for j in range(m+3)]
        assert a[m-1] == a[m] == a[m+1], m
        assert all(a[k] > a[k+1] for k in range(m-1)), m
        assert a[m+1] > a[m+2], m

    cases = [mp.mpf('0.001'),mp.mpf('0.08'),mp.mpf('0.35'),mp.mpf('0.999'),
             mp.mpf('1'),mp.mpf('1.001'),mp.mpf('1.1'),mp.mpf('1.9'),
             mp.mpf('2'),mp.mpf('2.5'),mp.mpf('3'),mp.mpf('3.8'),
             mp.mpf('5'),mp.mpf('10.7')]
    numeric_count=0
    maxerr=mp.mpf('0')
    for x in cases:
        vals=[lam_closed(j,x) for j in range(65)]
        for j in range(0,17):
            v=lam(j,x)
            err=abs(v-vals[j]);maxerr=max(err,maxerr)
            assert err < mp.mpf('1e-42'),(j,x,err)
            numeric_count += 1
        if x<1:
            assert vals[1] > max(vals[0],*vals[2:])
            expected=1-(1+x*x)*mp.exp(-x)
        elif x==1:
            assert abs(vals[0]-vals[1]) < mp.mpf('1e-42')
            assert abs(vals[1]-vals[2]) < mp.mpf('1e-42')
            assert vals[0] > max(vals[3:])
            expected=1-2/mp.e
        else:
            assert vals[0] > max(vals[1:])
            expected=1-(1+x)*mp.exp(-x)
        assert abs(max(vals)-expected) < mp.mpf('1e-42'),x
        for j in range(25):
            delta=vals[j+1]-vals[j]
            prediction=-mp.exp(-x)*x**j/(mp.factorial(j+1))*(x-j)*(x-j-1)
            assert abs(delta-prediction) < mp.mpf('1e-42'),(j,x)
    print('FIRST_HERMITE_DISK_PASS adjacent_symbolic=35 integer_triples=35 integral_cases=',
          numeric_count,'area_grid=',len(cases),'max_integral_error=',mp.nstr(maxerr,5),sep='')


if __name__=='__main__':
    main()
