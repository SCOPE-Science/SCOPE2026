#!/usr/bin/env python3
"""Independent integer checks for the crown-poset support-enumerator formulas.
Run with Python 3.9 or newer: python verify.py
The unrestricted result follows from the proof, not from these finite checks.
"""
from itertools import combinations, product
from math import comb


def cycle_matching_formula(m):
    return [1] + [2*m*comb(2*m-j-1,j-1)//j for j in range(1,m+1)]


def matching_support_counts(m):
    # The comparability graph is the 2m-cycle with edges a_i-b_i, a_i-b_(i+1).
    neigh = [(1<<i)|(1<<((i+1)%m)) for i in range(m)]
    out = [0]*(m+1)
    for j in range(m+1):
        for A in combinations(range(m),j):
            for B in combinations(range(m),j):
                bmask=sum(1<<b for b in B)
                states={0}
                for a in A:
                    states={mask | (1<<b) for mask in states
                            for b in B if not (mask & (1<<b))
                            and (neigh[a] & (1<<b))}
                if bmask in states:
                    out[j]+=1
    return out


def gamma_formula(m):
    vals=cycle_matching_formula(m)
    vals[m]-=1
    return vals


def h_from_gamma(m,gamma):
    n=2*m
    return [sum(gamma[j]*comb(n-2*j,k-j)
                for j in range(m+1) if j<=k<=n-j)
            for k in range(n+1)]


def ideals(m):
    # a_i < b_i and a_i < b_(i+1) (mod m).
    result=[]
    for lower in range(1<<m):
        for upper in range(1<<m):
            if all(not (upper>>j&1) or
                   ((lower>>j&1) and (lower>>((j-1)%m)&1))
                   for j in range(m)):
                result.append((lower,upper,lower.bit_count()+upper.bit_count()))
    return result


def direct_h(m):
    bound=ideals(m)
    out=[0]*(2*m+1)
    # x_a <=1; every upper b has two lowers below, so x_b<=3.
    for lows in product(range(2),repeat=m):
        for ups in product(range(4),repeat=m):
            if all(sum(lows[i] for i in range(m) if (low>>i&1))+
                   sum(ups[i] for i in range(m) if (up>>i&1))<=size
                   for low,up,size in bound):
                out[sum(v>0 for v in lows)+sum(v>0 for v in ups)]+=1
    return out


def trace_matching(m):
    # trace of [[1,q],[1,0]]^(2m), via Lucas recurrence
    a,b=[2],[1]
    for n in range(2,2*m+1):
        nxt=[0]*max(len(b),len(a)+1)
        for k,v in enumerate(b): nxt[k]+=v
        for k,v in enumerate(a): nxt[k+1]+=v
        a,b=b,nxt
    return b


for m in range(3,9):
    actual=matching_support_counts(m)
    expected=gamma_formula(m)
    assert actual==expected, (m,actual,expected)
    assert trace_matching(m)==cycle_matching_formula(m)
    print('MATCHING_SUPPORT',m,'gamma',expected,'PASS')

for m in range(3,6):
    direct=direct_h(m)
    reconstructed=h_from_gamma(m,gamma_formula(m))
    assert direct==reconstructed,(m,direct,reconstructed)
    assert direct==direct[::-1]
    print('DIRECT_LATTICE',m,'lattice_points',sum(direct),'H',direct,'PASS')

for m in range(3,51):
    assert trace_matching(m)==cycle_matching_formula(m)
    g=gamma_formula(m)
    assert g[-1]==1
    h=h_from_gamma(m,g)
    assert h==h[::-1] and h[-1]==1
print('TRANSFER_AND_GAMMA_CROSSCHECK m=3..50 PASS')
print('VERIFY_OK')
