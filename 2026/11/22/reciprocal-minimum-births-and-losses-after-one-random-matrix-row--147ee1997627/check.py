#!/usr/bin/env python3
"""Finite exact and numerical checks for mutual-minimum row deletion.

Python standard library only. This is a checker, not an infinite-proof oracle.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import factorial, exp

def deletion_counts(v, n):
    rowmin = [min(range(n),key=lambda j:v[i*n+j]) for i in range(n)]
    colmin = [min(range(n),key=lambda i:v[i*n+j]) for j in range(n)]
    newcol = [min(range(1,n),key=lambda i:v[i*n+j]) for j in range(n)]
    before = {(i,rowmin[i]) for i in range(n) if colmin[rowmin[i]] == i}
    after = {(i,rowmin[i]) for i in range(1,n) if newcol[rowmin[i]] == i}
    assert not any(i != 0 for i,j in before-after)
    return len(before-after), len(after-before)

def exact_enumeration(n):
    tab=Counter(deletion_counts(v,n) for v in permutations(range(n*n)))
    den=factorial(n*n)
    def moment(f):
        return Fraction(sum(c*f(l,a) for (l,a),c in tab.items()),den)
    assert moment(lambda l,a:l) == Fraction(n,2*n-1)
    assert moment(lambda l,a:a) == Fraction(n,2*(2*n-1))
    assert moment(lambda l,a:l*a) == Fraction(n,2*(3*n-2))+Fraction(n,8*(2*n-1))
    assert sum(tab.values()) == den
    print('EXACT',n,'permutations',den,'outcomes',dict(sorted(tab.items())))

def simpson(f, N=4096):
    assert N%2 == 0
    s=f(0)+f(1)
    for i in range(1,N):
        s+=(4 if i%2 else 2)*f(i/N)
    return s/(3*N)

def pgf(s,t):
    return simpson(lambda u:(1+(s-1)*u+s*(t-1)*u*u/2)*exp((t-1)*u*u/4))

def closed_marginals():
    for s in (0,.2,.5,1):
        assert abs(pgf(s,1)-(1+s)/2)<1e-10
    for t in (0,.1,.25,.5,.8,1):
        assert abs(pgf(1,t)-exp((t-1)/4))<1e-10
    for s,t in ((0,0),(0,.4),(.7,.2),(1,1)):
        assert abs(pgf(s,t)-(s*exp((t-1)/4)+(1-s)*simpson(lambda u:(1-u)*exp((t-1)*u*u/4))))<1e-10
    # Exact derivatives of the limiting PGF at (s,t)=(1,1):
    assert Fraction(1,2)*Fraction(1,4)==Fraction(1,8)
    assert Fraction(11,48)-Fraction(1,8)==Fraction(5,48)
    assert Fraction(1,4)+Fraction(1,4)-2*Fraction(5,48)==Fraction(7,24)
    assert Fraction(11,48)/Fraction(1,2)==Fraction(11,24)
    assert (Fraction(1,4)-Fraction(11,48))/Fraction(1,2)==Fraction(1,24)
    for n in (2,3,4,5,10,100,10000):
        EL=Fraction(n,2*n-1)
        EA=Fraction(n,2*(2*n-1))
        ELA=Fraction(n,2*(3*n-2))+Fraction(n,8*(2*n-1))
        C=ELA-EL*EA
        assert C>0
        assert C==Fraction(n*(10*n*n-15*n+6),8*(2*n-1)**2*(3*n-2))
    print('LIMIT marginal PGFs, mixed moments, positive finite covariance: pass')

if __name__=='__main__':
    for n in (2,3):exact_enumeration(n)
    closed_marginals()
    print('All finite and numerical checks passed; no claim of mechanical certification of infinite limit.')
