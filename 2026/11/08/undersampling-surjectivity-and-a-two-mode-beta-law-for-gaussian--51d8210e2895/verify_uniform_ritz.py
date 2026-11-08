#!/usr/bin/env python3
"""Reproducibility checks for uniform-start sketched Ritz positivity.
Tests numeric algebraic identities and simulations; analytical proof is separate.
"""
import math
import numpy as np
from scipy.special import betainc

rng = np.random.default_rng(20261105)
checks = 0

def test(cond, message):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(message)

# Real generalized eigensign vs the exact normalized-correlation criterion.
for k in range(2, 10):
    for ratio in (1.1, 1.5, 2., 4., 10., 40.):
        A = np.diag((1., ratio))
        threshold = 4 * ratio / ((ratio+1)**2)
        for _ in range(125):
            S = rng.normal(size=(k, 2))
            W = S.T @ S
            B = (W@A+A@W)/2
            c = float(W[0,1]/math.sqrt(W[0,0]*W[1,1]))
            test((np.linalg.det(B) < 0) == (c*c > threshold), 'incorrect negative Ritz criterion')
            # The negative direction is an eigenvector of the generalized Rayleigh form.
            if np.linalg.det(B) < -1e-8:
                C = np.linalg.cholesky(W)
                E = np.linalg.solve(C, B) @ np.linalg.inv(C.T)
                eig = np.linalg.eigvalsh(E)
                test(eig[0] < 0, 'negative generalized Ritz witness missing')

# The sharp beta law and k=2 formula against independent Monte Carlo.
mc = []
for k in (2,3,4,6,10):
    for K in (2.,4.,10.):
        N = 17000
        u = rng.normal(size=(N,k)); v = rng.normal(size=(N,k))
        c2 = np.einsum('ij,ij->i',u,v)**2 / (np.einsum('ij,ij->i',u,u)*np.einsum('ij,ij->i',v,v))
        z = ((K-1)/(K+1))**2
        p = float(betainc((k-1)/2, 0.5, z))
        obs = float(np.mean(c2 > 1-z))
        margin = 6*math.sqrt(max(p*(1-p),0.01)/N)+0.005
        test(abs(obs-p) < margin, 'beta law simulation discrepancy')
        if k==2:
            test(abs(p-2/math.pi*math.asin(math.sqrt(z))) < 1e-13, 'k=2 closed form')
        mc.append((k,K,p,obs,margin))

# Under-sampling: real surjectivity verified for many n,k and t values.
for n in (2,3,4,7):
    A=np.diag(np.linspace(1.,2.7,n))
    for k in range(1,n):
        for _ in range(70):
            S=rng.normal(size=(k,n)); W=S.T@S
            _,_,VT=np.linalg.svd(S,full_matrices=True)
            z=VT[-1,:]; x=W@A@z
            c=x@W@A@z; e=x@W@x; d=x@W@A@x
            test(c>1e-15 and e>1e-15, 'noninvariance witness unexpectedly zero')
            for t in (-.05,-2.,.12,1.1):
                v=z+t*x
                R=(v@W@A@v)/(v@W@v)
                target=c/(t*e)+d/e
                test(abs(R-target)<max(1.,abs(target))*5e-6, 'surjectivity identity failed')

# Scalar matrices, regardless of sampling, retain their sole Ritz value.
for n in (2,4):
    for k in range(1,n+3):
        S=rng.normal(size=(k,n)); v=rng.normal(size=n)
        W=S.T@S; A=3.25*np.eye(n)
        test(abs((v@W@A@v)/(v@W@v)-3.25)<1e-11,'scalar exception')

print(f'PASS: {checks} numerical/algebraic checks')
print('Monte Carlo (k,K,theory,empirical,tolerance):')
for line in mc:print('  %d %.1f %.8f %.8f %.8f'%line)
