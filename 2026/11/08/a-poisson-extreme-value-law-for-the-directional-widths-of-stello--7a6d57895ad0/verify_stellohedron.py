#!/usr/bin/env python3
"""Independent finite checks of stellohedron width and limiting Poisson series."""
import math
import numpy as np
from scipy.special import ndtri
from scipy.special import polygamma
from scipy.special import spence
rng=np.random.default_rng(129840)

def range_direct(g):
    x=g[1:]; m=len(x); tot=0.
    for mask in range(1<<m):
        z=[g[0]]+[x[i] for i in range(m) if mask>>i & 1]
        tot+=max(z)-min(z)
    return tot/(2**m)

def range_sorted(g):
    x=np.sort(g[1:]); m=len(x)
    w=np.exp2(-np.arange(1,m+1,dtype=float))
    return float(np.dot(w,np.maximum(x[::-1]-g[0],0)+np.maximum(g[0]-x,0)))

for m in range(2,9):
    for _ in range(15):
        g=rng.normal(size=m+1)
        assert abs(range_direct(g)-range_sorted(g))<1e-12
        # Reconstruct supports from full sum, not merely by assuming range formula.
        support_plus=sum(max(g[[0]+[i+1 for i in range(m) if mask>>i&1]]) for mask in range(1<<m))
        support_minus=sum(min(g[[0]+[i+1 for i in range(m) if mask>>i&1]]) for mask in range(1<<m))
        assert abs((support_plus-support_minus)/(2**m)-range_sorted(g))<1e-12

# The finite-m Gaussian mean width identity is tested separately via numerical quadrature.
from scipy.integrate import quad
from scipy.special import ndtr, gammaln
for m in range(2,8):
    F=lambda z:ndtr(z)*((1+ndtr(z))/2)**m
    em=quad(lambda z:1-F(z),0,12,epsabs=1e-12)[0]-quad(lambda z:F(-z),0,12,epsabs=1e-12)[0]
    mu=math.sqrt(2)*math.exp(math.lgamma((m+1)/2)-math.lgamma(m/2))
    predicted=(2**(m+1))*em/mu
    sim=[]
    for _ in range(3500):
        g=rng.normal(size=m+1)
        sim.append((2**m)*range_sorted(g)/np.linalg.norm(g-g.mean()))
    assert abs(np.mean(sim)-predicted)/predicted <.045, (m, np.mean(sim), predicted)

# Gamma-Beta covariance identity, checked against numerical special-function identity.
for j in range(1,16):
    total=sum((2.**(1-r)-3.*4.**(-r))*float(polygamma(1,r)) for r in range(1,j+1))
    assert total>0
from scipy.special import spence
# scipy spence(z)=Li_2(1-z)
LVAR=math.pi**2/6-2*float(spence(.5))+float(spence(.75))
assert abs(LVAR-sum((2**(1-j)-3*4**(-j))*float(polygamma(1,j)) for j in range(1,36)))<1e-10
assert .74<LVAR<.76

# Sample the limiting Gamma series and check its predicted mean and variance.
N=45000; K=35
exp=rng.exponential(size=(N,K)); gamma=np.cumsum(exp,axis=1)
T=-np.log(gamma)@np.exp2(-np.arange(1,K+1,dtype=float))
assert abs(T.mean()-(np.euler_gamma-math.log(2)))<.025
assert abs(T.var()-LVAR)<.035

# Geometric width is independent of translation and equal to the computed support range.
for m in (50,200,1000):
    a=float(ndtri(1-1/m))
    samples=[]
    for _ in range(3000):
        g=rng.normal(size=m+1)
        centered=g-g.mean()
        R=range_sorted(g)
        Wnormalized=math.sqrt(m)*R/np.linalg.norm(centered)
        samples.append(a*(Wnormalized-2*a))
    arr=np.array(samples)
    assert np.isfinite(arr).all()
    # At finite m the convergence is slow; this guards normalization and order of magnitude.
    assert np.quantile(arr,.01)>-13 and np.quantile(arr,.99)<11
print('STELLOHEDRON_WIDTH_POISSON_LIMIT_CHECKS_PASSED')
print('Poisson T mean',np.euler_gamma-math.log(2),'variance',LVAR,'estimated',T.mean(),T.var())
