#!/usr/bin/env python3
"""Independent numerical and analytic checks for two-harmonic evolute loop."""
import math
import mpmath as mp
mp.mp.dps=70
b=mp.mpf('0.01')
C=128*mp.sqrt(3)/8505

def xy(u,a,b):
    x=-3*a*mp.cos(u)-a*mp.cos(3*u)+6*b*mp.cos(2*u)+3*b*mp.cos(4*u)
    y=3*a*mp.sin(u)-a*mp.sin(3*u)-6*b*mp.sin(2*u)+3*b*mp.sin(4*u)
    return x,y

def area(delta):
    a=6*b-delta
    u0=mp.acos(a/(6*b))
    def func(t):
        x,y=xy(t,a,b)
        yp=3*a*mp.cos(t)-3*a*mp.cos(3*t)-12*b*mp.cos(2*t)+12*b*mp.cos(4*t)
        return (x-xy(0,a,b)[0])*yp
    return abs(2*mp.quad(func,[0,u0])),u0
for r in ['0.1','0.05','0.02','0.01','0.005']:
 d=b*mp.mpf(r)
 v,u0=area(d)
 q=v/(d**mp.mpf('4.5')/b**mp.mpf('2.5'))
 print('delta/b=',r,'u0=',mp.nstr(u0,12),'scaled_area=',mp.nstr(q,18),'predicted=',mp.nstr(C,18))
assert abs(float(area(b*mp.mpf('0.005'))[0]/((b*mp.mpf('0.005'))**mp.mpf('4.5')/b**mp.mpf('2.5'))-C)) < .0002
print('EVOLUTE_TWO_HARMONIC_LOOP_CHECKS_OK')
