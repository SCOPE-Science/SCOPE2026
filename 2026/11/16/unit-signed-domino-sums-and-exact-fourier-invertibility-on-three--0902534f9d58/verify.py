#!/usr/bin/env python3
"""Independent exact checks for three-row domino Walsh multipliers."""
from functools import lru_cache

def graph(m):
    w=2*m; E=[]
    for c in range(w):
        for r in range(2):E.append(((r,c),(r+1,c),'v',c))
        if c+1<w:
            for r in range(3):E.append(((r,c),(r,c+1),'h',c))
    return E

def masks(m):
    edges=graph(m)
    at={ (r,c):[] for r in range(3) for c in range(2*m)}
    for i,(u,v,*_) in enumerate(edges):
        at[u].append((v,i));at[v].append((u,i))
    allv=tuple(at)
    def rec(remaining,mask):
        if not remaining:
            yield mask;return
        u=next(iter(remaining))
        for v,i in at[u]:
            if v in remaining:
                yield from rec(remaining-{u,v}, mask|(1<<i))
    return list(rec(frozenset(allv),0))

def fwht(x):
    step=1;N=len(x)
    while step<N:
        for i in range(0,N,step*2):
            for j in range(i,i+step):
                a,b=x[j],x[j+step];x[j],x[j+step]=a+b,a-b
        step*=2

def predicted_unsigned(m):
    a,v=1,0
    for _ in range(m):a,v=3*a+2*v,a+v
    return a

def signed_transfer(m):
    a,v=1,0
    for _ in range(m):a,v=-a+2*v,-a+v
    return a

def run():
    for m in range(1,4):
        es=graph(m);ts=masks(m);W=len(es)
        assert len(ts)==predicted_unsigned(m)
        witness=sum((-1)**sum(1 for j,e in enumerate(es) if e[2]=='v' and e[3]%2==0 and ((t>>j)&1)) for t in ts)
        assert witness==signed_transfer(m) and abs(witness)==1
        if m<=2:
            x=[0]*(1<<W)
            for t in ts:x[t]=1
            fwht(x)
            assert all(z&1 for z in x)
            assert min(abs(z) for z in x)==1
            assert max(abs(z) for z in x)==len(ts)
    a,v=1,0;c,d=1,0
    for m in range(1,501):
        a,v=-a+2*v,-a+v
        c,d=3*c+2*d,c+d
        assert a==(-1)**((m+1)//2)
        assert c%2==1
    print('THREE_ROW_DOMINO_FOURIER_EXACT_PASS full Walsh m=1,2; independent tilings m=1,2,3; transfer m=1..500')
if __name__=='__main__':run()
