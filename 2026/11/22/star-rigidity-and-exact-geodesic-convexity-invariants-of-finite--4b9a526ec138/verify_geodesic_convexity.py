#!/usr/bin/env python3
"""Finite evidence for geodesic convexity of projective-plane Levi graphs.
Independent bitset shortest-path closure and direct star-family check.
Requires only Python 3 standard library. Run: python3 verify_geodesic_convexity.py
"""
from itertools import combinations
from collections import Counter

def graph(q):
    assert q in (2,3,5,7), 'prime field orders supported'
    vectors = [(1,a,b) for a in range(q) for b in range(q)]
    vectors += [(0,1,a) for a in range(q)]+[(0,0,1)]
    n=len(vectors); adj=[0]*(2*n)
    for i,(a,b,c) in enumerate(vectors):
        for j,(x,y,z) in enumerate(vectors):
            if (a*x+b*y+c*z)%q==0:
                adj[i] |= 1<<(n+j)
                adj[n+j] |= 1<<i
    assert all(a.bit_count()==q+1 for a in adj)
    assert len(vectors)==q*q+q+1
    return adj,n

def intervals(adj):
    N=len(adj)
    d=[[99]*N for _ in range(N)]
    for i in range(N):
        d[i][i]=0; queue=[i]
        for k in queue:
            for j in range(N):
                if (adj[k]>>j)&1 and d[i][j]==99:
                    d[i][j]=d[i][k]+1;queue.append(j)
    return [[sum(1<<t for t in range(N) if d[i][t]+d[t][j]==d[i][j])
             for j in range(N)] for i in range(N)]

def hull(m,I):
    while True:
        bits=[i for i in range(len(I)) if (m>>i)&1]
        nxt=m
        for i,j in combinations(bits,2):nxt|=I[i][j]
        if nxt==m:return m
        m=nxt

def expected(adj,n):
    maxmask=(1<<(2*n))-1
    output={0,maxmask}
    for v in range(2*n):
        bits=[u for u in range(2*n) if adj[v]>>u&1]
        for m in range(1<<len(bits)):
            c=1<<v
            for t,u in enumerate(bits):
                if m>>t&1:c|=1<<u
            output.add(c)
    return output

def test(q):
    adj,n=graph(q);I=intervals(adj)
    E=expected(adj,n)
    formula=2+2*n*(2**(q+1))-n*(q+1)
    assert len(E)==formula,(q,len(E),formula)
    for m in E:assert hull(m,I)==m
    print('order',q,'vertices',2*n,'convex',len(E),'profile',sorted(Counter(x.bit_count() for x in E).items()))
    if q==2:
        allC={m for m in range(1<<(2*n)) if hull(m,I)==m}
        assert allC==E,(len(E),len(allC),len(E^allC))
        print('all 16384 subsets classified')
        # For every 4-subset, exhibit Radon partition and common-hull vertex.
        for A in combinations(range(2*n),4):
            mask=sum(1<<a for a in A)
            assert any(hull(sum(1<<i for i in part),I)&
                       hull(mask^sum(1<<i for i in part),I)
                       for k in (1,2) for part in combinations(A,k))
        print('all 1001 four-sets Radon decomposable')
        # Helly size four follows exact equivalence via intersections of point-deleted hulls.
        for A in combinations(range(2*n),4):
            h=[hull(sum(1<<i for i in A if i!=a),I) for a in A]
            assert h[0]&h[1]&h[2]&h[3]
        print('all 1001 four-sets meet the Helly criterion')
        # VCdim <=3: each four-set fails to be shattered by all convex subsets.
        for A in combinations(range(2*n),4):
            traces={tuple(i for i in A if m>>i&1) for m in E}
            assert len(traces)<16
        print('all 1001 four-sets fail to be shattered')
    if q==3:
        # All four-element subsets: Radon, Helly, and VC conditions by bit operations.
        for A in combinations(range(2*n),4):
            mask=sum(1<<a for a in A)
            H3=[hull(mask^(1<<a),I) for a in A]
            assert H3[0]&H3[1]&H3[2]&H3[3]
            assert any((hull(sum(1<<i for i in part),I)&hull(mask^sum(1<<i for i in part),I))
                       for k in (1,2) for part in combinations(A,k))
        print('all 14950 four-sets: Radon / Helly tests passed')
        for A in combinations(range(2*n),5):
            traces={sum((1<<j) for j,a in enumerate(A) if m>>a&1) for m in E}
            assert len(traces)<32
        print('all 65780 five-sets fail to be shattered')
    if q!=2:
        # Exhaustive triples: if the hull is proper, it is already one of the proved star forms.
        for A in combinations(range(2*n),3):
            c=hull(sum(1<<i for i in A),I)
            assert c in E
        print('all',len(list(combinations(range(2*n),3))),'triple hulls classified')

if __name__=='__main__':
    test(2); test(3); test(5)
    print('VERIFICATION PASS')
