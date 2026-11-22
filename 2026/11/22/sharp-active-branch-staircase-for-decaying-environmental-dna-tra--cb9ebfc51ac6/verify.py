#!/usr/bin/env python3
"""Standalone reproducibility checks for a parallel advective-decay allocation theorem.

Analytic proofs and their quantifiers are in RESULT.md; finite tests are diagnostics.
Requires only Python >=3.9 standard library.
"""
import itertools
import math
import random

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def outlet(alpha, p):
    return sum(math.exp(-alpha/x) if x > 0 else 0.0 for x in p)

def theorem_value(alpha, n):
    return max(k*math.exp(-alpha*k) for k in range(1,n+1))

def theorem_k(alpha,n):
    return [k for k in range(1,n+1) if abs(k*math.exp(-alpha*k)-theorem_value(alpha,n)) < 1e-12]

for n in range(2,19):
    ts = [math.log((k+1)/k) for k in range(1,n)]
    check(all(ts[k] < ts[k-1] for k in range(1,len(ts))), 'strict ordered critical values')
    for k in range(1,n):
        a = math.log((k+1)/k)
        check(abs(k*math.exp(-a*k)-(k+1)*math.exp(-a*(k+1)))<3e-15,'tie')
        vs=[j*math.exp(-a*j) for j in range(1,n+1)]
        check(all(v<=vs[k-1]+2e-14 for v in vs), 'dominant phase')
        check(all(v<=vs[k]+2e-14 for v in vs), 'adjacent dominant phase')
    for a in [0.05,.13,.22,.41,.62,.75,1,2,5]:
        v=theorem_value(a,n)
        for k in range(1,n+1):
            p=[0]*n
            for j in range(k):p[j]=1/k
            check(outlet(a,p)<=v+1e-14,'candidate support')

# Exact derivative identity checked numerically away from boundaries, with a
# symmetric stable difference step and a relative error tolerance.
for a in [.12,.4,.7,1.2]:
    for x in [.15,.27,.43,.68,.83]:
        h=2e-5
        f=lambda y:math.exp(-a/y)
        estimated=(f(x+h)-2*f(x)+f(x-h))/h**2
        formula=(a*math.exp(-a/x)/x**4)*(a-2*x)
        check(abs(estimated-formula)<1e-5*max(1,abs(formula)),'curvature')

# The noncentral stationary threshold u/sinh(u) decreases strictly in u>0.
u_prev=1.0
for j in range(1,8001):
    u = j/800
    t = u/math.sinh(u)
    check(t < u_prev+2e-14, 'unique pairwise noncentral root')
    u_prev=t

# Deterministic exact-grid and randomized-simplex stress tests.
for n in [2,3,4,5,8]:
    rng=random.Random(1900+n)
    for a in [.1,.3,.405,.5,.693,.8,1.4,3.]:
        v=theorem_value(a,n)
        for _ in range(1250):
            w=[rng.expovariate(1) for _ in range(n)]
            s=sum(w)
            p=[z/s for z in w]
            check(outlet(a,p)<=v+1e-12,'global random feasible point')
for a in [.1,.4,.6932,1.2]:
    v=theorem_value(a,3)
    for i in range(201):
        for j in range(201-i):
            p=(i/200,j/200,(200-i-j)/200)
            check(outlet(a,p)<=v+1e-12,'three-flow dense grid')

print(f'PASS: {checks} reproducibility assertions; analytic proof in RESULT.md')
