"""Independent numerical and algebraic checks for a Poisson-kernel null limit.
Run: python check.py
Only standard scientific Python packages are required.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import beta, gammaln

checks=0

def check(got, expected, rtol=2e-8, atol=2e-10, label=''):
    global checks
    checks += 1
    if not np.isclose(got, expected, rtol=rtol, atol=atol):
        raise AssertionError(f'{label}: got={got}, expected={expected}')


def cap_density_coefficient(q):
    return math.exp(gammaln((q+1)/2)-gammaln(q/2))/math.sqrt(math.pi)


def kernel(q, rho, theta):
    den=(1-rho)**2+2*rho*(1-math.cos(theta))
    return (1-rho*rho)/den**((q+1)/2)


def limit_cumulant(q, c, k):
    return 4**(k-1)*cap_density_coefficient(q)*beta(q/2, (k*(q+1)-q)/2)/c**(q*(k-1))

# Independently integrate the actual spherical-angle density and compare the
# harmonic semigroup identity for a selection of dimensions and bandwidths.
for q in range(1,6):
    a=cap_density_coefficient(q)
    for rho,sigma in [(0.12,0.27),(0.35,0.63),(0.71,0.78)]:
        integ=quad(lambda theta: a*math.sin(theta)**(q-1)*kernel(q,rho,theta)*kernel(q,sigma,theta), 0, math.pi, epsabs=1e-10, epsrel=1e-10, limit=250)[0]
        check(integ,(1+rho*sigma)/(1-rho*sigma)**q,label='cross-kernel')
        norm=quad(lambda theta: a*math.sin(theta)**(q-1)*kernel(q,rho,theta),0,math.pi,epsabs=1e-11,limit=250)[0]
        check(norm,1,label='unit-mass')

# Independently integrate the proposed joint Poisson shot-noise covariance.
for q in range(1,7):
    a=cap_density_coefficient(q)
    for c,d in [(0.4,0.4),(0.5,1.7),(1.0,3.0),(2.0,7.0)]:
        fn=lambda t: (a/2)*t**(q-1)*16*c*d/((c*c+t*t)*(d*d+t*t))**((q+1)/2)
        integ=quad(fn, 0, np.inf, epsabs=2e-11, epsrel=2e-11)[0]
        check(integ,4/(c+d)**q,rtol=1e-9,label='shot-cov')
        check(integ/math.sqrt(limit_cumulant(q,c,2)*limit_cumulant(q,d,2)),(2*math.sqrt(c*d)/(c+d))**q,label='log-correlation')
    for c in [0.2,1.0,3.1]:
        check(limit_cumulant(q,c,1),1,label='shot-mean')
        check(limit_cumulant(q,c,2),4/(2*c)**q,label='shot-variance')
        for k in [3,4,5]:
            fn=lambda t:(a/2)*t**(q-1)*(4*c/(c*c+t*t)**((q+1)/2))**k
            integ=quad(fn,0,np.inf,epsabs=2e-10,epsrel=2e-10)[0]
            check(integ,limit_cumulant(q,c,k),rtol=3e-8,label='higher cumulant')

# Finite-n exact covariance, divided by n^2, approaches the full critical
# covariance in dimensions q=1,...,5 without extraneous rescaling.
for q in range(1,6):
    for c,d in [(0.5,1),(1,1),(1,2)]:
        prev=None
        for n in (300,3000,30000):
            rho=1-c*n**(-2/q)
            sigma=1-d*n**(-2/q)
            if not 0<rho<1 or not 0<sigma<1: continue
            exact=2*(n-1)/n**3*((1+rho*sigma)/(1-rho*sigma)**q-1)
            limit=4/(c+d)**q
            if prev is not None: check(abs(exact-limit)<=abs(prev-limit)+1e-8,True,label='finite-n-convergence')
            prev=exact

# A direct Monte Carlo check of the rare close-pair count for the circle.
# This validates the geometric scale, not an infinite-dimensional proof.
rng=np.random.default_rng(20261115)
for q in (1,2):
    n=140
    L=2.0
    a=cap_density_coefficient(q)
    if q==1:
        theta=rng.uniform(0,2*np.pi,(1500,n))
        ds=np.abs(theta[:,:,None]-theta[:,None,:]); ds=np.minimum(ds,2*np.pi-ds)
    else:
        v=rng.standard_normal((1500,n,3)); v/=np.linalg.norm(v,axis=2,keepdims=True)
        dots=np.einsum('bik,bjk->bij',v,v)
        ds=np.arccos(np.clip(dots,-1,1))
    counts=np.count_nonzero(np.triu(ds<=L*n**(-2/q),1),axis=(1,2))
    mean_target=a*L**q/(2*q)
    check(np.mean(counts),mean_target,rtol=0.18,atol=0.04,label='close-pair-rate')
    check(np.mean(counts==0),math.exp(-mean_target),rtol=0.13,atol=0.04,label='close-pair-void')

print(f'PASS: {checks} numerical or algebraic assertions')
print('Critical scaling: rho_n(c)=1-c*n**(-2/q)')
print('Limit covariance: 4/(c+d)**q; normalized correlation: (2*sqrt(c*d)/(c+d))**q')
for q in (1,2,3):
    print('q=',q,'variance at c=1:',limit_cumulant(q,1,2),'third cumulant:',limit_cumulant(q,1,3))
