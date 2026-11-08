#!/usr/bin/env python3
"""Exact arithmetic and polynomial checks for four-column Paley Gram spectra."""
from itertools import combinations
from fractions import Fraction
from math import comb, isqrt


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def count_classes(p):
    R = {x*x % p for x in range(1,p)}
    counts = {0:0,2:0,4:0}
    for pts in combinations(range(p),4):
        vals = []
        for tri in combinations(pts,3):
            a,b,c=tri
            v = 1
            for u,w in ((a,b),(a,c),(b,c)):
                v *= 1 if (u-w)%p in R else -1
            vals.append(v)
        neg=vals.count(-1)
        assert neg in counts
        counts[neg]+=1
    return counts


def run():
    tests=0
    for p in [5,13,17,29,37,41]:
        assert is_prime(p) and p % 4==1
        counts=count_classes(p)
        a=p*(p-1)*(p-3)*(p-5)//192
        assert counts=={0:a,2:comb(p,4)-2*a,4:a},(p,counts,a)
        tests+=comb(p,4)
        R={x*x%p for x in range(1,p)}
        for b in range(1,p):
            f=[1 if ((c*c-1)%p) in R else -1 for c in range(p)] if False else [1 if (c*(c-b))%p in R else (-1 if c not in [0,b] else 0) for c in range(p)]
            assert sum(f)==-1,(p,b,sum(f))
            tests+=1
    # 4x4 signed Gram Seidel charpoly checks via elementary exact permutations.
    def det(A):
        if len(A)==1:return A[0][0]
        return sum((-1)**j * A[0][j] * det([row[:j]+row[j+1:] for row in A[1:]]) for j in range(len(A)))
    def charpoly(S):
        # interpolate determinant at five integers for the three proposed polynomials
        for t in [-3,-2,0,2,3]:
            A=[[t*(i==j)-S[i][j] for j in range(4)] for i in range(4)]
            yield t,det(A)
    for edges,roots in [((1,1,1),(3,-1,-1,-1)),((-1,-1,-1),(-3,1,1,1)),((-1,1,1),(1,-1,'sqrt5','-sqrt5'))]:
        a,b,c=edges
        S=[[0,1,1,1],[1,0,a,b],[1,a,0,c],[1,b,c,0]]
        for t,D in charpoly(S):
            exp=(t-3)*(t+1)**3 if edges==(1,1,1) else ((t+3)*(t-1)**3 if edges==(-1,-1,-1) else (t*t-1)*(t*t-5))
            assert D==exp,(edges,t,D,exp)
            tests+=1
    print('PALEY_FOUR_COLUMN_CHECKS_PASS', tests)
if __name__=='__main__':run()
