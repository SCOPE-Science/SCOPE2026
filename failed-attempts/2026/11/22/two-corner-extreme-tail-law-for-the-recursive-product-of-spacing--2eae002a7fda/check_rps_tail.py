#!/usr/bin/env python3
"""Reproduce finite-dimensional identities and boundary diagnostics for RPS tails.
All proofs for arbitrary dimensions are analytical; finite checks are corroboration only.
"""
import itertools
import math
import random

CHECKS = 0

def chk(pred, msg):
    global CHECKS
    if not pred:
        raise AssertionError(msg)
    CHECKS += 1

def product_of_linear_forms(v):
    m = len(v)
    product = 1.0
    for r in range(m):
        for i in range(m-r):
            form = sum(math.comb(r,h)*v[i+h] for h in range(r+1))
            product *= form
    return product

def recursive_rps(v):
    a = list(v)
    out = 0.0
    while True:
        out -= sum(math.log(q) for q in a)
        if len(a)==1:
            break
        a = [a[i]+a[i+1] for i in range(len(a)-1)]
        z = sum(a)
        a = [x/z for x in a]
    return out

def closed_rps(v):
    m = len(v)
    out = 0.
    for r in range(m):
        forms = [sum(math.comb(r,h)*v[i+h] for h in range(r+1)) for i in range(m-r)]
        out += len(forms)*math.log(sum(forms))-sum(math.log(z) for z in forms)
    return out

def random_simplex(m, rng):
    x = [rng.expovariate(1) for _ in range(m)]
    return [z/sum(x) for z in x]

def interval_count(s, m):
    return sum(all(j in s for j in range(i,i+r+1)) for r in range(m) for i in range(m-r))

def check():
    rng=random.Random(784211)
    for m in range(2,11):
        for _ in range(35):
            v=random_simplex(m,rng)
            chk(abs(recursive_rps(v)-closed_rps(v))<1e-10, f'closed={m}')
            chk(abs(recursive_rps(v)-closed_rps(list(reversed(v))))<1e-10, f'symmetry={m}')
        eq=[1/m]*m
        minimum=sum(k*math.log(k) for k in range(1,m+1))
        chk(abs(recursive_rps(eq)-minimum)<1e-10, f'minimum={m}')
        for mask in range(1,(1<<m)-1):
            s={j for j in range(m) if mask&(1<<j)}
            h=interval_count(s,m)
            k=len(s)
            chk(h <= k*(k+1)//2, f'run bound {m} {mask}')
            if 2*h==m*k:
                chk(k==m-1 and s in (set(range(1,m)),set(range(m-1))),f'critical set {m} {mask}')
            else:
                chk(2*h<m*k, f'not critical {m} {mask}: {h}, {k}')
        for _ in range(12):
            u=random_simplex(m-1,rng)
            q=product_of_linear_forms(u)
            K=m*(m-1)//2
            for eps in (1e-4, 1e-6):
                d=[1-eps]+[eps*x for x in u]
                error=recursive_rps(d)-K*math.log(1/eps)+math.log(q)
                chk(abs(error)<(2**m)*eps*100, f'corner {m}, {eps}: {error}')
    # The m=2 tail is explicit: R=-log(U(1-U)).
    for t in (5,10,15,20):
        exact=1-math.sqrt(1-4*math.exp(-t))
        chk(abs(exact*math.exp(t)/2-1)<5*math.exp(-t),f'm=2 constant {t}')
    a3=2*math.gamma(1/3)**2/math.gamma(2/3)
    chk(abs(a3-10.599832501712696)<1e-11,'m=3 beta constant')
    print('CHECKS_PASSED',CHECKS)
    print('m=3 exact upper-tail prefactor',f'{a3:.14f}')
    print('m=2 prefactor 2, tail rate 1; m=3 tail rate 2/3')

if __name__=='__main__':
    check()
