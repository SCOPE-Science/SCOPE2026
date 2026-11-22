#!/usr/bin/env python3
"""Independent conditional-longitude quadrature for ring-torus endpoint tails.

Run: python3 verify_torus_tail.py
Standard library only; finite numerical tests supplement the analytical proof.
"""
import math

PI=math.pi

def radical_inverse(i, base):
    f=1.0/base
    value=0.0
    while i:
        i,remainder=divmod(i,base)
        value += remainder*f
        f /= base
    return value

def exact_conditional_longitude_probability(R,r,alpha,beta,epsilon):
    A=R+r
    p=R+r*math.cos(alpha)
    q=R+r*math.cos(beta)
    dz=r*(math.sin(alpha)-math.sin(beta))
    h=((2*A-epsilon)**2-p*p-q*q-dz*dz)/(2*p*q)
    if h >= 1: return 0.0
    if h <= -1: return 1.0
    return math.acos(h)/PI

def exact_angle_quadrature(R,r,epsilon,n=32768,radial_scale=1.5):
    """Radially integrate the two meridian angles; integrate longitude analytically.

    The integration disk is 1.5 times the leading quadratic projection ellipse.
    The small tested epsilons are checked against a wider disk for containment.
    """
    A=R+r
    sc=radial_scale*math.sqrt(2*epsilon/r)
    tc=radial_scale*math.sqrt(2*A*epsilon/(r*R))
    total=0.0
    for i in range(1,n+1):
        angle=2*PI*radical_inverse(i,3)
        rho=math.sqrt(radical_inverse(i,2))
        s=sc*rho*math.cos(angle)
        t=tc*rho*math.sin(angle)
        alpha=(s+t)/math.sqrt(2)
        beta=(s-t)/math.sqrt(2)
        # Area-uniform meridian density, not uniform parameter density.
        weight=(R+r*math.cos(alpha))*(R+r*math.cos(beta))/(4*PI*PI*R*R)
        total += weight*exact_conditional_longitude_probability(R,r,alpha,beta,epsilon)
    return PI*sc*tc*total/n

def leading_coefficient(R,r):
    return 2*(R+r)**2/(3*PI**2*r*R**2.5)

def dimensionless_coefficient(k):
    return 2**2.5*(1+k)**3.5/(3*PI**2*k**2.5)

def check():
    checks=0
    # Exact geometry tests of all three coordinates and the angular marginal.
    for R,r in [(1.2,1.0),(2.,1.),(4.,1.)]:
        for epsilon in [0.02,0.005]:
            p=exact_angle_quadrature(R,r,epsilon)
            asymp=leading_coefficient(R,r)*epsilon**1.5
            assert abs(p/asymp-1)<0.025, (R,r,epsilon,p,asymp,p/asymp)
            checks+=1
        # Compare 1.5x and 2x normal neighborhoods at the smaller cutoff.
        p=exact_angle_quadrature(R,r,0.005,32768,radial_scale=1.5)
        q=exact_angle_quadrature(R,r,0.005,32768,radial_scale=2.0)
        assert abs(p/q-1)<0.007,(R,r,p,q)
        checks+=1
    for k in [1.05,1.2,1.8,2.,2.4,2.7,3.,4.,6.,20.]:
        h=dimensionless_coefficient(k)
        hstar=dimensionless_coefficient(2.5)
        assert h>=hstar-1e-13
        derivative=(2*k-5)/(2*k*(k+1))
        if k<2.5: assert derivative<0
        elif k>2.5: assert derivative>0
        checks+=1
    assert abs(dimensionless_coefficient(2.5) - 2*math.sqrt(2)*7**3.5/(3*PI**2*5**2.5))<1e-12
    checks+=1
    print('VERIFY_TORUS_DIAMETER_TAIL_OK',checks)

if __name__ == '__main__':
    check()
