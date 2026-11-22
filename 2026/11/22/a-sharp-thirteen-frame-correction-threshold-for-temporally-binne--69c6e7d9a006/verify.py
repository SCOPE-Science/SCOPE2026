#!/usr/bin/env python3
"""Exact rational checks for a canonical differential-photometry boxcar model.

This program checks algebraic identities and finite boundary cases; the proof
of the unbounded-index assertion is supplied in RESULT.md.
"""
from fractions import Fraction as Q


def b_closed(m):
    assert isinstance(m, int) and m >= 0
    n = 2*m + 1
    return Q(3) + Q(4,n) - Q(4,2**m) - Q(2,n*4**m)


def b_sums(m):
    n = 2*m+1
    rho = Q(1,2)
    c = 1 + 2*sum((rho**j for j in range(1,m+1)), Q(0))
    s = n + 2*sum(((n-k)*rho**k for k in range(1,n)), Q(0))
    return 2*c-Q(s,n)


def risk(m,eta):
    return 1+(eta-b_closed(m))/(2*m+1)


def numerator(m):
    n = 2*m+1
    y = Q(1,2**m)
    return -8+2*y*n*(n+2)+Q(1,2)*y*y*(3*n+8)


def run():
    checks=0
    for m in range(0,45):
        assert b_sums(m)==b_closed(m); checks+=1
        assert b_closed(m+1)-b_closed(m)==numerator(m)/((2*m+1)*(2*m+3)); checks+=1
    for m in range(0,6):
        assert numerator(m)>0; checks+=1
    assert numerator(6)<0; checks+=1
    assert b_closed(6)==Q(86399,26624); checks+=1
    eta_star=b_closed(6)
    for m in range(0,250):
        if m != 6:
            assert b_closed(m)<eta_star; checks+=1
        assert risk(m,eta_star)>=1; checks+=1
    assert risk(6,eta_star)==1; checks+=1
    eta=Q(13,4)
    assert risk(5,eta)>risk(6,eta)<risk(7,eta); checks+=1
    for m in range(0,250):
        assert risk(m,eta)>1; checks+=1
    assert Q(13,4)>eta_star; checks+=1
    for m in range(6,250):
        n=2*m+1
        assert Q(n+4,2*n)<1; checks+=1
        assert Q(3*n+14,4*(3*n+8))<1; checks+=1
    print('PASS:',checks,'exact-rational supplementary assertions')

if __name__=='__main__':
    run()
