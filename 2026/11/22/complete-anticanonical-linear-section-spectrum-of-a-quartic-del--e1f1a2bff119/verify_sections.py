#!/usr/bin/env python3
"""Exact projective-section census for an explicit quartic del Pezzo surface over F5.

Usage: python3 verify_sections.py
Python 3 standard library only. No input files or external programs.
"""
from collections import Counter
from itertools import combinations, permutations, product

Q = 5

def projective_points(n=5):
    # Unique homogeneous representative: first nonzero coordinate equals one.
    for v in product(range(Q), repeat=n):
        if any(v) and next(x for x in v if x) == 1:
            yield v

def equations(v):
    a, b, c, d, e = v
    q3 = b*b + 2*a*c + 2*d*d + 4*c*e + 2*d*e + e*e
    q4 = (2*b*c + c*c + 2*a*d + 2*b*d + 2*c*d + d*d
          + 2*a*e + 2*b*e + 2*c*e + d*e + 4*e*e)
    return q3 % Q, q4 % Q

def linear_subspaces_by_equations(k, n=5):
    # All and only rank-k row-reduced matrices, hence each codimension-k
    # projective linear subspace of PG(n-1,Q) exactly once.
    for pivots in combinations(range(n), k):
        free = [(i,j) for i in range(k) for j in range(n)
                if j not in pivots and j > pivots[i]]
        for vals in product(range(Q), repeat=len(free)):
            rows = [[0]*n for _ in range(k)]
            for i,j in enumerate(pivots):
                rows[i][j] = 1
            for (i,j), x in zip(free, vals):
                rows[i][j] = x
            yield tuple(tuple(r) for r in rows)

def zeros(rows, points):
    return sum(all(sum(a*b for a,b in zip(r,v)) % Q == 0 for r in rows)
               for v in points)

def smooth_pencil_test():
    # Coefficient matrices for twice the two quadratic forms.
    A = ((0,0,2,0,0), (0,2,0,0,0), (2,0,0,0,4),
         (0,0,0,4,2), (0,0,4,2,2))
    B = ((0,0,0,2,2), (0,0,2,2,2), (0,2,2,2,2),
         (2,2,2,2,1), (2,2,2,1,8))
    def mul(f,g):
        a = [0]*(len(f)+len(g)-1)
        for i,x in enumerate(f):
            for j,y in enumerate(g): a[i+j] = (a[i+j]+x*y)%Q
        return a
    det = [0]*6
    for pi in permutations(range(5)):
        inv = sum(pi[i] > pi[j] for i in range(5) for j in range(i+1,5))
        prod = [1]
        for i,j in enumerate(pi): prod = mul(prod,[B[i][j],A[i][j]])
        sgn = -1 if inv % 2 else 1
        for i,x in enumerate(prod): det[i] = (det[i] + sgn*x)%Q
    assert det == [3,3,3,3,2,3], det
    def trim(a):
        a = a[:]
        while len(a)>1 and a[-1]==0: a.pop()
        return a
    def rem(a,b):
        a=trim(a);b=trim(b)
        while len(a)>=len(b) and any(a):
            mult = a[-1]*pow(b[-1],-1,Q)%Q
            shift = len(a)-len(b)
            for j,v in enumerate(b):a[j+shift]=(a[j+shift]-mult*v)%Q
            a=trim(a)
        return a
    def gcd(a,b):
        while any(b):a,b=b,rem(a,b)
        return trim(a)
    der = [(i*det[i])%Q for i in range(1,len(det))]
    assert len(gcd(det,der))==1
    print('smoothness: squarefree degree-five discriminant det(t*2Q3+2Q4)')

EXPECTED = {
    1: {0:1,2:46,3:62,4:63,5:122,6:126,7:124,8:108,9:82,10:47},
    2: {0:5880,1:7081,2:4770,3:1935,4:640},
    3: {0:15935,1:3906,2:465},
    4: {0:750,1:31},
}

def main():
    all_points = list(projective_points())
    assert len(all_points)==781
    X = [p for p in all_points if equations(p)==(0,0)]
    assert len(X)==31
    smooth_pencil_test()
    for k in range(1,5):
        hist=Counter()
        for rows in linear_subspaces_by_equations(k):
            hist[zeros(rows,X)] += 1
        assert hist == EXPECTED[k], (k, hist)
        print('codimension',k,'total',sum(hist.values()),'histogram',sorted(hist.items()))
    H1=EXPECTED[1]
    weights=Counter({31-n:4*m for n,m in H1.items()})
    assert sum(weights.values())==3124
    print('nonzero codeword weights',sorted(weights.items()))
    print('generalized Hamming weights',[21,27,29,30,31])
    print('PASS')

if __name__=='__main__': main()
