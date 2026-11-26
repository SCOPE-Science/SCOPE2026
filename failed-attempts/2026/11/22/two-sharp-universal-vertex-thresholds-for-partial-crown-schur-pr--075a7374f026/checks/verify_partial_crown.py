"""Finite diagnostics for a partial-matching deletion Schur norm theorem.

Requires numpy and scipy; these finite checks complement, not replace, the proof.
Run: python3 checks/verify_partial_crown.py
"""
import math
import numpy as np
from scipy.optimize import minimize

checks = 0

def check(cond, context):
    global checks
    assert bool(cond), context
    checks += 1

def closed(k, r, s):
    base = 2.0 - 2.0/k
    if r == 0 and s == 0:
        return base
    if r == 0 or s == 0:
        return k / math.sqrt(2*k-1) if k <= 3 else base
    return ((k-1)+2*k*math.sqrt(k+2))/(4*k-1) if k <= 4 else base

def optimal_mass(k, r, s):
    if r == s == 0:
        return 1.0
    if r == 0 or s == 0:
        return min(1.0, (k-1)**2/(2*k-1))
    return min(1.0, k/(4*k-1)*(1+2*(k-1)/math.sqrt(k+2)))

def mask(k, r, s):
    B = np.ones((k+r, k+s), dtype=float)
    for i in range(k): B[i,i]=0.0
    return B

def weighted_nuclear(B, p, q):
    return float(np.linalg.svd(np.sqrt(p)[:,None]*B*np.sqrt(q)[None,:], compute_uv=False).sum())

def stationary_profiles(k, r, s):
    x = optimal_mass(k,r,s)
    if r == s == 0:
        return np.full(k,1.0/k), np.full(k,1.0/k)
    p = np.r_[np.full(k,x/k), np.full(r,(1-x)/r) if r else []]
    q = np.r_[np.full(k,x/k), np.full(s,(1-x)/s) if s else []]
    if r and not s: q = np.full(k,1.0/k)
    if s and not r: p = np.full(k,1.0/k)
    return p, q

# Exact closed-form discriminants and branch switches, using high precision floats.
for k in range(2,121):
    base=2-2/k
    x1=(k-1)**2/(2*k-1)
    xb=k/(4*k-1)*(1+2*(k-1)/math.sqrt(k+2))
    d1=(k*k-4*k+2)/(2*k*(k-1))
    db=(k*k-5*k+2)/(k*(k-1))
    check((x1 < 1) == (k <= 3),('one threshold',k))
    check((xb < 1) == (k <= 4),('both threshold',k))
    check((d1 < 0) == (k <=3),('one derivative',k))
    check((db < 0) == (k <=4),('both derivative',k))
    check(abs((k-1)/k + (k-1)/k - base)<1e-12,('core singulars',k))
    x=optimal_mass(k,1,0)
    f=(k-1)/k*math.sqrt(x)+math.sqrt(1-(2*k-1)*x/k**2)
    check(abs(f-closed(k,1,0))<1e-11,('one formula',k))
    x=optimal_mass(k,1,1)
    h=(k-1)*x/k+math.sqrt(1+2*x/k-(4*k-1)*x*x/k**2)
    check(abs(h-closed(k,1,1))<1e-11,('both formula',k))
    check(closed(k,0,0)<=closed(k,1,0)+1e-12,('monotonic one',k))
    check(closed(k,1,0)<=closed(k,1,1)+1e-12,('monotonic two',k))

# Direct singular-value witnesses and duplication invariance.
for k in range(2,21):
    for r,s in [(0,0),(1,0),(0,1),(1,1),(2,3),(4,2)]:
        p,q=stationary_profiles(k,r,s)
        check(abs(p.sum()-1)<1e-12 and abs(q.sum()-1)<1e-12,('mass',k,r,s))
        val=weighted_nuclear(mask(k,r,s),p,q)
        check(abs(val-closed(k,r,s))<1e-10,('nuclear witness',k,r,s,val,closed(k,r,s)))

# Independent unconstrained numerical maximization over ALL row and column
# probabilities, including nonsymmetric ones (local optimization, not a proof).
for k in range(2,9):
    for r,s in [(0,0),(1,0),(0,1),(1,1),(2,3)]:
        B=mask(k,r,s)
        nr,nc=B.shape
        def soft(z):
            e=np.exp(z-z.max());return e/e.sum()
        def objective(z):
            return -weighted_nuclear(B,soft(z[:nr]),soft(z[nr:]))
        rng=np.random.default_rng(2026+k+10*r+s)
        best=-float('inf')
        for _ in range(4):
            z=rng.normal(size=nr+nc)
            res=minimize(objective,z,method='BFGS',options={'gtol':5e-8,'maxiter':300})
            best=max(best,-float(res.fun))
        check(best <= closed(k,r,s)+2e-8,('numerical upper',k,r,s,best))
        check(best >= closed(k,r,s)-1e-5,('numerical lower',k,r,s,best))

# Known small values: the 3x3 9/7 norm and the 3x2 2/sqrt(3) norm.
check(abs(closed(2,1,1)-9/7)<1e-13,'known 9/7')
check(abs(closed(2,1,0)-2/math.sqrt(3))<1e-13,'known 2/sqrt(3)')
print('PARTIAL_CROWN_SCHUR_DIAGNOSTIC_OK',checks)
