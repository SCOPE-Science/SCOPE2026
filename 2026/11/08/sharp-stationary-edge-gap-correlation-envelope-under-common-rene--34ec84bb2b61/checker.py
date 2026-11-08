"""Finite diagnostics for the sharp renewal-reset extreme-gap correlation theorem.
The exact inequalities and limiting statements are proved in RESULT.md, not by this code.
Run with Python 3, numpy and scipy: python checker.py
"""
import math
import numpy as np
from scipy.special import ndtri

rng = np.random.default_rng(20261103)
b = lambda n: float(ndtri(1-1/n))

def rho(m1, m15, m2):
    kappa = m15*m15/(m1*m2)
    return (9-8*kappa)/(18-8*kappa)

# Deterministic, memoryless, and increasingly two-point reset intervals.
assert abs(rho(1, 1, 1)-0.1)<1e-14
assert abs(rho(1, math.gamma(2.5), 2)-(4-math.pi)/(8-math.pi))<1e-14
Rvals=[2,4,10,100,1000,1000000]
vals=[]
for R in Rvals:
    p=R**(-1.5)
    m1=1-p+p*R
    m15=1-p+p*R**1.5
    m2=1-p+p*R**2
    v=rho(m1,m15,m2)
    vals.append(v)
    assert 0.1<v<0.5
assert all(x<y for x,y in zip(vals,vals[1:])),vals
assert vals[-1]>.49, vals[-1]

# Cauchy-Schwarz moment inequality and lower/upper correlation limits.
for _ in range(10000):
    t=np.exp(rng.normal(size=4)*rng.uniform(.01,5))
    weights=rng.dirichlet(np.ones(4))
    m1=float(np.dot(weights,t));m15=float(np.dot(weights,t**1.5));m2=float(np.dot(weights,t*t))
    assert m15*m15<=m1*m2*(1+1e-12)
    assert 0.1-1e-12<=rho(m1,m15,m2)<.5

# Exact finite-N cancellation of common renewal age in an energy-normalized gap.
for n in (4,13,300,1500):
    for _ in range(30):
        z=rng.normal(size=n)
        age1=rng.uniform(.0001, 1)
        age2=rng.uniform(.0001, 1000)
        def norm_gap(age):
            x=np.sqrt(age)*z
            top=np.sort(x)[-4:][::-1]
            return (np.arange(1,4)*b(n)*(top[:-1]-top[1:])/
                    np.sqrt(np.mean(x*x)))
        assert np.allclose(norm_gap(age1),norm_gap(age2),rtol=2e-12,atol=2e-12)

# Finite population simulation of gap correlation for deterministic and exponential clocks.
n=7000; trials=8000; m=2
z_means=[]; gap_batches=[]
for i in range(0,trials,100):
    z=rng.normal(size=(100,n))
    top=np.sort(np.partition(z, n-m-1, axis=1)[:,n-m-1:],axis=1)[:,::-1]
    gaps=(np.arange(1,m+1)[None,:]*b(n)*(top[:,:-1]-top[:,1:]))
    gap_batches.append(gaps)
gaps=np.concatenate(gap_batches)
assert np.max(np.abs(gaps.mean(axis=0)-1)) < .11
for name, age, theory, tol in (
    ('periodic',rng.uniform(size=trials),.1,.075),
    ('Poisson',rng.exponential(size=trials),(4-math.pi)/(8-math.pi),.08)):
    w=gaps*np.sqrt(age)[:,None]
    empirical=np.corrcoef(w.T)[0,1]
    assert abs(empirical-theory)<tol, (name, empirical, theory)
    print(name, 'sample correlation', empirical, 'limit', theory)
print('PASS: 10000 randomized moment inequality checks; exact endpoint formulas; 120 scale-invariance checks; 16000 gap rows')
print('two-point upper endpoint rho:',vals[-1])
