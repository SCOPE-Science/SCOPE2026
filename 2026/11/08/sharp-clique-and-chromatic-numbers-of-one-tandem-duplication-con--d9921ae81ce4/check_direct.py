#!/usr/bin/env python3
"""Independent direct tandem-duplication-ball compatibility and coloring checks."""
from itertools import product

def derivative(word,k,q):
    return tuple((word[i+k]-word[i])%q for i in range(len(word)-k))

def color(word,k,q):
    n=len(word)
    b=derivative(word,k,q)
    rs=[]; z=0
    for v in b:
        if v==0:z+=1
        else:rs.append(z);z=0
    rs.append(z)
    s=len(rs)-1
    if all(r<k for r in rs):return 0
    d=s+1
    return sum(i*(r//k) for i,r in enumerate(rs))%d

def children(w,k):
    return {w[:i+k]+w[i:i+k]+w[i+k:] for i in range(len(w)-k+1)}

def check(q,k,n):
    ws=list(product(range(q),repeat=n))
    d={w:children(w,k) for w in ws}
    rev={}
    for w,outputs in d.items():
        for z in outputs: rev.setdefault(z,[]).append(w)
    edges=set()
    for vs in rev.values():
        for j,w in enumerate(vs):
            for x in vs[j+1:]:
                edges.add((w,x) if w<x else (x,w))
    K=max(1,n-2*k+1)
    assert all(color(w,k,q) in range(K) for w in ws)
    assert all(color(x,k,q)!=color(y,k,q) for x,y in edges)
    # Explicit clique via a derivative nonzero skeleton and one length-k zero block.
    if K>1:
        skeleton=(1,)*(n-2*k)
        clique=[]
        for j in range(K):
            z=skeleton[:j]+(0,)*k+skeleton[j:]
            x=[0]*k
            for a in z: x.append((x[-k]+a)%q)
            clique.append(tuple(x))
        assert len(set(clique))==K
        assert all((x,y) in edges or (y,x) in edges for i,x in enumerate(clique) for y in clique[i+1:])
    else:
        assert not edges
    print(f"q={q} k={k} n={n} vertices={len(ws)} edges={len(edges)} verified_chromatic={K}")

if __name__=='__main__':
    for q in (2,3):
        for k in (1,2,3):
            for n in range(k,min(10 if q==2 else 7,k+6)+1):
                if q**n<=4096:check(q,k,n)
    print('VERIFY_DIRECT_OK')
