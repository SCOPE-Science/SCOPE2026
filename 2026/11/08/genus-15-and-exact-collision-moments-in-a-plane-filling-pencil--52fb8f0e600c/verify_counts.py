#!/usr/bin/env python3
"""Independent direct finite-field collision counts, including quadratic fields."""
from collections import Counter
from math import gcd

def prime(p):
    assert p>3 and p!=7
    keys=Counter(((1-pow(t,7,p))*pow(t,-3,p))%p for t in range(1,p))
    n=[keys.get(k,0) for k in range(p)]
    direct=sum(u*(u-1) for u in n)
    formula=sum(1 for t in range(1,p) for u in range(1,p) if t!=u and
                ((1-pow(t,7,p))*pow(t,-3,p))%p==((1-pow(u,7,p))*pow(u,-3,p))%p)
    assert direct==formula
    if gcd(7,p-1)==1:
        expected=p-gcd(3,p-1)-gcd(4,p-1)
        assert direct==expected,(p,direct,expected)
        assert sum(u*u for u in n)==2*p-1-gcd(3,p-1)-gcd(4,p-1)
    print(p,'ordered off-diagonal pairs',direct,'singular members',sum(u>0 for u in n))

# finite-field model F_{p^2}=F_p[v]/(v^2-c), c a quadratic nonresidue
class GF2:
    def __init__(self,p,c):self.p=p;self.c=c;self.e=[(a,b) for a in range(p) for b in range(p)]
    def mul(self,x,y):
        a,b=x;c,d=y;return ((a*c+self.c*b*d)%self.p,(a*d+b*c)%self.p)
    def pow(self,x,n):
        if n<0:return self.pow(x,self.p*self.p-1+n%(self.p*self.p-1))
        a=(1,0)
        while n:
            if n&1:a=self.mul(a,x)
            x=self.mul(x,x);n//=2
        return a
    def sub(self,x,y):return ((x[0]-y[0])%self.p,(x[1]-y[1])%self.p)

def quadratic(p,c):
    assert pow(c,(p-1)//2,p)==p-1
    f=GF2(p,c); zero=(0,0);one=(1,0)
    keys=Counter(f.sub(f.pow(t,-3),f.pow(t,4)) for t in f.e if t!=zero)
    q=p*p;ns=[keys.get(k,0) for k in f.e]
    pairs=sum(n*(n-1) for n in ns)
    if gcd(7,q-1)==1:
        assert pairs==q-gcd(3,q-1)-gcd(4,q-1),(q,pairs)
    # Checks total incidence of rational singularities and moments
    assert sum(ns)==q-1 and sum(n*n for n in ns)==pairs+q-1
    print(q,'ordered off-diagonal pairs',pairs)

for p in (5,11,13,17,19,23,29,31,37,41,43,47,53,59,61,71,73):prime(p)
for p,c in ((5,2),(11,2),(13,2)):quadratic(p,c)
print('FINITE_FIELD_MOMENTS_PASS')
