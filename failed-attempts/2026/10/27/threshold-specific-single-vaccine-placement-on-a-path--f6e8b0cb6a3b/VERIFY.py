#!/usr/bin/env python3
"""Exact finite checks for path-vaccination outbreak tail optimizers.

All probabilities are rational; enumeration is independent of the closed forms.
The universal statements require the accompanying analytical proof.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product

@lru_cache(None)
def enumerate_weighted_counts(m, p):
    """Dictionary size -> sum of source-weighted cluster probabilities in a path."""
    assert m >= 0
    if m == 0:
        return {}
    result = {j: Fraction(0) for j in range(1, m+1)}
    for bonds in product((0,1), repeat=m-1):
        q = p**sum(bonds) * (1-p)**(m-1-sum(bonds))
        lengths = []
        run = 1
        for edge in bonds:
            if edge:
                run += 1
            else:
                lengths.append(run)
                run = 1
        lengths.append(run)
        for run in lengths:
            result[run] += run*q
    assert sum(result.values()) == m
    return result

def exact_tail_weight(m, threshold, p):
    if m < threshold:
        return Fraction(0)
    if threshold == 1:
        return Fraction(m)
    return p**(threshold-1)*(threshold+(m-threshold)*(threshold-(threshold-1)*p))

def exact_mean_weight(m,p):
    return m + 2*sum((m-j)*p**j for j in range(1,m))

def optimum_tail_splits(M, threshold):
    if threshold == 1 or threshold > M:
        return set(range(M+1))
    if M >= 2*threshold-1:
        return {threshold-1, M-threshold+1}
    return set(range(M-threshold+1, threshold))

checks=0
probs=[Fraction(1,4), Fraction(1,2), Fraction(3,4)]
for p in probs:
    for m in range(11):
        counts = enumerate_weighted_counts(m,p)
        for s in range(1,m+3):
            enumerated=sum(weight for size,weight in counts.items() if size>=s)
            assert enumerated == exact_tail_weight(m,s,p), (m,s,p,enumerated,exact_tail_weight(m,s,p))
            checks+=1
        enumerated_mean=sum(size*weight for size,weight in counts.items())
        assert enumerated_mean == exact_mean_weight(m,p)
        checks+=1
    for M in range(2,11):
        means={a: exact_mean_weight(a,p)+exact_mean_weight(M-a,p) for a in range(M+1)}
        min_mean=min(means.values())
        assert {a for a,v in means.items() if v==min_mean} == {M//2,(M+1)//2}
        checks+=1
        for s in range(1,M+3):
            risk={a: exact_tail_weight(a,s,p)+exact_tail_weight(M-a,s,p) for a in range(M+1)}
            min_risk=min(risk.values())
            expected=optimum_tail_splits(M,s)
            actual={a for a,v in risk.items() if v==min_risk}
            assert actual == expected, (M,s,p,actual,expected)
            checks+=1
        if M>=4:
            risk_center=exact_tail_weight(M//2,2,p)+exact_tail_weight(M-M//2,2,p)
            risk_near=exact_tail_weight(1,2,p)+exact_tail_weight(M-1,2,p)
            assert risk_center-risk_near == p**2
            checks+=1

p=Fraction(1,2)
M=4
mean_mid=(exact_mean_weight(2,p)+exact_mean_weight(2,p))/M
mean_near=(exact_mean_weight(1,p)+exact_mean_weight(3,p))/M
risk2_mid=(exact_tail_weight(2,2,p)+exact_tail_weight(2,2,p))/M
risk2_near=(exact_tail_weight(1,2,p)+exact_tail_weight(3,2,p))/M
risk3_mid=(exact_tail_weight(2,3,p)+exact_tail_weight(2,3,p))/M
risk3_near=(exact_tail_weight(1,3,p)+exact_tail_weight(3,3,p))/M
assert (mean_mid,mean_near,risk2_mid,risk2_near,risk3_mid,risk3_near)==(Fraction(3,2),Fraction(13,8),Fraction(1,2),Fraction(7,16),Fraction(0),Fraction(3,16))
checks+=1
print('VERIFICATION_OK', checks, 'exact-rational assertions')
print('P5 example mean',mean_mid,mean_near,'tail2',risk2_mid,risk2_near,'tail3',risk3_mid,risk3_near)
