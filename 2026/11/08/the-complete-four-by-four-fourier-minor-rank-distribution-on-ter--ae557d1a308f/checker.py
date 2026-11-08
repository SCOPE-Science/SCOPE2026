#!/usr/bin/env python3
"""Exact four-column Fourier-rank census on ternary affine spaces.

All finite base cases are exhaustive; determinants are in Z[omega].
A second exact check uses a split prime larger than any minor norm.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb

REPRESENTATIVES = {
    'line_plus_point': ((0,0),(1,0),(2,0),(0,1)),
    'cap': ((0,0),(1,0),(0,1),(1,1)),
    'simplex': ((0,0,0),(1,0,0),(0,1,0),(0,0,1)),
}
EXPECTED = {
 'line_plus_point': ((0,9,0,0,0),(0,0,36,0,0),(0,0,3,81,0),(0,0,0,45,81)),
 'cap': ((0,9,0,0,0),(0,0,36,0,0),(0,0,6,78,0),(0,0,0,45,81)),
 'simplex': ((0,27,0,0,0),(0,0,351,0,0),(0,0,63,2862,0),(0,0,0,3213,14337)),
}
P = 1000003
# P=1 modulo 3, and P is prime; the first nontrivial cubic root is chosen.
assert P % 3 == 1
assert all(P % t for t in range(2, int(P**.5)+1))
OMEGA_MOD = next(pow(g, (P-1)//3, P) for g in range(2,20)
                 if pow(g,(P-1)//3,P)!=1)
assert OMEGA_MOD != 1 and pow(OMEGA_MOD,3,P)==1

def exponent_matrix(A,B):
    return [[sum(x*y for x,y in zip(a,b))%3 for b in B] for a in A]

def det_eisenstein(M):
    """Return integers (u,v) with determinant = u+v*omega."""
    n=len(M)
    tallies=[0,0,0]
    for sigma in permutations(range(n)):
        inversions=sum(sigma[i]>sigma[j]
                       for i in range(n) for j in range(i+1,n))
        exponent=sum(M[i][sigma[i]] for i in range(n))%3
        tallies[exponent] += -1 if inversions%2 else 1
    return (tallies[0]-tallies[2],tallies[1]-tallies[2])

def exact_rank(M):
    rows=len(M); columns=len(M[0])
    for k in range(min(rows,columns),0,-1):
        for I in combinations(range(rows),k):
            for J in combinations(range(columns),k):
                if det_eisenstein([[M[i][j] for j in J] for i in I])!=(0,0):
                    return k
    return 0

def modular_rank(M):
    A=[[pow(OMEGA_MOD,x,P) for x in row] for row in M]
    m=len(A); n=len(A[0]); rank=0
    for j in range(n):
        pivot=next((i for i in range(rank,m) if A[i][j]),None)
        if pivot is None: continue
        A[rank],A[pivot]=A[pivot],A[rank]
        mult=pow(A[rank][j],P-2,P)
        A[rank]=[(mult*x)%P for x in A[rank]]
        for i in range(rank+1,m):
            if A[i][j]:
                factor=A[i][j]
                A[i]=[(x-factor*y)%P for x,y in zip(A[i],A[rank])]
        rank+=1
        if rank==min(m,n):break
    return rank

def base_histogram(A):
    points=tuple(product(range(3),repeat=len(A[0])))
    table={}
    for t in range(1,5):
        counts=Counter()
        for B in combinations(points,t):
            M=exponent_matrix(A,B)
            r=exact_rank(M)
            assert r == modular_rank(M), (A,B,r)
            counts[r]+=1
        assert sum(counts.values())==comb(len(points),t)
        table[t]=tuple(counts.get(r,0) for r in range(5))
    return tuple(table[t] for t in range(1,5))

def weights(M):
    return (0, comb(M,4) if M>=4 else 0,
            2*M*(comb(M,3) if M>=3 else 0)+comb(M,2)**2,
            3*M*M*comb(M,2), M**4)

def rank_counts(d):
    assert d>=3
    Q=3**d
    rows={'line_plus_point':Q*(Q-1)*(Q-3)//6,
          'cap':Q*(Q-1)*(Q-3)//8}
    rows['simplex']=comb(Q,4)-rows['line_plus_point']-rows['cap']
    assert all(x>=0 for x in rows.values())
    rank=[0]*5
    for name,hist in EXPECTED.items():
        dim=3 if name=='simplex' else 2
        w=weights(3**(d-dim))
        for t in range(1,5):
            for r in range(1,5):
                rank[r]+=rows[name]*hist[t-1][r]*w[t]
    assert sum(rank)==comb(Q,4)**2
    return tuple(rank[1:])

if __name__=='__main__':
    for name,A in REPRESENTATIVES.items():
        actual=base_histogram(A)
        assert actual==EXPECTED[name],(name,actual)
    assert rank_counts(3)==(0,4359420,90239994,213403086)
    for d in (3,4,5,6):
        rank=rank_counts(d)
        print('d=',d,'counts=',rank)
    print('TERNARY_FOURIER_RANK_CENSUS_PASS')
