#!/usr/bin/env python3
"""Standalone exhaustive graph-based checks for full ladder edge-query theorem.
Run with Python 3: python3 full_checker.py
The graph is constructed from its 2n vertices, not from the tiling recurrence.
"""
from math import comb
from itertools import combinations
from collections import defaultdict


def ladder_perfect_matchings(n):
    """Return edge-incidence masks: rungs 0..n-1, top  n..2n-2, bottom 2n-1..3n-3."""
    edgelist=[]
    for i in range(n): edgelist.append((2*i, 2*i+1))
    for i in range(n-1): edgelist.append((2*i, 2*i+2))
    for i in range(n-1): edgelist.append((2*i+1, 2*i+3))
    adj=[[] for _ in range(2*n)]
    for idx,(a,b) in enumerate(edgelist):
        adj[a].append((b,idx));adj[b].append((a,idx))
    out=set()
    def rec(remaining,mask):
        if not remaining:out.add(mask);return
        a=min(remaining)
        for b,idx in adj[a]:
            if b in remaining:rec(remaining-{a,b},mask|(1<<idx))
    rec(set(range(2*n)),0)
    return tuple(out)


def bruteforce_shat(concepts, S):
    positions=[i for i in range(max(1,S.bit_length())) if S>>i&1]
    outcomes={sum(((c>>i)&1)<<j for j,i in enumerate(positions)) for c in concepts}
    return len(outcomes)==(1<<len(positions))


def valid_rung_component(pattern):
    n=len(pattern);i=0
    while i<n:
        j=i+1
        while j<n and pattern[j]!=pattern[j-1]:j+=1
        if pattern[i] and (j-i)%2: return False
        i=j
    return True


def theorem_shat(n,S):
    H=[]
    for i in range(n-1):
        a=(S>>(n+i))&1
        b=(S>>(2*n-1+i))&1
        if a and b:return False
        if a or b:H.append(i)
    occupied=set()
    for i in H:
        if i in occupied or (i+1) in occupied:return False
        occupied.update((i,i+1))
    for i in occupied:
        if S>>i&1:return False
    v=[(S>>i)&1 for i in range(n)]
    start=0
    for i in sorted(occupied):
        if start<i and not valid_rung_component(v[start:i]):return False
        start=i+1
    return valid_rung_component(v[start:])


def recurrent_poly(N):
    out=[[1],[1]]
    for n in range(2,N+1):
        A=out[n-1];B=out[n-2];C=out[n-3] if n>=3 else []
        p=[0]*max(len(A),len(B)+1,len(C)+1)
        for j,x in enumerate(A):p[j]+=x
        for j,x in enumerate(B):p[j+1]+=4*x
        for j,x in enumerate(C):p[j+1]-=x
        while p[-1]==0:p.pop()
        out.append(p)
    return out


def coeff_formula(n,k):
    if n<2*k:return 0
    return sum(comb(k,r)*3**r*comb(n-2*k+r,r) for r in range(k+1))


def main():
    # n=0 has one empty matching and one shattered empty query support.
    ps=recurrent_poly(100)
    checks=0
    for n in range(1,7):
        concepts=ladder_perfect_matchings(n)
        counts=[0]*(n+1)
        face_masks=[]
        for S in range(1<<(3*n-2)):
            observed=bruteforce_shat(concepts,S)
            structural=theorem_shat(n,S)
            assert observed==structural,(n,S,observed,structural)
            if observed:counts[S.bit_count()]+=1;face_masks.append(S)
            checks+=1
        assert counts[:len(ps[n])]==ps[n],(n,counts,ps[n])
        assert not any(counts[len(ps[n]):]),(n,counts,ps[n])
        if n==6:
            faces=set(face_masks)
            facets=[S for S in faces if all((S|1<<j) not in faces for j in range(3*n-2) if not (S>>j&1))]
            print('n6 facet dimensions',sorted({S.bit_count() for S in facets}),'total facets',len(facets))
        print(n,'concepts',len(concepts),'shattered polynomial',ps[n])
    # Larger sizes: test the structural characterization directly against a reduced
    # (rung + one cut per position) query universe, which is the only quotient under
    # identical top and bottom queries.
    for n in range(7,10):
        C=ladder_perfect_matchings(n)
        projection=[(c&((1<<(2*n-1))-1)) for c in C]
        counts=[0]*(n+1)
        for S in range(1<<(2*n-1)):
            assert bruteforce_shat(projection,S)==theorem_shat(n,S),(n,S)
            checks+=1
        print('reduced exhaustive agreement',n,'supports',1<<(2*n-1))
    for n in range(101):
        assert all(ps[n][k]==coeff_formula(n,k) for k in range(len(ps[n]))),(n,ps[n])
        if n>0:assert len(ps[n])-1==n//2
        if n>=2 and n%2==0:assert ps[n][n//2]==4**(n//2)
        if n>=3 and n%2:assert ps[n][n//2]==(3*(n//2)+4)*4**(n//2-1)
    print('PASS full edge-query characterization, enumerator, closed coefficients, VC rank')
    print('Direct support comparisons:',checks)
    print('Exact symbolic-integer coefficient checks for all n <=100')

if __name__=='__main__':main()
