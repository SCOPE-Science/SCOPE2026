"""Deterministic numerical checks for a collective rightmost-reset model.

These checks are finite diagnostics, not a proof of the infinite-time theorem.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr

PHI = lambda z: math.exp(-z*z/2)/math.sqrt(2*math.pi)

def m_n(n):
    return quad(lambda z: n*z*PHI(z)*ndtr(z)**(n-1),-12,12,epsabs=1e-12)[0]

def threshold(n,D,r):
    return math.sqrt(math.pi*D*r/2)*m_n(n)

assert abs(m_n(1)) < 1e-11
assert abs(m_n(2)-1/math.sqrt(math.pi)) < 1e-11
assert abs(m_n(3)-3/(2*math.sqrt(math.pi))) < 1e-11
assert abs(threshold(2,2.,3.)-math.sqrt(3.)) < 1e-10
assert all(m_n(i+1)>m_n(i) for i in range(1,10))
# Conditional Gaussian-maximum identity versus direct independent sampling.
rng=np.random.default_rng(20261119)
for n in [2,3,5,9]:
    T=rng.exponential(scale=1/3,size=70000)
    X=rng.standard_normal((T.size,n))
    Y=-0.37*T+np.sqrt(4*T)*np.max(X,axis=1)
    expected=threshold(n,2.,3.)/3.-0.37/3.
    standard_error=Y.std(ddof=1)/math.sqrt(len(Y))
    assert abs(Y.mean()-expected)<5.5*standard_error,(n,Y.mean(),expected,standard_error)
print('PASS: normal-maximum integrals, monotone critical drifts, 4 independent endpoint-skeleton Monte Carlo checks.')
for n in [1,2,3,4,10]: print(f'n={n}  m_n={m_n(n):.12f}  vcrit(D=r=1)={threshold(n,1,1):.12f}')
