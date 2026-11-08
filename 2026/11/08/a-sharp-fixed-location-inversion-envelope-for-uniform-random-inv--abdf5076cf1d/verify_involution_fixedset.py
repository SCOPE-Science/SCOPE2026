#!/usr/bin/env python3
"""Exact enumeration checks for location-conditioned inversions in involutions."""
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict
from itertools import combinations

@lru_cache(None)
def perfect_matchings(verts):
    if not verts:
        return ((),)
    head=verts[0]
    return tuple(((head, b),)+tail
                 for b in verts[1:]
                 for tail in perfect_matchings(tuple(x for x in verts[1:] if x!=b)))

def inv_count(perm):
    n=len(perm)
    return sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))

def predict(n, fixed):
    fixed=set(fixed)
    remaining=tuple(i for i in range(1,n+1) if i not in fixed)
    r=len(remaining)
    if r==0:
        return Fraction(0)
    x=sum(sum(y<s for y in remaining)*sum(y>s for y in remaining) for s in fixed)
    return Fraction(r*r,4)+Fraction(2*x,r-1)

def run(nmax=12):
    assertions=0
    trials=0
    for n in range(2,nmax+1):
        for k in range(n+1):
            if (n-k)%2:continue
            r=n-k
            for S in combinations(range(1,n+1),k):
                R=tuple(i for i in range(1,n+1) if i not in S)
                arr=[]
                for pairs in perfect_matchings(R):
                    perm=list(range(1,n+1))
                    for a,b in pairs:
                        perm[a-1]=b
                        perm[b-1]=a
                    arr.append(inv_count(perm))
                empirical=Fraction(sum(arr),len(arr))
                expected=predict(n,S)
                assert empirical==expected,(n,S,empirical,expected)
                assertions+=1
                if r>=2:
                    lower=Fraction(r*r,4)
                    upper=lower+Fraction(k*r*r,2*(r-1))
                    assert lower<=expected<=upper
                    assertions+=2
                trials+=len(arr)
                if r>=2 and k>=1:
                    # Fully exact unique extremizer gap conditions, not location uniqueness.
                    A=[sum(x<s for x in R) for s in S]
                    is_lower=all(a in (0,r) for a in A)
                    is_upper=all(a==r//2 for a in A)
                    assert (expected==lower)==is_lower,(n,S,'lower')
                    assert (expected==upper)==is_upper,(n,S,'upper')
                    assertions+=2
    print('PASS', 'nmax=',nmax,'fixed-set checks=',assertions,'involutions=',trials)

if __name__=='__main__':run()
