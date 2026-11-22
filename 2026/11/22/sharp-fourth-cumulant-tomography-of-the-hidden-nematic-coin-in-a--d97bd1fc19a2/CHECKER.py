#!/usr/bin/env python3
"""Exact symbolic and finite-step checks for directional cumulant inversion.

Dependencies: Python 3, sympy, numpy.  The infinite-time theorem uses the
separate spectral proof; the numerical comparisons here are diagnostics.
"""
from math import comb
import sympy as sp
import numpy as np


def symbolic_checks():
    p, c, eta, z, q = sp.symbols('p c eta z q', real=True)
    a = (1 + eta + 2*p)/4
    b = (1 + eta - 2*p)/4
    left = (1 - eta + 2*c)/4
    right = (1 - eta - 2*c)/4
    C = sp.Matrix([[a, right, b, left], [left, a, right, b],
                   [b, left, a, right], [right, b, left, a]])
    s = p*p + c*c
    h = (1-p)**2 + c*c
    W = (1+p)**2 + c*c
    P0 = (z-1)*(z-eta)*((z-p)**2+c*c)
    QA = -z*((1+eta+2*p)*z*z - 2*(s+eta*p+eta+p)*z
             + (1+eta)*s+2*eta*p)/2
    Q1 = -z*((1+eta)*s+2*eta*p+(1+eta+2*p)*z*z)
    Q2 = z*z*(s+eta*p+eta+p)
    P_axis = (z*sp.eye(4)-sp.diag(q,1,1/q,1)*C).det(method='domain-ge')
    P_diag = (z*sp.eye(4)-sp.diag(q,q,1/q,1/q)*C).det(method='domain-ge')
    u=(q+1/q)/2
    assert sp.cancel(P_axis-(P0+(u-1)*QA)) == 0
    assert sp.cancel(P_diag-(P0+(u-1)*Q1+(u*u-1)*Q2)) == 0
    Pp=sp.diff(P0,z).subs(z,1)
    assert sp.factor(Pp-(1-eta)*h)==0
    A=sp.factor(-QA.subs(z,1)/(2*Pp))
    assert sp.factor(A-(1-s)/(4*h))==0
    BA=sp.factor(-(sp.diff(P0,z,2).subs(z,1)*A*A/2
                   +sp.diff(QA,z).subs(z,1)*A/2 + QA.subs(z,1)/24)/Pp)
    BD=sp.factor(-(sp.diff(P0,z,2).subs(z,1)*A*A/2
                   +A*(sp.diff(Q1,z).subs(z,1)/4
                      +sp.diff(Q2,z).subs(z,1)/2)
                   +Q1.subs(z,1)/96 + Q2.subs(z,1)/12)/Pp)
    Delta=-(s+6*p+5)/(4*h)+3*W/(2*h*(1-eta))
    assert sp.factor(24*(BA-BD)-Delta)==0
    assert sp.factor(sp.diff(Delta,eta)-3*W/(2*h*(1-eta)**2))==0
    inverse=1-6*W/(4*h*sp.Symbol('observed')+s+6*p+5)
    assert sp.factor(inverse.subs(sp.Symbol('observed'),Delta)-eta)==0
    print('PASS: both 4x4 determinant identities, spectral coefficients, '
          'cumulant contrast, strict derivative, and inversion')


def numeric_checks():
    choices=[(0.0,0.0,0.0),(0.0,0.0,-0.8),(0.2,0.1,0.3),
             (-0.3,0.2,0.1),(0.5,0.1,0.2),(0.1,-0.5,-0.5)]
    for p,c,eta in choices:
        a=(1+eta+2*p)/4; b=(1+eta-2*p)/4
        left=(1-eta+2*c)/4; right=(1-eta-2*c)/4
        assert min(a,b,left,right)>0
        C=np.array([[a,right,b,left],[left,a,right,b],
                    [b,left,a,right],[right,b,left,a]],dtype=float)
        rates=[]
        for vv in [np.array([1.,0,-1,0]),
                   np.array([1.,1,-1.,-1.])/np.sqrt(2)]:
            mom=np.zeros((5,4),dtype=float);mom[0,:]=0.25
            N=3000
            for _ in range(N):
                pr=C@mom.T
                nxt=np.zeros_like(mom)
                for j in range(5):
                    for k in range(j+1):
                        nxt[j,:]+=comb(j,k)*(vv**(j-k))*pr[:,k]
                mom=nxt
            x=mom.sum(axis=1)
            rates.append((x[4]-3*x[2]**2)/N)
        h=(1-p)**2+c*c;s=p*p+c*c;W=(1+p)**2+c*c
        exact=-(s+6*p+5)/(4*h)+3*W/(2*h*(1-eta))
        error=abs(rates[0]-rates[1]-exact)
        assert error<0.025, (p,c,eta,error)
        print(f'finite-step: p={p:+.2f}, c={c:+.2f}, '
              f'eta={eta:+.2f}, absolute asymptotic error={error:.6g}')
    print('PASS: six independent Markov moment-hierarchy comparisons')


if __name__ == '__main__':
    symbolic_checks()
    numeric_checks()
