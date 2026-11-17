"""Exact finite audit of diameter formulas for diagonal cube sections.

This script is illustrative; the theorem is proved analytically by
vertex classification and the strict rearrangement inequality.
"""
from fractions import Fraction
from itertools import combinations
from math import factorial

def vertices(n, q):
    k = int(q)
    r = q-Fraction(k)
    vals = set()
    inds = tuple(range(n))
    for ones in combinations(inds,k):
        remain=[i for i in inds if i not in ones]
        fractional_positions=remain if r else [None]
        for j in fractional_positions:
            v=[Fraction(0)]*n
            for i in ones:v[i]=Fraction(1)
            if j is not None:v[j]=r
            vals.add(tuple(v))
    return sorted(vals)

def theorem(n,q):
    if q==0:return Fraction(0),0
    k=int(q);r=q-k
    if r==0:
        return Fraction(8*k),factorial(n)//(2*factorial(k)**2*factorial(n-2*k))
    if n%2 and k==(n-1)//2:
        return Fraction(8*k),factorial(n)//(2*factorial(k)**2)
    assert 2*(k+1)<=n
    return Fraction(8)*(k+r*r),factorial(n)//(2*factorial(k)**2*factorial(n-2*k-2))

def check():
    tested=0
    for n in range(3,8):
        fractions=[Fraction(a,b) for b in (1,2,3) for a in range(b*n//2+1) if Fraction(a,b)<=Fraction(n,2)]
        for q in sorted(set(fractions)):
            vv=vertices(n,q)
            ds=[sum(4*(a-b)**2 for a,b in zip(v,w)) for v,w in combinations(vv,2)]
            dmax=max(ds,default=Fraction(0))
            count=sum(d==dmax for d in ds) if ds else 0
            expected=theorem(n,q)
            assert (dmax,count)==expected,(n,q,(dmax,count),expected)
            tested+=1
    print(f'PASS: {tested} exact slice cases, all diameter values and diametral unordered-pair counts')
if __name__=='__main__': check()
