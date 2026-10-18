#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

def norm2_centered(vals):
    N=len(vals)
    s=sum(vals)
    return sum(Fraction(v*v) for v in vals)-Fraction(s*s,N)

def classified_facets(parts):
    N=sum(parts)
    starts=[]
    t=0
    for q in parts:
        starts.append(list(range(t,t+q)))
        t+=q
    seen=set()

    # Type (i)
    for A in starts:
        q=len(A)
        if q<2:
            continue
        for signs in product((-1,1), repeat=q):
            if len(set(signs))<2:
                continue
            f=[0]*N
            for v,s in zip(A,signs):
                f[v]=s
            # normalize by subtracting the first entry only for duplicate key modulo constants
            key=tuple(x-f[0] for x in f)
            seen.add(key)

    # Type (ii)
    for bits in product((0,1), repeat=N):
        if min(bits)==max(bits):
            continue
        nonconst=[]
        allconst=True
        for A in starts:
            ss={bits[v] for v in A}
            if len(ss)>1:
                allconst=False
                nonconst.append(A)
        if allconst or len(nonconst)>=2:
            key=tuple(x-bits[0] for x in bits)
            seen.add(key)
    return [list(k) for k in seen]

def check(parts):
    assert len(parts)>=3 and all(q>=1 for q in parts)
    N=sum(parts); m=max(parts)
    A=Fraction(m,1)-Fraction(m%2,N)
    B=Fraction((N*N)//4,N)
    target=max(A,B)
    facets=classified_facets(parts)
    vals=[norm2_centered(f) for f in facets]
    assert max(vals)==target, (parts,max(vals),target)

    # Explicit feasible type-A labeling.
    idx=parts.index(m)
    off=sum(parts[:idx])
    f=[0]*N
    if m>=2:
        plus=m//2
        if m%2:
            plus=(m+1)//2
        for j in range(m):
            f[off+j]=1 if j<plus else -1
        assert norm2_centered(f)==A
    # Explicit balanced binary labeling.
    g=[1 if i<(N//2) else 0 for i in range(N)]
    assert norm2_centered(g)==B

    # Contact norms agree with the two source types.
    return len(facets), target

cases=[
    (1,1,1),
    (2,1,1),
    (3,1,1),
    (2,2,1),
    (3,2,1),
    (4,1,1),
    (2,2,2),
    (3,3,1),
    (4,2,1),
    (2,2,2,1),
    (3,2,2,1),
]
total=0
for p in cases:
    nf,_=check(p)
    total+=nf

print(f"VERIFY_OK multipartite-sep-inradius cases={len(cases)} classified_facets={total}")
