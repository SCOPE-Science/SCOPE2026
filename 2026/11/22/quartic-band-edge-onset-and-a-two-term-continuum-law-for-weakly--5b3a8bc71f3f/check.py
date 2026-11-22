"""Finite diagnostics for a half-line Jacobi spectral asymptotic; not a proof.
Dependencies: Python 3.10+, NumPy 1.24+, SciPy 1.10+.
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq

checks = 0

def ck(condition, label):
    global checks
    assert condition, label
    checks += 1

def thresholds(m):
    return [1/math.cos((2*j-1)*math.pi/(2*(m+1)))
            for j in range(1,(m+1)//2+1)]

def eigs(m, t, n=600):
    weights = np.ones(n-1)
    weights[:m] = t
    return eigh_tridiagonal(np.zeros(n), weights, select='i',
                            select_range=(n-15,n-1),eigvals_only=True)

# Exact finite-prefix count checked well away from finite-section band-edge contamination.
for m in range(1,11):
    for t in [1.03,1.10,1.25,1.5,2.0,3.0,5.0]:
        expected = sum(t > tc+1e-8 for tc in thresholds(m))
        observed = sum(lam > 2.0001 for lam in eigs(m,t))
        if any(abs(t-tc) < .025 for tc in thresholds(m)):
            continue  # do not use a finite truncation to decide near-threshold modes
        ck(observed == expected, f'finite-count {m=} {t=} {expected=} {observed=}')

# Continuum mode roots, with no numerical use of finite-section edge eigenvalues.
for alpha in [1.5,3.0,8.0,20.0,50.0]:
    for j in range(1,6):
        lo=(j-.5)*math.pi
        hi=min(j*math.pi, math.sqrt(2*alpha))
        if hi <= lo: continue
        def f(s):
            return s*math.cos(s)+math.sqrt(max(0,2*alpha-s*s))*math.sin(s)
        s=brentq(f,lo,hi)
        k=math.sqrt(2*alpha-s*s)
        coefficient=2*k*s*s/(1+k)
        ck(k>0 and coefficient>0,f'continuum root {alpha=} {j=}')
        for m in [100,300,700]:
            t=1+alpha/m**2
            def match(k2):
                z=math.cosh(k2/m)/t
                theta=math.acos(z)
                return t*math.sin(m*theta)-math.exp(k2/m)*math.sin((m+1)*theta)
            km=brentq(match,max(0,k-.3),min(math.sqrt(2*alpha),k+.3))
            lam=2*math.cosh(km/m)
            drift=m**3*(lam-2-k*k/m**2)
            ck(abs(drift/coefficient-1)< max(.4, 200/m),
               f'noncritical drift {alpha=} {j=} {m=}')

# Quartic critical edge: use the exact scalar equation to avoid finite-section artifacts.
for j in range(1,5):
    a=(2*j-1)**2*math.pi**2/8
    for m in [100,300,700]:
        t=1+a/m**2
        def match(k):
            z=math.cosh(k/m)/t
            theta=math.acos(z)
            return t*math.sin(m*theta)-math.exp(k/m)*math.sin((m+1)*theta)
        k=brentq(match,0,min(1.2,3*a/m))
        ratio=(2*math.cosh(k/m)-2)*m**4/(4*a*a)
        ck(.25<ratio<1.05,f'critical quartic {j=} {m=} {ratio=}')
print(f'WEAK_BLOCK_EDGE_DIAGNOSTIC_OK {checks}')
