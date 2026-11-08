#!/usr/bin/env python3
"""Independent direct-state orbit enumeration, no symbolic powers or rank computations."""
import itertools
from collections import Counter

def wave(qs):
    vs=list(itertools.product(*(range(q) for q in qs)))
    neighbors=[[j for j,v in enumerate(vs) if sum(x!=y for x,y in zip(u,v))==1] for u in vs]
    return len(vs),neighbors

def step(s,n,neigh):
    x=s&((1<<n)-1); y=s>>n
    z=y
    for i,inds in enumerate(neigh):
        bit=(y>>i)&1
        for j in inds:bit^=(x>>j)&1
        if bit:z|=(1<<i)
        else:z&=~(1<<i)
    return (x<<n)|z

def direct(qs):
    n,ns=wave(qs);hist=Counter()
    for s in range(1<<(2*n)):
        v=step(s,n,ns)
        for k in range(1,13):
            if v==s:hist[k]+=1;break
            v=step(v,n,ns)
        else:raise AssertionError('period >12')
    return hist

def formula(qs):
    d=len(qs);odd=[q for q in qs if q%2]; even=[q for q in qs if not q%2]
    from math import prod
    h=[sum(prod(q-1 for i,q in enumerate(odd) if i not in S) for r in range(len(odd)+1) for S in itertools.combinations(range(len(odd)),r) if (d+r)%2==a) for a in (0,1)]
    M=prod(even);C=prod(q-2 for q in even)
    a=h[0]*(M+C)//2;b=h[1]*(M+C)//2
    F={1:2**a,2:2**(2*a),3:2**(a+2*b),4:2**(2*h[0]*M),6:2**(2*a+2*h[1]*M),12:2**(2*prod(qs))}
    Cnt={1:F[1],2:F[2]-F[1],3:F[3]-F[1],4:F[4]-F[2],6:F[6]-F[3]-F[2]+F[1],12:F[12]-F[6]-F[4]+F[2]}
    return {k:v for k,v in Cnt.items() if v}

if __name__=='__main__':
    for qs in [(2,),(3,),(2,2),(2,3),(3,3)]:
        x=direct(qs);y=formula(qs)
        assert dict(x)==y,(qs,x,y)
        print('BRUTE_OK',qs,'states',sum(x.values()),'period_counts',dict(sorted(x.items())))
