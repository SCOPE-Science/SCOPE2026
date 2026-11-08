#!/usr/bin/env python3
"""Finite diagnostics for the periodic tree-shift Floquet conditioning theorem.
These tests do not replace the infinite-dimensional proof.
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal

count = 0

def check(cond, message):
    global count
    assert bool(cond), message
    count += 1

def cyclic(weights):
    p = len(weights)
    C = np.zeros((p, p))
    for j, w in enumerate(weights):
        C[(j + 1) % p, j] = w
    return C

def modulus(weights, r):
    return float(np.linalg.svd(cyclic(weights) - r*np.eye(len(weights)), compute_uv=False)[-1])

def radial_data(weights):
    p = len(weights)
    root = np.prod(weights)**(1/p)
    a = np.ones(p)
    for j in range(1, p):
        a[j] = a[j-1] * weights[j-1]/root
    slope = p/(np.linalg.norm(a)*np.linalg.norm(1/a))
    return root, a, slope

def finite_min(weights, r, N):
    # (W-rI)^*(W-rI) on the first N basis vectors, including the full forward image.
    p = len(weights)
    diag = np.array([weights[j%p]**2 + r*r for j in range(N)], dtype=float)
    off = np.array([-r*weights[j%p] for j in range(N-1)], dtype=float)
    eig = float(eigh_tridiagonal(diag, off, select='i', select_range=(0,0), eigvals_only=True)[0])
    return math.sqrt(max(eig,0.0))

for counts in ([1,2], [1,4], [2,3,1], [1,4,1,4], [1,1,4,4], [1,2,3,4], [2,1,3,1,4]):
    weights = np.sqrt(np.asarray(counts, dtype=float))
    root, a, slope = radial_data(weights)
    C = cyclic(weights)
    check(np.linalg.norm(C@a-root*a)<1e-10, 'right Perron vector')
    check(np.linalg.norm(C.T@(1/a)-root/a)<1e-10, 'left Perron vector')
    check(0 < slope <= 1+1e-12, 'sharp Cauchy-Schwarz coefficient')
    check(abs(modulus(weights,root))<1e-9, 'unique predicted zero')
    for r in [0.0, .1, .5, 1.0, root*.8, root*.95, root*1.05, 1.3*root, 2*root, 3*root]:
        exact = modulus(weights,r)
        for N in [60,120,240]:
            f = finite_min(weights,r,N)
            check(f+1e-7>=exact,'compression lower bound')
            check(f-exact<0.075, 'finite section approaches bulk lower modulus')
    for e in [1e-2,3e-3,1e-3]:
        pred = slope*e
        actual = modulus(weights,root+e)
        check(abs(actual-pred) <= 2.5*e*e, 'linear singular-value coefficient')

for d in [2,3,4,9,16,25]:
    q = math.sqrt(d)
    r0, _, la = radial_data([1,q,1,q])
    r1, _, lc = radial_data([1,1,q,q])
    check(abs(r0-r1)<1e-12,'equal geometric-mean radius')
    check(abs(la-2*math.sqrt(q)/(1+q))<1e-12,'alternating coefficient')
    check(abs(lc-4*q/(1+q)**2)<1e-12,'clustered coefficient')
    check(lc < la,'strict arrangement effect')
    for r in np.linspace(0, 2*max(r0,1), 24):
        W=np.array([1,q])
        explicit=math.sqrt(max(0.0,r*r+(1+d)/2 - math.sqrt(((d-1)/2)**2+r*r*(1+q)**2)))
        check(abs(modulus(W,r)-explicit)<1e-7,'two-period explicit formula')

print(f'PASS: {count} supplementary finite assertions')
