#!/usr/bin/env python3
"""Reproducible exact checks for Euclidean vertex chords in two-row ladder order polytopes."""
from collections import Counter
from math import comb
from fractions import Fraction

def choose2(t):
    return comb(t,2) if t>=2 else 0

def formula(n,k):
    # comparable and incomparable numbers of unordered vertex pairs
    comp=2*choose2(n-k+2)+sum(choose2(n-max(u,k-u)+2) for u in range(1,k))
    inc=(k-1)*choose2(n-k+2)
    return comp,inc

def enumerate_pairs(n):
    verts=[(a,b) for a in range(n+1) for b in range(a,n+1)]
    ans=Counter()
    for i,(a,b) in enumerate(verts):
        for c,d in verts[i+1:]:
            k=abs(a-c)+abs(b-d)
            inc=((a<c and b>d) or (a>c and b<d))
            ans[(k,inc)]+=1
    return ans

for n in range(2,19):
    counts=enumerate_pairs(n)
    N=(n+1)*(n+2)//2
    assert sum(counts.values())==comb(N,2)
    assert sum(v for (k,inc),v in counts.items() if inc)==comb(n+2,4)
    assert sum(k*v for (k,inc),v in counts.items() if inc)==comb(n+2,4)*Fraction(2*n+6,5) \
        if (comb(n+2,4)*(2*n+6))%5==0 else Fraction(sum(k*v for (k,inc),v in counts.items() if inc),1)==Fraction(comb(n+2,4)*(2*n+6),5)
    for k in range(1,2*n+1):
        c,i=formula(n,k)
        assert counts[(k,False)]==c,(n,k,'comp',counts[(k,False)],c)
        assert counts[(k,True)]==i,(n,k,'inc',counts[(k,True)],i)
    assert counts[(2*n,False)]==1
    for h in range(n):
        rhs=sum(comb(min(j,h-j)+2,2) for j in range(h+1))
        assert counts[(2*n-h,False)]==rhs

# exact conditional variance of incomparable distance for growing n
for n in range(3,19):
    counts=enumerate_pairs(n)
    T=comb(n+2,4)
    mu=Fraction(2*n+6,5)
    var=sum((Fraction(k)-mu)**2*v for (k,inc),v in counts.items() if inc)/T
    assert var==Fraction((n-2)*(n+3),25)

# density integrates to one, with incomparable mass one third, compared to unconditional mean 8/15.
from sympy import symbols,integrate, Rational, simplify
x=symbols('x',real=True)
f1=x*(19*x*x-42*x+24)/3
f2=(2-x)**3/3
assert simplify(integrate(f1,(x,0,1))+integrate(f2,(x,1,2)))==1
assert simplify(integrate(x*f1,(x,0,1))+integrate(x*f2,(x,1,2)))==Rational(8,15)
assert integrate(4*x*(1-x)**2,(x,0,1))==Rational(1,3)
print('LADDER_CHORD_JOINT_SPECTRUM_PASS: n=2..18 direct pair comparisons, exact beta-binomial moments and limit densities')
