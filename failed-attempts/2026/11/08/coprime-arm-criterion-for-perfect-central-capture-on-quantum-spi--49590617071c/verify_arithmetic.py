#!/usr/bin/env python3
"""Exact adjacency-walk rank versus divisor-count protection on spider networks."""
from itertools import product
from math import gcd
from functools import reduce
import sympy as sp

def totient(n):
    return sum(gcd(k,n)==1 for k in range(1,n+1))

def formula(L):
    return sum(totient(b)*max(sum(x%b==0 for x in L)-1,0) for b in range(2,max(L)+1))

def build(L):
    count=1+sum(x-1 for x in L)
    h=sp.zeros(count)
    ix=1
    for length in L:
        old=0
        for v in range(1,length):
            h[old,ix]=h[ix,old]=1
            old=ix
            ix+=1
    return h

def walk_rank(H):
    n=H.rows; x=sp.eye(n)[:,0]; pieces=[]
    for j in range(n):
        pieces.append(x)
        x=H*x
    return sp.Matrix.hstack(*pieces).rank()

cases=0
for q in (3,4):
    ranges=[(2,3,4,5)]*q if q==3 else [(2,3,4)]*q
    for L in product(*ranges):
        H=build(L)
        expected=formula(L)
        got=H.rows-walk_rank(H)
        assert expected==got, (L,expected,got)
        # full capture iff denominators are pairwise coprime
        coprime=all(gcd(L[i],L[j])==1 for i in range(q) for j in range(i))
        assert (expected==0)==coprime
        cases+=1
print('PASS exact integer walk ranks / divisor dimension / pairwise coprime criterion:',cases,'spider graphs')
