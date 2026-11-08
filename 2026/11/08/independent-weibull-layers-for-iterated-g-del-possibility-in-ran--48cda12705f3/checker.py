#!/usr/bin/env python3
"""Finite deterministic checks for rooted max-min iterated fuzzy diamonds."""
from itertools import product
from fractions import Fraction
from math import factorial
import random

def diamond_step(R,p):
    n=len(R)
    return [max(min(R[i][j],p[j]) for j in range(n)) for i in range(n)]

def as_walk_maxmin(R,p,root,depth):
    n=len(R)
    best=0
    for seq in product(range(n), repeat=depth):
        cur=root; v=p[seq[-1]]
        for nxt in seq:
            v=min(v,R[cur][nxt]);cur=nxt
        best=max(best,v)
    return best

def check_semantics():
    checked=0
    for n in (1,2,3):
        for bits in product((0,1), repeat=n*n+n):
            R=[list(bits[i*n:(i+1)*n]) for i in range(n)]
            p=list(bits[n*n:]); cur=p
            for d in range(1,5):
                cur=diamond_step(R,cur)
                for root in range(n):
                    assert cur[root]==as_walk_maxmin(R,p,root,d), (n, d, root, R, p)
                    checked+=1
    for n in (2,3,4):
        rng=random.Random(13415+n)
        for j in range(25):
            R=[[rng.random() for _ in range(n)] for _ in range(n)]
            p=[rng.random() for _ in range(n)]; cur=p
            for d in range(1,5):
                cur=diamond_step(R,cur)
                for root in range(n):
                    assert abs(cur[root]-as_walk_maxmin(R,p,root,d))<1e-14
                    checked+=1
    return checked

def all_second_paths(a,b):
    # root is 0; first rooted path is (0,1,...,a).
    # Second path visits distinct nonroot vertices chosen among first a
    # and new canonical labels a+1, a+2,... as introduced.
    def rec(seq,used,new_max):
        if len(seq)==b:
            yield (0,)+tuple(seq);return
        for v in range(1,a+1):
            if v not in used:
                yield from rec(seq+[v],used|{v},new_max)
        v=new_max+1
        yield from rec(seq+[v],used|{v},v)
    yield from rec([],set(),a)

def check_overlap(K=5):
    cases=0; dependent=0; worst=Fraction(-10,1); worst_case=None
    for a in range(1,K+1):
        P=tuple(range(a+1)); p_edges=set(zip(P[:-1],P[1:]));p_nonroot=set(P[1:])
        for b in range(a,K+1):
            for Q in all_second_paths(a,b):
                if a==b and Q==P: continue
                q_edges=set(zip(Q[:-1],Q[1:]))
                h=len(p_edges&q_edges)+int(P[-1]==Q[-1])
                cases+=1
                if h==0: continue
                dependent+=1
                v=len(p_nonroot&set(Q[1:]))
                assert 1<=h<=v, (a,b,P,Q,h,v)
                exponent=Fraction(a*h,a+1)-v
                assert exponent<=-Fraction(1,K+1), (a,b,P,Q,exponent)
                if exponent>worst:worst=exponent;worst_case=(a,b,P,Q,h,v)
    return cases, dependent, str(worst), worst_case

if __name__=='__main__':
    print('SEMANTIC_WALK_CHECKS',check_semantics())
    a,b,c,d=check_overlap()
    print('DISTINCT_PATH_OVERLAP_CHECKS',a,'DEPENDENT',b,'MAX_EXPONENT',c, 'MAX_CASE',d)
    print('ROOTED_GODEL_DIAMOND_CHECKS_OK')
