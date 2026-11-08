"""Exact rational checks for arclength Lipschitz variance with prescribed bridge length.
This program checks independently derived finite consequences; it is not a proof of the general theorem.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from random import Random


def matrix_K(n):
    K=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i<j:
                row.append(F((2*i+1)*(2*(n-j)-1),4*n**4))
            elif i>j:
                row.append(F((2*j+1)*(2*(n-i)-1),4*n**4))
            else:
                row.append(F(i,n**3)+F(1,3*n**3)-F((2*i+1)**2,4*n**4))
        K.append(row)
    return K


def V_from_h(h,K):
    n=len(h)
    return sum((h[i]*h[j]*K[i][j] for i in range(n) for j in range(n)),F(0))


def bound(L,B):
    return ((L+B)**3-4*B**3)/(48*L)

# Exhaustive independent discretized variational comparisons.
count=0
for n in range(2,11):
    K=matrix_K(n)
    for k in range(n+1):
        results=[]
        for S in combinations(range(n),k):
            z=set(S)
            h=[F(1,2)*(1+int(i in z)) for i in range(n)]
            results.append((V_from_h(h,K),S))
        val=max(v for v,_ in results)
        centers=[S for v,S in results if v==val]
        predicted=tuple(range((n-k)//2,(n-k)//2+k))
        assert predicted in centers, (n,k,predicted,centers)
        assert len(centers)==(1 if (n-k)%2==0 or k in (0,n) else 2), (n,k,centers)
        count+=len(results)
print('EXACT_DISCRETIZED_BRIDGE_BUDGET_OPTIMA_OK',count)

# Independent barbell arclength pushforward calculation.
# For B in [0,L], each exterior tail has density 2/L, length (L-B)/4;
# central bridge has density 1/L, length B.
cases=0
for den in range(1,16):
    for num in range(den+1):
        L=F(den+3,5)
        B=L*F(num,den)
        c=(L-B)/4
        # symmetric x: [0,B/2] density 1/L and [B/2,B/2+c] density 2/L.
        v=F(2,L)*( (B/2)**3/3 + F(2,3)*((B/2+c)**3-(B/2)**3) )
        assert v==bound(L,B),(L,B,v,bound(L,B))
        assert v>=L*L/48 and v<=L*L/12
        cases+=1
print('EXACT_BARBELL_SHARPNESS_IDENTITY_OK',cases)

# Arbitrary connected sampled simple graphs, finite edgewise affine Lipschitz profiles.
# Edge lengths integral; bridge lengths by deletion connectivity.
def connected(n,edges,skip=None):
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for i,(v,w,l) in enumerate(edges):
            if i==skip: continue
            if v==u and w not in seen:seen.add(w);stack.append(w)
            if w==u and v not in seen:seen.add(v);stack.append(v)
    return len(seen)==n

def bridge_mass(n,edges):
    return sum(l for k,(i,j,l) in enumerate(edges) if not connected(n,edges,skip=k))

rng=Random(63177);checks=0
for n in range(2,11):
    for _ in range(120):
        edges=[(i,rng.randrange(i),F(rng.randrange(1,9),4)) for i in range(1,n)]
        for i,j in combinations(range(n),2):
            if rng.randrange(6)==0 and not any({i,j}=={a,b} for a,b,_ in edges):
                edges.append((i,j,F(rng.randrange(1,9),4)))
        L=sum((e[2] for e in edges),F(0)); B=bridge_mass(n,edges)
        for __ in range(15):
            vals=[F(rng.randrange(-12,13),3) for i in range(n)]
            factor=min([F(1)]+[l/abs(vals[i]-vals[j]) for i,j,l in edges if vals[i]!=vals[j]])
            vals=[v*factor for v in vals]
            mean=sum((l*(vals[i]+vals[j])/2 for i,j,l in edges),F(0))/L
            second=sum((l*(vals[i]**2+vals[i]*vals[j]+vals[j]**2)/3 for i,j,l in edges),F(0))/L
            variance=second-mean**2
            assert variance<=bound(L,B),(n,edges,vals,variance,bound(L,B))
            checks+=1
print('RATIONAL_AFFINE_GRAPH_LIPSCHITZ_CHECKS_OK',checks)
print('ALL_BRIDGE_BUDGET_VARIANCE_CHECKS_OK')
