#!/usr/bin/env python3
"""Independent enumeration of unit-conjugacy orbits of cycle retractions.
Scientific computation; no external libraries required.
"""
from collections import Counter
from itertools import product

def interval_walk_numbers(n):
    if n%2: return {n:(1,1,1)}
    out={}
    for k in range(2,n//2+2):
        L=n-k+1
        v=[0]*k;v[k-1]=1
        for j in range(L):
            v=[(v[i-1] if i>0 else 0)+(v[i+1] if i+1<k else 0) for i in range(k)]
        T=v[0]
        h=L//2
        v=[0]*k;v[k-1]=1
        for j in range(h):
            v=[(v[i-1] if i>0 else 0)+(v[i+1] if i+1<k else 0) for i in range(k)]
        if L%2==0:
            assert k%2==1
            S=v[(k-1)//2]
        else:
            assert k%2==0
            S=v[k//2-1]+v[k//2]
        assert T>=S and (T-S)%2==0
        out[k]=(T,S,(T+S)//2)
    out[n]=(1,1,1)
    return out

def conjugacy_brute(n):
    es=set()
    for start in range(n):
        for increments in product((-1,1),repeat=n):
            if sum(increments)%n:continue
            f=[start]
            for s in increments[:-1]:f.append((f[-1]+s)%n)
            f=tuple(f)
            if all(f[f[i]]==f[i] for i in range(n)):es.add(f)
    group=[]
    for s in (-1,1):
        for t in range(n):
            g=tuple((s*i+t)%n for i in range(n))
            inv=[0]*n
            for i,j in enumerate(g):inv[j]=i
            group.append((g,inv))
    classes=[]
    while es:
        f=next(iter(es))
        orbit=set()
        for g,gi in group:
            orbit.add(tuple(g[f[gi[i]]] for i in range(n)))
        assert orbit<=es
        es-=orbit
        classes.append((len(set(f)),len(orbit)))
    return Counter(classes)

for n in range(4,17):
    p=interval_walk_numbers(n)
    total=sum(n*T for k,(T,S,_) in p.items() if k<n)+1
    num_orb=sum(c for T,S,c in p.values())
    if n<=16:
        got=conjugacy_brute(n)
        want=Counter({(n,1):1})
        if n%2==0:
            for k,(T,S,_) in p.items():
                if k==n:continue
                if S:want[(k,n)]+=S
                if T>S:want[(k,2*n)]+=(T-S)//2
        assert got==want,(n,got,want)
        assert sum(v*w for (k,v),w in got.items())==total,(n,total)
        assert sum(got.values())==num_orb,(n,num_orb)
    print('n',n,'T_S',p,'idempotents',total,'orbits',num_orb,'brute',n<=16)
print('CYCLE_ORBIT_CLASSIFICATION_VERIFIED')
