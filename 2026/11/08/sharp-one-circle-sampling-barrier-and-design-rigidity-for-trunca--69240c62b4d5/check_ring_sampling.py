#!/usr/bin/env python3
"""Numerical spot-checks of circular Fock sampling spectra and sharp asymptotics.
Scientific claims and proofs are supplied separately; finite checks are corroboration only.
"""
import math
import numpy as np

checks=0

def check(c, message):
    global checks
    checks+=1
    if not c: raise AssertionError(message)

def fock_matrix(n,angles,x,weights=None):
    ks=np.arange(n)
    if weights is None: weights=np.ones(len(angles))/len(angles)
    return np.sqrt(np.asarray(weights))[:,None]*np.exp(-x/2)*np.exp(1j*np.outer(angles,ks))*np.exp(0.5*(ks*np.log(x)-np.array([math.lgamma(k+1) for k in ks])))

def cond(n,angles,x,weights=None):
    ss=np.linalg.svd(fock_matrix(n,angles,x,weights),compute_uv=False)
    return float(ss[0]/ss[-1]) if ss[-1]>0 else np.inf

def x_star(n):
    return math.exp(math.lgamma(n)/(n-1))

def bound(n,x):
    logs=[k*math.log(x)-math.lgamma(k+1) for k in range(n)]
    return math.exp((max(logs)-min(logs))/2)

rng=np.random.default_rng(290473)
for n in range(2,14):
    x=x_star(n)
    base=bound(n,x)
    for m in [n,n+1,n+4,2*n]:
        a=2*math.pi*np.arange(m)/m
        test=cond(n,a,x)
        check(abs(test/base-1)<1e-8,(n,m,test,base))
        for factor in [0.49,0.81,0.95,1.05,1.25,2.1]:
            test2=cond(n,a,x*factor)
            check(test2>base*(1+1e-8),(n,m,factor,test2,base))
        for rep in range(4):
            perturb=rng.uniform(-0.19,0.19,m)
            c=cond(n,a+perturb,x)
            check(c>base*(1+1e-9),(n,m,rep,c,base))
        for rep in range(4):
            random_angles=np.sort(rng.uniform(0,2*math.pi,m))
            c=cond(n,random_angles,x)
            check(c>=base*(1-2e-8),(n,m,rep,c,base))
        for rep in range(4):
            weights=rng.random(m)
            weights/=weights.sum()
            testw=cond(n,a,x,weights)
            check(testw>=base*(1-1e-8),(n,m,rep,testw,base))
            if m==n:
                check(testw>base*(1+1e-9),(n,m,rep,testw,base))
    check(x<=n-1+1e-12,n)
# Nonregular circle designs formed by a union of rotated regular polygons.
for n in range(2,13):
    for d in (2,3):
        ang=np.concatenate([2*math.pi*np.arange(n)/n+0.23*j for j in range(d)])
        check(abs(cond(n,ang,x_star(n))/bound(n,x_star(n))-1)<1e-8,(n,d))
# Nonuniform positive weights can be optimal if at least two regular n-gon blocks.
for n in range(2,13):
    m=3*n
    angles=np.concatenate([2*math.pi*np.arange(n)/n+0.31*j for j in range(3)])
    weights=np.concatenate([np.ones(n)*z/n for z in (0.1,0.37,0.53)])
    check(abs(cond(n,angles,x_star(n),weights)/bound(n,x_star(n))-1)<1e-8,(n,"weighted design"))
# Asymptotic including complete polynomial prefactor (numerical logarithms to avoid overflow).
for n in [100, 300, 1000, 3000, 10000]:
    t=n-1
    x=x_star(n)
    mode=math.floor(x)
    exact_log=(mode*math.log(x)-math.lgamma(mode+1))/2
    asymptotic=t/(2*math.e) + ((1/math.e)-1)/4*math.log(2*math.pi*t)+1/4
    err=abs(exact_log-asymptotic)
    check(err<15*math.log(n)**2/n,(n,err))
print(f'FOCK_CIRCULAR_SAMPLING_CHECKS_PASS {checks}')
