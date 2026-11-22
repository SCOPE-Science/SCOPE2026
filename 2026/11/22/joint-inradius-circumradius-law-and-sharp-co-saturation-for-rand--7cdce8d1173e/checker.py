#!/usr/bin/env python3
"""Standalone numerical checks for planar inradius/circumradius of circular-cylinder shadows.

All identities in the accompanying proof are analytic; discretizations here are diagnostics.
Standard library only.
"""
from math import sin, cos, sqrt, atan, pi, isclose
from random import Random

N = 0

def check(ok, label):
    global N
    N += 1
    if not ok:
        raise AssertionError(label)


def analytic_radii(R, q, theta):
    C, S = cos(theta), sin(theta)
    I = R * min(1.0, C + q * S)
    O = R * (C + q * S if theta < atan(q) else sqrt(1 + q*q))
    return I, O


def numeric_radii_from_support(R, q, theta, m=900):
    C, S = cos(theta), sin(theta)
    vals = []
    for j in range(m+1):
        phi = pi*j/(2*m)
        vals.append(R*sqrt(cos(phi)**2+C*C*sin(phi)**2)+R*q*S*sin(phi))
    return min(vals), max(vals)


def numeric_circum_from_rim(R, q, theta, m=1500):
    C, S = cos(theta), sin(theta)
    return max(sqrt((R*sin(2*pi*j/m))**2+(R*C*cos(2*pi*j/m)+R*q*S)**2)
               for j in range(m))


def p_joint(q):
    return 1/sqrt(1+q*q) - max(0.0, (1-q*q)/(1+q*q))


def cdf_in(t, q):
    if q >= 1:
        return 0.0 if t < 1 else 1.0
    if t < q:
        return 0.0
    if t >= 1:
        return 1.0
    return (t-q*sqrt(max(0, 1+q*q-t*t)))/(1+q*q)


def cdf_out(t, q):
    upper = sqrt(1+q*q)
    if t < 1:
        return 0.0
    if t >= upper:
        return 1.0
    return 1-(t+q*sqrt(max(0,1+q*q-t*t)))/(1+q*q)


def run():
    rng = Random(814151)
    for R in (0.4, 1.0, 2.7):
        for q in (0.07, 0.3, 0.77, 0.99, 1., 1.01, 1.7, 4.3):
            angles = [0., pi/2, atan(q), atan(q)/3, .999*atan(q)]
            if 2*atan(q) < pi/2:
                angles += [2*atan(q), 1.002*atan(q), .999*2*atan(q)]
            angles += [rng.random()*pi/2 for _ in range(15)]
            for theta in angles:
                Ia, Oa = analytic_radii(R,q,theta)
                In, On = numeric_radii_from_support(R,q,theta)
                Or = numeric_circum_from_rim(R,q,theta)
                check(abs(Ia-In) < 2e-9*R, ('support minimum',R,q,theta,Ia,In))
                check(abs(Oa-On) < 1e-5*R, ('support maximum',R,q,theta,Oa,On))
                check(abs(Oa-Or) < 2e-5*R, ('projected circular rims',R,q,theta,Oa,Or))
                check(Ia <= Oa + 1e-13*R, ('radius order',R,q,theta))
    # Uniform viewing-coordinate integration, independent of symbolic inverse formulas.
    M = 24000
    for q in (0.2, 0.65, 0.98, 1., 1.1, 2.0, 5.0):
        sample = [analytic_radii(1., q, __import__('math').acos((j+.5)/M)) for j in range(M)]
        upper = sqrt(1+q*q)
        for k in range(1,16):
            tI=(q if q<1 else 1)+(1-(q if q<1 else 1))*k/17
            tO=1+(upper-1)*k/17
            eI=sum(I<=tI for I,O in sample)/M
            eO=sum(O<=tO for I,O in sample)/M
            check(abs(eI-cdf_in(tI,q))<2/M, ('inradius cdf',q,tI,eI))
            check(abs(eO-cdf_out(tO,q))<2/M, ('circumradius cdf',q,tO,eO))
        both=sum((abs(I-1)<1e-11 and abs(O-upper)<1e-11) for I,O in sample)/M
        check(abs(both-p_joint(q))<2/M, ('joint atom',q,both,p_joint(q)))
        check(p_joint(q)<=1/sqrt(2)+1e-12, ('global atom bound',q))
    for k in range(1,1000):
        q=k/1000
        left=q*(4-sqrt(1+q*q))/(1+q*q)**2
        check(left>0,('strict inc',q))
        right=-q/(1+q*q)**1.5
        check(right<0,('strict dec',q))
    check(abs(p_joint(1)-1/sqrt(2))<1e-15, 'exact optimum')
    print('PASSED',N,'numerical and derivative-sign diagnostics')

if __name__ == '__main__':
    run()
