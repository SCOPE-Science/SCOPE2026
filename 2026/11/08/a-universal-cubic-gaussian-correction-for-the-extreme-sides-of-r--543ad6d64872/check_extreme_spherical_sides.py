#!/usr/bin/env python3
"""Numerical checks for fixed-three-point spherical extreme-side asymptotics.

Requires numpy and scipy. Finite sampling and quadrature, not mathematical proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln, ndtr


def density_one(d, r):
    c = math.exp(math.lgamma(d/2)-0.5*math.log(math.pi)-math.lgamma((d-1)/2))
    return c * max(0., 1-r*r)**((d-3)/2)


def exact_right_angle(d):
    # From planar rotational symmetry: Pr(two fresh cap events | inner product r)
    return quad(lambda r: density_one(d,r)*(0.25+math.asin(r)/(2*math.pi)),0.,1.,epsabs=2e-11)[0]


def simulate(d,t,n=120000,seed=100):
    rng=np.random.default_rng(seed+d)
    successes_max=successes_min=0
    threshold=-math.sin(t/math.sqrt(d))
    for start in range(0,n,3000):
        k=min(3000,n-start)
        x=rng.normal(size=(k,3,d))
        x/=np.linalg.norm(x,axis=2,keepdims=True)
        a=np.einsum('ij,ij->i',x[:,0,:],x[:,1,:])
        b=np.einsum('ij,ij->i',x[:,0,:],x[:,2,:])
        c=np.einsum('ij,ij->i',x[:,1,:],x[:,2,:])
        successes_max+=int(np.count_nonzero((a>=threshold)&(b>=threshold)&(c>=threshold)))
        successes_min+=int(np.count_nonzero((a>=threshold)|(b>=threshold)|(c>=threshold)))
    return successes_max/n,successes_min/n


def main():
    assert abs(exact_right_angle(3) - (0.25 - 1/(4*math.pi))) < 2e-10
    phi0=(2*math.pi)**-0.5
    for d in (8,32,128,512):
        p=exact_right_angle(d)
        pred=.125+phi0**3/math.sqrt(d)
        assert abs(p-pred) < 0.12/d
        print('exact_right_angle',d,round(p,9),'two_term',round(pred,9))
    for d,t in ((16,-.5),(32,0.),(128,.65)):
        max_est,min_est=simulate(d,t)
        phi=math.exp(-t*t/2)/math.sqrt(2*math.pi)
        pred_max=ndtr(t)**3+phi**3/math.sqrt(d)
        pred_min=1-ndtr(-t)**3+phi**3/math.sqrt(d)
        assert abs(max_est-pred_max)<.04
        assert abs(min_est-pred_min)<.04
        print('sample',d,t,round(max_est,6),round(min_est,6),round(pred_max,6),round(pred_min,6))
    print('SPHERICAL_THREE_SIDE_CUBIC_CORRECTION_OK')


if __name__=='__main__':
    main()
