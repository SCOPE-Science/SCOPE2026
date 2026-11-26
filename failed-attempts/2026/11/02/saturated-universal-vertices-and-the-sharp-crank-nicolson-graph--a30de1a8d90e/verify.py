"""Reproducible exact arithmetic checks of sharp graph Crank--Nicolson positivity claims.

Run with Python 3 standard library: python verify.py
"""
from fractions import Fraction as F
from random import Random
from itertools import combinations
from math import sqrt

def invert(a):
    n = len(a)
    z = [[F(a[i][j]) for j in range(n)] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        k = next(k for k in range(j,n) if z[k][j] != 0)
        z[j], z[k] = z[k], z[j]
        t = z[j][j]
        z[j] = [v/t for v in z[j]]
        for i in range(n):
            if i != j:
                t = z[i][j]
                if t:
                    z[i] = [z[i][k] - t*z[j][k] for k in range(2*n)]
    return [row[n:] for row in z]

def cn(w, s):
    n = len(w)
    M = [[F(int(i==j)) + s*(sum(w[i]) if i==j else -w[i][j]) for j in range(n)] for i in range(n)]
    R = invert(M)
    return [[2*R[i][j] - F(int(i==j)) for j in range(n)] for i in range(n)]

def connected(w):
    vis = {0}; stack=[0]
    while stack:
        i=stack.pop()
        for j in range(len(w)):
            if w[i][j] and j not in vis:
                vis.add(j); stack.append(j)
    return len(vis)==len(w)

def saturated(w,c):
    return {i for i in range(len(w)) if all(w[i][j]==c for j in range(len(w)) if j!=i)}

def multipartite(parts, c=1):
    groups = [i for i, count in enumerate(parts) for _ in range(count)]
    n=len(groups)
    return [[F(c if i!=j and groups[i]!=groups[j] else 0) for j in range(n)] for i in range(n)], groups

rng=Random(170613)
checks={'connected_graphs':0,'universal_examples':0,'off_diagonals':0,'partitions':0,'threshold_brackets':0}
for n in range(3,9):
    for trial in range(76):
        c=F(3)
        w=[[F(0) for j in range(n)] for i in range(n)]
        # Connected spanning tree, optional extra edges with independently chosen weights.
        for v in range(1,n):
            u=rng.randrange(v)
            w[u][v]=w[v][u]=F(rng.randint(1,3))
        for i,j in combinations(range(n),2):
            if not w[i][j]:
                w[i][j]=w[j][i]=F(rng.randint(0,3))
        assert connected(w)
        C=cn(w, F(1,3*(n-2)))
        eq=saturated(w,c)
        assert all(sum(row)==1 for row in C)
        for i in range(n):
            assert C[i][i]>=0
            assert (C[i][i]==0)==(i in eq)
            for j in range(n):
                if i!=j:
                    assert C[i][j]>0
                    checks['off_diagonals']+=1
        if eq:
            Cnext=cn(w,F(101,100)*F(1,3*(n-2)))
            assert any(Cnext[i][i]<0 for i in eq)
            checks['universal_examples']+=1
        checks['connected_graphs']+=1

# Construct every nondecreasing integer partition for n<=9 with >=2 parts.
def partitions(n, smallest=1):
    for k in range(smallest, n+1):
        if k==n: yield (k,)
        else:
            for rest in partitions(n-k,k):yield (k,)+rest

for n in range(3,10):
    for parts in partitions(n):
        if len(parts)<2:continue
        a=min(parts)
        w,grp=multipartite(parts)
        d=(a*a+4*(n-a)*(n-2))**.5
        sstar=(a+d)/(2*(n-a)*(n-2))
        # Rigorous rational enclosing intervals for the algebraic root (20 decimals).
        # Use integer square root to obtain certified rational interval.
        from math import isqrt
        scale=10**16
        raw=a*a+4*(n-a)*(n-2)
        floorroot=isqrt(raw*scale*scale)
        lo=(F(a)+F(floorroot,scale))/(2*(n-a)*(n-2))
        hi=(F(a)+F(floorroot+1,scale))/(2*(n-a)*(n-2))
        assert (n-a)*(n-2)*lo*lo-a*lo-1<=0
        assert (n-a)*(n-2)*hi*hi-a*hi-1>=0
        Clo=cn(w,lo)
        Chi=cn(w,hi)
        minvertices={i for i,g in enumerate(grp) if parts[g]==a}
        for i in range(n):
            assert Clo[i][i]>=0
            assert (Chi[i][i]<0)==(i in minvertices)
        checks['partitions']+=1
        checks['threshold_brackets']+=len(minvertices)

print('VERIFICATION_OK',checks)
