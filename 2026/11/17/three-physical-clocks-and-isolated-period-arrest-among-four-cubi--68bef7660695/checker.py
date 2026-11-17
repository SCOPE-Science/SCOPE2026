#!/usr/bin/env python3
"""Exact-rational and numerical checks for anisotropic torus meridians.
The analytical proof, not quadrature, establishes the universal statements.
"""
from fractions import Fraction as F
from math import sqrt, cos, pi, exp, log

def polynomial_cofactor_check():
    cases=[(F(3,2),F(3),F(1),F(1,2),F(1,3),F(-1,4),F(2,5)),
           (F(5,4),F(2),F(4,3),F(1,5),F(-2,3),F(3,7),F(-1,2))]
    for a,k,c,lam,x,y,z in cases:
        r2=x*x+y*y
        K=k+lam*x
        P=K*x*z/4+c*x*y*y
        Q=K*y*z/4-c*x*x*y
        R=K*(-a*a*r2+z*z+a**4-1)/2
        S=(r2-a*a)**2+z*z-1
        deriv=4*(r2-a*a)*(x*P+y*Q)+2*z*R
        assert deriv==K*z*S

def simpson(f,n=30000):
    assert n%2==0
    h=2*pi/n
    s=f(0)+f(2*pi)
    for j in range(1,n):s+=(4 if j%2 else 2)*f(j*h)
    return s*h/3

def stats(a,k,c,lam,n=30000):
    R=sqrt(a*a+1)
    assert 0<lam<k/R
    out={}
    for sign in (-1,0,1):
        def vel(t):return k+sign*lam*sqrt(a*a+cos(t))
        I=simpson(lambda t: 1/vel(t),n)
        T=2*simpson(lambda t:1/(vel(t)*(a*a+cos(t))),n)
        out[sign]=(T,I,exp(-2*c*I) if sign else exp(2*c*I))
    assert out[1][0] < out[0][0] < out[-1][0]
    assert 0<out[-1][2]<out[1][2]<1<out[0][2]
    D=(k*k-lam*lam*a*a)**2-lam**4
    assert abs(log(out[1][2])+log(out[-1][2]) +8*pi*c*k/sqrt(D))<1e-7
    assert abs(out[0][0] -4*pi/(k*sqrt(a**4-1)))<1e-7
    assert abs(log(out[0][2])-4*pi*c/k)<1e-7
    return out

if __name__=='__main__':
    polynomial_cofactor_check()
    a,k,c=1.5,3.,1.
    R=sqrt(a*a+1); lc=k/R
    print('lambda_critical',lc)
    for epsilon in (0.2,0.05,0.01,0.002):
        lam=(k-epsilon)/R
        out=stats(a,k,c,lam,40000)
        Tminus=out[-1][0]; Iminus=out[-1][1]
        print('epsilon',epsilon,'T_+ T_y T_-',*[round(out[s][0],8) for s in (1,0,-1)],
              'sqrt(eps)*T_-',round(sqrt(epsilon)*Tminus,8),
              'sqrt(eps)*(-log mu_-)',round(sqrt(epsilon)*2*c*Iminus,8))
    print('predicted limiting period',4*pi/(R*sqrt(k)))
    print('predicted limiting negative log multiplier',4*pi*c*R/sqrt(k))
    print('ANISOTROPIC_TORUS_CHECK_OK')
