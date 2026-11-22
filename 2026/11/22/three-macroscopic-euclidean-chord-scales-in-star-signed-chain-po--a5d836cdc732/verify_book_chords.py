#!/usr/bin/env python3
"""Exact finite verification of Euclidean chord enumeration for anchored book-graph Lipschitz polytopes.
Only Python's standard library is used. Run: python3 verify_book_chords.py
"""
from itertools import product
from collections import Counter
from math import comb

def vertices(m):
    S=[]
    for leaves in product((-1,0),repeat=m): S.append((1,)+leaves)
    for leaves in product((0,1),repeat=m): S.append((-1,)+leaves)
    for leaves in product((-1,1),repeat=m): S.append((0,)+leaves)
    return S

def mul(p,q):
    d=Counter()
    for a,x in p.items():
        for b,y in q.items():d[a+b]+=x*y
    return d

def power(poly,m):
    out={0:1}
    for _ in range(m):out=mul(out,poly)
    return out

def formula(m):
    ans=Counter()
    for weight,poly,shift in [
        (1,{0:2,4:2},0),
        (2,{0:2,1:2},0),
        (4,{0:1,1:2,4:1},1),
        (2,{0:1,1:2,4:1},4)]:
        for k,n in power(poly,m).items():ans[k+shift]+=weight*n
    return ans

def check():
    total=0
    for m in range(1,9):
        vv=vertices(m)
        assert len(vv)==3*2**m==len(set(vv))
        got=Counter()
        for a in vv:
            for b in vv:
                got[sum((x-y)**2 for x,y in zip(a,b))]+=1
        exp=formula(m)
        assert got==exp,(m,got-exp,exp-got)
        assert got[0]==3*2**m
        assert max(got)==4*(m+1)
        assert got[4*m+4]==2
        assert got[4*m+1]==4*m+4
        total+=len(vv)**2
    for m in range(1,101):
        exp=formula(m)
        assert sum(exp.values())==9*4**m
        assert exp[0]==3*2**m
        assert exp[4*m+4]==2
    print('BOOK_CHORD_SPECTRUM_PASS ordered_pair_tests=',total,'symbolic_dimensions=100')

if __name__=='__main__':check()
