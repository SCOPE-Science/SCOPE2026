#!/usr/bin/env python3
"""Exact rational checks for a clipped-ramp stratified control variate.

No external packages required. Rational evaluations complement, but do not
replace, the Hilbert-space minimax proof in RESULT.md.
"""
from fractions import Fraction as F


def clipped_pieces(n):
    n = F(n)
    a = (n - 1) / (2*n)
    b = (n + 1) / (2*n)
    return [(F(0), a, -F(1)/(2*n), F(0)),
            (a, b, -F(1,2), F(1)),
            (b, F(1), F(1)/(2*n), F(0))]


def integrate_linear(pieces, t=F(0)):
    out=F(0)
    for lo, hi, aa, bb in pieces:
        l=max(lo,t)
        if l<hi:
            out += aa*(hi-l)+bb*(hi*hi-l*l)/2
    return out


def integrate_square(pieces):
    out=F(0)
    for lo,hi,aa,bb in pieces:
        out+=aa*aa*(hi-lo)+aa*bb*(hi*hi-lo*lo)+bb*bb*(hi**3-lo**3)/3
    return out


def worst_step_risk(n, t, pieces=None):
    if pieces is None:pieces=clipped_pieces(n)
    assert integrate_linear(pieces)==0
    a=integrate_square(pieces)
    covariance=integrate_linear(pieces,t)
    return (n*a+t*(1-t)-2*covariance)/n**2


def theorem(n):
    n=F(n)
    return F(1)/(4*n**2)-F(1)/(4*n**3)+F(1)/(12*n**4)


def expected_lower(n):
    n=F(n)
    # Uniform prior on jump position in the central interval:
    # E[t(1-t)] - ||E h_t||^2/n.
    m2=F(1,4)-F(1)/(12*n*n)
    h2=F(1,4)-F(1)/(6*n)
    return (m2-h2/n)/n**2


def main():
    checks=0
    for n in [1,2,3,4,5,8,12,20]:
        pieces=clipped_pieces(n)
        assert integrate_linear(pieces)==0; checks+=1
        norm=integrate_square(pieces)
        assert norm==F(1,4*n*n)-F(1,6*n**3);checks+=1
        assert expected_lower(n)==theorem(n);checks+=1
        lo=F(n-1,2*n);hi=F(n+1,2*n)
        at=worst_step_risk(n,F(1,2))
        assert at==theorem(n);checks+=1
        for k in range(301):
            t=F(k,300)
            risk=worst_step_risk(n,t)
            assert risk<=theorem(n);checks+=1
            if lo<=t<=hi:
                assert risk==theorem(n);checks+=1
        assert theorem(n)<F(1,4*n*n);checks+=1
        print(f'n={n:2d}, sharp risk={theorem(n)}, baseline={F(1,4*n*n)}, risk ratio={4*n*n*theorem(n)}')
    assert theorem(2)==F(7,192);checks+=1
    assert theorem(1)==F(1,12);checks+=1
    # Exact explicit covariance test for n=2, two jumps of heights 1/3, 2/3
    n=2; pc=clipped_pieces(n)
    t1=F(1,3); t2=F(3,4)
    h1=F(1,3);h2=F(2,3)
    c1=integrate_linear(pc, F(2,3)) # global t1 lies in first cell: local 2/3
    c2=integrate_linear(pc, F(1,2)) # global t2 lies in second cell: local 1/2
    v= (h1*h1*F(2,9)+h2*h2*F(1,4)
       -2*h1*c1-2*h2*c2+2*integrate_square(pc))/4
    assert v<=theorem(2);checks+=1
    print(f'multiple-jump test, n=2: variance={v}, maximum={theorem(2)}')
    print(f'PASS: {checks} exact rational assertions')

if __name__=='__main__':main()
