#!/usr/bin/env python3
"""Exhaustive exact and recurrence checks: uniform recursive-tree degrees and rooted subtree sizes."""
from itertools import product
from fractions import Fraction

def predicted(n,i,j):
    if i < j:
        return Fraction(-(n-j),j*j)
    if i==j:
        return Fraction((n-j)*(j-1),j*j)
    return Fraction(0)

def verify():
    checks=0
    for n in range(2,10):
        total=0
        sd=[0]*(n+1); ss=[0]*(n+1)
        ds=[[0]*(n+1) for _ in range(n+1)]
        for choices in product(*(range(1,k) for k in range(2,n+1))):
            par=[0,0]+list(choices)
            d=[0]*(n+1);s=[1]*(n+1)
            for child in range(2,n+1):d[par[child]]+=1
            for child in range(n,1,-1):s[par[child]]+=s[child]
            total+=1
            for i in range(1,n+1):
                sd[i]+=d[i];ss[i]+=s[i]
                for j in range(1,n+1):ds[i][j]+=d[i]*s[j]
        for i in range(1,n+1):
            assert Fraction(sd[i],total)==sum((Fraction(1,t) for t in range(i,n)),Fraction(0)),(n,i,'degree')
            for j in range(1,n+1):
                actual=Fraction(ds[i][j],total)-Fraction(sd[i]*ss[j],total*total)
                assert actual==predicted(n,i,j),(n,i,j,actual,predicted(n,i,j))
                checks+=1
        for j in range(1,n+1):
            assert sum((predicted(n,i,j) for i in range(1,n+1)),Fraction(0))==0
            checks+=1
    for n in range(2,110):
        for j in range(1,n+1):
            # variance/mean conservation of total number of edges
            assert sum((predicted(n,i,j) for i in range(1,n+1)),Fraction(0)) == 0
            checks+=1
    print('PASS',checks,'exact checks; all recursive trees with <=9 nodes enumerated')
if __name__=='__main__':verify()
