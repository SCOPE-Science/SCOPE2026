#!/usr/bin/env python3
"""Reproducible finite checks for heterogeneous Dirichlet join limits.

Standard-library only. These are diagnostics, not a substitute for the proof.
"""
from math import comb, gamma, isclose
from itertools import combinations
from fractions import Fraction
from random import Random
from collections import Counter

N_CHECKS = 0

def check(statement, detail=''):
    global N_CHECKS
    assert statement, detail
    N_CHECKS += 1

def coefficients(alpha):
    n = len(alpha)
    A = sum(alpha)
    arr = []
    for k in range(1, n):
        r = n-k
        subsets = list(combinations(range(n), r))
        shape = min(sum(alpha[i] for i in J) for J in subsets)
        minimizing = [J for J in subsets if sum(alpha[i] for i in J) == shape]
        coeff = len(minimizing)*gamma(A)/(gamma(shape+1)*gamma(A-shape))
        arr.append((shape,len(minimizing),coeff,minimizing))
    return arr

def finite_beta_tail(a,b,t):
    # For positive integer a,b, exactly P(Beta(a,b) <= t).
    N=a+b-1
    return sum(Fraction(comb(N,j))*t**j*(1-t)**(N-j) for j in range(a,N+1))

for n in range(2,9):
    for k,(shape,h,c,faces) in enumerate(coefficients([1]*n),1):
        check(shape==n-k)
        check(h==comb(n,k))
        check(isclose(c,comb(n,k)*comb(n-1,k-1),rel_tol=1e-12))

# An example with both a tied minimal face and three distinct scales.
alpha=[1,1,2,4]
obs=coefficients(alpha)
for k,(shape,h,c,faces) in enumerate(obs,1):
    check((shape,h,round(c))==[(4,1,35),(2,1,21),(1,2,14)][k-1])

# All rank pairs satisfy the exponent separation used in the proof.
for al in ([1,1,1,1],[1,1,2,4],[2,3,4,5],[1,2,2,6,7]):
    shapes=[o[0] for o in coefficients(al)]
    n=len(al)
    for k in range(1,n):
        for ell in range(k+1,n):
            for J in combinations(range(n),n-k):
                for K in combinations(range(n),n-ell):
                    shapeK=sum(al[i] for i in K)
                    extra=sum(al[i] for i in J if i not in K)
                    exponent=Fraction(shapeK,shapes[ell-1])+Fraction(extra,shapes[k-1])
                    check(exponent>1, (al,k,ell,J,K,exponent))

# Any two distinct faces at fixed rank have strictly larger union shape.
for al in ([1,1,1,1],[1,1,2,4],[2,3,4,5],[1,2,2,6,7]):
    n=len(al)
    for k in range(1,n):
        shape=coefficients(al)[k-1][0]
        faces=list(combinations(range(n),n-k))
        for i,J in enumerate(faces):
            for K in faces[i+1:]:
                union=set(J)|set(K)
                check(sum(al[x] for x in union)>shape)

# Exact small-t asymptotic ratio in a nontrivial integer case.
for k,(shape,h,c,faces) in enumerate(obs,1):
    A=sum(alpha)
    for j in (3,4,5):
        t=Fraction(1,10**j)
        marginal=sum(finite_beta_tail(sum(alpha[i] for i in J),A-sum(alpha[i] for i in J),t)
                     for J in faces)
        ratio=float(marginal/t**shape)/c
        check(0.99 < ratio <= 1.01,(k,j,ratio))

# Simple empirical diagnostic of joint scaling and inactive concavification.
rng=Random(312026)
M=400
rep=800
values=[[] for k in range(3)]
concave_count=0
winners_distinct=0
for repeat in range(rep):
    best=[float('inf')]*3
    witness=[-1]*3
    for j in range(M):
        g=[rng.gammavariate(shape,1.0) for shape in alpha]
        S=sum(g)
        x=sorted((a/S for a in g),reverse=True)
        suffix=[1-sum(x[:k]) for k in range(1,4)]
        for k in range(3):
            if suffix[k]<best[k]:
                best[k]=suffix[k]
                witness[k]=j
    d1,d2,d3=best
    slopes=[1-d1,d1-d2,d2-d3,d3]
    if all(slopes[i]>=slopes[i+1]-1e-13 for i in range(3)):
        concave_count+=1
    if len(set(witness))==3:
        winners_distinct+=1
    for k,(shape,h,c,faces) in enumerate(obs):
        values[k].append((M*c)**(1/shape)*best[k])

for k,xx in enumerate(values):
    # For rate-one Weibull with shape gamma, median is (log 2)^(1/gamma).
    med=sorted(xx)[len(xx)//2]
    benchmark=0.6931471805599453**(1/obs[k][0])
    check(abs(med-benchmark)<0.24,(k,med,benchmark))
check(concave_count/rep>.90)
check(winners_distinct/rep>0.80)
print('checks_passed',N_CHECKS)
print('example',[(s,h,c) for s,h,c,_ in obs])
print('simulated_concavity_fraction',concave_count/rep)
print('simulated_distinct_winner_fraction',winners_distinct/rep)
