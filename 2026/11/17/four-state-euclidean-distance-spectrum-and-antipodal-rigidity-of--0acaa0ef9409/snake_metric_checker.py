#!/usr/bin/env python3
"""Exact Euclidean squared-distance polynomial for linked type-C snake-interval polytopes.
Runs independently with Python 3 only. No external data.
"""
from collections import defaultdict
from math import ceil

STATES=tuple((i,j) for i in (0,1) for j in (0,1))

def feasible(n,mask):
    demands=[sum((mask>>j)&1 for j in range(i,n)) for i in range(n)]
    return [u for u in range(1<<n) if all(demands[i]<= (u>>i).bit_count()<=demands[i]+1 for i in range(n))]

def transfer_polynomial(n,mask):
    # R is a column of four coefficient vectors indexed by y_i,y'_i.
    R=[{} for _ in STATES]
    R[0]={0:1}
    for i in range(n-1,-1,-1):
        s=(mask>>i)&1
        T=[]
        for a,b in STATES:
            v=defaultdict(int)
            for j,(c,d) in enumerate(STATES):
                if ((a>=c and b>=d) if s==0 else (a<=c and b<=d)):
                    diff=abs((a-b)-(c-d))
                    assert diff<=1
                    for k,count in R[j].items():
                        v[k+diff]+=count
            T.append(dict(v))
        R=T
    out=defaultdict(int)
    for poly in R:
        for d,ct in poly.items():out[d]+=ct
    return dict(out)

def full_criteria(n,mask):
    # Each complete two-coordinate block from the right has one member in S.
    for i in range(n-2,0,-2):
        if ((mask>>(i-1))&3).bit_count()!=1:
            return False
    return True

def verify(nmax=11):
    configs=0; pairs=0; full=0
    for n in range(2,nmax+1):
        expected_num=2**(n//2)
        expected_pairs=2**(ceil(n/2)-1)
        got_num=0
        for mask in range(1<<(n-1)):
            vertices=feasible(n,mask)
            obs=defaultdict(int)
            for u in vertices:
                for v in vertices:
                    obs[(u^v).bit_count()]+=1
            ex=transfer_polynomial(n,mask)
            assert ex==dict(obs),(n,mask,ex,dict(obs))
            assert sum(ex.values())==len(vertices)**2
            assert (ex.get(n,0)>0) == full_criteria(n,mask), (n,mask,ex.get(n,0))
            if full_criteria(n,mask):
                got_num+=1
                assert ex[n]==2*expected_pairs,(n,mask,ex[n],expected_pairs)
            configs+=1; pairs+=len(vertices)**2
        assert got_num==expected_num,(n,got_num,expected_num)
        full+=got_num
    print(f'TYPE_C_SNAKE_METRIC_PASS n=2..{nmax} profiles={configs} ordered_pairs={pairs} full_diameter_profiles={full}')

if __name__=='__main__': verify()
