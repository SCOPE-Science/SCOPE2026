#!/usr/bin/env python3
"""Exact finite-field verification of triangular evolution-algebra idempotent counts."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb

POLY={2:0b11,4:0b111,8:0b1011}

def mult(a,b,q):
    p=POLY[q];v=0
    while b:
        if b&1:v^=a
        b>>=1;a<<=1
        if a&q:a^=p
    return v

def distribution(n):
    p={1:Fraction(1)}
    for _ in range(1,n):
        new={}
        for d,w in p.items():
            new[d]=new.get(d,Fraction(0))+w*(1-Fraction(1,2**d))
            new[d+1]=new.get(d+1,Fraction(0))+w*Fraction(1,2**d)
        p=new
    return {2**d-1:w for d,w in sorted(p.items())}

def run(n,q):
    positions=[(i,j) for j in range(n) for i in range(j+1)]
    diagonal=[k for k,(i,j) in enumerate(positions) if i==j]
    fields=[tuple(range(1,q)) if i in diagonal else tuple(range(q)) for i in range(len(positions))]
    vectors=list(product(range(q),repeat=n))
    tally=Counter()
    total=0
    for vals in product(*fields):
        mat=[[0]*n for _ in range(n)]
        for (i,j),val in zip(positions,vals):mat[j][i]=val
        hits=0
        for x in vectors:
            if all(x[j]==sum_mult(mat[j],x,j,q) for j in range(n)):
                hits+=1
        tally[hits-1]+=1
        total+=1
    predicted=distribution(n)
    observed={k:Fraction(v,total) for k,v in sorted(tally.items())}
    assert observed==predicted,(n,q,observed,predicted)
    mean=sum(k*v for k,v in observed.items())
    var=sum((k-mean)**2*v for k,v in observed.items())
    assert mean==n and var==comb(n,2),(n,q,mean,var)
    assert total==(q-1)**n*q**(n*(n-1)//2)
    print(f'PASS q={q} n={n} matrices={total} vectors_per_matrix={q**n} distribution='+str({k:int(v) for k,v in sorted(tally.items())})+f' mean={mean} variance={var}')
    return total

def sum_mult(row,x,j,q):
    s=0
    for i in range(j+1):s^=mult(row[i],mult(x[i],x[i],q),q)
    return s

def main():
    cases=[(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(1,4),(2,4),(3,4),(1,8),(2,8)]
    ct=0
    for n,q in cases:ct+=run(n,q)
    print('VERIFY_OK cases=',len(cases),'total_matrices=',ct)
if __name__=='__main__':main()
