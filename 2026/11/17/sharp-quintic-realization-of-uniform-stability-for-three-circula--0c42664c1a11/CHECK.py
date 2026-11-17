#!/usr/bin/env python3
"""Reproducible exact-rational algebra and numerical Floquet illustration for prescribed circles.
Requires SymPy and SciPy. This finite checker does not replace the universal sign proof.
"""
import sympy as s
from scipy.integrate import quad
from math import sin,cos,pi,exp
x,y=s.symbols('x y', real=True)
r1,r2,r3=s.Rational(2,5),s.Rational(1,5),s.Rational(1,5)
f1=x*x+y*y-r1*r1;f2=x*x+y*y-r2*r2;f3=(x-1)**2+y*y-r3*r3
F=s.expand(f1*f2*f3); lam=s.Integer(1); eta=s.Integer(-1)
for beta in [s.Rational(-1,100),s.Rational(1,100)]:
    B=x*x+y*y+beta*y-(r1*r1+r2*r2)/2
    H=lam*f1*f2-f3*B
    P=s.expand(y*H-eta*s.diff(F,y));Q=s.expand(lam*f1*f2-x*H+eta*s.diff(F,x))
    for f,K in [(f1,2*(lam-2*eta)*y*f2),(f2,2*(lam-2*eta)*y*f1),(f3,2*y*(B+2*eta*(f1+f2)))]:
        assert s.expand(s.diff(f,x)*P+s.diff(f,y)*Q-K*f)==0
    assert max(s.Poly(P,x,y).total_degree(),s.Poly(Q,x,y).total_degree())==5
    Bf=s.lambdify((x,y),B,'math');f1f=s.lambdify((x,y),f1,'math');f2f=s.lambdify((x,y),f2,'math');f3f=s.lambdify((x,y),f3,'math')
    dd=float(r1*r1-r2*r2)
    chis=[]
    for radius,index in [(float(r1),1),(float(r2),2)]:
        def integrate(theta):
            X=radius*cos(theta);Y=radius*sin(theta)
            k=(6*dd if index==1 else -6*dd)*Y
            omega=f3f(X,Y)*(Bf(X,Y)-2*(f2f(X,Y) if index==1 else f1f(X,Y)))
            return k/abs(omega)
        chi=quad(integrate,0,2*pi,epsabs=1e-12)[0];chis.append(chi)
    def integrate3(theta):
        X=1+float(r3)*cos(theta);Y=float(r3)*sin(theta)
        k=2*Y*(Bf(X,Y)-2*(f1f(X,Y)+f2f(X,Y)))
        return k/(3*abs(f1f(X,Y)*f2f(X,Y)))
    chis.append(quad(integrate3,0,2*pi,epsabs=1e-12)[0])
    assert all((c>1e-8 if beta>0 else c < -1e-8) for c in chis)
    print('VERIFY_OK', 'beta=', beta, 'degrees=5', 'cofactor_identities=3','characteristic_exponents=', chis)
