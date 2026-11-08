#!/usr/bin/env python3
"""Exact checks for the simplex-skeleton Minkowski filtration.
Only Python's standard library is needed. Finite tests corroborate the proof;
they do not replace its all-dimensional arguments.
"""
from fractions import Fraction as Q
from math import factorial, comb
from itertools import combinations
import random

CHECKS = 0

def check(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def det(mat):
    a = [[Q(x) for x in row] for row in mat]
    n = len(a)
    out = Q(1)
    for col in range(n):
        piv = next((i for i in range(col,n) if a[i][col]),None)
        if piv is None:
            return Q(0)
        if piv != col:
            a[piv],a[col] = a[col],a[piv]
            out = -out
        pivot = a[col][col]
        out *= pivot
        for i in range(col+1,n):
            z = a[i][col]/pivot
            for j in range(col+1,n):
                a[i][j] -= z*a[col][j]
            a[i][col] = Q(0)
    return out

def top_sum(x, s):
    return sum(sorted(x, reverse=True)[:s],Q(0))

def gf2_rank(columns):
    pivots = {}
    for col in columns:
        while col:
            p = col.bit_length()-1
            if p in pivots:
                col ^= pivots[p]
            else:
                pivots[p]=col
                break
    return len(pivots)

def skeleton_betti(n,k):
    # Reduced integral homology is free for simplex skeleta;
    # these mod-2 ranks independently check the predicted Betti ranks.
    faces = {j:list(combinations(range(n), j+1)) for j in range(k)}
    ranks = {0:1} # augmentation from zero chains
    for j in range(1,k):
        ind = {F:i for i,F in enumerate(faces[j-1])}
        cols=[]
        for F in faces[j]:
            bits=0
            for t in range(len(F)):
                sub=F[:t]+F[t+1:]
                bits ^= 1<<ind[sub]
            cols.append(bits)
        ranks[j]=gf2_rank(cols)
    ranks[k]=0
    return [len(faces[j])-ranks[j]-ranks[j+1] for j in range(k)]

for n in range(3,9):
    d=n-1
    for k in range(1,n):
        betti=skeleton_betti(n,k)
        for i,actual in enumerate(betti):
            check(actual==(comb(d,k) if i==k-1 else 0),
                  ('homology',n,k,i,actual))

rng=random.Random(106)
for n in range(3,11):
    d=n-1
    b=[]
    for j in range(1,n):
        b.append(tuple(Q(int(i<j))-Q(j,n) for i in range(n)))
    gram=[[sum((b[i][t]*b[j][t] for t in range(n)),Q(0))
           for j in range(d)] for i in range(d)]
    check(det(gram)==Q(1,n), ('gram',n))
    for s in range(1,n):
        qs=[Q(min(j,s))-Q(j*s,n) for j in range(1,n)]
        for j in range(1,n):
            check(top_sum(b[j-1],s)==qs[j-1],('ray',n,s,j))
        prod=Q(1)
        for q in qs: prod*=q
        pred=Q(factorial(d)*n**d,
               factorial(s)*factorial(n-s-1)*(n-s)**s*s**(n-s-1))
        check(Q(factorial(d),1)/prod==pred,('volume',n,s))
        # The last phase of deficit uses W vertices b_j/q_j.
        smallest=min(min(x/q for x in bj) for bj,q in zip(b,qs))
        check(smallest==Q(-(n-1),s),('last-phase-range',n,s))
        for _ in range(100):
            # Independently check membership through a face witness.
            raw=[rng.randint(1,50) for _ in range(n)]
            p=[Q(x,sum(raw)) for x in raw]
            lam=Q(rng.randint(0,15),rng.randint(1,9))
            alpha=Q(1,1)/(1+lam)
            criterion=top_sum(p,s)>=alpha
            face_criterion=any(sum((p[i] for i in S),Q(0))>=alpha
                               for S in combinations(range(n),s))
            check(criterion==face_criterion, ('face-exact',n,s))
            if criterion:
                S=max(combinations(range(n),s),
                      key=lambda S:sum(p[i] for i in S))
                mass=sum((p[i] for i in S),Q(0))
                y=[p[i]/mass if i in S else Q(0) for i in range(n)]
                z=[((1+lam)*p[i]-y[i])/lam if lam else Q(0)
                   for i in range(n)]
                if lam:
                    check(all(x>=0 for x in z) and sum(z)==1,
                          ('decomposition',n,s))
                    check(all(y[i]>=0 for i in range(n)) and sum(y)==1,
                          ('face',n,s))
        for _ in range(30):
            # Convex-hull simplex triangulation is linear for top-s sum.
            sigma=list(range(n))
            rng.shuffle(sigma)
            vals=[rng.randint(0,20) for _ in range(n)]
            T=sum(vals)
            if not T: continue
            p=[Q(0) for _ in range(n)]
            vertex_top=Q(0)
            for j,v in enumerate(vals,1):
                S=set(sigma[:j]); weight=Q(v,T)
                for i in S: p[i]+=weight/Q(j)
                vertex_top+=weight*Q(min(s,j),j)
            check(top_sum(p,s)==vertex_top,('PL affine',n,s))

print('PASS:', CHECKS, 'exact assertions; n=3..10, all skeleton ranks and barycentric tests')
