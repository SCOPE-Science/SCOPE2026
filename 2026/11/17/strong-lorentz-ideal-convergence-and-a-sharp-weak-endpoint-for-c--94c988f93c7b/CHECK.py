#!/usr/bin/env python3
"""Finite numerical and exact checks; not a substitute for the proof."""
import math
from fractions import Fraction

for p,q in [(1,1),(2,1),(1.5,3),(3,0.5)]:
    y=[(k+1)**(-1/p)*(1+0.3/(k+1)) for k in range(96)]
    r=p/2
    A=[v**r for v in y]
    G=[]
    gsum=0.0
    for k,v in enumerate(y,1):
        gsum+=math.log(v)
        G.append(math.exp(gsum/k))
        assert G[-1] <= (sum(A[:k])/k)**(1/r)*(1+1e-12)
    assert all(G[k+1]<=G[k]+1e-12 for k in range(len(G)-1))

for n in range(10):
    t=Fraction(2,5)
    coeff=[Fraction(math.comb(n,h))*t**h*(1-t)**(n-h) for h in range(n+1)]
    assert sum(coeff)==1
    if n:
        prev=[Fraction(math.comb(n-1,h))*t**h*(1-t)**(n-1-h) for h in range(n)]
        assert coeff == [((1-t)*(prev[h] if h<n else 0)+t*(prev[h-1] if h else 0)) for h in range(n+1)]
    for j in [0,1,10,1000]:
        v=math.exp(-sum(float(c)*math.log(j+h+1) for h,c in enumerate(coeff))/2)
        assert 0<v<=(j+1)**(-0.5)*(1+1e-12)
print('PASS: 4 geometric-envelope probes, 10 exact binomial recurrences, 40 shift probes')
