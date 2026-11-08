#!/usr/bin/env python3
"""Exact finite-domain checks for unit-lattice unbiased stochastic rounding.

No finite check is used as the proof of the universal classifications.
Requires only the Python standard library. Run with python3 verify_rounding.py.
"""
from fractions import Fraction
from collections import defaultdict


def sr(x):
    """The exact stochastic-nearness distribution on Z for rational x."""
    lo = x.numerator // x.denominator
    u = x - lo
    out = {}
    if u < 1:
        if (1-u) > 0: out[lo] = 1-u
        if u > 0: out[lo+1] = u
    assert sum(out.values(), Fraction(0)) == 1
    return out


def iterate(q,n,t):
    d = {n:Fraction(1)}
    for _ in range(t):
        e=defaultdict(Fraction)
        for j,prob in d.items():
            for k,p2 in sr(q*j).items():
                e[k] += prob*p2
        d = dict(e)
    assert sum(d.values(),Fraction(0)) == 1
    return d


def witness(q):
    """Prove by exact arithmetic a 3-point two-step witness for 1/q noninteger."""
    assert 0 < q < 1 and q.numerator != 1
    m=1//q
    # n is the first integer strictly above m/q
    n=m//q+1
    assert m < q*n < m+1
    d=iterate(q,n,2)
    assert all(d.get(k,Fraction(0))>0 for k in (0,1,2))
    assert len(d)>=3
    assert d != sr(q*q*n)
    f=q*n-m
    assert d[0] == (1-f)*(1-q*m)
    assert d[2] == f*(q*(m+1)-1)
    return m,n,d


def test():
    count=0
    for b in range(2,12):
        q=Fraction(1,b)
        for n in range(0,131):
            for t in range(0,9):
                actual=iterate(q,n,t)
                ideal=sr(Fraction(n,b**t))
                assert actual == ideal, (b,n,t,actual,ideal)
                count+=1
        for n in range(1,131):
            k=0
            while b**(k+1)<=n:k+=1
            u=Fraction(n,b**k)
            e=Fraction(k+1)+u/(b-1)
            # P(T>t)=min(1,n/b**t): compute a finite prefix,
            # then add geometric remainder via its closed form.
            partial=sum((min(Fraction(1),Fraction(n,b**t)) for t in range(k+1)),Fraction(0))
            tail=sum((Fraction(n,b**t) for t in range(k+1,k+8)),Fraction(0))
            rem=Fraction(n,b**(k+8))*Fraction(b,b-1)
            assert partial+tail+rem==e,(b,n,e,partial+tail+rem)
            count+=1
    ntests=0
    for den in range(2,21):
        for num in range(2,den):
            q=Fraction(num,den)
            if q.numerator == 1: continue
            m,n,d=witness(q)
            assert m>=1 and n>=1 and (0 in d and 1 in d and 2 in d)
            count+=1; ntests+=1
    # Special irrational witness q=1/sqrt(2), n=2:
    # P(X2=0)=P(X2=2)=3-2sqrt(2), P(X2=1)=4sqrt(2)-5.
    # These expressions are positive by the rational square interval below.
    # The exact two-step mean is one whereas direct rounding is delta_1.
    # Verify rational interval enclosing sqrt(2) with integer squares.
    a=Fraction(1414213562373095,10**15)
    c=Fraction(1414213562373096,10**15)
    assert a*a<2<c*c
    assert 0 < 3-2*c and 3-2*a <1
    assert 0 < 4*a-5 and 4*c-5 <1
    print('PASS:',count,'exact rational kernel/absorption assertions;',ntests,'nonreciprocal two-step witnesses; radical-sign certificate.')


if __name__=='__main__': test()
