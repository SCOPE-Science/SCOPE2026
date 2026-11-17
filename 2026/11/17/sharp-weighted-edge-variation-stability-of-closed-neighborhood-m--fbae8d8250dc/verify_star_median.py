#!/usr/bin/env python3
"""Exact rational diagnostics for closed-neighborhood median variation on stars.

A median of an even-length list means the arithmetic mean of the two
central order statistics. This is a self-contained finite diagnostic;
the general theorem follows from its separate analytical proof.
"""
from fractions import Fraction as Q
from itertools import permutations
from random import Random


def median(values):
    s=sorted(values)
    m=len(s)//2
    return s[m] if len(s)%2 else (s[m-1]+s[m])/2


def filt(x):
    return [median(x)] + [(x[0]+v)/2 for v in x[1:]]


def variation(x, weights):
    return sum((w*abs(x[i+1]-x[0]) for i,w in enumerate(weights)), Q(0))


def claimed(k,weights):
    if k==1: return Q(0)
    total=sum(weights,Q(0))
    least=min(weights)
    return total/least-Q(1,2) if k%2==0 else (total-least)/(2*least)


def witness(k,j):
    if k==1: return [Q(0),Q(1)]
    x=[Q(0)]*(k+1)
    remain=[i for i in range(1,k+1) if i!=j]
    if k%2==0:
        m=k//2
        for i in remain[:m-1]:x[i]=Q(-2)
        for i in remain[m-1:]:x[i]=Q(3)
    else:
        m=(k-1)//2
        for i in remain[:m-1]:x[i]=Q(-2)
        x[remain[m-1]]=Q(2)
        for i in remain[m:]:x[i]=Q(3)
    x[j]=Q(1)
    return x


def pair_ratio(x,y,weights):
    diff=[a-b for a,b in zip(y,x)]
    den=variation(diff,weights)
    assert den>0
    fx,fy=filt(x),filt(y)
    numerator=variation([b-a for a,b in zip(fx,fy)],weights)
    return numerator/den


def jacobian_from_order(order,k,weights):
    # order is a permutation of 0..k by ascending data rank;
    # the center output is the median (one or midpoint of two indices)
    m=(k+1)//2
    central=[order[m]] if (k+1)%2 else [order[m-1],order[m]]
    coeff=[Q(central.count(j),len(central)) for j in range(1,k+1)]
    total=sum(weights)
    norm=max(sum(weights[i]*abs((Q(1,2) if i==j else Q(0))-coeff[j]) for i in range(k))/weights[j]
             for j in range(k))
    return norm


def run():
    rng=Random(20261109)
    perms=0
    for k in range(1,8):
        ws=([Q(1)]*k,[Q(2*i+1) for i in range(k)],
            [Q(rng.randint(1,21)) for _ in range(k)])
        for w in ws:
            limit=claimed(k,w)
            if k<=6:
                localmax=max(jacobian_from_order(p,k,w) for p in permutations(range(k+1)))
                perms+=(k+1) if False else __import__('math').factorial(k+1)
                assert localmax==limit,(k,w,localmax,limit)
            j=min(range(1,k+1),key=lambda i:w[i-1])
            x=witness(k,j)
            y=x[:]
            y[j]+=Q(1,17)
            if k>=2:
                assert pair_ratio(x,y,w)==limit,(k,w,x,y,pair_ratio(x,y,w),limit)
            else:
                assert pair_ratio(x,y,w)==Q(0)
    print('EXHAUSTIVE_STRICT_ORDER_JACOBIAN_COMPARISONS_PASSED',perms)
    witnesses=0
    tests=0
    for k in range(1,31):
        for seed in range(6):
            w=[Q(1+(i*7+seed*11)%29) for i in range(k)]
            j=min(range(1,k+1),key=lambda i:w[i-1])
            x=witness(k,j)
            y=x[:]
            y[j]+=Q(1,101)
            if k==1:
                assert pair_ratio(x,y,w)==0
            else:
                assert pair_ratio(x,y,w)==claimed(k,w)
            witnesses+=1
        for test in range(170):
            w=[Q(rng.randint(1,13)) for _ in range(k)]
            x=[Q(rng.randint(-20,20)) for _ in range(k+1)]
            y=[Q(rng.randint(-20,20)) for _ in range(k+1)]
            if variation([a-b for a,b in zip(x,y)],w)==0:
                continue
            assert pair_ratio(x,y,w)<=claimed(k,w),(k,w,x,y)
            tests+=1
    print('EXACT_WEIGHTED_PAIR_WITNESSES_PASSED',witnesses)
    print('EXACT_ARBITRARY_TWO_INPUT_CHECKS_PASSED',tests)
    # Nonexpansivity characterizes the edge-weight structure, exactly.
    for k in range(1,21):
        equal=[Q(1)]*k
        got=claimed(k,equal)<=1
        assert got==(k in (1,3))
    print('EXACT_NONEXPANSIVITY_CLASSIFICATION_PASSED')
    print('ALL_STAR_CLOSED_NEIGHBORHOOD_MEDIAN_CHECKS_PASSED')

if __name__=='__main__':
    run()
