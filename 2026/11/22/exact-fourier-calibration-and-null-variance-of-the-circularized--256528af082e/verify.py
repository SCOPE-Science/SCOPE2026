#!/usr/bin/env python3
"""Reproduce numerical checks for the circularized AD null limit.
Requires mpmath (pip install mpmath). This file is an auxiliary checker;
all infinite-dimensional claims have analytic proofs in RESULT.md.
"""
import math
from random import Random
import mpmath as mp
mp.mp.dps = 48
checks=0

def close(actual,expected,tolerance,description):
    global checks
    assert abs(actual-expected)<tolerance, (description,str(actual),str(expected))
    checks+=1

def positive(expr,description):
    global checks
    assert expr,description
    checks+=1

def kernel(x):
    if x==0 or x==1: return mp.mpf(1)
    return 1+2*(x*mp.log(x)+(1-x)*mp.log(1-x))

def lam(k):
    a=2*mp.pi*k
    return 4*(mp.euler+mp.log(a)-mp.ci(a))/(a*a)

exact_var=(42-4*mp.pi**2)/9
classical_ad_var=2*mp.pi**2/3-6
close(2*sum(mp.mpf(1)/(k*k*(k+1)*(k+1)) for k in range(1,5000)),classical_ad_var,mp.mpf('1e-10'),'classical AD spectral variance')
k2=mp.quad(lambda x: kernel(x)**2,[0,mp.mpf('0.5'),1])
close(2*k2,exact_var,mp.mpf('1e-39'),'closed variance via beta integration')
close(mp.quad(kernel,[0,mp.mpf('.5'),1]),0,mp.mpf('1e-39'),'zero Fourier mode')
for k in range(1,8):
    f=mp.quad(lambda x: kernel(x)*mp.cos(2*mp.pi*k*x),[0,mp.mpf('.5'),1])
    close(f,lam(k),mp.mpf('1e-38'),f'Fourier mode k={k}')
    positive(lam(k)>0,f'positivity k={k}')
    if k>1: positive(lam(k-1)>lam(k),f'mode decay k={k}')
K=250
partial_var=4*sum(lam(k)**2 for k in range(1,K+1))
positive(0<exact_var-partial_var<mp.mpf('1e-7'),'variance tail positive and small')
# Compare exact null mean with independent beta/digamma representation.
for m in (2,3,4,5,10,25,100):
    direct=sum(2*(mp.digamma(m)-mp.mpf(i)/m*mp.digamma(i)
           -(1-mp.mpf(i)/m)*mp.digamma(m-i)
           +mp.mpf(i)/m*mp.log(mp.mpf(i)/m)
           +(1-mp.mpf(i)/m)*mp.log(1-mp.mpf(i)/m)) for i in range(1,m))
    folded=m+1-mp.mpf(2)/m+(mp.mpf(4)/m)*sum(i*mp.log(mp.mpf(i)/m) for i in range(1,m))
    close(direct,folded,mp.mpf('1e-38'),f'finite mean m={m}')
    positive(direct>0, 'positive expected divergence')
# Check Euler-Gamma representation of circular spacings and their beta moments.
rng=Random(42)
m=18
reps=2200
sum_stat=0.0
for rep in range(reps):
    z=[rng.expovariate(1) for _ in range(m)]
    s=sum(z)
    ds=[x/s for x in z]
    total=0.0
    for c in range(m):
        u=0.0
        for i in range(1,m):
            u+=ds[(c+i-1)%m]
            p=i/m
            total+=-2*(p*math.log(u/p)+(1-p)*math.log((1-u)/(1-p)))
    sum_stat+=total/m
empirical=sum_stat/reps
exact=float(m+1-2/m+(mp.mpf(4)/m)*sum(i*mp.log(mp.mpf(i)/m) for i in range(1,m)))
positive(abs(empirical-exact)<0.09,'Monte Carlo finite-sample expectation')
print('PASS',checks,'checks')
print('exact limiting mean = 1; limiting variance =',mp.nstr(exact_var,25))
print('finite m=18 empirical mean',empirical,'exact mean',exact)
print('variance first 250 harmonic pairs',mp.nstr(partial_var,25))
print('first three spectral weights',*[mp.nstr(lam(k),19) for k in [1,2,3]])
