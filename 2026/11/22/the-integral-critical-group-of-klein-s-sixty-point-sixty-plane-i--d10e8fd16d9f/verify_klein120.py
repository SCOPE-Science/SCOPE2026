#!/usr/bin/env python3
"""Exact-arithmetic verification of Klein's 60-point/60-plane incidence graph.

Requires Python 3.9+ standard library only. All calculations use integers.
The prime-power elimination is a valid Smith-form calculation over Z/(p**K).
"""
from collections import Counter
from itertools import combinations, product
from math import prod


def coords():
    # Gaussian integers (real, imaginary); projective representatives in P^3.
    P = []
    for i in range(4):
        x = [(0, 0)] * 4
        x[i] = (1, 0)
        P.append(tuple(x))
    for a,b in combinations(range(4),2):
        for z in ((1,0),(-1,0),(0,1),(0,-1)):
            x = [(0,0)]*4
            x[a] = (1,0)
            x[b] = z
            P.append(tuple(x))
    for s in product((1,-1),repeat=3):
        P.append(((1,0),)+tuple((z,0) for z in s))
    for j in range(1,4):
        other = [h for h in range(1,4) if h != j]
        for s,a,b in product((1,-1),repeat=3):
            x = [(0,0)]*4
            x[0] = (1,0)
            x[j] = (s,0)
            x[other[0]] = (0,a)
            x[other[1]] = (0,b)
            P.append(tuple(x))
    assert len(P) == 60 and len(set(P)) == 60
    return P


def incidence():
    P = coords()
    def orthogonal(x,y):
        real = sum(a*c-b*d for (a,b),(c,d) in zip(x,y))
        imag = sum(a*d+b*c for (a,b),(c,d) in zip(x,y))
        return int(real == 0 and imag == 0)
    B = [[orthogonal(x,y) for y in P] for x in P]
    assert all(sum(row) == 15 for row in B)
    assert all(sum(B[i][j] for i in range(60)) == 15 for j in range(60))
    assert all(B[i][j] == B[j][i] for i in range(60) for j in range(60))
    assert sum(sum(row) for row in B) == 900
    return B


def mul(A,B):
    n=len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for k,a in enumerate(A[i]):
            if a:
                for j,b in enumerate(B[k]):
                    if b: C[i][j] += a*b
    return C


def check_spectrum(B):
    # The published geometry does not supply the integral Smith invariants.
    # These rational eigenvalue multiplicities are independently certified
    # by the exact polynomial identity and six exact power traces.
    eig = {15:1,-3:5,-5:9,-1:12,5:15,1:18}
    n = len(B)
    I = [[int(i==j) for j in range(n)] for i in range(n)]
    power = I
    for r in range(6):
        assert sum(power[i][i] for i in range(n)) == sum(m*(lam**r) for lam,m in eig.items())
        power = mul(power,B)
    P = I
    for lam in eig:
        Q = [[B[i][j] - lam*int(i==j) for j in range(n)] for i in range(n)]
        P = mul(P,Q)
    assert all(a==0 for row in P for a in row)
    # The Laplacian eigenvalues are 15 +/- each eigenvalue of B.
    lap = Counter()
    for lam,m in eig.items():
        lap[15+lam] += m
        lap[15-lam] += m
    assert lap[0]==1 and sum(lap.values())==120
    determinant = prod(t**m for t,m in lap.items() if t>0)//120
    assert determinant == 2**235 * 3**15 * 5**48 * 7**30
    return determinant


def laplacian(B):
    L = [[0]*120 for _ in range(120)]
    for i in range(120):L[i][i] = 15
    for i in range(60):
        for j,b in enumerate(B[i]):
            if b: L[i][60+j]=L[60+j][i]=-1
    return L


def prime_valuations(L,p,K,deleted):
    # Local diagonal equivalence in Z/p^K: a unit pivot splits off one
    # Smith factor of the current valuation, and a p-divisible remaining
    # block can be divided by p, increasing all remaining valuations.
    mod = p**K
    M = [[a%mod for j,a in enumerate(row) if j != deleted]
         for i,row in enumerate(L) if i != deleted]
    n = len(M)
    k = v = 0
    vals = []
    while k<n:
        ij = next(((i,j) for i in range(k,n) for j in range(k,n)
                   if M[i][j]%p != 0),None)
        if ij is None:
            assert all(M[i][j]%p == 0 for i in range(k,n) for j in range(k,n))
            assert mod > p
            for i in range(k,n):
                for j in range(k,n): M[i][j]//=p
            mod//=p;v+=1
            continue
        i,j = ij
        M[k],M[i] = M[i],M[k]
        for row in M: row[k],row[j] = row[j],row[k]
        pivot = M[k][k]
        assert pivot%p != 0
        inv=pow(pivot,-1,mod)
        for i in range(k+1,n):
            coef=(M[i][k]*inv)%mod
            if coef:
                for j in range(k+1,n):
                    M[i][j] = (M[i][j]-coef*M[k][j])%mod
        vals.append(v)
        k+=1
    return vals


def main():
    B=incidence()
    det=check_spectrum(B)
    L=laplacian(B)
    profiles={}
    for p,K in ((2,12),(3,8),(5,6),(7,5)):
        a=prime_valuations(L,p,K,0)
        b=prime_valuations(L,p,K,119)
        assert a==b and len(a)==119
        profiles[p]=a
        print('prime',p,'valuation_multiplicities',dict(sorted(Counter(a).items())))
    expected={2:235,3:15,5:48,7:30}
    assert {p:sum(v) for p,v in profiles.items()}==expected
    invariants=[prod(p**prof[i] for p,prof in profiles.items()) for i in range(119)]
    assert all(invariants[i+1]%invariants[i] == 0 for i in range(118))
    assert prod(invariants)==det
    expected_group={1:64,2:7,4:1,20:3,40:14,1120:16,4480:3,13440:7,40320:3,201600:1}
    assert dict(Counter(invariants))==expected_group
    print('invariant_factors',dict(sorted(Counter(invariants).items())))
    print('vertices',120,'edges',900,'cycle_rank',781)
    print('spanning_tree_count','2^235 * 3^15 * 5^48 * 7^30')
    print('KLEIN_60_15_INTEGRAL_CRITICAL_GROUP_OK')

if __name__=='__main__': main()
