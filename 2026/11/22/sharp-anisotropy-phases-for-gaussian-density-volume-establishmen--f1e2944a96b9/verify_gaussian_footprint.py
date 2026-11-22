#!/usr/bin/env python3
"""Deterministic checks of a Gaussian density-threshold footprint design theorem."""
import math
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import gammaln

nchecks = 0

def check(condition, msg='check failed'):
    global nchecks
    nchecks += 1
    if not condition:
        raise AssertionError(msg)


def ball_volume(d):
    return math.exp(.5*d*math.log(math.pi) - math.lgamma(.5*d+1))


def det_bounds(d, trace, K):
    mx = (trace / d)**(d/2)
    if K==1:
        return mx, mx, [0]
    vals = []
    for k in range(1,d):
        small = trace/(d+k*(K-1))
        vals.append((math.exp(.5*(d*math.log(small)+k*math.log(K))),k))
    low = min(v for v,_ in vals)
    which = [k for v,k in vals if abs(math.log(v/low))<1e-12]
    return low, mx, which


def required_mass(d, threshold, area, D):
    z = (area/(ball_volume(d)*D))**(2/d)
    return threshold*(2*math.pi)**(d/2)*D*math.exp(.5*z)


def prediction(d, trace, K, alpha, area):
    lo, hi, kk = det_bounds(d,trace,K)
    dc=area/(ball_volume(d)*d**(d/2))
    D = min(hi,max(lo,dc))
    return D, required_mass(d,alpha,area,D), kk


def footprint(d, alpha, N, D):
    v = math.log(N/(alpha*(2*math.pi)**(d/2)*D))
    return 0. if v<=0 else ball_volume(d)*D*(2*v)**(d/2)

rng=np.random.default_rng(0x45AB)
for d in range(2,10):
    for K in [1.0,1.1,1.5,3.0,10.0,100.0]:
        tr=0.5+0.3*d
        lo,hi,ks=det_bounds(d,tr,K)
        check(lo<=hi*(1+1e-12))
        if K>1:
            # Generic points of eigenvalue simplex, with the required condition-number cap.
            for _ in range(300):
                a=np.exp(rng.uniform(0,math.log(K),size=d))
                lam=tr*a/a.sum()
                D=math.exp(.5*sum(np.log(lam)))
                check(D>=lo-1e-10, f'd={d},K={K},D={D} < {lo}')
                check(D<=hi+1e-10)
        for frac in [.2, .8, 1.,1.3,2.5]:
            A = frac*ball_volume(d)*d**(d/2)*hi
            D, N, _=prediction(d,tr,K,1.25,A)
            check(abs(footprint(d,1.25,N,D)/A-1)<2e-12)
            numerical=minimize_scalar(lambda x:math.log(required_mass(d,1.25,A,math.exp(x))),
                                      bounds=(math.log(lo),math.log(hi)), method='bounded',
                                      options={'xatol':1e-12}) if lo<hi else None
            if numerical:
                check(math.log(N)<=numerical.fun+1e-10, f'bad optimum {d,K,frac}')
                check(abs(D-math.exp(numerical.x))<2e-4*hi)

# Exact 2D example with finite anisotropy ceiling.
d, tr, K, alpha, area=2,2.,9.,1.,math.pi
D, N, kk=prediction(d,tr,K,alpha,area)
N_iso=required_mass(d,alpha,area, tr/2)
check(abs(D-.6)<1e-12)
check(kk==[1])
check(8<N<9)
check(N<N_iso)
print('CHECKS',nchecks)
print('EXAMPLE: dimension=2, trace=2, K=9, alpha=1, area=pi')
print('minimum founder mass',format(N,'.12f'))
print('isotropic founder mass',format(N_iso,'.12f'))
print('reduction_fraction',format(1-N/N_iso,'.9f'))
print('min determinant sqrt',D,'covariance eigenvalues', [0.2,1.8])
