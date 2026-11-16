#!/usr/bin/env python3
"""Independent exact Fourier-spectrum histogram check for noncyclic four-color group V_4."""
from itertools import product
from collections import Counter

def edges_for(blocks):
    es=set()
    for b in blocks:
        for v in b:
            for w in b:
                if v<w:es.add((v,w))
    return sorted(es)

def fwht(v):
    n=len(v);h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(h):
                a,b=v[i+j],v[i+j+h]
                v[i+j],v[i+j+h]=a+b,a-b
        h*=2
    return v

def direct_fourier(blocks):
    n=1+max(x for b in blocks for x in b)
    arr=[0]*(4**n); edges=edges_for(blocks)
    for c in product(range(4),repeat=n):
        if all(c[u]!=c[v] for u,v in edges):
            ind=sum(z<<(2*i) for i,z in enumerate(c));arr[ind]=1
    fwht(arr)
    return Counter(arr)

def predicted_spectrum(blocks):
    q=4
    local2=Counter({q-1:1,-1:q-1})
    local3=Counter({(q-1)*(q-2):1,-(q-2):3*(q-1),2:(q-1)*(q-2)})
    z=Counter({q:1})
    n=1
    for b in blocks:
        local=local2 if len(b)==2 else local3
        n+=len(b)-1
        nxt=Counter()
        for old,a in z.items():
            for new,bcount in local.items():nxt[old*new]+=a*bcount
        z=nxt
    assert sum(z.values())==q**(n-1)
    z[0]=q**n-q**(n-1)
    return z

if __name__=='__main__':
    cases=[[(0,1,2),(0,3,4)],[(0,1,2),(2,3,4)],
           [(0,1,2),(2,3,4),(4,5)],[(0,1,2),(2,5),(5,3,4)],
           [(0,1),(1,2),(2,3)],[(0,1),(0,2),(0,3)],
           [(0,1,2),(2,3)]]
    for b in cases:
        observed=direct_fourier(b)
        expected=predicted_spectrum(b)
        assert observed==expected,(b,observed,expected)
        print('PASS',{'blocks':list(map(list,b)),'coefficients':sum(observed.values()),'spectrum':dict(sorted(observed.items()))})
