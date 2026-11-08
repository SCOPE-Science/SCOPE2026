#!/usr/bin/env python3
"""Finite-plane two-line trace checks; self-contained and deterministic.

Singer cyclic difference sets define PG(2,q) for q in 2,3,4,5.
This checks the finite examples only, not the universal incidence proof.
"""
from collections import Counter
from itertools import combinations
from math import comb
from random import Random

DIFFERENCE_SETS = {
    2: (0, 1, 3),
    3: (0, 1, 3, 9),
    4: (0, 1, 4, 14, 16),
    5: (0, 1, 3, 8, 12, 18),
}


def data(q):
    n = q*q + q + 1
    D = DIFFERENCE_SETS[q]
    assert len(D) == q + 1
    differences = [(a-b)%n for a in D for b in D if a != b]
    assert sorted(differences) == list(range(1, n))
    lines = tuple(sum(1<<((a+i)%n) for a in D) for i in range(n))
    assert len(set(lines)) == n
    assert all(L.bit_count() == q+1 for L in lines)
    for p in range(n):
        assert sum(bool(L & (1<<p)) for L in lines) == q+1
    concepts = tuple(set(A|B for A in lines for B in lines))
    assert len(concepts) == n + comb(n,2)
    return lines, concepts


def expected_coefficient(q,k):
    v = q*q+q+1
    if k == 0: return 1
    if k == 1: return v
    if k == 2: return comb(v,2)
    if k == 3: return comb(v,3) - (v if q==2 else 0)
    if k == 4: return 0 if q==2 else comb(v,4)-v*comb(q+1,4)
    if k == 5:
        if q==2: return 0
        B = v*comb(q+1,2)*comb(q,2)**2
        if q==3: return B
        return v*comb(q+1,3)*comb(q*q,2)-B
    return 0


def structurally_shattered(q,k,t,has_four):
    if k<=2: return True
    if k==3: return q>=3 or t==0
    if k==4: return q>=3 and not has_four
    if k==5: return (q==3 and t==2) or (q>=4 and t in (1,2))
    return False


def check(q):
    lines,concepts=data(q)
    n=q*q+q+1
    total=0
    for k in range(0,7):
        if q==5 and k==6:
            rng=Random(20261102)
            supports=[tuple(sorted(rng.sample(range(n),k))) for _ in range(350)]
            mode='sampled'
        else:
            supports=combinations(range(n),k)
            mode='exhaustive'
        count=0; classes=Counter(); examined=0
        for S in supports:
            examined+=1
            mask=sum(1<<p for p in S)
            t=sum((L&mask).bit_count()==3 for L in lines)
            has_four=any((L&mask).bit_count()>=4 for L in lines)
            expected=structurally_shattered(q,k,t,has_four)
            traces={C&mask for C in concepts}
            actual=(len(traces)==1<<k)
            if actual!=expected:
                raise AssertionError(('structural discrepancy',q,k,S,actual,expected,t))
            if actual:
                count+=1
                if k==5: classes[t]+=1
        if mode=='exhaustive':
            pred=expected_coefficient(q,k)
            assert count==pred,(q,k,count,pred)
        print('q=%d k=%d mode=%s checked=%d shattered=%d triple_types=%s' % (
            q,k,mode,examined,count,dict(sorted(classes.items()))),flush=True)
        total+=examined
    print('ORDER_PASS q=%d total_supports=%d' % (q,total),flush=True)
    return total

if __name__=='__main__':
    cumulative=sum(check(q) for q in DIFFERENCE_SETS)
    print('ALL_TWO_LINE_PROJECTIVE_SHATTERING_CHECKS_PASS supports=%d' % cumulative,flush=True)
