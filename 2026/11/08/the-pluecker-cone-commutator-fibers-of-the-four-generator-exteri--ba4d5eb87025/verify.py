#!/usr/bin/env python3
"""Independent Pluecker-wedge count and direct Grassmann multiplication checks."""
from itertools import product
from collections import Counter
import random

def wedge(u,v,q):
    return tuple((u[i]*v[j]-u[j]*v[i])%q for i in range(4) for j in range(i+1,4))

def mul(a,b,q):
    out=[0]*16
    for x,c in enumerate(a):
        if c==0: continue
        for y,d in enumerate(b):
            if d==0 or x&y:continue
            inv=sum((x >> (j+1)).bit_count() for j in range(4) if y>>j&1)
            out[x|y]=(out[x|y]+(-1 if inv%2 else 1)*c*d)%q
    return out

def direct_formula(a,b,q):
    odds=[1,2,4,8,7,11,13,14]
    ua=[a[1],a[2],a[4],a[8]]; va=[b[1],b[2],b[4],b[8]]
    alpha=[a[7],a[11],a[13],a[14]]
    beta=[b[7],b[11],b[13],b[14]]
    co=[0]*16
    for (i,j),z in zip(((i,j)for i in range(4)for j in range(i+1,4)),wedge(ua,va,q)):
        co[(1<<i)|(1<<j)]=2*z%q
    t=(ua[0]*beta[3]-ua[1]*beta[2]+ua[2]*beta[1]-ua[3]*beta[0]
       +alpha[0]*va[3]-alpha[1]*va[2]+alpha[2]*va[1]-alpha[3]*va[0])
    co[15]=2*t%q
    return co

def check(q):
    vec=list(product(range(q),repeat=4))
    c=Counter(wedge(u,v,q) for u in vec for v in vec)
    num=(q-1)*(q*q+1)*(q*q+q+1)
    assert c[(0,)*6]==q**4+(q**4-1)*q
    assert len(c)-1==num
    assert set(c.values())=={q**4+(q**4-1)*q,q*(q*q-1)}
    rng=random.Random(11173+q)
    for k in range(10000):
        a=[rng.randrange(q) for _ in range(16)]
        b=[rng.randrange(q) for _ in range(16)]
        x=mul(a,b,q); y=mul(b,a,q)
        assert [(s-t)%q for s,t in zip(x,y)]==direct_formula(a,b,q)
    print('q=',q,' bivector-pair enumerated=',len(vec)**2,' direct Grassmann multiplications=10000 VERIFY_OK')
for q in [3,5]:check(q)
