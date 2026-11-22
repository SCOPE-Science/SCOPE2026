#!/usr/bin/env python3
"""Check the metric coefficient and direct small-loop areas of ellipse evolutoids.

Requirements: Python 3, numpy, scipy, sympy. This is a numerical/algebraic
reproducibility aid, not a replacement for the mathematical proof.
"""
from math import atan, sqrt, pi
import numpy as np
from scipy.optimize import root
from scipy.integrate import quad
import sympy as sp

T, A, B = sp.symbols('T A B', positive=True)
X = -A*T+B*T**3/3
Y = A*T**2/2-B*T**4/4
z = sp.sqrt(3*A/B)
model = sp.simplify(sp.integrate((X*sp.diff(Y,T)-Y*sp.diff(X,T))/2,(T,-z,z)))
assert sp.simplify(model-8*sp.sqrt(3)*A**sp.Rational(7,2)/(35*B**sp.Rational(3,2))) == 0

def loop(a,b,delta):
    D=a*a-b*b; S=a*a+b*b
    H=sqrt(4*a*a*b*b+9*D*D)
    ac=atan(2*a*b/(3*D)); alpha=ac+delta
    phi0=atan(-a/b)
    rho0=S**1.5/(2**1.5*a*b)
    AA=rho0*H/(2*a*b)
    BB=rho0*3*D*S*S/(2*a*a*b*b*H)
    initial=sqrt(3*AA*delta/BB)

    def data(phi):
        Q=a*a*np.cos(phi)**2+b*b*np.sin(phi)**2
        p=np.sqrt(Q)
        pd=-D*np.cos(phi)*np.sin(phi)/p
        rho=a*a*b*b/p**3
        return p,pd,rho
    def curve(phi):
        p,pd,rho=data(phi)
        th=phi+alpha
        h=p*np.cos(alpha)+pd*np.sin(alpha)
        hd=pd*np.cos(alpha)+(rho-p)*np.sin(alpha)
        return np.array([h*np.cos(th)-hd*np.sin(th), h*np.sin(th)+hd*np.cos(th)])
    solution=root(lambda z: curve(z[0])-curve(z[1]), [phi0-initial,phi0+initial],tol=1e-11)
    assert solution.success,solution.message
    f1,f2=solution.x
    assert f1<f2 and f1<phi0<f2
    assert np.linalg.norm(curve(f1)-curve(f2)) < 1e-9
    def integrand(phi):
        p,pd,rho=data(phi)
        Q=a*a*np.cos(phi)**2+b*b*np.sin(phi)**2
        g=3*D*np.sin(phi)*np.cos(phi)/Q
        r=rho*(np.cos(alpha)+g*np.sin(alpha)); th=phi+alpha
        xy=curve(phi)
        cp=r*np.array([-np.sin(th),np.cos(th)])
        return (xy[0]*cp[1]-xy[1]*cp[0])/2
    actual=2*abs(quad(integrand,f1,f2,epsabs=2e-12,epsrel=2e-10)[0])
    predicted=H**5/(210*(a*b)**2.5*D**1.5)*delta**3.5
    return actual/predicted

for (a,b) in ((1.5,1.),(2.,1.),(3.,1.)):
    ratios=[loop(a,b,d) for d in (0.005,0.002,0.001)]
    assert 0.985 < min(ratios) < 1.001
    assert abs(ratios[-1]-1)<abs(ratios[0]-1)
    print('ellipse',a,b,'small-loop/prediction',ratios)

m0=sqrt(3/7)
aspect=(1+sqrt(22))/sqrt(21)
assert abs(1.5*(aspect-1/aspect)-m0)<1e-12

def normalized(m):
    return (16/105)*(3/2)**1.5*(1+m*m)**2.5/m**1.5
assert normalized(m0)<normalized(0.5) and normalized(m0)<normalized(0.8)
print('EVOLUTOID_SWALLOWTAIL_METRIC_LOOP_CHECKS_OK')
