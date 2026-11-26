"""Finite numerical cross-checks of the Bernstein--Durrmeyer spectral formulas.

These checks supplement, and do not replace, the analytical proof.
Requires numpy and scipy. Run: python check.py
"""
import math
import numpy as np
from scipy.special import roots_legendre, eval_legendre
from scipy.special import comb

def lamb(n, k):
    return float(math.prod((n+1-r)/(n+1+r) for r in range(1,k+1))) if k <= n else 0.0

def error(n):
    m=n+1
    return sum(math.exp(-k*(k+1))-lamb(n,k)**m for k in range(1,n+1)) + sum(math.exp(-k*(k+1)) for k in range(n+1,28))

checks=0
for n in range(1,13):
    nodes,weights=roots_legendre(2*n+8)
    xs=(nodes+1)/2
    ws=weights/2
    B=np.array([comb(n,j)*xs**j*(1-xs)**(n-j) for j in range(n+1)]).T
    K=(n+1)*B@B.T
    Q=np.array([np.sqrt(2*k+1)*eval_legendre(k,nodes) for k in range(n+3)]).T
    diag=(Q*ws[:,None]).T@K@(Q*ws[:,None])
    expected=np.diag([lamb(n,k) for k in range(n+3)])
    assert np.max(np.abs(diag-expected)) < 3e-10,(n,np.max(np.abs(diag-expected)))
    checks+=1
    assert (n/(n+2))**n > math.exp(-2)
    checks+=1
    for k in range(1,n+3):
        assert lamb(n,k)**(n+1) <= math.exp(-k*(k+1))+1e-14
        checks+=1
    m=n+1
    bound=(4/m**2)*sum((k*(k+1))**2*math.exp(-k*(k+1)) for k in range(1,28))
    assert error(n) <= bound+1e-12
    checks+=1

lim=sum((k*(k+1))**2*math.exp(-k*(k+1))/6 for k in range(1,28))
assert abs(lim-0.10524363373849793)<1e-12
checks+=1
for n in (20,40,80,160,320):
    assert abs((n+1)**2*error(n)-lim) < 0.006/n
    checks+=1
for n in (20,40,80,160):
    m=n+1
    lhs=m**2*(math.exp(-2)-(n/(n+2))**m)
    assert abs(lhs-2*math.exp(-2)/3)<0.10/m
    checks+=1
print(f"PASS: {checks} finite assertions; scaled trace limit = {lim:.15f}")
