#!/usr/bin/env python3
"""Independent finite checks of the cyclic-invariant non-three-connected graph complex.
Standard library only; the uniform theorem is proved in RESULT.md, not by enumeration.
"""
from itertools import combinations
from math import prod
from math import gcd
from collections import Counter


def orbit_edges(n, d):
    return frozenset(tuple(sorted((i, (i+d) % n))) for i in range(n))


def adjacency(n, edges):
    a=[set() for _ in range(n)]
    for i,j in edges:
        a[i].add(j)
        a[j].add(i)
    return a


def connected_after_removal(a, removed):
    rem=set(removed)
    n=len(a)
    remaining=[i for i in range(n) if i not in rem]
    if not remaining: return True
    seen={remaining[0]}; stack=[remaining[0]]
    while stack:
        v=stack.pop()
        for w in a[v]:
            if w not in rem and w not in seen:
                seen.add(w);stack.append(w)
    return len(seen)==len(remaining)


def k3_connected(n,edges):
    a=adjacency(n,edges)
    if not connected_after_removal(a,()): return False
    for v in range(n):
        if not connected_after_removal(a,(v,)):return False
    for v in range(n):
        for w in range(v+1,n):
            if not connected_after_removal(a,(v,w)):return False
    return True


def predicted_allowed(n,ds):
    if not ds:return True
    return gcd(n,*ds)>1 or (len(ds)==1 and gcd(n,ds[0])==1)


def rows(n):
    ds=range(1,n//2+1)
    orbits={d:orbit_edges(n,d) for d in ds}
    assert len(set(orbits.values()))==len(orbits)
    out=[]
    for mask in range(1<<len(orbits)):
        selected=[d for idx,d in enumerate(orbits) if (mask>>idx)&1]
        edge_union=set().union(*(orbits[d] for d in selected)) if selected else set()
        truth=not k3_connected(n,edge_union)
        expected=predicted_allowed(n,selected)
        assert truth==expected,(n,selected,truth,expected)
        out.append(mask) if truth and mask else None
    return out


def gf2rank(columns):
    pivots={}
    for col in columns:
        v=col
        while v:
            bit=v.bit_length()-1
            if bit not in pivots:
                pivots[bit]=v
                break
            v^=pivots[bit]
    return len(pivots)


def bettis(n,faces):
    groups={d:[] for d in range(n//2)}
    for f in faces:
        groups[f.bit_count()-1].append(f)
    groups={k:v for k,v in groups.items() if v}
    ranks={}
    for d in groups:
        if d==0:ranks[d]=0;continue
        target={v:i for i,v in enumerate(groups[d-1])}
        cols=[]
        for f in groups[d]:
            bits=0
            for b in range(n//2):
                if (f>>b)&1:
                    g=f^(1<<b)
                    bits^=1<<target[g]
            cols.append(bits)
        ranks[d]=gf2rank(cols)
    bs=[len(groups[d])-ranks[d]-ranks.get(d+1,0) for d in sorted(groups)]
    while bs and bs[-1]==0:bs.pop()
    return bs


def exp_bettis(n):
    t=n
    primes=[]
    for p in range(2,n+1):
        if t%p==0:
            primes.append(p)
            while t%p==0:t//=p
        if t==1:break
    r=len(primes)
    phi=sum(1 for d in range(1,n) if gcd(n,d)==1)
    discrete=phi//2
    if r==1 and n==primes[0]:
        return [discrete]
    if n!=__import__('math').prod(primes):
        return [discrete+1]
    if r==2:
        return [discrete+2]
    arr=[discrete+1]+[0]*(r-2)
    arr[r-2]=1
    return arr


def main():
    print('MODEL: cyclic edge-orbit complex for not-3-connected graphs')
    for n in range(4,23):
        faces=rows(n)
        if n<=20:
            got=bettis(n,faces)
            expected=exp_bettis(n)
            assert got==expected,(n,got,expected)
        else:got=[]
        print('n=%2d orbit_vertices=%2d nonempty_faces=%5d ordinary_F2_betti=%s' %(n,n//2,len(faces),got))
    # Reflections stabilize each cyclic edge-orbit, not merely its union.
    for n in range(4,31):
        for d in range(1,n//2+1):
            edges=orbit_edges(n,d)
            reflected=frozenset(tuple(sorted(((-i)%n,(-j)%n))) for i,j in edges)
            assert edges==reflected,(n,d)
    print('REFLECTIONS_FIX_EACH_CYCLIC_EDGE_ORBIT_PASS n=4..30')

    # Verify the entire prime-cover nerve, including the first genuine circle at n=30
    # and the first four-prime sphere at n=210, without large chain matrices.
    for n in (6,10,12,15,30,42,60,105,210):
        primes=[p for p in range(2,n+1) if n%p==0 and all(p%q for q in range(2,int(p**0.5)+1))]
        dists=set(range(1,n//2+1))
        common={p:dists.intersection({d for d in dists if d%p==0}) for p in primes}
        all_support=[]
        for k in range(1,len(primes)+1):
            for J in combinations(primes,k):
                I=set.intersection(*(common[p] for p in J))
                if I: all_support.append(J)
        pred_full=(n != prod(primes))
        assert (tuple(primes) in all_support)==pred_full,(n,primes,all_support)
        assert all(J in all_support for k in range(1,len(primes)) for J in combinations(primes,k))
        print('n=%3d prime_nerve_rank=%d whole_intersection=%s' %(n,len(primes),pred_full))
    print('ALL_CYCLIC_NON3CONNECTED_FACE_AND_HOMOLOGY_CHECKS_PASS')

if __name__=='__main__':main()
