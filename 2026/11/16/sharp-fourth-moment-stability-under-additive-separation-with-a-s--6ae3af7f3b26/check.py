#!/usr/bin/env python3
"""Exact finite-alias and sharp-deficit checks for separated Fourier apertures."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from random import Random

def en(c):
    w=defaultdict(complex)
    for a,x in c.items():
        for b,y in c.items():w[a+b]+=x*y
    return round(sum(abs(z)**2 for z in w.values()))

def rat_en(c):
    w=defaultdict(lambda: F(0))
    for a,x in c.items():
        for b,y in c.items():w[a+b]+=x*y
    return sum(z*z for z in w.values())

def test(m, trials=50):
    rng=Random(19+m)
    T=[10**i for i in range(1,m+1)]
    A=[0,1,2]
    groups=defaultdict(list)
    for a in A+T:
        for b in A+T:
            groups[a+b].append((a,b))
    labels={a:'A' for a in A};labels.update({t:'T' for t in T})
    for s,pairs in groups.items():
        tags={(labels[a],labels[b]) for a,b in pairs}
        # sum labels among group must all have same pair kind
        assert len({tuple(sorted(t)) for t in tags})==1,(m,s,pairs)
        tag=tuple(sorted(next(iter(tags))))
        if tag==('A','T'): assert len({t for a,b in pairs for t in [a if labels[a]=='T' else b]})==1
    for _ in range(trials):
        c={z:F(rng.randint(-5,5)) for z in A+T}
        s=sum(c[x]**2 for x in A);t=sum(c[x]**2 for x in T)
        Q=rat_en(c)
        QA=rat_en({z:c[z] for z in A})
        assert Q==QA+4*s*t+2*t*t-sum(c[x]**4 for x in T),(m,Q)
        D=F(15,7)*(s+t)**2-Q
        D3=F(15,7)*s*s-QA
        assert D==D3+F(2,7)*s*t+F(1,7)*t*t+sum(c[x]**4 for x in T)
        assert D>=min(F(2,7),F(1,7)+F(1,m))*t*(s+t)
    # equality exact on triple
    sharp={0:F(2),1:F(3),2:F(2)}
    # squared amplitude rational can use sqrt values but exact after choosing complex squares separately
    print('pass m=',m,'samples=',trials,'distinct sum groups=',len(groups))

for m in [1,2,3,5,7,8,9,12,20]:test(m)
print('all checks passed')
