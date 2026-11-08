#!/usr/bin/env python3
"""Exact small-order verification of induced-motif / isolation covariance in G(n,m)."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial

MOTIFS = {
    "P3": (3, ((0, 1), (1, 2))),
    "K3": (3, ((0, 1), (0, 2), (1, 2))),
    "P4": (4, ((0, 1), (1, 2), (2, 3))),
    "claw": (4, ((0, 1), (0, 2), (0, 3))),
    "C4": (4, ((0, 1), (1, 2), (2, 3), (0, 3))),
    "diamond": (4, ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3))),
    "K4": (4, tuple(combinations(range(4), 2))),
}

def fall(a, r):
    if r < 0 or a < r: return 0
    out = 1
    for j in range(r): out *= a-j
    return out

def b_factor(n,k,h,m):
    N, L, K = comb(n, 2), comb(n-1, 2), comb(k, 2)
    q = K-h
    if m > L-q: return Fraction(0)
    return Fraction(n-k,n)*Fraction(fall(N,K),fall(L,K))*Fraction(fall(L-m,q),fall(N-m,q))

def expected_cov(n,k,h,c,m):
    N,L,K = comb(n,2),comb(n-1,2),comb(k,2)
    q=K-h
    if not (h <= m <= N-q) or m > L: return Fraction(0)
    ei=Fraction(n*comb(L,m),comb(N,m))
    et=Fraction(comb(n,k)*c*comb(N-K,m-h),comb(N,m))
    return ei*et*(b_factor(n,k,h,m)-1)

def motif_class(k, edges):
    local_edges = tuple(combinations(range(k),2))
    idx={e:i for i,e in enumerate(local_edges)}
    out=set()
    for perm in permutations(range(k)):
        mask=0
        for a,b in edges:
            mask|=1<<idx[tuple(sorted((perm[a],perm[b])))]
        out.add(mask)
    return out

def exhaustive(n, motif):
    k,edges=MOTIFS[motif]
    if n <= k: return 0
    N=comb(n,2)
    big_edges=tuple(combinations(range(n),2))
    big_idx={e:i for i,e in enumerate(big_edges)}
    local_edges=tuple(combinations(range(k),2))
    patterns=motif_class(k,edges)
    c=len(patterns)
    subsets=[]
    for vertices in combinations(range(n),k):
        subsets.append([(big_idx[(vertices[a],vertices[b])],li) for li,(a,b) in enumerate(local_edges)])
    inv=1<<N
    accum=defaultdict(lambda:[0,0,0,0])
    for mask in range(inv):
        m=mask.bit_count()
        degrees=[0]*n
        for i,(u,v) in enumerate(big_edges):
            if (mask>>i)&1:degrees[u]+=1; degrees[v]+=1
        iso=sum(d==0 for d in degrees)
        t=0
        for pairs in subsets:
            pattern=0
            for bi,li in pairs:
                pattern|=((mask>>bi)&1)<<li
            if pattern in patterns:t+=1
        row=accum[m];row[0]+=1;row[1]+=iso;row[2]+=t;row[3]+=iso*t
    checks=0
    for m,(count,sum_i,sum_t,sum_it) in accum.items():
        measured=Fraction(sum_it,count)-Fraction(sum_i*sum_t,count**2)
        predicted=expected_cov(n,k,len(edges),c,m)
        assert measured==predicted,(n,motif,m,measured,predicted)
        checks+=1
    return checks

if __name__=='__main__':
    total=0
    for motif in MOTIFS:
        for n in range(MOTIFS[motif][0]+1,7):
            z=exhaustive(n,motif)
            total+=z
            print(motif,n,z,'exact covariance checks')
    # Exact monotonicity, threshold and tree shape independence on parameter grids.
    for k in range(3,13):
        for n in range(k+1,k+25):
            N,L,K=comb(n,2),comb(n-1,2),comb(k,2)
            for h in range(k-1,K):
                vals=[b_factor(n,k,h,m) for m in range(h,L+1)]
                assert all(a>b for a,b in zip(vals[:-1],vals[1:]) if a>0)
                assert vals[-1]==0
                total+=1
    print('PASSED:',total,'exact brute-force and parameter monotonicity checks')
