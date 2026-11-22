#!/usr/bin/env python3
"""Reproduce exact polynomial identities and numerical asymptotics for a rational competitive map.

Only the Python standard library is required. All finite computations are diagnostics;
proof for arbitrary parameters is supplied in RESULT.md.
"""
from fractions import Fraction as Q
from math import log, isfinite

def setup(a, b, c, d):
    D = b * (c*d-1) + a*d
    assert D > a*d and c*d > 1
    X = a*b/D
    p = a+X
    lam = a*d/D
    kap = a*d/(b*(a+c*b))
    assert 0 < lam < 1
    return D, X, p, lam, kap

def step(a, b, c, d, p, x, y):
    return (p*x/(a+x+c*y), b*y/(d*x+y))

def defect(b, X, x, y):
    return x/X+y/b-1

cases = [(1, 3, 2, 2), (2, 5, 3, 1), (3, 7, 2, 3), (5, 2, 3, 2)]
for aa, bb, cc, dd in cases:
    a, b, c, d = map(Q, (aa, bb, cc, dd))
    D, X, p, lam, kap = setup(a,b,c,d)
    assert d*X*(a+c*b) == b*p
    assert p/(a+c*b) == lam
    assert b/(d*X) == 1/lam
    assert kap == a*d/(b*(a+c*b))
    # These rational tests exercise points on either side of the invariant segment.
    for x in (Q(1,17), X/4, Q(2,3), X*3):
        for y in (Q(1,7), b/3, Q(7,2), b*2):
            xx, yy = step(a,b,c,d,p,x,y)
            k = a*d*x/((a+x+c*y)*(d*x+y))
            assert defect(b,X,xx,yy) == k*defect(b,X,x,y)
            assert xx > 0 and yy > 0 and k > 0
    # Whole two-sided explicit segment solution for n=-8,...,8.
    x0 = X/4
    for n in range(-8,9):
        xn = X/(1+(X/x0-1)*lam**(-n))
        yn = b*(1-xn/X)
        xnext = X/(1+(X/x0-1)*lam**(-n-1))
        ynext = b*(1-xnext/X)
        assert step(a,b,c,d,p,xn,yn) == (xnext,ynext)
        assert 0<xn<X and 0<yn<b
        assert defect(b,X,xn,yn)==0

# The first case has a sharp exponent 0.5*log(2/11).
a,b,c,d = 1.0,3.0,2.0,2.0
D,X,p,lam,kap = [float(v) for v in setup(Q(1),Q(3),Q(2),Q(2))]
x,y=0.1,0.5
H = defect(b,X,x,y)
assert H != 0
accumulated_log_defect=log(abs(H))
for j in range(300):
    U=a+x+c*y
    V=d*x+y
    factor=a*d*x/(U*V)
    assert factor>0
    accumulated_log_defect += log(factor)
    x,y=step(a,b,c,d,p,x,y)
    assert isfinite(x) and isfinite(y) and x>0
assert abs(accumulated_log_defect/(300**2)-log(lam)/2)<0.03
print('LESLIE_HETEROCLINIC_CHECK_OK')
