#!/usr/bin/env python3
"""Finite numerical checks for the finite-memory switching optimum theorem.

Dependencies: numpy >= 1.24 and scipy >= 1.10. The infinite assertions
are established analytically in RESULT.md, not by numerical tests.
"""
import math
import numpy as np
from scipy.special import roots_laguerre
from scipy.optimize import brentq

NODES, WEIGHTS = roots_laguerre(128)

def moments(gamma, D=1.0, tau=1.0):
    """Moments of the OU phase kernel by scaled Gauss-Laguerre quadrature."""
    a = float(gamma) + float(D)
    z = NODES
    factor = np.exp(D*tau * (-np.expm1(-z/(a*tau))))
    return tuple(float(np.dot(WEIGHTS, factor*z**j) / a**(j+1))
                 for j in (0, 1, 2))

def h(gamma, D=1.0, tau=1.0):
    m0,m1,_=moments(gamma,D,tau)
    return m0/m1-gamma

def gamma_opt(beta, D=1.0,tau=1.0,mu=1.0):
    m0,m1,_=moments(0,D,tau)
    bc=mu*m1/m0
    if beta<=bc:
        return 0.0
    target=mu/beta
    hi=1.0
    while h(hi,D,tau)>target:
        hi*=2
    return brentq(lambda g:h(g,D,tau)-target,0,hi,xtol=2e-12)

def checks():
    n=0
    for D,tau in [(1.0,1.0),(0.3,2.5),(3.0,0.25)]:
        for gamma in (0.0,0.05,0.2,1.0,4.0,20.0):
            m0,m1,m2=moments(gamma,D,tau)
            assert m0*m2<2*m1*m1,n
            n+=1
            assert h(gamma+1e-4,D,tau)<h(gamma,D,tau),n
            n+=1
        a,b,c=moments(0,D,tau)
        bc=b/a
        for beta in [bc*0.75,bc,bc*1.01,bc*2,bc*6]:
            g=gamma_opt(beta,D,tau)
            if beta<=bc: assert g==0
            else: assert g>0 and abs(h(g,D,tau)-1/beta)<1e-9
            n+=1
    a,b,c=moments(0)
    bc=b/a
    L=2-a*c/(b*b)
    assert abs(bc-1.260202010789377)<1e-12
    n+=1
    g=gamma_opt(2)
    assert abs(g-1.8258281068692734)<1e-9
    n+=1
    for delta in (0.0001,0.001,0.01):
        approx=delta/(bc*bc*L)
        actual=gamma_opt(bc+delta)
        assert abs(actual/approx-1)<5*delta
        n+=1
    for beta in (100,1000):
        g=gamma_opt(beta)
        assert abs(g/(2*beta)-1)<1/beta
        n+=1
    for beta in (bc*1.1,bc*2,bc*4):
        g=gamma_opt(beta)
        vals=[2/((1+beta*rate)*moments(rate)[0]) for rate in (0,g/2,g,2*g,4*g)]
        assert vals[2]<min(vals[0],vals[1],vals[3],vals[4])
        n+=1
    print(f'PASS {n} numerical checks; beta_c={bc:.15f}; gamma*(2)={gamma_opt(2):.15f}')

if __name__=='__main__':
    checks()
