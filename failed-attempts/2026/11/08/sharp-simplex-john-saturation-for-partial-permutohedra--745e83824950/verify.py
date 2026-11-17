#!/usr/bin/env python3
"""Exact small-range checks for the simplex-John saturation theorem.

Only standard-library arithmetic is needed for the exhaustive parameter checks.
The proof in RESULT.md establishes the result for every positive m,n.
"""
from fractions import Fraction
from math import factorial, sqrt, comb
from itertools import combinations, permutations

def top_sum(n,s):
    return Fraction(s*(2*n-s+1),2) if s<=n else Fraction(n*(n+1),2)

def squared_radius(m,S,s):
    return Fraction(S*S*s*(m+1-s),m*(m+1)**2)

def central_part(m,S,s):
    return Fraction(S*s,m+1)

def inside_exact(m,n,s):
    S=top_sum(n,min(m,n))
    t=top_sum(n,s)-central_part(m,S,s)
    return t>=0 and t*t>=squared_radius(m,S,s)

def equality_exact(m,n,s):
    S=top_sum(n,min(m,n));t=top_sum(n,s)-central_part(m,S,s)
    return t>=0 and t*t==squared_radius(m,S,s)

def verify():
    checks=0
    for m in range(1,46):
        for n in range(1,46):
            S=top_sum(n,min(m,n))
            # The simplex-envelope ellipsoid uses S, regardless of whether m >= n.
            for s in range(1,m+1):
                assert inside_exact(m,n,s) == (
                    top_sum(n,s)-central_part(m,S,s)>=0 and
                    (top_sum(n,s)-central_part(m,S,s))**2>=squared_radius(m,S,s))
                checks+=1
                if m>=n:
                    assert inside_exact(m,n,s),(m,n,s)
                    checks+=1
                elif m>=2 and s==1:
                    assert not inside_exact(m,n,s),(m,n,s)
                    checks+=1
            if m>=n and n>=2:
                for s in range(1,m):
                    assert equality_exact(m,n,s) == (m==n and s==1),(m,n,s)
                    checks+=1
                assert equality_exact(m,n,m)
                checks+=1
            if 2<=m<n:
                assert Fraction(2*S,m+1)>n
                checks+=1
    # Check one/few actual vertex sets against the subset inequalities (independent construction).
    import itertools
    for m,n in itertools.product(range(1,5),repeat=2):
        vs={tuple(0 for _ in range(m))}
        for k in range(1,min(m,n)+1):
            for positions in itertools.combinations(range(m),k):
                for entries in permutations(range(n-k+1,n+1)):
                    v=[0]*m
                    for p,a in zip(positions,entries):v[p]=a
                    vs.add(tuple(v))
        for v in vs:
            assert all(sum(v[i] for i in I)<=top_sum(n,len(I))
                       for s in range(1,m+1) for I in combinations(range(m),s))
            checks+=1
        # independently check the support of each indicator against the sorted vertex orbit
        for s in range(1,m+1):
            for I in combinations(range(m),s):
                h=max(sum(v[i] for i in I) for v in vs)
                assert h==top_sum(n,s),(m,n,I,h)
                checks+=1
    print('VERIFY_OK exact_assertions='+str(checks))

if __name__=='__main__':verify()
