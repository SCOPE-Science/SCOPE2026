#!/usr/bin/env python3
"""Deterministic independent numerical and algebraic checks for Cassini normal multiplicity.
Run: python3 geometry_cassini_normal_check.py; requires only the Python standard library.
Finite grids corroborate, but do not replace, the analytic proof.
"""
from math import sin, cos, pi, sqrt, acos, atan2, floor
import cmath

def tangent_rate(s,t):
    return (s*s+2+3*s*cos(t))/(2*(1+s*s+2*s*cos(t)))

def turn_halfwidth(s):
    assert 1 < s < 2
    phi=acos((s*s+2)/(3*s))
    psi=acos(sqrt((s*s-1)/3))
    return psi-2*phi

def curve(s,t):
    w=1+s*complex(cos(t),sin(t))
    arg=atan2(w.imag,w.real)
    if s>1:
        arg += 2*pi*floor((t+pi-1e-12)/(2*pi))
    return sqrt(abs(w))*complex(cos(arg/2),sin(arg/2))

def formula_curvature(s,t):
    return (s*s+2+3*s*cos(t))/(s*(1+s*s+2*s*cos(t))**.75)

def direct_curvature(s,t):
    z=curve(s,t)
    w=s*complex(cos(t),sin(t))
    zp=1j*w/(2*z)
    zpp=-w/(2*z)+w*w/(4*z*z*z)
    return (zp.conjugate()*zpp).imag/abs(zp)**3

def quad_abs(s,n=50000):
    length=4*pi if s>1 else 2*pi
    h=length/n
    return (2 if s<1 else 1)*h*sum(abs(tangent_rate(s,(i+.5)*h)) for i in range(n))

def exact_abs(s):
    if s<1:return 4*pi  # both convex components
    if s>=2:return 2*pi
    return 2*pi+4*turn_halfwidth(s)

def tangent_angle(s,t):
    w=1+s*complex(cos(t),sin(t))
    phase=atan2(w.imag,w.real)+2*pi*floor((t+pi-1e-12)/(2*pi))
    return t+pi/2-phase/2

def count_preimages(s,target,n=15000):
    # t in [0,4*pi], count crossings of the lifted tangent-angle level.
    h=4*pi/n
    vals=[tangent_angle(s,i*h) for i in range(n+1)]
    answer=0
    for k in range(-1,3):
        v=target+2*pi*k
        answer+=sum((a-v)*(b-v)<0 for a,b in zip(vals,vals[1:]))
    return answer

def run():
    checks=0
    for s in [.15,.47,.85,1.02,1.1,1.3,1.6,1.95,2.0,2.3,3.5]:
        for j in range(1,67):
            t=(j+.37)*(2*pi if s<1 else 4*pi)/68
            a=direct_curvature(s,t)
            b=formula_curvature(s,t)
            assert abs(a-b)<2e-10*(1+abs(b)), (s,t,a,b)
            checks+=1
        actual=quad_abs(s)
        expected=exact_abs(s)
        assert abs(actual-expected)<4e-6, (s,actual,expected)
        print('s=',s,'absolute_turning=',format(expected,'.12f'),'quadrature_error=',format(actual-expected,'.3g'))
        checks+=1
    for s in [1.1,1.3,1.6,1.95]:
        m=128
        counts=[count_preimages(s,(j+.347)*2*pi/m,n=5000) for j in range(m)]
        assert set(counts).issubset({1,3}), (s,set(counts))
        observed=sum(v==3 for v in counts)/m
        expected=turn_halfwidth(s)/pi
        assert abs(observed-expected)<.015, (s,observed,expected)
        print('s=',s,'triple_normal_fraction=',format(expected,'.12f'),'sampled=',observed)
        checks+=1
    for s in [1.0001,1.00001,1.999,1.9999]:
        A=turn_halfwidth(s)
        q=(pi/2-A)/sqrt(s-1) if s<1.1 else A/(2-s)**1.5
        target=sqrt(6) if s<1.1 else 2/(3*sqrt(3))
        assert abs(q-target)/target<.002
        print('endpoint',s,'scaled_coefficient=',q,'target=',target)
        checks+=1
    print('PASS:',checks,'deterministic assertions')
if __name__=='__main__':run()
