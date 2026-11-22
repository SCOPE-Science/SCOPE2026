#!/usr/bin/env python3
"""Independent finite-state checks for a finite-difference cellular automaton.
All operations use elementary integers mod p, without external dependencies.
"""
from itertools import product
from math import comb

def rank_mod_p(rows,p):
    if not rows:return 0
    a=[list(map(lambda x:x%p,r)) for r in rows]
    m=len(a);n=len(a[0]); rank=0
    for j in range(n):
        pivot=next((i for i in range(rank,m) if a[i][j]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        z=pow(a[rank][j],-1,p)
        a[rank]=[(z*v)%p for v in a[rank]]
        for i in range(m):
            if i==rank:continue
            c=a[i][j]
            if c:a[i]=[(v-c*w)%p for v,w in zip(a[i],a[rank])]
        rank+=1
        if rank==m:break
    return rank

def row(e,t,p):
    return [comb(e,j)%p for j in range(t)]

def predicted_rank(N,L,R,t):
    hi=max(L,R);lo=min(L,R)
    return min(t,hi) if t<=N else hi+min(t-N,lo)

def direct_patterns(E,t,p):
    if t==0:return 1
    out=set()
    for prefix in product(range(p),repeat=t):
        s=list(prefix)
        for i in range(max(E)-t+1):
            z=sum(((-1)**j)*comb(t,j)*s[i+j] for j in range(t))
            s.append(((-1)**(t+1)*z)%p)
        out.add(tuple(s[i] for i in E))
    return len(out)

nchecks=0;nwords=0
for p, ns, maxt in [(2,[2,4,8],10),(3,[3,9],7)]:
    for N in ns:
        for L in range(1,min(N,4)+1):
            for R in range(1,min(N,4)+1):
                E=list(range(L))+list(range(N,N+R))
                for t in range(0,min(maxt,N+min(L,R)+1)+1):
                    r=rank_mod_p([row(e,t,p) for e in E],p)
                    expected=predicted_rank(N,L,R,t)
                    assert r==expected, (p,N,L,R,t,r,expected)
                    if t<=7:
                        got=direct_patterns(E,t,p)
                        assert got==p**expected,(p,N,L,R,t,got,expected)
                        nwords+=p**t
                    nchecks+=1
print('PASS: two-block ranks',nchecks,'direct initial words',nwords)
