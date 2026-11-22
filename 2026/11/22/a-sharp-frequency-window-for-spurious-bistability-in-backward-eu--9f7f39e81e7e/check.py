#!/usr/bin/env python3
"""Standalone exact-rational and numerical stress checks for backward-Euler Hopf map.
This finite checker is a supplement, not a proof of universal claims.
Requires only Python 3 standard library.
"""
from fractions import Fraction as Q
from math import sqrt, hypot


def jacobian_det(a,b,u):
    return (a+u)*(a+3*u)+b*b

def radial_image(a,b,h,s):
    return s*hypot(a+h*s*s,b)

def next_radius(a,b,h,target):
    if target==0:return 0.
    lo,hi=0., max(1.,target)
    while radial_image(a,b,h,hi) < target:hi*=2
    for _ in range(96):
        mid=(lo+hi)/2
        if radial_image(a,b,h,mid) < target:lo=mid
        else:hi=mid
    return (lo+hi)/2

def check_case(b,c,a):
    h=Q(1)
    assert b>0 and b*b+c*c==1 and c>0 and a< -c
    assert 3*b*b > a*a  # strict derivative positivity for all radii
    u_i=-a-c;u_o=-a+c
    assert Q(0)<u_i<u_o
    assert (a+u_i)**2+b*b == 1
    assert (a+u_o)**2+b*b == 1
    assert a*a+b*b>1
    assert jacobian_det(a,b,u_i)==1-2*c*u_i
    assert jacobian_det(a,b,u_o)==1+2*c*u_o
    assert Q(0)<jacobian_det(a,b,u_i)<1
    assert jacobian_det(a,b,u_o)>1
    for k in range(600):
        u=Q(k,113)
        assert jacobian_det(a,b,u)>0
    for radius, expected in [(0.10*sqrt(float(u_i)),0),(0.75*sqrt(float(u_i)),0),
                             ((sqrt(float(u_i))+sqrt(float(u_o)))/2,sqrt(float(u_o))),
                             (2.6*sqrt(float(u_o)),sqrt(float(u_o)))]:
        x=radius
        for _ in range(450):
            y=next_radius(float(a),float(b),1.,x)
            assert x==0 or y>=0
            x=y
        assert abs(x-expected)<1.e-6,(b,c,a,radius,x,expected)
    return u_i,u_o,jacobian_det(a,b,u_i),jacobian_det(a,b,u_o)

cases=[(Q(3,5),Q(4,5),Q(-9,10)),(Q(4,5),Q(3,5),Q(-1))]
for b,c,a in cases:
    print('case b,c,a=',b,c,a, 'inner²,outer²,implicit radial slopes=',check_case(b,c,a))
# The necessary and sufficient nonempty window test is algebraic 3b²>c² iff b>1/2.
for numer in range(1,100):
    b=Q(numer,100)
    c2=1-b*b
    assert (3*b*b>c2) == (b>Q(1,2))
# For positive b and a<0, the minimum of det DP over u>=0 occurs at u=-2a/3.
for b in [Q(1,4),Q(1,2),Q(3,5),Q(4,5),Q(5,4)]:
    for a in [Q(-3),Q(-1),Q(-1,2),Q(0),Q(1)]:
        u0=max(Q(0),-Q(2,3)*a)
        assert all(jacobian_det(a,b,u0) <= jacobian_det(a,b,max(Q(0),u0+Q(k,1000))) for k in (-200,-100,-1,0,1,100,200))
        if a<0:
            assert jacobian_det(a,b,u0)==b*b-a*a/3
print('PASS: rational radii, Jacobian, multipliers, phase window and radial iterates')
