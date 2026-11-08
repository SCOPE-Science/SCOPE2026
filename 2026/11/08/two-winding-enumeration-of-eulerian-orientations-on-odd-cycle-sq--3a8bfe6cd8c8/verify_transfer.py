#!/usr/bin/env python3
"""Independent eight-state transfer proof checks using exact polynomial arithmetic."""
from collections import defaultdict,Counter
from math import comb

def product(A,B):
    n=len(A)
    C=[[Counter() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if not A[i][k]: continue
            for j in range(n):
                for (p,q),v in A[i][k].items():
                    for (r,s),w in B[k][j].items():
                        C[i][j][(p+r,q+s)]+=v*w
    return C

def transfer():
    states=[(a,b,c) for a in range(2) for b in range(2) for c in range(2)]
    T=[[Counter() for _ in states] for _ in states]
    for i,(a,b,c) in enumerate(states):
        for x in (0,1):
            for y in (0,1):
                if x+y!=a+b: continue
                j=states.index((x,c,y))
                T[i][j][(x,y)]+=1
    return T

def polynomial(n):
    c=Counter({(0,0):1,(n,n):1})
    for j in range(n//2+1):
        factor=n*comb(n-j,j)//(n-j)
        c[n-2*j,j]+=factor
        c[2*j,n-j]+=factor
    return c

T=transfer()
P=T
for n in range(1,16):
    if n>1: P=product(P,T)
    tally=Counter()
    for i in range(8): tally.update(P[i][i])
    if n>=5:
        assert tally==polynomial(n), (n,tally,polynomial(n))
        print(f"n={n} trace={sum(tally.values())} profile_terms={len(tally)} MATCH")
print("PASS transfer matrix and binomial formula for n=5..15")
