"""Exact small-order verification for left-spine and leaf dependence in random BSTs.

Run: python verify.py  (Python standard library only).

All finite exhaustive comparisons use rational arithmetic. Infinite-order
claims in the accompanying argument rely on their symbolic proofs, not this test.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial

def formula(n,j):
    if j == 1: return Q(1,4)
    if j == n: return -Q(1,2*n*(n-1))
    return -Q(2,3*j*(j-1)*(j+1))

def total(n): return Q((n-2)*(n+1),12*n*(n-1))

def cond_two(n):
    assert n >= 3
    h=sum((Q(1,i) for i in range(1,n)),Q(0))
    extra=Q(5*n*n-15*n+12,6*(n-2)*(n-1))/h
    return Q(n,3)+extra

checks=0
for n in range(2,9):
    counts=[0]*(n+1)
    sums=[0]*(n+1)
    key_leaf_sums=[0]*n; key_mixed_sums=[0]*n
    sumt=suml=sumtl=0
    for priority_order in permutations(range(n)):
        time=[0]*n
        for k, key in enumerate(priority_order):time[key]=k
        rec=0;last=n+1
        for key,t in enumerate(time):
            if t < last:rec+=1;last=t
        leaves=[int((i==0 or time[i]>time[i-1]) and
                    (i==n-1 or time[i]>time[i+1])) for i in range(n)]
        leaf_count=sum(leaves)
        counts[rec]+=1
        sums[rec]+=leaf_count
        sumt+=rec;suml+=leaf_count;sumtl+=rec*leaf_count
        for j,leaf in enumerate(leaves,1):
            key_leaf_sums[j-1]+=leaf
            key_mixed_sums[j-1]+=rec*leaf
    den=factorial(n)
    cov=Q(sumtl,den)-Q(sumt,den)*Q(suml,den)
    assert cov==total(n),(n,cov,total(n));checks+=1
    for j in range(1,n+1):
        value=Q(key_mixed_sums[j-1],den)-Q(sumt,den)*Q(key_leaf_sums[j-1],den)
        assert value==formula(n,j),(n,j,value,formula(n,j))
        checks+=1
    if n>=3:
        assert Q(sums[1],counts[1])==Q(n,3);checks+=1
        assert Q(sums[2],counts[2])==cond_two(n);checks+=1
        assert Q(sums[n],counts[n])==1;checks+=1
        assert Q(sums[2],counts[2])>Q(sums[1],counts[1]);checks+=1
        assert Q(sums[2],counts[2])>Q(sums[n],counts[n]);checks+=1

for n in range(2,1001):
    assert sum((formula(n,j) for j in range(1,n+1)),Q(0))==total(n)
    checks+=1
for n in range(3,1001):
    h=sum((Q(1,i) for i in range(1,n)),Q(0))
    delta=cond_two(n)-Q(n,3)
    assert delta==Q(5*n*n-15*n+12,6*(n-2)*(n-1))/h and delta>0
    checks+=1
print(f'PASS: {checks} exact rational comparisons; exhaustive permutations through n=8')
