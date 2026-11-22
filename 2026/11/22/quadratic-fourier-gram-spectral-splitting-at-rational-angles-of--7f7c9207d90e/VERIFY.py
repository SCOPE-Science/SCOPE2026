#!/usr/bin/env python3
"""Numerical and exact-rational checks for a geometric-orbit Fourier Gram transition.

Dependencies: Python 3, NumPy.  This is a finite stress test, not a proof of
asymptotics for all parameters; the accompanying analytic argument is needed.
"""
from fractions import Fraction
from math import gcd, pi
import numpy as np

assertions = 0


def check(statement, context):
    global assertions
    assertions += 1
    if not statement:
        raise AssertionError(context)


def gram(L, K, p, a, eps):
    n = L + K
    angle = 2 * pi * a / L + eps
    i = np.arange(n)
    return (1-p) / (1-p * np.exp(1j * (i[None,:]-i[:,None]) * angle))


def soft_matrix(L,K,p,a):
    r = np.arange(L)
    weights = (1-p)*p**r/(1-p**L)
    roots = np.exp(2j*pi*a*r/L)
    Z = roots[:, None] ** np.arange(K)[None,:]
    H = (Z.conj().T * weights) @ Z
    C = L**4 * p**L / (2*(1-p**L)**2)
    return C*H, weights


# Exact rational checks for the two-residue modal spectrum.
for p in (Fraction(1,3), Fraction(2,5), Fraction(3,4)):
    w0, w1 = 1/(1+p), p/(1+p)
    check(w0+w1 == 1, 'exact mass normalization')
    h_off = w0-w1
    check(1-h_off == 2*p/(1+p), 'exact first mode')
    check(1+h_off == 2/(1+p), 'exact second mode')
    c = 8*p**2/(1-p**2)**2
    check(c > 0, 'positive transition factor')

# The fixed-rational rank and every soft-branch asymptotic.
for L in (2,3,4,5):
    for a in range(1,L):
        if gcd(a,L) != 1: continue
        for p in (.4,.55,.7):
            for K in range(1,L+1):
                M, w = soft_matrix(L,K,p,a)
                eig_expected = np.sort(np.linalg.eigvalsh(M))
                check(np.min(eig_expected)>0, ('positive soft matrix', L,K,p,a))
                eig_old = np.linalg.eigvalsh(gram(L,K,p,a,0))
                check(np.max(abs(eig_old[:K])) < 3e-13,
                      ('exact-resonance K-fold nullspace', L,K,p,a))
                check(np.min(eig_old[K:])>0, ('hard spectral gap', L,K,p,a))
                for eps in (0.0002,0.0001,-0.0001):
                    eig_now = np.linalg.eigvalsh(gram(L,K,p,a,eps))[:K]/eps**2
                    err = max(abs(eig_now-eig_expected))/max(1,max(abs(eig_expected)))
                    check(err < .008, ('soft eigenvalue asymptotic',L,K,p,a,eps,err))
                if K==L:
                    hard = np.sort(2*L*w)
                    check(np.max(abs(eig_old[K:]-hard)) < 4e-13,
                          ('hard spectrum', L,p,a))
                    soft = np.sort((L**4*p**L/(2*(1-p**L)**2))*L*w)
                    check(np.max(abs(eig_expected-soft))<1e-10,
                          ('fully explicit soft spectrum',L,p,a))
                    for eps in (0.0002,-0.0002):
                        lam = np.linalg.eigvalsh(gram(L,L,p,a,eps))
                        kappa = np.sqrt(lam[-1]/lam[0])
                        predicted = 2*(1-p**L)/(L**2*p**(L-.5))/abs(eps)
                        check(abs(kappa/predicted-1)<.008,
                              ('sharp sampling condition number',L,p,a,eps))

print(f'PASS: {assertions} assertions')
