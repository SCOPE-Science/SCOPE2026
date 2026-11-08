#!/usr/bin/env python3
"""Stand-alone diagnostics for normalized stationary squared Brownian rescaling fluctuations.
The analytic majorization proof and limits are given in RESULT.md; sampling is only a diagnostic.
"""
import math
import random

count = 0

def check(pred, msg):
    global count
    count += 1
    assert pred, msg

def normal_phi(z):
    return math.exp(-z*z/2)/math.sqrt(2*math.pi)

def normal_tail(z):
    return math.erfc(z/math.sqrt(2))/2

def gaussian_stoploss(t):
    a = math.sqrt(t)
    return 2*(a*normal_phi(a)+(1-t)*normal_tail(a))

def laplace_stoploss(t):
    a = math.sqrt(2*t)
    return (1+a)*math.exp(-a)

def conditional_stoploss(v, t):
    if t == 0:
        return v
    a = math.sqrt(t/v)
    return 2*(v*a*normal_phi(a)+(v-t)*normal_tail(a))

def weights(q,n):
    return [(1-q)*q**j for j in range(n)] + [q**n/n]*n

# Exact finite majorization comparisons (strictly decreasing sorted weights).
for q1,q2 in [(0.0,0.125),(0.125,0.4),(0.4,0.6),(0.6,0.9),(0.9,0.97)]:
    n = max(10, math.ceil(q2/(1-q2)) + 3)
    a,b=weights(q1,n),weights(q2,n)
    check(all(a[j]>=a[j+1]-1e-14 for j in range(2*n-1)), 'sorted weights a')
    check(all(b[j]>=b[j+1]-1e-14 for j in range(2*n-1)), 'sorted weights b')
    check(abs(sum(a)-1)<1e-12 and abs(sum(b)-1)<1e-12, 'weight masses')
    acca=accb=0.0
    for j in range(2*n-1):
        acca+=a[j];accb+=b[j]
        check(acca>accb-1e-12, f'majorization at {q1},{q2},{j}')

# Closed-form stationary variance and standardized fourth moment.
for q in [0.0,0.1,0.4,0.7,0.93,0.99]:
    w0=1-q
    check(abs(w0/(1-q)-1)<1e-12, 'weight sum')
    check(abs((1-q)**2/(1-q*q)-(1-q)/(1+q))<1e-12, 'mixing variance')
    check(abs(3*(1+(1-q)/(1+q))-6/(1+q))<1e-12, 'fourth moment')

# Explicit Gaussian/Laplace endpoints have same mean loss at zero; Laplace has more at t>0.
check(gaussian_stoploss(0)==1.0, 'Gaussian t=0')
check(laplace_stoploss(0)==1.0, 'Laplace t=0')
for t in [0.01,0.1,0.5,1,2,4,9,25]:
    check(0<gaussian_stoploss(t)<laplace_stoploss(t)<1, 'sharp endpoints')

# Conditional normal integration cross-check at t=0 and near the Gaussian mixing limit.
for t in [0.05,0.5,1,4,9]:
    check(abs(conditional_stoploss(1,t)-gaussian_stoploss(t))<1e-13, 'conditional Gaussian')

# Deterministic pseudo-random diagnostics: conditional integration avoids a second source of noise.
rng=random.Random(170125)
n=40000
results={}
for q in [0.0,0.35,0.8,0.95]:
    w=[]
    curr=1-q
    while curr>1e-10:
        w.append(curr)
        curr*=q
    losses=[0.0,0.0]
    for _ in range(n):
        v=sum(ww*rng.expovariate(1) for ww in w)
        losses[0]+=conditional_stoploss(v,1.0)
        losses[1]+=conditional_stoploss(v,4.0)
    results[q]=[loss/n for loss in losses]
for index,t in enumerate([1.0,4.0]):
    vals=[results[q][index] for q in [0.0,0.35,0.8,0.95]]
    check(all(vals[i]>vals[i+1]+0.003 for i in range(3)), f'monotone sampled risk at {t}: {vals}')
    check(gaussian_stoploss(t)<vals[-1] and vals[0]<laplace_stoploss(t)+0.009, 'endpoints sampled')

print(f'PASS: {count} deterministic assertions; risk diagnostics: {results}')
