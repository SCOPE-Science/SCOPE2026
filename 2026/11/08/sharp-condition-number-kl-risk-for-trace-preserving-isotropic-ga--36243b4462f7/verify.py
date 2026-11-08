#!/usr/bin/env python3
"""Deterministic numerical stress tests for a sharp isotropic-Gaussian KL bound.

Run: python3 verify.py
The finite tests check formulas and examples; the theorem relies on its analytic proof.
"""
from fractions import Fraction
from itertools import product
from math import floor, isfinite, log, sqrt
from random import Random

rng = Random(814273)
count = {'exact_identity': 0, 'vertex_enumeration': 0, 'random_matrix_spectra': 0,
         'derivative_sign': 0, 'continuous_critical': 0, 'large_contrast': 0}

def kl(vals):
    n = len(vals)
    mean = sum(vals)/n
    return 0.5*(mean*sum(1/y for y in vals)-n + sum(log(y) for y in vals)-n*log(mean))

def f(q, kappa):
    a = kappa - 1.0
    return 0.5*(a*a/kappa*q*(1-q) + q*log(kappa) - log(1+q*a))

def sharp(n, kappa):
    return max(n*f(j/n, kappa) for j in range(n+1))

def fprime(q, kappa):
    a = kappa - 1.0
    return a*a/kappa*(1-2*q) + log(kappa) - a/(1+q*a)

for n in range(2, 12):
    for num, den in [(11,10),(3,2),(2,1),(7,2),(4,1),(19,3),(100,1)]:
        k = Fraction(num, den)
        for j in range(1,n):
            vals=[Fraction(1)]*(n-j)+[k]*j
            m=sum(vals)/n
            left=m*sum(1/y for y in vals)-n
            right=Fraction(j*(n-j),n)*(k-1)**2/k
            assert left==right,(n,k,j,left,right)
            count['exact_identity']+=1

for n in range(2, 9):
    for k in [1.02,1.3,2.,4.,11.,80.]:
        max_val=sharp(n,k)
        all_v=[kl(y) for y in product([1.,k],repeat=n)]
        assert abs(max_val-max(all_v))<=2e-10*max(1.,max_val)
        count['vertex_enumeration']+=len(all_v)

for n in [2,3,5,8,12,19]:
    for k in [1.03,1.5,2.,3.,9.,70.,1000.]:
        target=sharp(n,k)
        for _ in range(450):
            vals=[k**rng.random() for _ in range(n)]
            err=kl(vals)
            assert err<=target+1e-9*max(1.,target),(n,k,err,target)
            count['random_matrix_spectra']+=1

for n in range(2,12):
    for _ in range(200):
        other=[10**rng.uniform(-1,2) for _ in range(n-1)]
        b=sum(other); t=sum(1/y for y in other); a=b*t-n*(n-1)
        # Discriminant argument in the proof: P'(y)>0 for every positive y.
        assert b*t >= (n-1)**2-1e-8
        for y in [0.0001,0.1,0.5,1.,10.,100.,10000.]:
            deriv=3*t*y*y+2*a*y+(n-1)*b
            assert deriv>0,(n,other,y,deriv)
            count['derivative_sign']+=1

for n in range(2, 20):
    for k in [1.002,1.02,1.1,1.4,2.,3.,4.,8.,12.,99.]:
        assert fprime(0.,k)>0 and fprime(1.,k)<0
        left,right=0.,1.
        for _ in range(70):
            mid=(left+right)/2
            if fprime(mid,k)>0: left=mid
            else: right=mid
        q=(left+right)/2
        j=max(range(n+1),key=lambda j: f(j/n,k))
        assert j in (floor(n*q),floor(n*q)+1),(n,k,q,j)
        count['continuous_critical']+=1

for n in range(2,18):
    k=1e7
    limit=floor(n*n/4)/(2*n)
    observed=sharp(n,k)/k
    assert abs(observed-limit)<3e-5,(n,observed,limit)
    count['large_contrast']+=1

assert all(isfinite(float(v)) for v in count.values())
print('VERIFY_OK', count)
