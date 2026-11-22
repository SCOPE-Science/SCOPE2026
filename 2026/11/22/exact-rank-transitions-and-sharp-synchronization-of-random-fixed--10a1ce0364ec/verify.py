#!/usr/bin/env python3
"""Check rank transitions and prescribed constant fibers of uniform fixed-rank idempotents."""
import itertools, math
from fractions import Fraction
from collections import Counter

def sample_idempotents(n,r):
    for roots in itertools.combinations(range(n),r):
        outsiders=[i for i in range(n) if i not in roots]
        for assigned in itertools.product(roots,repeat=n-r):
            f=list(range(n))
            for x,y in zip(outsiders,assigned): f[x]=y
            yield tuple(f)

def trans(n,r,s,t):
    total=Fraction(0)
    for a in range(max(0,s-(n-r)),min(r,s)+1):
        b=s-a
        H=math.comb(r,a)*math.comb(n-r,b)
        target=math.comb(r-a,t-a) if a<=t<=r else 0
        if target==0:continue
        hit=sum((-1)**j*math.comb(t-a,j)*(t-j)**b for j in range(t-a+1))
        total+=Fraction(H*target*hit,math.comb(n,s)*r**b)
    return total

def comp(f,g): # f after g
    return tuple(f[x] for x in g)

for n in range(3,6):
 for r in range(2,n):
    E=list(sample_idempotents(n,r)); N=math.comb(n,r)*r**(n-r)
    assert len(E)==N
    for s in range(1,r+1):
        S=range(s)
        observed=Counter(len({e[x] for x in S}) for e in E)
        for t in range(1,s+1): assert Fraction(observed[t],N)==trans(n,r,s,t), (n,r,s,t,observed)
        assert sum(trans(n,r,s,t) for t in range(1,s+1))==1
    d=Fraction((n-r)*(n+r-1),r*n*(n-1))
    assert trans(n,r,2,2)==1-d
    # enumerate product layers. For n=5 r=4: N=20, N^3=8000 feasible.
    dist=Counter({e:1 for e in E})
    v={s:Fraction(s==r) for s in range(1,r+1)}
    for k in range(1,4):
        if k>1:
            new=Counter()
            for e in E:
                for f,c in dist.items(): new[comp(e,f)]+=c
            dist=new
            v={t:sum(v[s]*trans(n,r,s,t) for s in range(1,r+1)) for t in range(1,r+1)}
        actual=Counter()
        for f,c in dist.items():actual[len(set(f))]+=c
        assert all(Fraction(actual[t],N**k)==v[t] for t in v),(n,r,k,actual,v)
        constants=[dist.get(tuple([j]*n),0) for j in range(n)]
        assert len(set(constants))==1
        assert Fraction(constants[0],N**k)==v[1]/n
    print(f'PASS n={n} r={r} #idem={N}; rank-Markov and each constant fiber checked through k=3; pair survival={1-d}')
print('ALL TESTS PASS')
