#!/usr/bin/env python3
"""Independent graph-theoretic power-domination and local-slide verification."""
from itertools import combinations
from math import factorial

def check(n):
    k=(n-2)//2
    verts=list(combinations(range(n),2)); N=len(verts)
    adj=[0]*N
    for i,(a,b) in enumerate(verts):
        for j,(c,d) in enumerate(verts):
            if i!=j and (a in (c,d) or b in (c,d)):
                adj[i] |= 1<<j
    allmask=(1<<N)-1
    closed=[a|(1<<i) for i,a in enumerate(adj)]
    def power_dominates(sel):
        observed=0
        for v in sel:
            observed |= closed[v]
        remaining=allmask & ~observed
        while remaining:
            fresh=0
            observed_bits=observed
            while observed_bits:
                x=observed_bits&-observed_bits
                v=x.bit_length()-1; observed_bits ^= x
                available=adj[v]&remaining
                if available and not available&(available-1):
                    fresh |= available
            if not fresh:
                return False
            observed |= fresh
            remaining &= ~fresh
        return True
    for size in range(1,k):
        assert not any(power_dominates(S) for S in combinations(range(N),size)), (n,size)
    actual=[]
    for S in combinations(range(N),k):
        ok=power_dominates(S)
        covered={w for i in S for w in verts[i]}
        match=(len(covered)==2*k)
        assert ok==match, (n,S,ok,match)
        if ok: actual.append(S)
    V=factorial(n)//(2**(k+1)*factorial(k))
    assert len(actual)==V
    aset=set(actual)
    degrees=[]; triangles2=0
    for S in actual:
        neigh=set()
        for i in S:
            for j in range(N):
                if j in S: continue
                if adj[i]>>j&1:
                    nxt=tuple(sorted(tuple(v for v in S if v!=i)+(j,)))
                    if nxt in aset: neigh.add(nxt)
        degrees.append(len(neigh))
        assert len(neigh)==4*k
        neigh=list(neigh)
        for u in range(len(neigh)):
            for v in range(u):
                A,B=set(neigh[u]),set(neigh[v]);
                if len(A&B)==k-1:
                    aa=next(iter(A-B)); bb=next(iter(B-A))
                    if adj[aa]>>bb&1:
                        triangles2+=1
    assert triangles2//3 == 4*k*V//3
    print(f'n={n} k={k} chosen_candidates={sum(1 for _ in combinations(range(N),k))} '
          f'optimal={V} degree={4*k} triangles={triangles2//3} OK')

for n in (4,6,8,10): check(n)
print('VERIFY_PREDICATE_OK')
