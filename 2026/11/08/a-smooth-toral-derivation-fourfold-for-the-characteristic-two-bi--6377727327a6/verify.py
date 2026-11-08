"""Finite checks for toral derivations of a two-variable square-zero algebra.
Run: python3 verify.py; no nonstandard packages.
"""
from itertools import product
from collections import Counter

def mul(q,a,b):
    if q==2:return a&b
    if q!=4:raise ValueError(q)
    p=0
    while b:
        if b&1:p^=a
        a<<=1
        if a&4:a^=7
        b>>=1
    return p

def derivation(q,f,g):
    a,b,c,d=f;e,h,i,j=g
    return [[0,a,e,0],[0,b,h,e],[0,c,i,a],[0,d,j,b^i]]

def idempotent(q,M):
    return all((sum([0]) if False else xor_product(q,M,i,j)) == M[i][j]
               for i in range(4) for j in range(4))

def xor_product(q,M,i,j):
    s=0
    for h in range(4):s^=mul(q,M[i][h],M[h][j])
    return s

def rank(q,M):
    A=[r[:] for r in M];z=0
    for c in range(4):
        j=next((i for i in range(z,4) if A[i][c]),None)
        if j is None:continue
        A[z],A[j]=A[j],A[z]
        inv=next(k for k in range(1,q) if mul(q,k,A[z][c])==1)
        A[z]=[mul(q,inv,x) for x in A[z]]
        for i in range(4):
            if i!=z and A[i][c]:
                fac=A[i][c]
                A[i]=[x^mul(q,fac,y) for x,y in zip(A[i],A[z])]
        z+=1
    return z

def census(q):
    count=Counter(); found={}
    for coords in product(range(q), repeat=8):
        f,g=coords[:4],coords[4:];M=derivation(q,f,g)
        if idempotent(q,M):
            if f[0] or g[0]:key='nonzero_constant'
            elif all(x==0 for x in coords):key='zero'
            elif f[1]^g[2] ==1:key='projection_rank_one' # trace 1 for 2x2 idempotent P in char 2
            else:key='projection_rank_two'
            count[key]+=1;found.setdefault(key,(f,g,M))
            if key!='zero':assert rank(q,M)==2
    expected={'zero':1,'projection_rank_one':q*q*(q+1),'projection_rank_two':q*q,
              'nonzero_constant':q*q*(q*q-1)}
    assert dict(count)==expected,(q,count,expected)
    print('q=',q,'zero/rank-one/rank-two/nonzero-constant:',[count[k] for k in expected],
          'total=',sum(count.values()),'PASS')
    return found

for q in (2,4):census(q)

# Tangent space: derivative of D^2-D at D, restricted to all 8 derivation parameters.
def tangent_dim(D):
    cols=[]
    for h in range(8):
        coordinates=[0]*8;coordinates[h]=1
        E=derivation(2,coordinates[:4],coordinates[4:]);out=[]
        for j in (1,2):
            for i in range(4):
                a=0
                for z in range(4): a^=(D[i][z]&E[z][j])^(E[i][z]&D[z][j])
                out.append(a^E[i][j])
        cols.append(sum(x<<k for k,x in enumerate(out)))
    piv={}
    for c in cols:
        while c:
            k=c.bit_length()-1
            if k in piv:c^=piv[k]
            else:piv[k]=c;break
    return 8-len(piv)

canonical=[
    ((0,0,0,0),(0,0,0,0)),
    ((0,1,0,0),(0,0,0,0)),
    ((0,1,0,0),(0,0,1,0)),
    ((1,1,0,0),(0,0,0,0)),
]
for n,(f,g) in zip(('zero','rank_one','rank_two','nonzero_constant'),canonical):
    D=derivation(2,f,g)
    assert idempotent(2,D)
    t=tangent_dim(D)
    assert t==(0 if n=='zero' else 4)
    print('tangent dimension',n,t,'PASS')
print('ALL_TORAL_DERIVATION_CHECKS_PASS')
