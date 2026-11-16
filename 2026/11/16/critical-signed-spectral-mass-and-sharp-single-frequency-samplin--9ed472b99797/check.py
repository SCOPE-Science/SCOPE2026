#!/usr/bin/env python3
"""Supplementary reproducibility checks for a compact ball-power Fourier kernel.
Run with Python 3, NumPy, and SciPy. These finite checks are not a proof of infinite asymptotics.
"""
import math
import numpy as np
from scipy.special import jv, gamma
from scipy.integrate import quad, simpson

def spectrum(d, beta, r):
    if r == 0:
        return math.pi**(d/2)*gamma(beta+1)/gamma(d/2+beta+1)
    return (2*math.pi)**(d/2)*2**beta*gamma(beta+1)*r**(-d/2-beta)*jv(d/2+beta,r)

def direct_radial(d,beta,r):
    nu=d/2-1
    if r == 0:
        return 2*math.pi**(d/2)/gamma(d/2)*quad(lambda s:(1-s*s)**beta*s**(d-1),0,1,epsabs=1e-12)[0]
    return (2*math.pi)**(d/2)*r**(1-d/2)*quad(lambda s:(1-s*s)**beta*jv(nu,r*s)*s**(d/2),0,1,epsabs=1e-11)[0]

def A(d):
    return 4*gamma((d+1)/2)/(math.pi**1.5*gamma(d/2))

def V_trunc(d,beta,R,step=0.015):
    r=np.linspace(0,R,round(R/step)+1)
    # use Bessel radial integrand to avoid singularity at 0
    nu=d/2+beta
    f=np.zeros_like(r)
    f[1:]=r[1:]**(d/2-beta-1)*abs(jv(nu,r[1:]))
    C=(2*math.pi)**(d/2)*2**beta*gamma(beta+1)
    surf=2*math.pi**(d/2)/gamma(d/2)
    return surf*C/(2*math.pi)**d*simpson(f,x=r)

checks=0
for d in [1,2,3,4]:
    for beta in [.5,1.25,2.75]:
        for r in [0,.4,2.5,8.5]:
            a=spectrum(d,beta,r)
            b=direct_radial(d,beta,r)
            assert abs(a-b)<2e-9*(1+abs(b)),(d,beta,r,a,b)
            checks+=1
for d in [1,2,3,4]:
    bc=(d-1)/2
    S=2*math.pi**(d/2)/gamma(d/2)
    C=(2*math.pi)**(d/2)*2**bc*gamma(bc+1)*math.sqrt(2/math.pi)
    assert abs(S*C*2/math.pi/(2*math.pi)**d-A(d)) < 1e-12
    checks+=1
# At the critical index the slope converges to the predicted constant.
for d in [2,3]:
    bc=(d-1)/2
    vals=[V_trunc(d,bc,R) for R in [100,300,900]]
    slopes=[(vals[j+1]-vals[j])/math.log([100,300,900][j+1]/[100,300,900][j]) for j in [0,1]]
    assert all(abs(s-A(d))<.012 for s in slopes),(d,slopes,A(d))
    checks+=2
# A finite critical-window check with errors of order one.
for d in [2,3]:
    for lam in [-1,0,1]:
        R=900
        beta=(d-1)/2+lam/math.log(R)
        val=V_trunc(d,beta,R)
        F=-math.expm1(-lam)/lam if lam else 1
        print("window",d,lam,"actual",val,"leading",A(d)*math.log(R)*F,"remainder",val-A(d)*math.log(R)*F)
        assert abs(val-A(d)*math.log(R)*F)<3.5,(d,lam,val)
        checks+=1
print('PASS',checks,'independent radial integration, normalization, critical slope, and window checks')
for d in [2,3,4]:print('d',d,'critical_beta',(d-1)/2,'residue',A(d))
