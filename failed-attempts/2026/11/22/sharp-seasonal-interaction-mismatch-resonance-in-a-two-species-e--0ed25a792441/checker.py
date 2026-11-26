#!/usr/bin/env python3
"""Reproducibility checks for the two-species seasonal feedback theorem.

Requires numpy, scipy and sympy. The analytical proof is in RESULT.md;
finite computations are corroboration, not substitutes for that proof.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from numpy.linalg import eigvals
from sympy import Matrix, symbols, simplify


def verify_symbolic():
    b, c, p, q, kappa, eps, u = symbols('b c p q kappa eps u', positive=True)
    B = Matrix([[0,b],[-c,0]])
    H = Matrix([[0,p],[-q,0]])
    assert B*H-H*B == (p*c-b*q)*Matrix([[1,0],[0,-1]])
    A = -kappa*eps*Matrix.eye(2) + B + eps*u*H
    assert simplify((A[0,0]+A[1,1])/2 + kappa*eps)==0
    assert simplify(A.det() - (kappa**2*eps**2 + (b+eps*p*u)*(c+eps*q*u)))==0
    J=Matrix([[0,1],[-1,0]])
    K=Matrix([[0,1],[1,0]])
    d, delta=symbols('d delta', real=True)
    C=(d*K-delta*J)/2
    assert simplify(C*C-(d*d-delta*delta)*Matrix.eye(2)/4)==Matrix.zeros(2)
    print('PASS symbolic: commutator, frozen eigenvalues, averaged eigenvalues')


def exponent(eps, omega, b=1.,c=1.,p=2.,q=.5,kappa=.25):
    T=2*math.pi/omega
    def rhs(t,z):
        a=math.cos(omega*t)
        A=np.array([[-kappa*eps, b+eps*p*a],[-c-eps*q*a,-kappa*eps]])
        return (A@z.reshape(2,2)).ravel()
    s=solve_ivp(rhs,(0,T),np.eye(2).ravel(),rtol=3e-12,atol=5e-14)
    assert s.success
    M=s.y[:,-1].reshape(2,2)
    return math.log(max(abs(eigvals(M))))/T, M


def main():
    verify_symbolic()
    pred=1/8
    for eps in [.1,.05,.025,.0125]:
        z,M=exponent(eps,2.)
        assert z>0 and abs(z/eps-pred)<0.001
        assert abs(np.linalg.det(M)-math.exp(-.5*eps*math.pi))<5e-10
        z4,_=exponent(eps,4.)
        assert abs(z4+.25*eps)<2e-10
    print('PASS positive near 2:1 resonance and exact nonresonant damping at frequency 4')
    for delta in [-1.,-.7,-.5,0.,.5,.7,1.]:
        eps=.01
        actual,_=exponent(eps,2+delta*eps)
        estimated=-.25+.5*math.sqrt(max(0,.75**2-delta**2))
        assert abs(actual/eps-estimated)<.005,(delta,actual/eps,estimated)
    print('PASS detuned weak-forcing Floquet exponent approximates analytic limit')
    for eps in [.02,.07,.11]:
        val,_=exponent(eps,2.,b=1.,c=1.,p=2.,q=2.,kappa=.25)
        assert abs(val+.25*eps)<3e-10
    print('PASS proportional environmental modulation: exact damping')

if __name__=='__main__': main()
