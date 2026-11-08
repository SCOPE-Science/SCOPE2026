#!/usr/bin/env python3
"""Reproducibility checks for Euclidean clearance to the 1-skeleton of a cube."""
import math
import numpy as np
import itertools
from scipy.integrate import quad
from scipy.special import gamma

def cdf_3(r):
    if r <= 0: return 0.0
    if r <= 1: return 3*math.pi*r*r/4 - math.sqrt(2)*r**3
    if r < math.sqrt(2):
        return (3*r*r*(math.asin(1/r)-math.pi/4)
                -math.sqrt(2)*r**3+(2*r*r+1)*math.sqrt(r*r-1))
    return 1.0

def cdf_3_quad(r):
    if r<=0: return 0
    upper=min(1.,r)
    pivot=min(upper,r/math.sqrt(2))
    I1=quad(lambda v:(1-v)*v,0,pivot,epsabs=1e-13)[0]
    I2=quad(lambda v:(1-v)*math.sqrt(max(0.,r*r-v*v)),pivot,upper,epsabs=1e-13)[0]
    return 6*(I1+I2)

def cdf_general_d(r,d):
    assert d>=3
    omega=lambda n: math.pi**(n/2)/gamma(n/2+1)
    A=d*omega(d-1)/2**(d-1)
    # B from spherical Monte Carlo? not needed for special d=3
    assert d==3
    B=math.sqrt(2)
    ans=A*r**(d-1)-B*r**d
    if r>1:
        ans+=math.factorial(d)*omega(d-2)/(2**(d-2)*math.factorial(d-2))*quad(lambda t:(t-1)*(r*r-t*t)**((d-2)/2),1,r,epsabs=1e-12)[0]
    return ans

def run():
    rng=np.random.default_rng(20261107)
    N=1200000
    x=rng.random((N,3))
    gaps=2*np.minimum(x,1-x) # normalized by half side
    gaps.sort(axis=1)
    r=np.linalg.norm(gaps[:,:2],axis=1)
    for t in [0.15,0.3,0.5,0.75,0.99,1.,1.01,1.05,1.12,1.2,1.3,1.4]:
        target=cdf_3(t)
        q=cdf_3_quad(t)
        q2=cdf_general_d(t,3)
        empirical=float(np.mean(r<=t))
        error=abs(empirical-target)
        assert abs(target-q)<3e-10,(t,target,q)
        assert abs(target-q2)<3e-10,(t,target,q2)
        assert error<0.004,(t,error)
        print(f'r={t:.3f} analytic={target:.9f} integral={q:.9f} empirical={empirical:.9f}')
    def poly(t):return 3*math.pi*t*t/4 -math.sqrt(2)*t**3
    for e in [0.05,0.03,0.015,0.007]:
        q=(cdf_3(1+e)-poly(1+e))/e**2.5
        print('delta',e,'cusp_ratio',q, 'expected',8*math.sqrt(2)/5)
        assert abs(q-8*math.sqrt(2)/5)<0.5
    # Directly enumerate all finite cube edges to check the key geometric lemma.
    for d in (3,4,5):
        pts=rng.random((125,d))
        gap=2*np.minimum(pts,1-pts)
        gap.sort(axis=1)
        formula=np.sqrt(np.sum(gap[:,:d-1]**2,axis=1))/2
        brute=np.full(len(pts),np.inf)
        for free in range(d):
            other=[i for i in range(d) if i!=free]
            for bits in itertools.product((0.,1.),repeat=d-1):
                end=np.asarray(bits)
                ds=np.sum((pts[:,other]-end)**2,axis=1)
                brute=np.minimum(brute,np.sqrt(ds))
        assert np.max(abs(brute-formula))<3e-15
        # An independent Monte Carlo check of the exact squared-distance moment.
        z=rng.random((200000,d))
        gaps=np.minimum(z,1-z)
        exact_squared=np.sum(gaps**2,axis=1)-np.max(gaps**2,axis=1)
        expected=d*(d-1)/(12*(d+2))
        assert abs(float(np.mean(exact_squared))-expected)<0.002
        print('dimension',d,'mean_square',float(np.mean(exact_squared)),'exact',expected)
    # Exact analytical coefficient of the first clipping correction.
    def omega(k):return math.pi**(k/2)/gamma(k/2+1)
    for d in range(3,9):
        K=4*(d-1)*omega(d-2)/((d+2)*2**((d-2)/2))
        delta=.006
        cap=d*(d-1)*omega(d-2)/2**(d-2)*quad(
            lambda t:(t-1)*((1+delta)**2-t*t)**((d-2)/2),
            1,1+delta,epsabs=1e-14)[0]
        assert abs(cap/(K*delta**((d+2)/2))-1)<0.03
    # exact E squared in unit side cube: each gap U_i uniform [0,1/2],
    # min squared pair = sum U_i^2 - max_i U_i^2
    exact=3/12 - (3/5)/4
    empirical2=float(np.mean((r/2)**2))
    print('second moment exact',exact,'empirical',empirical2)
    assert abs(empirical2-exact)<0.002
    print('CUBIC_EDGE_CLEARANCE_EXACT_DISTRIBUTION_OK',N)

if __name__=='__main__':run()
