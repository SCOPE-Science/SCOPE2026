#!/usr/bin/env python3
"""Independent numeric and algebraic checks of the ellipsoidal capsule Petty profile.
Only the Python standard library is required. Analytic theorem does not depend on sampling.
"""
from math import pi,gamma,sqrt,comb,isclose
from fractions import Fraction

def kappa(d):
    return pi ** (d/2) / gamma(d/2+1)

def I(j):
    return sqrt(pi)*gamma(j/2+1)/(2*gamma(j/2+1.5))

def u_coefficients(d):
    a=kappa(d-1)
    return [2*kappa(d-1)*a**(d-j)*(kappa(d-2)/kappa(d-1))**j * I(d-1-j) /kappa(d)**(d-1-j) for j in range(d)]
    # For j: factors (2*kappa(d-2))^j/(2*kappa(d-1))^j cancel.

def quotient_poly(d,t):
    u=u_coefficients(d)
    y=2*kappa(d-1)*t/(kappa(d)+2*kappa(d-1)*t)
    return sum(comb(d-1,j)*u[j]*(y**j)*((1-y)**(d-1-j)) for j in range(d))

def quotient_quadrature(d,t,N=12000):
    if N%2: raise ValueError('N must be even')
    a=kappa(d-1)
    b=2*t*kappa(d-2)
    step=2*a/N
    tot=0.
    for i in range(N+1):
        z=-a+step*i
        val=(b+sqrt(max(0.,a*a-z*z)))**(d-1)
        tot+=val*(1 if i==0 or i==N else (4 if i%2 else 2))
    pvol=kappa(d-1)*step*tot/3
    return pvol/(kappa(d)+2*t*kappa(d-1))**(d-1)

def check():
    checks=0
    # Exact symbolic 3D identity: (8*t^2+w*t+w/3) - (3*w/4)(t+2/3)^2 = (8-3*w/4)t^2.
    # Represent the polynomial as a pair (rational constant, rational multiplier of w=pi^2).
    w=Fraction(1)
    for j,c0,cw in [(0,Fraction(0),Fraction(1,3)),(1,Fraction(0),Fraction(1)),(2,Fraction(8),Fraction(0))]:
        dj=[Fraction(4,9),Fraction(4,3),Fraction(1)][j]
        assert c0 == (Fraction(8) if j==2 else Fraction(0))
        assert cw-Fraction(3,4)*dj == (-Fraction(3,4) if j==2 else Fraction(0))
        checks+=2
    # Rational bound pi < 22/7 implies 8-3pi^2/4>0.
    assert Fraction(8)>Fraction(3,4)*Fraction(22,7)**2
    checks+=1
    for d in range(3,13):
        u=u_coefficients(d)
        base=kappa(d-1)**d/kappa(d)**(d-2)
        endpoint=2*kappa(d-1)**2*(kappa(d-2)/kappa(d-1))**(d-1)
        assert isclose(u[0],base,rel_tol=1e-12)
        assert isclose(u[1],u[0],rel_tol=1e-12)
        assert isclose(u[-1],endpoint,rel_tol=1e-12)
        checks+=3
        for j in range(1,d-1):
            assert u[j+1]>u[j]*(1+1e-12), (d,j)
            checks+=1
        vals=[quotient_poly(d,t) for t in [0,0.1,0.5,1,3,10,1000]]
        assert all(vals[j+1]>vals[j] for j in range(6))
        assert vals[0]>=base*(1-1e-12) and vals[-1]<endpoint
        checks+=7
        for t in [0,0.5,3,10]:
            q1=quotient_poly(d,t)
            q2=quotient_quadrature(d,t)
            assert isclose(q1,q2,rel_tol=4e-6,abs_tol=4e-6),(d,t,q1,q2)
            checks+=1
    # Exact specialization d=3.
    for t in [0,0.125,0.3,1,3,12]:
        Q=(pi*pi*(t+1/3)+8*t*t)/(t+2/3)**2
        Q_alt=3*pi*pi/4 +(8-3*pi*pi/4)*(t/(t+2/3))**2
        assert isclose(quotient_poly(3,t),Q,rel_tol=1e-12)
        assert isclose(Q,Q_alt,rel_tol=1e-12)
        checks+=2
    print('PASS',checks,'independent numerical/algebraic comparisons, d=3..12; exact symbolic d=3 coefficient identity.')
if __name__=='__main__':check()
