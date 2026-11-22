#!/usr/bin/env python3
"""Finite checks of top-power distribution and maximal block length on rooted tree incidence matrices.
Only prime-field configurations are exhaustively enumerated; the theorem is all finite fields."""
from itertools import product
from collections import Counter
from fractions import Fraction
from math import comb


def tree(b,h):
    levels=[[0]]; edges=[]; nxt=1
    for _ in range(h):
        new=[]
        for u in levels[-1]:
            for _ in range(b):
                v=nxt; nxt+=1; new.append(v); edges.append((u,v))
        levels.append(new)
    return nxt,edges,levels


def mul(A,B,q):
    n=len(A); C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,a in enumerate(A[i]):
            if a:
                for j,b in enumerate(B[k]):
                    if b: C[i][j]=(C[i][j]+a*b)%q
    return C


def powers(A,h,q):
    n=len(A); P=[[int(i==j) for j in range(n)] for i in range(n)]
    found=0; top=None
    for k in range(1,h+1):
        P=mul(P,A,q)
        if any(any(row) for row in P): found=k
        if k==h: top=P
    return found+1,top


def poly_mul(x,y):
    r=[Fraction(0)]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y): r[i+j]+=a*b
    return r


def pred_poly(b,h,q):
    # Polynomial recurrence for number Z_h of surviving root-to-leaf paths.
    F=[Fraction(0),Fraction(1)]
    for _ in range(h):
        G=[z*Fraction(q-1,q) for z in F]
        G[0]+=Fraction(1,q)
        H=[Fraction(1)]
        for _ in range(b): H=poly_mul(H,G)
        F=H
    return F


def length_cdf(b,h,q,k):
    # Exact joint DP for maximal nonzero-edge chain and rooted chain cutoff.
    vals=[Fraction(1)]*(k+1)
    for _ in range(h):
        prev=vals
        vals=[(Fraction(1,q)*prev[k]+Fraction(q-1,q)*(prev[r-1] if r else Fraction(0)))**b for r in range(k+1)]
    return vals[k]


def check(b,h,q):
    n,edges,levels=tree(b,h); counts=Counter(); length_counts=Counter(); N=q**len(edges)
    for values in product(range(q),repeat=len(edges)):
        A=[[0]*n for _ in range(n)]
        for (u,v),a in zip(edges,values): A[u][v]=a
        nu,top=powers(A,h,q)
        z=sum(int(top[0][v]!=0) for v in levels[-1])
        counts[z]+=1; length_counts[nu]+=1
        assert (nu==h+1)==(z>0)
        # Independent graph reachability: longest run of edges whose entries are nonzero.
        dist=[0]*n
        for u,v in edges:
            if A[u][v]: dist[v]=max(dist[v],dist[u]+1)
        # Above recurrence misses a path that starts after a zero edge only if dist is
        # reset correctly, which it is: every vertex may start a zero-length path.
        assert nu==max(dist)+1, (b,h,q,values,nu,dist)
        assert all(all(x==0 for x in top[i]) for i in range(1,n))
    F=pred_poly(b,h,q)
    for z,count in counts.items(): assert Fraction(count,N)==F[z],(b,h,q,z,count,F[z])
    assert all(F[z]==Fraction(counts.get(z,0),N) for z in range(len(F)))
    for k in range(h+1):
        assert length_cdf(b,h,q,k)==Fraction(sum(v for nu,v in length_counts.items() if nu<=k+1),N),(b,h,q,k)
    print(f'PASS b={b} h={h} q={q} matrices={N} dimension={n} top_support_counts={dict(sorted(counts.items()))}')

for case in [(2,1,2),(2,2,2),(2,2,3),(2,3,2),(3,2,2)]: check(*case)

p=1.0
for h in range(1,10001):
    p=1-(1-p/2)**2
    assert 3/(h+3)<=p<=4/(h+4)
print('PASS critical recurrence bounds for h=1..10000; h*p_h at h=10000:',float(10000*p))
for q in [3,4,5,8,9]:
    p=1.; t=(q-1)/q
    for _ in range(2000): p=1-(1-t*p)**2
    target=q*(q-2)/(q-1)**2
    assert abs(p-target)<1e-10
print('PASS supercritical fixed point at q=3,4,5,8,9')


def check_full_radical(b,h,q):
    # Enumerate all strictly comparable pairs, including long (non-cover) intervals.
    n,edges,levels=tree(b,h)
    parent={v:u for u,v in edges}
    intervals=[]
    for v in range(1,n):
        w=v
        while w in parent:
            u=parent[w]; intervals.append((u,v)); w=u
    counts=Counter()
    for values in product(range(q),repeat=len(intervals)):
        A=[[0]*n for _ in range(n)]
        for (u,v),a in zip(intervals,values): A[u][v]=a
        nu,top=powers(A,h,q)
        z=sum(top[0][v]!=0 for v in levels[-1]);counts[z]+=1
        assert (nu==h+1)==(z>0)
    F=pred_poly(b,h,q)
    N=q**len(intervals)
    assert len(intervals)==sum(d*b**d for d in range(1,h+1))
    assert all(F[z]==Fraction(counts.get(z,0),N) for z in range(len(F)))
    print(f'PASS full radical b={b} h={h} q={q} dimension={len(intervals)} matrices={N} top_support_counts={dict(sorted(counts.items()))}')

check_full_radical(2,2,2)
