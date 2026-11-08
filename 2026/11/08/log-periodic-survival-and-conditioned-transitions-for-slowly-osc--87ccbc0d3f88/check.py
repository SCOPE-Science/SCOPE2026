#!/usr/bin/env python3
"""Reproduce exact two-state coefficients and finite-horizon diagnostics.

All inequalities about infinite horizons are proved analytically in RESULT.md.
This program is a finite, independent check, not an infinite certificate.
"""
from fractions import Fraction as F
from math import cos, exp, log, sin

checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

def dot(v, w):
    return sum((a * b for a, b in zip(v,w)), F(0))

K = [[F(1,2), F(1,4)], [F(1,4), F(1,2)]]
B = [[F(1,8), F(0)], [F(0), F(0)]]
lam = F(3,4)
Q = [[z/lam for z in row] for row in K]
A = [[z/lam for z in row] for row in B]
pi = [F(1,2),F(1,2)]
g = [sum(row) for row in A]
kappa = dot(pi,g)
u = [F(1,8), F(-1,8)]
C = [[A[i][j] + Q[i][j]*(u[j]-u[i]-kappa)
      for j in range(2)] for i in range(2)]
check(lam == F(3,4), 'Perron eigenvalue')
check(all(sum(row)==lam for row in K), 'right Perron eigenvector')
check(all(dot(pi,[Q[i][j] for i in range(2)])==pi[j] for j in range(2)), 'stationary row')
check(all(sum(row)==1 for row in Q), 'Doob rows')
check(all(sum(row) <= 1 for row in K), 'sub-stochastic rows')
check(all(sum(row) <= 1 for row in [[K[i][j]+B[i][j] for j in range(2)] for i in range(2)]), 'uniform bound')
check(kappa==F(1,12), 'mean modulation')
check(all(u[i]-sum(Q[i][j]*u[j] for j in range(2))==g[i]-kappa for i in range(2)), 'Poisson equation')
check(dot(pi,u)==0,'centered Poisson solution')
check(C==[[F(1,9),-F(1,9)],[F(1,18),-F(1,18)]],'conditioned response matrix')
check(all(sum(row)==0 for row in C),'response rows conserve mass')

# Backward harmonic recursion with terminal normalizing profile.  The
# finite-horizon approximations allow a non-asymptotic numerical check.
def next_horizon(horizon, sample_indices):
    h = [exp(-float(kappa)*sin(log(horizon)))]*2
    results={}
    for n in range(horizon-1, 0, -1):
        f=cos(log(n))/n
        fn=[[float(Q[i][j])+float(A[i][j])*f for j in range(2)] for i in range(2)]
        if n in sample_indices:
            den=[sum(fn[i][j]*h[j] for j in range(2)) for i in range(2)]
            transformed=[[fn[i][j]*h[j]/den[i] for j in range(2)] for i in range(2)]
            results[n]=transformed
        h=[sum(fn[i][j]*h[j] for j in range(2)) for i in range(2)]
    return h, results

samples=[100, 200, 300, 500, 750, 1000, 1500, 2200, 4000, 7500]
h_early, transformed=next_horizon(150000,set(samples))
for n in samples:
    for i in range(2):
        for j in range(2):
            prediction=float(Q[i][j])+cos(log(n))*float(C[i][j])/n
            error=abs(transformed[n][i][j]-prediction)
            check(error <= 5/n**2, f'first order discrepancy n={n} i={i} j={j} error={error}')
    check(all(abs(sum(transformed[n][i])-1)<1e-11 for i in range(2)), 'stochastic conditioned rows')

# Compute the survival amplitude normalized by the predicted log-periodic
# scalar, using rescaled products to avoid exponential underflow.
def amplitude(horizon, initial_state):
    row=[0.0,0.0]; row[initial_state]=1.0
    log_norm=0.0
    for n in range(1,horizon):
        f=cos(log(n))/n
        new=[sum(row[i]*(float(Q[i][j])+f*float(A[i][j])) for i in range(2)) for j in range(2)]
        mass=sum(new)
        log_norm+=log(mass)
        row=[z/mass for z in new]
    return exp(log_norm-float(kappa)*sin(log(horizon)))

amps=[]
for n in (500,1000,2000,4000,8000,16000):
    amps.append(amplitude(n,0))
check(max(amps[-3:])-min(amps[-3:]) < 3e-5,'normalized survival amplitude settles')
check(all(a>0 for a in amps),'survival amplitudes positive')
print('CHECKS_PASSED',checks)
print('EXACT_RESPONSE',[[str(z) for z in row] for row in C])
print('SURVIVAL_AMPLITUDES',[round(z,9) for z in amps])
print('LIMITATIONS: finite-horizon checks do not prove asymptotic theorems')
