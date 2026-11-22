#!/usr/bin/env python3
"""Exact checks of a bilayer majority fixed-state classification.
Run: python3 verify.py   (standard library only).
All computations use integers, including the representative antagonism a=2
in the degree-three intermediate interval (1,3).
"""
from itertools import product

SPINS = ((-1,-1),(-1,1),(1,-1),(1,1))


def prism(n):
    assert n >= 3
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for row in range(2):
            u=2*i+row
            for j in ((i-1)%n, (i+1)%n):
                v=2*j+row
                adj[u].add(v);adj[v].add(u)
        u,v=2*i,2*i+1
        adj[u].add(v);adj[v].add(u)
    return [tuple(sorted(x)) for x in adj]


def complete(k):
    return [tuple(j for j in range(k) if j!=i) for i in range(k)]


def biclique(a,b):
    return [tuple(range(a,a+b)) for _ in range(a)]+[tuple(range(a)) for _ in range(b)]


def stable_microscopic(adjA,adjB,a_mask,b_mask,a):
    v=len(adjA)
    for i in range(v):
        si=1 if a_mask>>i&1 else -1
        ti=1 if b_mask>>i&1 else -1
        hA=sum(1 if a_mask>>j&1 else -1 for j in adjA[i])-a*ti
        hB=sum(1 if b_mask>>j&1 else -1 for j in adjB[i])-a*si
        if hA*si<=0 or hB*ti<=0: return False
    return True


def stable_classified(adjA,adjB,a_mask,b_mask):
    n=len(adjA)
    allmask=(1<<n)-1
    if a_mask == b_mask and a_mask in (0,allmask):return True
    if b_mask != (allmask^a_mask):return False
    for i in range(n):
        si=(a_mask>>i)&1
        if not any(((a_mask>>j)&1)==si for j in adjA[i]):return False
        if not any(((a_mask>>j)&1)==si for j in adjB[i]):return False
    return True


def exhaustive_comparison(adjA,adjB):
    n=len(adjA)
    assert len(adjB)==n
    assert all(len(v)==3 for v in adjA) and all(len(v)==3 for v in adjB)
    actual=predicted=0
    for a_mask in range(1<<n):
        for b_mask in range(1<<n):
            a=stable_microscopic(adjA,adjB,a_mask,b_mask,2)
            b=stable_classified(adjA,adjB,a_mask,b_mask)
            assert a==b, (n,a_mask,b_mask,a,b)
            actual+=a
            predicted+=b
    assert actual==predicted
    return actual


def transfer():
    # Four possible two-vertex rung colorings; states are pairs of rungs.
    pairs=list(product(range(4),repeat=2))
    T=[[0]*16 for _ in range(16)]
    for k,(left,mid) in enumerate(pairs):
        for r,(m,right) in enumerate(pairs):
            if mid!=m:continue
            x,y,z=SPINS[left],SPINS[mid],SPINS[right]
            allowed=(y[0]==y[1]) or all(x[h]==y[h] or z[h]==y[h] for h in range(2))
            if allowed:T[k][r]=1
    return T


def mul(A,B):
    n=len(A);m=len(B[0]);p=len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(p)) for j in range(m)] for i in range(n)]


def trace(A):return sum(A[i][i] for i in range(len(A)))


def coeffs_char(T):
    # Faddeev-LeVerrier: exact integer characteristic polynomial.
    n=len(T); B=[row[:] for row in T]
    c=[1]
    for k in range(1,n+1):
        t=trace(B)
        assert t%k==0, (k,t)
        ck=-(t//k)
        c.append(ck)
        if k==n:break
        for i in range(n):B[i][i]+=ck
        B=mul(T,B)
    return c


def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c


def expected_char():
    # Ascending powers: x^8(x^2+2)(x^2-x+1)(x^4-3x^3-x^2+2)
    p=[1]
    for q in ([0]*8+[1],[2,0,1],[1,-1,1],[2,0,-1,-3,1]):p=poly_mul(p,q)
    return list(reversed(p))


def run():
    T=transfer(); assert coeffs_char(T)==expected_char()
    mat=[[int(i==j) for j in range(16)] for i in range(16)]
    expected={3:34,4:118,5:364,6:1164,7:3826,8:12462,9:40390,10:131186,11:426496,12:1386004}
    for n in range(1,13):
        mat=mul(mat,T)
        if n>=3:assert trace(mat)==expected[n], (n,trace(mat))
    # Full state-space enumeration: n=3 and n=4 prisms and two other cubic networks.
    samples=[('K4',complete(4),complete(4),None),('K33',biclique(3,3),biclique(3,3),None),('prism3',prism(3),prism(3),36),('prism4',prism(4),prism(4),120)]
    for label,graphA,graphB,want in samples:
        got=exhaustive_comparison(graphA,graphB)
        if want is not None:assert got==want,(label,got,want)
        print(f'{label}: all {4**len(graphA)} two-layer states examined; fixed={got}')
    print('16x16 transfer polynomial verified exactly; counts n=3..12 verified; PASS')

if __name__=='__main__':run()
