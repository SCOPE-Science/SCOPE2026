"""Supplementary finite checks of the Laurent polynomial identities for phaseless ellipse sampling.

This is a supplementary checker; the infinite statements rely on the written proof.
Run: python ellipse_phase_checker.py
"""
import itertools
import numpy as np
import sympy as sp

w,z=sp.symbols('w z')
checks=0
for a,b in [(sp.Integer(3),sp.Integer(1)),(sp.Rational(7,2),sp.Rational(1,3))]:
    F=[sp.Integer(2),z]
    for j in range(2,7): F.append(sp.expand(z*F[-1]-a*b*F[-2]))
    for d in range(1,7):
        assert sp.simplify(F[d].subs(z,a*w+b/w)-(a**d*w**d+b**d/w**d))==0
        checks+=1
        profile=sp.expand((a**d*w**d+b**d/w**d)*(a**d/w**d+b**d*w**d))
        assert sp.simplify(profile-(a**(2*d)+b**(2*d)+a**d*b**d*(w**(2*d)+w**(-2*d))))==0
        checks+=1

rng=np.random.default_rng(20261104)
for d in (1,2,3,4):
    for a,b in ((.75,.25),(.65,.35)):
        num=4*d
        for theta0 in (0.,0.071):
            theta=theta0+2*np.pi*np.arange(num)/num
            pts=a*np.exp(1j*theta)+b*np.exp(-1j*theta)
            # Evaluation of an arbitrary real Hermitian quadratic form on polynomial coefficients.
            V=np.vander(pts,d+1,increasing=True)
            design=[]
            for u in range(d+1):
                design.append(np.abs(V[:,u])**2)
                for v in range(u+1,d+1):
                    design.append(2*np.real(V[:,u]*np.conj(V[:,v])))
                    design.append(-2*np.imag(V[:,u]*np.conj(V[:,v])))
            D=np.column_stack(design)
            assert np.linalg.matrix_rank(D,tol=1.e-8)==num
            checks+=1
            c=(rng.normal(size=d+1)+1j*rng.normal(size=d+1))
            I=np.abs(V@c)**2
            W=np.exp(1j*theta)
            P0=np.poly1d(np.polyfit(W,W**(2*d)*I,num-1))
            Q=np.poly1d(np.poly(W))
            C=P0(0)/(1-np.prod(W))
            P=P0+C*Q
            Ws=np.exp(1j*rng.uniform(-np.pi,np.pi,size=25))
            pred=np.polyval(P,Ws)/Ws**(2*d)
            true=np.abs(np.polynomial.polynomial.polyval(a*Ws+b/Ws,c))**2
            assert np.max(np.abs(pred-true))<1e-6, (d, a, b, np.max(np.abs(pred-true)))
            checks+=1
        theta=(2*np.arange(num)+1)*np.pi/num
        pts=a*np.exp(1j*theta)+b*np.exp(-1j*theta)
        Fd=np.polynomial.Polynomial([2.])
        if d>=1:
            Fd=np.polynomial.Polynomial([0.,1.])
            Fprev=np.polynomial.Polynomial([2.])
            for k in range(2,d+1):
                Fnext=np.polynomial.Polynomial([0.,1.])*Fd-a*b*Fprev
                Fprev,Fd=Fd,Fnext
        vals=Fd(pts)
        assert np.max(np.abs(np.abs(vals)**2-(a**(2*d)+b**(2*d))))<1e-6
        checks+=1
print('ELLIPSE_PHASE_CHECK_PASS',checks)
