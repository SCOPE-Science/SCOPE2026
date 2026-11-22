#!/usr/bin/env python3
"""Finite independent enumeration of parity-constrained ideal shattering."""
from itertools import product
from math import comb

def all_concepts(k, L, parity):
    masks=[]
    for t in product(range(L+1),repeat=k):
        if sum(t)%2 != parity: continue
        h=0
        for c,z in enumerate(t):
            for a in range(z): h |= 1 << (c*L+a)
        masks.append(h)
    return masks

def expected(k,L,p):
    z=[comb(k,j)*L**j for j in range(k+1)]
    m=0 if (L%2==0 and p==0) else (2**k if L%2==0 else 2**(k-1))
    z[-1]-=m
    return z

def profile(k,L,p):
    concepts=all_concepts(k,L,p)
    out=[0]*(k+1)
    faces={}
    for s in range(1<<(k*L)):
        n=s.bit_count()
        if n>k: continue
        if len({h & s for h in concepts})==1<<n:
            out[n]+=1
            faces.setdefault(n,[]).append(s)
    return out,faces

def rank(columns):
    piv={}
    for v in columns:
        while v:
            j=v.bit_length()-1
            if j in piv: v^=piv[j]
            else:
                piv[j]=v;break
    return len(piv)

def homology(k,L,p,faces):
    if k==1:
        return {0:len(faces.get(1,[]))-1} if faces.get(1) else {-1:1}
    # Independent row/column representation of the simplicial boundary.
    # Include empty face in dimension -1 to calculate reduced groups.
    boundary_rank={}
    for s in range(1,k+1):
        D=faces.get(s,[])
        R=faces.get(s-1,[])
        rid={v:i for i,v in enumerate(R)}
        cols=[]
        for facet in D:
            col=0;t=facet
            while t:
                q=t&-t;t-=q
                col^=1<<rid[facet^q]
            cols.append(col)
        boundary_rank[s]=rank(cols)
    b={}
    for s in range(1,k+1):
        value=len(faces.get(s,[]))-boundary_rank.get(s,0)-boundary_rank.get(s+1,0)
        if value:b[s-1]=value
    return {a:v for a,v in b.items() if v}

def topology_expected(k,L,p):
    m=0 if (L%2==0 and p==0) else (2**k if L%2==0 else 2**(k-1))
    if L==2 and p==1:
        return {k-2:2**k-1}
    b=(L-1)**k-m
    return {k-1:b} if b else {}

def run():
    case_count=0
    for L in (2,3,4,5):
      for k in (1,2,3):
       for parity in (0,1):
        got,faces=profile(k,L,parity)
        want=expected(k,L,parity)
        assert got==want,(L,k,parity,got,want)
        case_count+=1
        if L<=4:
            top=homology(k,L,parity,faces)
            want_h=topology_expected(k,L,parity)
            assert top==want_h,(L,k,parity,top,want_h)
            print(f"L={L} k={k} p={parity}: f={got} Betti_mod2={top}")
    print("PASS: %d exact shattering profiles; 18 independent boundary-rank checks."%case_count)
if __name__=="__main__":run()
