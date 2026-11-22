#!/usr/bin/env python3
"""Recompute nilpotent regular-multiplication Jordan partitions in a three-axis squarefree complete intersection. No external dependencies."""
from collections import Counter
from itertools import product
import sys

def mul_table(q):
    if q==4:
        def add(a,b):return a^b
        def mul(a,b):
            c=0
            for i in range(2):
                for j in range(2):
                    if ((a>>i)&1) and ((b>>j)&1): c^=1<<(i+j)
            if c&8:c^=0b1100
            if c&4:c^=0b111
            return c
    else:
        def add(a,b):return (a+b)%q
        def mul(a,b):return (a*b)%q
    return [[add(i,j) for j in range(q)] for i in range(q)], [[mul(i,j) for j in range(q)] for i in range(q)]

def rank(A,q,add,mul,neg):
    M=[row[:] for row in A]
    r=0
    for c in range(len(M[0])):
        t=next((j for j in range(r,len(M)) if M[j][c]),None)
        if t is None:continue
        M[r],M[t]=M[t],M[r]
        pivot=M[r][c];inv=next(i for i in range(1,q) if mul[pivot][i]==1)
        M[r]=[mul[inv][x] for x in M[r]]
        for i in range(r+1,len(M)):
            f=M[i][c]
            if f:M[i]=[add[M[i][j]][neg[mul[f][M[r][j]]]] for j in range(len(M[0]))]
        r+=1
        if r==len(M):break
    return r

def partition(f,q,add,mul,neg):
    # Faster: compute coefficient arrays of f^2 and f^3 and use multiplication matrix directly
    g=[0]+list(f)
    ranks=[]
    for e in range(1,5):
        if e>1:
            old=g;g=[0]*8
            for a in range(1,8):
                for b in range(1,8):
                    if not (a&b):g[a|b]=add[g[a|b]][mul[old[a]][f[b-1]]]
        N=[[0]*8 for _ in range(8)]
        for s in range(8):
            for t in range(1,8):
                if not s&t:N[s|t][s]=g[t]
        ranks.append(rank(N,q,add,mul,neg))
    r0=8;ranks=[r0]+ranks+[0]
    parts=[]
    for size in range(4,0,-1):
        n=(ranks[size-1]-ranks[size])-(ranks[size]-ranks[size+1]);parts.extend([size]*n)
    assert sum(parts)==8,(f,parts,ranks)
    return tuple(parts)

def sum_mod(v,add):
    s=0
    for x in v:s=add[s][x]
    return s

def predicted(q,p):
    C=Counter();C[(1,)*8]=1;C[(2,)+(1,)*6]=q-1
    C[(2,2)+(1,)*4]=(q**3-1)*q
    if p==2:
        C[(2,)*4]=(q**3-1)*q**4
    else:
        C[(2,)*4]=3*(q-1)*q**3
        C[(3,2,2,1)]=3*(q-1)**2*q**3
        C[(3,3,1,1)]=3*(q-1)**2*q**4
        C[(3,3,2) if p==3 else (4,2,2)]=(q-1)**3*q**4
    return C

def main(q,exhaustive=True):
    p=2 if q==4 else q
    add,mul=mul_table(q);neg=[next(j for j in range(q) if add[i][j]==0) for i in range(q)]
    C=Counter()
    import random
    random.seed(0x5169+q)
    seq=product(range(q),repeat=7) if exhaustive else (tuple(random.randrange(q) for _ in range(7)) for _ in range(50000))
    for f in seq:
        j=partition(f,q,add,mul,neg)
        C[j]+=1
    P=predicted(q,p)
    if exhaustive:
        assert C==P,(q,C,P)
        print('EXHAUSTIVE PASS q=',q,'elements=',q**7,'strata=',sorted(C.items()))
    else:
        assert set(C).issubset(set(P)),(q,C,P)
        print('SAMPLED PASS q=',q,'sample size=50000','observed strata=',sorted(C))
if __name__=='__main__':
    for q in [2,3,4,5]:main(q,True)
    for q in [7,11]: main(q,False)
