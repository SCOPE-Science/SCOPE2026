#!/usr/bin/env python3
"""Supplementary finite checks for antipodal two-channel cyclic Fourier frames.

Run with: python CHECK.py  (requires numpy). Numerical tests are not proofs.
"""
import math
import numpy as np

n_checks=0
rng=np.random.default_rng(20261115)
def ck(condition,what):
    global n_checks
    n_checks+=1
    if not bool(condition): raise AssertionError(what)

def profile(m,t):
    k=np.arange(m)
    return np.exp(-8*t*np.sin(np.pi*k/m)**2)

def eval_gap(a,r,w=1.0):
    return w*a+(2-w)*np.roll(a,r)

# Universal majorization of BOTH frame extrema for arbitrary strict cyclic radial profiles.
for n in range(4,51,2):
    R=n//2
    for _ in range(40):
        radial=np.sort(rng.uniform(.01,3,R+1))[::-1]
        a=np.r_[radial,radial[R-1:0:-1]]
        ref=eval_gap(a,R)
        for r in range(1,R):
            cur=eval_gap(a,r)
            ck(cur.min() < ref.min()+1e-12,('universal min',n,r))
            ck(cur.max() > ref.max()-1e-12,('universal max',n,r))
        for r in range(1,R+1):
            for w in (.13,.47,1.0,1.58,1.91):
                cur=eval_gap(a,r,w)
                eq=eval_gap(a,r)
                ck(cur.min() <= eq.min()+1e-12,('balanced lower',n,r,w))
                ck(cur.max() >= eq.max()-1e-12,('balanced upper',n,r,w))

# Exact heat formula, unique global best pair and power balancing.
for n in range(2,61,2):
    R=n//2
    for t in (.002,.03,.17,.41,.9,2.4,5.1):
        a=profile(n,t)
        f=eval_gap(a,R)
        expected_B=2*math.exp(-4*t)*math.cosh(4*t)
        expected_A=2*math.exp(-4*t)*(1 if n%4==0 else math.cosh(4*t*math.sin(math.pi/n)))
        ck(np.isclose(f.max(),expected_B,rtol=5e-10,atol=3e-14),('B heat',n,t))
        ck(np.isclose(f.min(),expected_A,rtol=5e-10,atol=3e-14),('A heat',n,t))
        for r in range(1,R):
            ff=eval_gap(a,r)
            ck(ff.min()<f.min()*(1+1e-9),('min strict',n,t,r))
            ck(ff.max()>f.max()*(1-1e-9),('max strict',n,t,r))
        for w in (.2,.6,1.4,1.8):
            fw=eval_gap(a,R,w)
            ck(fw.max()>f.max()*(1-1e-9),('unique weight',n,t,w))

# Direct frame construction versus spectral eigenvalues (different construction).
for n in (2,4,6,8,10,12,14,16,18):
    j=np.arange(n)
    F=np.exp(-2*np.pi*1j*j[:,None]*j[None,:]/n)/math.sqrt(n)
    eigen=4*np.sin(np.pi*j/n)**2
    for t in (.02,.23,1.5):
        g=F.conj().T@ (np.exp(-t*eigen)/math.sqrt(n))
        for r in range(1,n//2+1):
            atoms=[]
            for ell in (0,r):
                for shift in range(n):
                    atoms.append(np.exp(2j*np.pi*ell*j/n)*np.roll(g,shift))
            M=np.stack(atoms,axis=1)
            S=M@M.conj().T
            observed=np.linalg.eigvalsh(S)
            predicted=np.sort(eval_gap(np.exp(-2*t*eigen),r))
            ck(np.allclose(observed,predicted,atol=1e-10,rtol=1e-10),('direct matrix',n,r,t))
print(f'CHECK_OK assertions={n_checks}')
