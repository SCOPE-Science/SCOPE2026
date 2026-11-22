"""Exact finite checks for fixed-point-conditioned cyclic descents."""
from itertools import permutations
from math import factorial, comb
from fractions import Fraction
from collections import defaultdict

def D(m):
    return sum((-1)**j*factorial(m)//factorial(j) for j in range(m+1))

def regression(n,k):
    m=n-k
    if m == 1: raise ValueError('no permutation with exactly n-1 fixed points')
    if m == 0: return Fraction(1)
    return (Fraction(n,2)-Fraction(k*k-3*k+1,2*(n-1))+
            Fraction((m-1)*(-1)**m,2*(n-1)*D(m)))

checks=0
for n in range(3,9):
    bins=defaultdict(lambda: [0,0])
    fac=[0]*(n+1); mix=[0]*(n+1)
    for p in permutations(range(n)):
        F=sum(p[i]==i for i in range(n))
        C=sum(p[i]>p[(i+1)%n] for i in range(n))
        bins[F][0]+=C; bins[F][1]+=1
        x=1
        for r in range(n+1):
            fac[r]+=x; mix[r]+=x*C
            x*=F-r
    for k,(total,count) in bins.items():
        assert Fraction(total,count)==regression(n,k),(n,k,total,count)
        checks+=1
    for r in range(n+1):
        assert fac[r]==factorial(n), (n,r)
        expect=Fraction(n,2)-Fraction(r*(r-1),2*(n-1)) if r<n else Fraction(1)
        assert Fraction(mix[r],factorial(n))==expect,(n,r)
        checks+=2
    max_val=max(Fraction(s,c) for s,c in bins.values())
    max_ks={k for k,(s,c) in bins.items() if Fraction(s,c)==max_val}
    assert max_ks==({1} if n%2 else {2}), (n,max_ks)
    checks+=1
print('Exact enumeration assertions passed:',checks)
