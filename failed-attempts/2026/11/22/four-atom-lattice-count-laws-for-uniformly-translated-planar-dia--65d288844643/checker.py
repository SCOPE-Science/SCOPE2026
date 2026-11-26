#!/usr/bin/env python3
"""Exact arithmetic consistency and deterministic geometric checks for a diamond count law."""
from fractions import Fraction as F
from collections import Counter
from math import floor, ceil

def predicted(n, s):
    assert isinstance(n,int) and n>=1 and F(0)<=s<F(1)
    if s<=F(1,2):
        return {2*n*n:(1-2*s)**2,2*n*n+n:4*s*(1-2*s),
                2*n*n+2*n:2*s*s,2*n*n+2*n+1:2*s*s}
    t=1-s
    return {2*n*n+2*n:2*t*t,2*n*n+2*n+1:2*t*t,
            2*n*n+3*n+1:4*t*(1-2*t),2*n*n+4*n+2:(1-2*t)**2}

def count(n,s,u,v):
    r=n+s; a=u+v;b=u-v
    p=range(ceil(a-r),floor(a+r)+1)
    q=range(ceil(b-r),floor(b+r)+1)
    return sum((x-y)%2==0 for x in p for y in q)

checks=0
for n in range(1,16):
    for s in [F(0),F(1,17),F(1,10),F(1,4),F(2,5),F(1,2),F(3,5),F(3,4),F(7,8),F(16,17)]:
        pmf=predicted(n,s)
        assert sum(pmf.values())==1
        assert min(pmf.values())>=0
        assert sum(value*p for value,p in pmf.items())==2*(n+s)**2
        checks+=3
        # Numerical distribution via an independently defined lattice count
        # at rational grid centres, with deterministic off-boundary shifts.
        if n in (1,2,5):
            m=120
            observed=Counter(count(n,s,F(i,m)+F(1,3*m),
                                         F(j,m)+F(1,7*m))
                             for i in range(m) for j in range(m))
            assert set(observed).issubset(set(pmf))
            # The specified phases are rational aligned with this grid except
            # the 1/17 and 16/17 cases; bounded Riemann grid error is allowed.
            for v,prob in pmf.items():
                assert abs(F(observed[v],m*m)-prob)<F(3,100)
                checks+=1
print('PASS',checks,'exact rational identities and distribution comparisons')
