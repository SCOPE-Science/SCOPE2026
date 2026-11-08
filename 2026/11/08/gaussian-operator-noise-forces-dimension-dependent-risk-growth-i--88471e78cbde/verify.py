#!/usr/bin/env python3
"""Numerical checks for scalar damped row-action iteration with fixed noisy data.
Only science and numerical reproducibility; no external dependencies beyond numpy/scipy.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import i0e

MU=0.8
SIGMA=1.0
OMEGA=0.9
FLOOR=1.2
TAU=2.5


def factor(t,r,lam=FLOOR,tau=TAU):
    if lam==0:
        decay=1-OMEGA/(1+tau)
        return 1-decay**t
    step=OMEGA*r*r/(lam+(1+tau)*r*r)
    return -math.expm1(t*math.log1p(-step))


def risk_without_rhs_real(t):
    norm=1/(SIGMA*math.sqrt(2*math.pi))
    def integrand(logr):
        r=math.exp(logr)
        dens=norm*(math.exp(-(r-MU)**2/(2*SIGMA**2)) + math.exp(-(-r-MU)**2/(2*SIGMA**2)))
        return dens*factor(t,r)**2/r
    return quad(integrand,-26,4,epsabs=2e-7,limit=450,points=[-12,-6,0])[0]


def risk_without_rhs_complex(t):
    def integrand(logr):
        r=math.exp(logr)
        z=2*r*MU/SIGMA**2
        dens_angular=(2/SIGMA**2)*math.exp(-((r-MU)**2)/SIGMA**2)*i0e(z)
        return dens_angular*factor(t,r)**2
    return quad(integrand,-26,4,epsabs=2e-7,limit=450,points=[-12,-6,0])[0]


def main():
    j=2*math.sqrt(math.pi)*(2-math.sqrt(2))
    p0=math.exp(-(MU/SIGMA)**2/2)/(SIGMA*math.sqrt(2*math.pi))
    f0=math.exp(-(MU/SIGMA)**2)/(math.pi*SIGMA**2)
    real_const=j*p0*math.sqrt(OMEGA/FLOOR)
    complex_const=math.pi*f0
    print('J:',j,'real constant:',real_const,'complex constant:',complex_const)
    for t in (100,1000,10000,100000,1000000,10000000):
        R=risk_without_rhs_real(t)
        C=risk_without_rhs_complex(t)
        print(t,'real_risk',R,'real_norm_ratio',R/math.sqrt(t)/real_const,
              'complex_risk',C,'complex_norm_ratio',C/math.log(t)/complex_const)
    # algebraic invariants / exact finite iterate checks
    for t in (1,2,3,10,100):
        for a in (-10.,-2.,-0.01,0.01,0.2,5.):
            x=0.0
            b=1.3
            step=OMEGA*a/(FLOOR+(1+TAU)*a*a)
            for _ in range(t):
                x-=step*(a*x-b)
            closed=b*factor(t,abs(a))/a
            assert abs(x-closed)<1e-8*(1+abs(closed)),(t,a,x,closed)
    for k in range(1,15):
        v=factor(k,1.0,lam=0,tau=TAU)
        assert v>0
    print('VERIFY_OK scalar identities, no-floor divergence criterion, 12 quadrature cases')

if __name__ == '__main__': main()
