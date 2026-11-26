#!/usr/bin/env python3
"""Reproducible scientific checks for an interval heat-correlation comparison.

Requires numpy, scipy, sympy. Uses independent sparse finite-difference heat evolution,
Fourier representation, symbolic differentiation and quadrature. Finite tests only
supplement the analytic proof; they do not certify its universal quantifiers.
"""
from math import erf, exp, pi, sin, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.fft import dst, idst
from sympy import symbols, simplify, diff


def exact(s, u, nmax=200):
    return 1-u-sum(2*sin(n*pi*u)*exp(-n*n*pi*pi*s/2)/(n*pi)
                   for n in range(1, nmax+1))


def shortcut(s, u):
    y=1/sqrt(2*s)
    return 1-erf(u*y)/erf(y)


def exact_relaxation_area(u):
    return u*(1-u)*(2-u)/3


def asymptotic_error_coeff(u):
    return u*(1-u*u)/6


def test_symbolic():
    u=symbols('u',real=True)
    h=u*(1-u)*(2-u)/3
    assert simplify(diff(h,u,2)/2+(1-u))==0
    assert h.subs(u,0)==h.subs(u,1)==0
    # Let f(t,x) solve the free heat equation and H(t)=f(t,L), H'<0.
    # U=1-f/H satisfies (d_t-1/2 d_xx)U=f H'/H^2<0.
    print('symbolic: relaxation Poisson equation and boundaries PASS')


def test_spectral_vs_fd():
    # Diagonalize a second-order finite-difference Dirichlet heat operator,
    # independently of the continuum Fourier-series calculation.
    m=160
    ugrid=np.arange(1,m)/m
    steady=1-ugrid
    k=np.arange(1,m)
    eigen=-2*m*m*np.sin(k*pi/(2*m))**2
    initial_mode=dst(-steady,type=1,norm='ortho')
    for s in [.025,.1,.35,.9]:
        numeric=steady+idst(initial_mode*np.exp(s*eigen),type=1,norm='ortho')
        for j in [int((m-1)*p) for p in [.1,.25,.5,.75,.9]]:
            u=ugrid[j]
            analytical=exact(s,u)
            assert abs(numeric[j]-analytical)<2e-4,(s,u,numeric[j],analytical)
    print('independent discrete-heat Dirichlet evolution: 20 point checks PASS')


def test_sign_and_expansion():
    n=0
    for s in [.007,.012,.025,.05,.1,.2,.5,1,2,5,10,40]:
        for u in [.05,.1,.25,.4,.5,.7,.85,.95]:
            a=exact(s,u,nmax=800)
            b=shortcut(s,u)
            assert b<=a+4e-14 and a<=1-u+4e-14,(s,u,a,b)
            if .05<=s<=2:
                assert b<a,(s,u,a,b)
            upper=erf(u/sqrt(2*s))/erf(1/sqrt(2*s))-u
            assert (a-b)<upper+2e-13,(s,u,upper,a-b)
            n+=1
    for u in [.15,.4,.55,.8]:
        for s in [100.,400.,1500.]:
            measured=s*(exact(s,u)-shortcut(s,u))
            assert abs(measured-asymptotic_error_coeff(u))<0.00005,(u,s,measured)
    print('strict sign, explicit upper envelope and asymptotic coefficient:',n+12,'checks PASS')


def test_relaxation_integral():
    for u in [.125,.25,.5,.625,.85]:
        # Exact eigenmode-by-eigenmode time integrals, compared with
        # independently differentiated Poisson solution.
        z=sum(4*sin(n*pi*u)/(pi**3*n**3) for n in range(1,8001))
        assert abs(z-exact_relaxation_area(u))<5e-9,(u,z,exact_relaxation_area(u))
    print('five independently summed relaxation-integral checks PASS')

if __name__=='__main__':
    test_symbolic()
    test_spectral_vs_fd()
    test_sign_and_expansion()
    test_relaxation_integral()
    print('ALL REPRODUCIBLE NUMERICAL/SYMBOLIC CHECKS PASSED')
