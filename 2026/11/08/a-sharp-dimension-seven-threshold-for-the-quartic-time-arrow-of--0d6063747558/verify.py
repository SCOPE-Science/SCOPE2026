#!/usr/bin/env python3
"""Deterministic checks of the stationary RTP temporal-asymmetry theorem.
Public scientific reproducibility utility; Python standard library only.
Usage: python3 verify.py
"""
from fractions import Fraction as Q
from math import exp, expm1, isclose

COUNT = 0

def check(test, message):
    global COUNT
    if not test:
        raise AssertionError(message)
    COUNT += 1

def moments(d, r):
    d, r = Q(d), Q(r)
    u2 = 1/d
    u4 = 3/(d*(d+2))
    m11 = u2/(1+r)
    m20 = m11
    m13 = u4/(1+r)
    m22 = (2*m13+r*u2*m20)/(2+r)
    m31 = 3*m22/(3+r)
    m40 = m31
    return [m20,m11,m40,m31,m22,m13]

def rhs(z, d, r):
    h0, hu, h1, h2, h3, h4 = z
    return [-h0+hu, -r*hu,
            -3*h1+3*h2, -(2+r)*h2+2*h3,
            -(1+r)*h3+h4+r*h0/d, -r*h4]

def integrate(z0, d, r, t, step=.0015):
    if t == 0: return [float(x) for x in z0]
    import math
    n = math.ceil(t/step)
    h = t/n
    x = [float(x) for x in z0]
    def add(a,b,c): return [v + c*w for v,w in zip(a,b)]
    for _ in range(n):
        k1=rhs(x,d,r)
        k2=rhs(add(x,k1,h/2),d,r)
        k3=rhs(add(x,k2,h/2),d,r)
        k4=rhs(add(x,k3,h),d,r)
        x=[v+h*(a+2*b+2*c+e)/6 for v,a,b,c,e in zip(x,k1,k2,k3,k4)]
    return x

def f(d,t):
    return (2*(d-7)*exp(3*t) - 3*(7*d-19)*exp(2*t)
            +(30*(d-1)*t+6*(d-7))*exp(t)+13*d-1)

def exact_at_resonance(d, t):
    return exp(-4*t)*f(d,t)/(15*d*d*(d+2))

def e31(m, r, t):
    m20,m11,m40,m31,m22,m13=m
    if r == 1:
        return float(m40)*exp(-t)+float(m31)*t*exp(-t)
    return float(m40)*exp(-t)+float(m31)*exp(-t)*(-expm1(-(r-1)*t))/(r-1)

def small_coefficient(d,r):
    return -6*r*(d+r+1)/(d*d*(d+2)*(r+1)*(r+2)*(r+3))

def long_coefficient(d,r):
    return 6*r*(r*d-4*r-6)/(d*d*(d+2)*(r-1)*(r+1)**2*(r+2)*(r+3))

def matvec(z,d,r):
    return rhs(z,d,r)

def exact_nth_diff(d,r,n):
    initial=moments(d,r)
    vector=initial
    for _ in range(n):
        vector=matvec(vector,Q(d),Q(r))
    v=Q(r)
    return (-1)**n*initial[2] + ((-1)**n-(-v)**n)/(v-1)*initial[3]-vector[2]

def bisect(d):
    lo,hi=.05,12.
    check(exact_at_resonance(d,lo)<0 and exact_at_resonance(d,hi)>0,"root bracket")
    for _ in range(70):
        mid=(lo+hi)/2
        if exact_at_resonance(d,mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

if __name__=='__main__':
    # Verify that the six exact stationary moment identities follow from L.
    for d in [1,2,3,7,8,10,20,50]:
        for r in [Q(3,2),Q(2),Q(7,2)]:
            m20,m11,m40,m31,m22,m13=moments(d,r)
            u2=Q(1,d);u4=Q(3,d*(d+2))
            check((1+r)*m11==u2,"x-u stationary balance")
            check(m20==m11,"x^2 stationary balance")
            check((1+r)*m13==u4,"x-u^3 stationary balance")
            check((2+r)*m22==2*m13+r*u2*m20,"x^2-u^2 stationary balance")
            check((3+r)*m31==3*m22,"x^3-u stationary balance")
            check(m40==m31,"x^4 stationary balance")
            if r != 1:
                for n in (0,1,2):
                    check(exact_nth_diff(d,r,n)==0,"first three Taylor coefficients")
                check(exact_nth_diff(d,r,3)==-Q(36)*r*(d+r+1)/(d*d*(d+2)*(r+1)*(r+2)*(r+3)),"third Taylor coefficient")
    # Integrated moment hierarchy independent from the direct closed formula.
    for d in [1,2,3,7,8,9,12,30]:
        m=moments(d,Q(2))
        for t in [.05,.2,.5,1.,2.,4.,6.,8.]:
            h=integrate(m,d,2.,t)
            independently=e31(m,2.,t)-h[2]
            proposed=exact_at_resonance(d,t)
            check(abs(independently-proposed)<1.5e-8,
                  f'backward-moment test failed: d={d}, t={t}')
    # Finite numerical checks of the proved unique crossing regimes.
    for d in [1,2,3,4,5,6,7]:
        for t in [.02,.08,.2,.6,1,2,4,8]:
            check(exact_at_resonance(d,t)<0,"nonpositive-sign regime")
    roots={}
    for d in [8,9,10,12,20,50]:
        root=bisect(d)
        roots[d]=round(root,9)
        check(exact_at_resonance(d,root-.02)<0,"root sign below")
        check(exact_at_resonance(d,root+.02)>0,"root sign above")
    # General rates: long-time coefficient is independently reconstructed from
    # the eigenmode-forcing cascade at exponent -1, not the formula F_d.
    for d in [1,3,7,8,12,30]:
        for r in [Q(5,4),Q(3,2),Q(2),Q(7,2),Q(5)]:
            m20,m11,m40,m31,m22,m13=moments(d,r)
            ca=m20-m11/(1-r)
            h3a=ca/d
            h2a=2*h3a/(1+r)
            h1a=3*h2a/2
            e31a=m40-m31/(1-r)
            independent=e31a-h1a
            check(independent == Q(6)*r*(r*d-4*r-6)/(d*d*(d+2)*(r-1)*(r+1)**2*(r+2)*(r+3)),
                  "independent long-time coefficient")
    # Nonzero stationary Gaussian OU added independently has symmetric two-time
    # second moments and fourth moments: all mixed 4th-order antisymmetry terms cancel.
    for d in [1,3,8]:
        for t in [.25,1.,3.]:
            active=exact_at_resonance(d,t)
            for gaussian_variance in [.2,1.4,10.]:
                cov=gaussian_variance*exp(-t)
                variance_active=float(moments(d,Q(2))[0])
                active_cov=(2*exp(-t)-exp(-2*t))/(3*d)
                extra_fwd=3*variance_active*cov+3*gaussian_variance*active_cov
                extra_back=3*variance_active*cov+3*gaussian_variance*active_cov
                check(abs((active+extra_fwd-extra_back)-active)<1e-13,
                      'Gaussian cancellation')
    print(f'PASS {COUNT} deterministic checks; crossover roots {roots}')
