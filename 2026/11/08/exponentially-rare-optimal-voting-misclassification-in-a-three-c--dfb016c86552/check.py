#!/usr/bin/env python3
"""Finite reproduction checks for the three-class flip-game misclassification bound."""
from itertools import combinations, product
from collections import Counter
from math import comb
from random import Random


def actual(a,b,c):
    w=20*a+15*b+12*c
    return w==59 or w>=61


def classifier(a,b,c):
    return 2*(22*a+15*b+12*c)>=121


def certificate():
    # Labels (class,index), index 0,1,2,3,4.
    W=[]
    for t in range(60):
        i=t%5
        W.append(frozenset([(0,i),(1,i),(2,i),(2,(i+1)%5)]))
    L=[]
    for trio in combinations(range(5),3):
        L.extend([frozenset((0,i) for i in trio)]*2)
    for quad in combinations(range(5),4):
        L.extend([frozenset((1,i) for i in quad)]*3)
    L.extend([frozenset((2,i) for i in range(5))]*24)
    assert len(W)==60 and len(L)==59
    assert Counter(x for s in W for x in s)==Counter(x for s in L for x in s)
    for x in W:
        a,b,c=(sum(j==i for j,k in x) for i in range(3))
        assert (a,b,c)==(1,1,2) and actual(a,b,c)
    for x in L:
        a,b,c=(sum(j==i for j,k in x) for i in range(3))
        assert (a,b,c) in ((3,0,0),(0,4,0),(0,0,5)) and not actual(a,b,c)
    return W,L


def check_profiles():
    checks=0
    for a in range(6):
        for b in range(6-a):
            for c in range(6-a-b):
                assert (actual(a,b,c)!=classifier(a,b,c))==((a,b,c)==(3,0,0)),(a,b,c)
                checks+=1
    assert checks==56
    assert 6*12>60.5
    return checks


def check_profile_census():
    checks=0
    for m in range(5,61):
        errors=0
        for a,b,c in product(range(m+1),repeat=3):
            if actual(a,b,c)!=classifier(a,b,c):
                errors+=comb(m,a)*comb(m,b)*comb(m,c)
            checks+=1
        assert errors==comb(m,3),(m,errors)
        if m>=9:
            MW=m*m*comb(m,2)
            C3,C4,C5=comb(m,3),comb(m,4),comb(m,5)
            assert 60/MW<=20/C3
            assert 15/C4<=20/C3
            assert 24/C5<=20/C3
            assert min(MW,C3,C4,C5)==C3
    return checks


def check_full_coalitions():
    checked=0
    for m in (5,6):
        errors=0
        for mask in range(1<<(3*m)):
            a=(mask & ((1<<m)-1)).bit_count()
            b=((mask>>m)&((1<<m)-1)).bit_count()
            c=((mask>>(2*m))&((1<<m)-1)).bit_count()
            errors+=(actual(a,b,c)!=classifier(a,b,c))
            checked+=1
        assert errors==comb(m,3)
    return checked


def check_injections(W,L):
    rng=Random(271828)
    checked=0
    for m in (5,9,13):
        for _ in range(100):
            injections=[rng.sample(range(m),5) for _ in range(3)]
            X=[[rng.randrange(80) for i in range(m)] for k in range(3)]
            q=rng.randrange(1,160)
            def score(S):
                return sum(X[j][injections[j][i]] for j,i in S)
            # In every injection the weighted total on each side is identical.
            assert sum(map(score,W))==sum(map(score,L))
            # If all winning coalitions passed, at least one losing coalition must fail.
            assert not (all(score(S)>=q for S in W) and all(score(S)<q for S in L))
            checked+=1
    return checked

if __name__=='__main__':
    W,L=certificate()
    print('certificate occurrences:',len(W),len(L),'with exact incidence balance')
    print('five-good-or-smaller profiles:',check_profiles())
    print('profile census evaluations:',check_profile_census())
    print('complete coalition evaluations:',check_full_coalitions())
    print('random injected trade certificates:',check_injections(W,L))
    print('ALL CHECKS PASS')
