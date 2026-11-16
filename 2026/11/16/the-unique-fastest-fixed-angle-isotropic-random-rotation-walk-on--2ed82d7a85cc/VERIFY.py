"""Supplemental exact-rational and finite Fourier checks for fixed-angle rotation mixing.

Run with Python 3 standard library: python VERIFY.py
The analytic proof, not these finite tests, establishes the infinite-dimensional result.
"""
from fractions import Fraction as F
from math import acos, sqrt, sin, cos, pi


def cubic(c):
    return 12*c**3 + 6*c**2 + c + 2


def poly(j,c):
    if j == 1: return (1+2*c)/3
    if j == 2: return (4*c*c+2*c-1)/5
    if j == 3: return (8*c**3+4*c*c-4*c-1)/7
    raise ValueError(j)

lo, hi=F(-5,7),F(-7,10)
assert cubic(lo)==F(-9,343)
assert cubic(hi)==F(31,250)
assert poly(2,F(-3,5))==F(-19,125)
assert poly(3,F(-3,5))==F(139,875)
assert F(139,875)>F(1,7)>F(2,15)>F(11,125)
assert 1/(9*sqrt(17/20)) < 2/15
for _ in range(100):
    m=(lo+hi)/2
    if cubic(m)<0: lo=m
    else: hi=m
c=float((lo+hi)/2)
rho=-poly(1,c)
theta=acos(c)
assert abs(poly(3,c)-rho)<1e-14
assert abs(poly(2,c))<rho
assert abs(theta-2.362917121238644)<1e-12
assert abs(rho-0.14122959002095445)<1e-12
checks=8
# Confirm that the trigonometric character and polynomial forms agree.
for j in (1,2,3):
    for k in range(1,101):
        u=pi*k/101
        assert abs(poly(j,cos(u))-sin((j+0.5)*u)/((2*j+1)*sin(u/2)))<2e-13
        checks+=1
# Finite stress test of the infinite-spin theorem, including all boundary angles.
for i in range(2001):
    cc=-1+i/1000
    ang=acos(cc)
    if ang==0: continue
    vals=[sin((j+0.5)*ang)/((2*j+1)*sin(ang/2)) for j in range(1,151)]
    assert max(map(abs,vals)) >= rho-1e-12
    checks+=1
for j in range(4,2001):
    assert abs(sin((j+0.5)*theta)/((2*j+1)*sin(theta/2)))<rho
    checks+=1
print('checks_passed',checks)
print('cos_angle',format(c,'.16f'))
print('angle_radians',format(theta,'.16f'))
print('angle_degrees',format(theta*180/pi,'.12f'))
print('optimal_L2_contraction',format(rho,'.16f'))
print('active_spins',1,3)
print('spin2',format(poly(2,c),'.16f'))
