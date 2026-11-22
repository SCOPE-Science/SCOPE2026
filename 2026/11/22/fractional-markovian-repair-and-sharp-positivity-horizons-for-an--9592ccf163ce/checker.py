"""Finite regression checks for signed-block fractional heat: independent matrix construction.

Run with Python 3, NumPy and SciPy: python checker.py
The analytical proof, not these finite checks, establishes the parameter-uniform theorem.
"""
import math
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq

COUNT = 0

def check(ok, note):
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError(note)


def setup(N, spec):
    """spec: (size, magnitude of negative internal conductance) pairs."""
    groups, off = [], 0
    for k, a in spec:
        check(k >= 2 and off + k <= N and 0 < a < N/k-1,
              'invalid signed-block family')
        groups.append((np.arange(off, off+k), a))
        off += k
    W = np.ones((N, N), dtype=float) - np.eye(N)
    for idx, a in groups:
        W[np.ix_(idx, idx)] = -a
        W[idx, idx] = 0
    L = np.diag(W.sum(axis=1)) - W
    return L, groups


def spectral_formula(N, groups, alpha, t):
    z = math.exp(-(N**alpha)*t)
    S = z*np.eye(N) + (1-z)*np.ones((N,N))/N
    for idx, a in groups:
        k = len(idx)
        lam = N-k*(1+a)
        v = math.exp(-(lam**alpha)*t)-z
        P = np.eye(k)-np.ones((k,k))/k
        S[np.ix_(idx, idx)] += v*P
    return S


def unique_horizon(N, k, a, alpha):
    lam = N-k*(1+a)
    q = 1-k/N
    crit = math.log(q)/math.log(lam/N)
    if alpha <= crit:
        return 0.0
    u = k/N
    d = (lam/N)**alpha
    # For s>0 the stabilized function has exactly one positive root.
    def h(s):
        return u*math.expm1(d*s) + q*math.expm1(-(1-d)*s)
    scale = 2*(q-d)/(q*(1-q))
    left = scale*0.01
    while h(left) >= 0:
        left *= 0.5
    right = max(1.0, 10*scale)
    while h(right) <= 0:
        right *= 2
    return brentq(h,left,right,xtol=1e-13)/(N**alpha)


specs = [
    (6, [(2, 0.22)]),
    (8, [(2, 0.2), (3, 0.4)]),
    (9, [(4, 0.13), (3, 0.4)]),
    (12, [(2, 0.45), (3, 0.2), (4, 0.1)]),
    (15, [(4, 0.3), (3, 0.12), (2, 0.2)]),
]
for N, spec in specs:
    L, groups = setup(N,spec)
    ev, U = eigh(L)
    check(abs(ev[0]) < 1e-11, 'constant mode not null')
    check(np.min(ev[1:]) > 1e-6, 'not positive on complement')
    expected = sorted([0] + [N]*(N-1-sum(k-1 for k,_ in spec)) +
                      [N-k*(1+a) for k,a in spec for _ in range(k-1)])
    check(np.max(np.abs(ev-np.array(expected))) < 1e-10,'spectral decomposition')
    eig_pos = np.where(ev < 1e-9, 0.0, ev)
    crits = [math.log(1-k/N)/math.log((N-k*(1+a))/N) for k,a in spec]
    for alpha in sorted(set([0.19,0.45,0.75,1.0,1.3,2.0] +
                            [c*0.97 for c in crits]+[c*1.03 for c in crits])):
        Lpower = (U * (eig_pos**alpha)) @ U.T
        for j in range(N):
            for i in range(N):
                if i==j: continue
                # Generator is Metzler precisely on/below all critical powers.
                if alpha < min(crits)-1e-7:
                    check(Lpower[i,j] < 1e-10, 'wrong Markov sign')
        horizon = max(unique_horizon(N,k,a,alpha) for k,a in spec)
        for t in [0.001,0.02,0.1,0.5,1.0,4.0,horizon*0.4,horizon*1.5]:
            if t<=0: continue
            S = (U * np.exp(-t*(eig_pos**alpha))) @ U.T
            T = spectral_formula(N,groups,alpha,t)
            check(np.max(np.abs(S-T)) < 2e-10, 'matrix exponential formula')
            check(np.max(np.abs(S.sum(axis=1)-1)) < 1e-10, 'mass conservation')
            row_formula = 1.0
            for idx, a in groups:
                k = len(idx)
                lam = N-k*(1+a)
                F = k/N+(1-k/N)*math.exp(-(N**alpha)*t) - math.exp(-(lam**alpha)*t)
                row_formula = max(row_formula, 1+2*(1-1/k)*max(-F,0))
            check(abs(np.max(np.sum(np.abs(S),axis=1))-row_formula) < 2e-10,
                  'sharp endpoint norm')
            if horizon>0 and t < 0.4*horizon+1e-15:
                check(np.min(S)<-1e-10 or horizon<1e-8,
                      'expected transient negative entry')
            if t>1.5*horizon and horizon>0:
                check(np.min(S)>-1e-11, 'expected restored positivity')

# Critical-onset constants (independent positive-root calculation).
for N,k,a in [(8,2,0.2),(8,3,0.4),(11,4,0.4)]:
    q = 1-k/N
    lam = N-k*(1+a)
    crit = math.log(q)/math.log(lam/N)
    slope = 2*(N**(1-crit))*math.log(N/lam)/k
    for eps in [0.001,0.0005]:
        observed=unique_horizon(N,k,a,crit+eps)
        check(abs(observed/eps/slope-1) < 0.01,
              'linear onset coefficient')

# Near spectral degeneracy: the recovery delay diverges like lambda^{-alpha}.
N,k,alpha = 10,3,0.65
for lam in [0.05,0.01,0.003]:
    a=(N-k-lam)/k
    tau=unique_horizon(N,k,a,alpha)
    check(abs(tau*(lam**alpha)/math.log(N/k)-1)<0.03,
          'near-degeneracy slowing constant')

print(f'VERIFICATION_OK {COUNT}')
