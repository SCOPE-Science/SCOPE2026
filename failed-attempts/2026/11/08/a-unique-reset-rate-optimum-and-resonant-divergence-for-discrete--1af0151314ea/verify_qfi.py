#!/usr/bin/env python3
"""Exact and independent matrix checks of a reset-qubit phase-estimation theorem."""
import math
import numpy as np
import sympy as sp

q, c, t, w, x = sp.symbols('q c t w x', real=True)
D = 1 + q*q - 2*q*c
Fq = q*(1-q)**2*(q+1)*((1+c)-(1+3*c)*q+2*q*q)/(2*D**3)
Ft = t*t*(1-t)*(1+w)**2*(2*t*t+w*(1-t))/(4*(t*t+w)**3)
assert sp.factor(Fq.subs({q:(1-t)/(1+t),c:(1-w)/(1+w)})-Ft)==0
P = 2*(t**5-(w+2)*t**4-2*w*t**3+2*w*(w+1)*t**2-3*w*w*t+w*w)
assert sp.factor(sp.diff(Ft,t)-((1+w)**2/4)*t*P/(t*t+w)**4)==0
Px = sp.expand(sp.cancel(P.subs(t,x/(1+x))*(1+x)**5))
expected = (2*w*w +4*w*w*x +4*w*x**2 -4*w*(w-2)*x**3
            -2*(w*w-w+2)*x**4 -2*(w+1)*x**5)
assert sp.factor(Px-expected)==0
assert sp.factor(P.subs(t,sp.Rational(1,2))-3*(2*w-1)/16)==0
assert sp.factor(Fq.subs(c,-1)-q*q*(1-q)**2/(1+q)**4)==0
assert sp.factor(Ft.subs(w,0)-(1-t)/(2*t*t))==0
assert sp.factor(sp.limit(Ft/w**(-1),w,0))==0  # fixed t has lower order than 1/w

checks=7
# Direct SLD matrix computation is independent of the Bloch-state QFI simplification.
for theta in [0.0125,0.07,0.3,0.7,1.2,1.85,2.4,math.pi]:
    for qv in [0.04,0.12,0.24,0.36,0.51,0.66,0.79,0.91]:
        r = 1-qv
        z = complex(math.cos(theta),math.sin(theta))
        cv = r/(1-qv*z)
        cp = 1j*r*qv*z/(1-qv*z)**2
        rho = np.array([[1,cv.conjugate()],[cv,1]],complex)/2
        drho = np.array([[0,cp.conjugate()],[cp,0]],complex)/2
        lam,V=np.linalg.eigh(rho)
        assert min(lam)>1e-10
        G=V.conj().T@drho@V
        L=V@((2*G)/(lam[:,None]+lam[None,:]))@V.conj().T
        direct=float(np.trace(rho@L@L).real)
        formula=float(Fq.subs({q:qv,c:math.cos(theta)}))
        assert abs(direct-formula)<1e-8*max(1,formula),(theta,qv,direct,formula)
        checks+=1
        # Direct renewal-series coherence check.
        Cfinite=sum(r*(qv*z)**k for k in range(800))
        assert abs(Cfinite-cv)<5e-12
        checks+=1

# Exact roots of the derivative polynomial for several rational w.
for ww in [sp.Rational(1,100),sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4),1,2,5,20,100]:
    roots=np.roots([float(v) for v in sp.Poly(P.subs(w,ww),t).all_coeffs()])
    good=[float(z.real) for z in roots if abs(z.imag)<1e-7 and 0<z.real<1]
    assert len(good)==1,(ww,roots)
    z=good[0]
    f=lambda a:float(Ft.subs({w:ww,t:a}))
    assert f(z)>f(z/2) and f(z)>f((z+1)/2)
    checks+=3

# Resonance double scaling: t_*(u)/u --> sqrt((1+sqrt(3))/2), w F_max --> sqrt(3)/18.
for u in [0.01,0.003,0.001]:
    ww=u*u
    roots=np.roots([float(v) for v in sp.Poly(P.subs(w,ww),t).all_coeffs()])
    sols=[float(z.real) for z in roots if abs(z.imag)<1e-5 and 0<z.real<1]
    assert len(sols)==1
    tm=sols[0]
    assert abs(tm/u-math.sqrt((1+math.sqrt(3))/2))<0.1
    assert abs((u*u)*float(Ft.subs({w:ww,t:tm}))-math.sqrt(3)/18)<0.004
    checks+=3
print(f'PASS: {checks} algebraic, matrix-SLD, series, root and asymptotic checks')
