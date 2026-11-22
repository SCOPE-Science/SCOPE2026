#!/usr/bin/env python3
"""Independent finite-ring Markov-chain and exact-algebra checks of stationary spin correlations."""
from fractions import Fraction
from math import isclose
import numpy as np
import sympy as sp
from scipy.linalg import solve

checks = 0

def check(condition, explanation):
    global checks
    if not condition: raise AssertionError(explanation)
    checks += 1

q=sp.symbols('q',positive=True)
r=(1-q)**2/q
for N in (5,6,7,8,13):
    C=lambda d:(q**d+q**(N-d))/(1+q**N)
    for d in range(1,N):
        check(sp.cancel(C(d-1)+C(d+1)-(2+r)*C(d))==0, f'pair recurrence N={N} d={d}')
    Ueq=(q**2+q**(N-2))/(1+q**N)
    Veq=(q**3+q**(N-3))/(1+q**N)
    gap=sp.factor(2*C(1)+C(3)+Veq-(4+r)*Ueq)
    desired=(1-q)**2*(q+q**(N-3))/(1+q**N)
    check(sp.cancel(gap-desired)==0, f'Gibbs four-spin residual N={N}')
    for qc in (sp.Rational(1,4),sp.Rational(1,3),sp.Rational(1,2),sp.Rational(2,3),sp.Rational(3,4)):
        check(desired.subs(q,qc)>0, f'gap positivity N={N}')

for qc in (sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4)):
    rc=(1-qc)**2/qc
    check(sp.cancel((2+rc)*qc-1-qc**2)==0,'infinite pair root')
    check(sp.cancel((4+rc)*qc**2-qc**3-(2*qc+qc**3)+qc*(1-qc)**2)==0,'infinite fourth identity')

# Finite continuous-time voter chain plus full global reset to fresh fair independent spins.
# This calculation uses the 2**N state Markov matrix without assuming the claimed correlation formulas.
for N in (5,6,7):
    m=1<<N
    Q=np.zeros((m,m),dtype=float)
    for state in range(m):
        for i in range(N):
            si=(state>>i)&1
            changes=int(si!=((state>>((i-1)%N))&1))+int(si!=((state>>((i+1)%N))&1))
            rate=changes/2.
            other=state ^ (1<<i)
            Q[state,other]+=rate
            Q[state,state]-=rate
    check(np.max(abs(Q.sum(axis=1)))<1e-13,f'row-sum N={N}')
    sgn=lambda z,i: 1 if (z>>(i%N))&1 else -1
    for qc in (0.25,0.5,0.75):
        rc=(1-qc)**2/qc
        pi=solve(rc*np.eye(m)-Q.T, np.full(m,rc/m),assume_a='gen',check_finite=True)
        check(abs(pi.sum()-1)<1e-11, f'mass N={N} q={qc}')
        check(pi.min()>0, f'strictly-positive law N={N} q={qc}')
        obs=lambda *i:sum(float(p)*np.prod([sgn(s,j) for j in i]) for s,p in enumerate(pi))
        c=lambda d:(qc**d+qc**(N-d))/(1+qc**N)
        for d in range(1,N):
            check(abs(obs(0,d)-c(d))<1e-10,f'pair N={N} d={d} q={qc}')
        U=obs(0,1,2,3)
        V=obs(N-1,1,2,3)
        Ug=(qc**2+qc**(N-2))/(1+qc**N)
        Vg=(qc**3+qc**(N-3))/(1+qc**N)
        residual=(4+rc)*(U-Ug)-(V-Vg)
        target=(1-qc)**2*(qc+qc**(N-3))/(1+qc**N)
        check(abs(residual-target)<1e-10,f'four-spin N={N} q={qc}')
        check(max(abs(U-Ug),abs(V-Vg))>=target/(5+rc)-1e-10,f'defect bound N={N}')

print(f'PASS {checks} assertions (symbolic identities, positivity and independently solved finite Markov chains)')
