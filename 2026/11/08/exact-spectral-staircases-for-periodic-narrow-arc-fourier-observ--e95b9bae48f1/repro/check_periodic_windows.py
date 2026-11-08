#!/usr/bin/env python3
"""Recompute spectral small-window constants for periodic Fourier apertures.

Requires Python 3 and mpmath. Finite tests supplement, not replace, the proof.
"""
from collections import defaultdict
from math import factorial, comb
import mpmath as mp

mp.mp.dps = 85
checks = 0

def check(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)

def blocks(q, frequencies):
    out = defaultdict(list)
    for k in frequencies:
        out[k % q].append((k - k % q) // q)
    return [sorted(out[r]) for r in sorted(out)]

def moment_constant(nodes, j):
    def moment_det(k):
        if k == 0:
            return mp.mpf(1)
        return mp.det(mp.matrix([
            [sum(mp.mpf(n)**(a+b) for n in nodes) for b in range(k)]
            for a in range(k)
        ]))
    w = moment_det(j+1)/moment_det(j)
    constant = (w * mp.power(2,2*j) /
                (mp.pi*(2*j+1)*factorial(j)**2*comb(2*j,j)**2))
    return constant, w

def gram_beta(nodes,beta):
    M = mp.matrix(len(nodes))
    for i,n in enumerate(nodes):
        for j,m in enumerate(nodes):
            M[i,j] = (beta/mp.pi if n == m else
                      mp.sin((n-m)*beta)/(mp.pi*(n-m)))
    return M

def full_gram(q, frequencies, alpha):
    M=mp.matrix(len(frequencies))
    for i,k in enumerate(frequencies):
        for j,l in enumerate(frequencies):
            if (k-l) % q:
                M[i,j]=0
            elif k==l:
                M[i,j]=q*alpha/mp.pi
            else:
                M[i,j]=q*mp.sin((k-l)*alpha)/(mp.pi*(k-l))
    return M

cases = [
    (3,[0,1,2,3,4,6]),
    (4,[0,1,2,3,4,8,12]),
    (2,[0,1,2,3,4]),
    (5,[0,1,2,5,6,10,15]),
    (7,[0,1,3,5]),
    (3,[-5,-3,0,2,3,6]),
]
for q, F in cases:
    grp = blocks(q,F)
    for B in grp:
        for j in range(len(B)):
            c,w = moment_constant(B,j)
            check(c > 0 and w > 0, (q,F,B,j,'positive'))
        if len(B)>1:
            ell = len(B)-1
            denom = mp.fsum(1/mp.fprod(mp.mpf(n-m) for m in B if m!=n)**2 for n in B)
            check(abs(moment_constant(B,ell)[1]*denom-1)<mp.mpf('1e-65'),
                  (q,B,'barycentric'))
    beta=mp.mpf('0.008')
    for B in grp:
        actual=list(reversed(list(mp.eigsy(gram_beta(B,beta),eigvals_only=True))))
        for j,e in enumerate(actual):
            c,_ = moment_constant(B,j)
            ratio=e/(c*beta**(2*j+1))
            check(abs(ratio-1)<mp.mpf('0.002'), (q,F,B,j,ratio))
    a=beta/q
    full=full_gram(q,F,a)
    eig_full=list(mp.eigsy(full,eigvals_only=True))
    eig_blocks=[]
    for B in grp:
        eig_blocks += list(mp.eigsy(gram_beta(B,beta),eigvals_only=True))
    for x,y in zip(sorted(eig_full), sorted(eig_blocks)):
        check(abs(x-y)<mp.mpf('1e-65'),(q,F,'block equality',x,y))
    # Direct integration of a handful of full-matrix entries.
    for i,j in [(0,0),(0,len(F)-1),(len(F)//2,len(F)-1)]:
        d=F[j]-F[i]
        integral=mp.fsum([mp.quad(lambda t:mp.exp(1j*d*t),
                                  [2*mp.pi*h/q-a,2*mp.pi*h/q+a])
                           for h in range(q)])/(2*mp.pi)
        check(abs(integral-full[i,j])<mp.mpf('1e-63'),
              (q,F,'integration',i,j))

# Example with residue multiplicities (3,2,1).
q=3;F=[0,1,2,3,4,6]
for a in ['.04','.02','.01']:
    alpha=mp.mpf(a)
    ev=list(mp.eigsy(full_gram(q,F,alpha),eigvals_only=True))
    ratio=(ev[-1]/ev[0])*alpha**4
    check(abs(ratio-mp.mpf('2.5'))<mp.mpf('0.012'), ('sharp coefficient',a,ratio))

print('PERIODIC_FOURIER_STAIRCASE_CHECKS_PASS',checks)
