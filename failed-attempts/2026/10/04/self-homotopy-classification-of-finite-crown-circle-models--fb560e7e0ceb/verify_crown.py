#!/usr/bin/env python3
from itertools import product


def leq(n,x,y):
    N=2*n
    return x==y or (x%2==0 and y%2==1 and ((y-x)%N in (1,N-1)))

def maps_crown(n):
    N=2*n
    evens=list(range(0,N,2)); odds=list(range(1,N,2))
    upp={(a,b):[y for y in range(N) if leq(n,a,y) and leq(n,b,y)] for a in range(N) for b in range(N)}
    out=[]
    for eimgs in product(range(N), repeat=n):
        f=[None]*N
        for e,v in zip(evens,eimgs): f[e]=v
        opts=[]
        for o in odds:
            ys=upp[(f[(o-1)%N], f[(o+1)%N])]
            if not ys: break
            opts.append(ys)
        else:
            for oimgs in product(*opts):
                g=f.copy()
                for o,v in zip(odds,oimgs): g[o]=v
                out.append(tuple(g))
    return out

def degree(n,f):
    N=2*n
    s=0
    for i in range(N):
        a,b=f[i],f[(i+1)%N]
        if a==b: d=0
        elif (b-a)%N==1: d=1
        elif (a-b)%N==1: d=-1
        else: raise AssertionError((n,i,a,b,f))
        s+=d
    assert s%N==0
    return s//N

def is_automorphism(n,f):
    N=2*n
    return len(set(f))==N and all(leq(n,i,j)==leq(n,f[i],f[j]) for i in range(N) for j in range(N))

def comparable(n,f,g):
    return all(leq(n,a,b) for a,b in zip(f,g)) or all(leq(n,b,a) for a,b in zip(f,g))

def component_count(n,maps):
    m=len(maps)
    parent=list(range(m))
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]];a=parent[a]
        return a
    def union(a,b):
        a,b=find(a),find(b)
        if a!=b: parent[b]=a
    for i in range(m):
        for j in range(i):
            if comparable(n,maps[i],maps[j]): union(i,j)
    return len({find(i) for i in range(m)})

def misses_vertex(f,N):
    return len(set(f))<N

expected_counts={2:36,3:234,4:1544,5:10030}
for n in range(2,6):
    ms=maps_crown(n)
    assert len(ms)==expected_counts[n]
    bins={}
    autos=0
    for f in ms:
        d=degree(n,f)
        bins[d]=bins.get(d,0)+1
        if d:
            assert abs(d)==1
            assert is_automorphism(n,f)
            autos+=1
        else:
            assert misses_vertex(f,2*n)
    assert bins.get(1)==n and bins.get(-1)==n
    assert bins.get(0)==len(ms)-2*n
    assert autos==2*n
    if n<=4:
        comps=component_count(n,ms)
        assert comps==2*n+1
    else:
        comps='not enumerated'
    print(f'n={n} maps={len(ms)} degree_bins={bins} automorphisms={autos} components={comps}')
print('VERIFY_OK')
