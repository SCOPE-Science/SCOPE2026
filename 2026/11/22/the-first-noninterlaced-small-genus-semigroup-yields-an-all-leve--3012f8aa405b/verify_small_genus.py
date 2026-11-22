#!/usr/bin/env python3
"""Exact finite reduction for the small-genus binomid theorem."""
from itertools import product

def gap_sets():
    result=[]
    for bits in product((0,1),repeat=5):
        S={0}|{i for i in range(1,6) if bits[i-1]}
        gap=tuple(i for i in range(1,6) if i not in S)
        if len(gap)>3:
            continue
        if all((a+b) in S or (a+b)>=6 for a in S for b in S):
            result.append(gap)
    return sorted(result,key=lambda x:(len(x),x))

wanted=[(),(1,),(1,2),(1,3),(1,2,3),(1,2,4),(1,2,5),(1,3,5)]
assert gap_sets()==wanted
checks=0
for gaps in wanted:
    def G(n):
        return sum(z<=n for z in gaps)
    for m in range(1,6):
        def e(j):
            return G(m)+G(j)-G(m+j)
        assert all(0<=e(j)<=G(m) for j in range(12))
        assert all(e(j)==G(m) for j in range(6,12))
        for L in range(1,6):
            for s in range(6):
                assert sum(e(j) for j in range(L)) <= sum(e(j) for j in range(s,s+L)), (gaps,m,L,s)
                checks+=1
    S={0}|(set(range(1,6))-set(gaps))
    bad=[n for n in S if n>=1 and n+2<6 and n+2 not in S]
    assert bool(bad)==(gaps==(1,2,5))
print('PASS:',len(wanted),'complete genus<=3 gap sets;',checks,'finite interval checks; unique noninterlaced gap set (1,2,5).')
