#!/usr/bin/env python3
"""Standalone finite checks for exponential-edge FPP on clique bouquets.
Uses exact rational arithmetic for the critical pole, tilted moments, and independent
phase-type matrix evaluation for representative finite flooding times.
"""
from fractions import Fraction as F
from math import log, log1p, exp, prod, isclose
from itertools import combinations
import numpy as np
from scipy.linalg import expm

checks=0
for k in range(2,81):
    # Every infectious vertex has an edge to each susceptible vertex.
    vertex_set=set(range(k+1))
    for j in range(1,k+1):
        for infected in combinations(range(k+1), j):
            if 0 not in infected: continue
            boundary=sum(1 for x in infected for y in vertex_set.difference(infected) if x != y)
            assert boundary == j*(k+1-j)
            checks += 1
        # The exhaustive subsets remain feasible through k=15. For larger k
        # only the simpler boundary-rate identity is checked algebraically.
        if k>=15: break
    rates=[F(j*(k+1-j),k) for j in range(1,k+1)]
    assert rates[0]==rates[-1]==1
    checks+=1
    if k>=3:
        assert min(rates[1:-1]) > 1
        checks+=1
    A=F(1)
    mu=F(0)
    var=F(0)
    for rate in rates[1:-1]:
        A*=rate/(rate-1)
        mu+=1/(rate-1)
        var+=1/(rate-1)**2
    assert A==(k-1)**2
    assert mu==F(2*k,k-1)*sum((F(1,j) for j in range(1,k-1)),F(0))
    assert var<40
    assert abs(2*log(k-1)-float(mu))<6
    checks+=4

# An independent phase-type evaluation of the hypoexponential distribution.
# This is not used as an infinite proof.
for k in range(2,19):
    rates=np.array([j*(k+1-j)/k for j in range(1,k+1)],dtype=float)
    Q=np.diag(-rates)
    for j in range(k-1): Q[j,j+1]=rates[j]
    for m in (10**3,10**5,10**7):
        y=2*log(k-1)+log(m)+log(log(m))
        survival=float(expm(Q*y)[0,:].sum())
        assert 0 < survival < 1
        assert 0.4 < m*survival < 1.8,(k,m,m*survival)
        checks+=2

# Exact independent checks for the two-slowest-gap case k=2.
for y in (F(1,4),F(2,3),F(3,2),F(5,1)):
    yy=float(y)
    surv=(1+yy)*exp(-yy)
    Q=np.array([[-1.,1.],[0.,-1.]])
    matrix_surv=float(expm(Q*yy)[0,:].sum())
    assert isclose(surv,matrix_surv,rel_tol=1e-13)
    checks+=1
print('VERIFY_OK',checks,'assertions')
