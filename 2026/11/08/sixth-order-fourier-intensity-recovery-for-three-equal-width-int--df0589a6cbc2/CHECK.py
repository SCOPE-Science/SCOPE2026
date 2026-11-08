"""Exact and numerical checks for equal-width three-interval Fourier-intensity jets.

Requirements: Python 3, SymPy, mpmath. No downloaded data required.
"""
import math
import random
import sympy as sp
from mpmath import mp

L,u,v,t,Q,A = sp.symbols('L u v t Q A', positive=True)
P2 = u**2+v**2+(u+v)**2
P4 = u**4+v**4+(u+v)**4
P6 = u**6+v**6+(u+v)**6
T = u**2+u*v+v**2
assert sp.expand(P2-2*T)==0
assert sp.expand(P4-2*T**2)==0
assert sp.expand(P6-2*T**3-3*(u*v)**2*(u+v)**2)==0
assert sp.expand((u+v)**2-T-u*v)==0

sinc_sq = 1-L**2*t**2/sp.Integer(12)+L**4*t**4/sp.Integer(360)-L**6*t**6/sp.Integer(20160)
interference = 9-P2*t**2 + P4*t**4/sp.Integer(12)-P6*t**6/sp.Integer(360)
poly=sp.Poly(sp.expand(L**2*sinc_sq*interference),t)
I2 = -2*L**2*P2 - sp.Rational(3,2)*L**4
I4 = 2*L**2*P4 + 2*L**4*P2 + sp.Rational(3,5)*L**6
I6 = -2*L**2*P6 - 5*L**4*P4 - 2*L**6*P2 - sp.Rational(9,28)*L**8
assert sp.expand(poly.coeff_monomial(t**2)*2-I2)==0
assert sp.expand(poly.coeff_monomial(t**4)*24-I4)==0
assert sp.expand(poly.coeff_monomial(t**6)*720-I6)==0
assert sp.expand(I4-(L**2*P2**2+2*L**4*P2+sp.Rational(3,5)*L**6))==0
# At fixed A, P6 is 2*A^3+3*Q^2*(A+Q). Its derivative in Q
# is strictly positive. The admissible endpoint Q=A/3 yields 22*A^3/9.
assert sp.expand((2*A**3 + 3*(A/sp.Integer(3))**2*(A+A/sp.Integer(3)))-sp.Rational(22,9)*A**3)==0
assert sp.expand(sp.diff(2*A**3+3*Q**2*(A+Q),Q)-3*Q*(2*A+3*Q))==0

mp.dps=65
random.seed(1804)
count=9

def forward(l,x,y):
    p2=x*x+y*y+(x+y)**2
    p4=x**4+y**4+(x+y)**4
    p6=x**6+y**6+(x+y)**6
    return (9*l*l, -2*l*l*p2-mp.mpf(3)/2*l**4,
            2*l*l*p4+2*l**4*p2+mp.mpf(3)/5*l**6,
            -2*l*l*p6-5*l**4*p4-2*l**6*p2-mp.mpf(9)/28*l**8)

def reconstruct(jets):
    i0,i2,i4,i6=jets
    l=mp.sqrt(i0)/3
    p2=-i2/(2*l*l)-mp.mpf(3)/4*l*l
    p4=p2*p2/2
    p6=(-i6-5*l**4*p4-2*l**6*p2-mp.mpf(9)/28*l**8)/(2*l*l)
    aa=p2/2
    target=(p6-2*aa**3)/3
    left,right=mp.mpf('0'),aa/3
    for _ in range(260):
        mid=(left+right)/2
        if mid*mid*(aa+mid)<target: left=mid
        else: right=mid
    qq=(left+right)/2
    dx=mp.sqrt(max(mp.mpf('0'),aa-3*qq))
    st=mp.sqrt(aa+qq)
    return (l,(st+dx)/2,(st-dx)/2,p2,p6,qq)

# Rational lengths and exact finite-dimensional Taylor coefficients.
for ln in (mp.mpf('0.5'),mp.mpf('1'),mp.mpf('1.25')):
    for x in (ln+mp.mpf('0.5'),ln+mp.mpf('1'),ln+mp.mpf('3')):
        for y in (ln+mp.mpf('0.4'),ln+mp.mpf('1'),ln+mp.mpf('2.5')):
            jets=forward(ln,x,y)
            l,rr,ss,p2,p6,qq=reconstruct(jets)
            assert abs(l-ln)<mp.mpf('1e-50')
            assert abs(rr-max(x,y))<mp.mpf('1e-35')
            assert abs(ss-min(x,y))<mp.mpf('1e-35')
            assert abs(jets[2]-(l*l*p2*p2+2*l**4*p2+mp.mpf(3)/5*l**6))<mp.mpf('1e-40')
            assert abs(forward(l,rr,ss)[3]-jets[3])<mp.mpf('1e-35')
            count+=5

# The stability exponent 1/2 is sharp on the constant-second-jet curve.
l=mp.mpf('1'); w=mp.mpf('2'); aa=3*w*w
base=forward(l,w,w)
for eps in ('0.01','0.001','0.0001','0.00001'):
    e=mp.mpf(eps)
    q=aa/3-e*e/3
    ss=mp.sqrt(aa+q)
    x,y=(ss+e)/2,(ss-e)/2
    dat=forward(l,x,y)
    assert abs(dat[0]-base[0])<mp.mpf('1e-40')
    assert abs(dat[1]-base[1])<mp.mpf('1e-40')
    assert abs(dat[2]-base[2])<mp.mpf('1e-40')
    assert abs((dat[3]-base[3])/e**2 - 2*l*l*aa**2)<mp.mpf('0.01')
    assert abs((x-y)/e-1)<mp.mpf('1e-40')
    count+=5

print('EQUAL_WIDTH_THREE_INTERVAL_JET_CHECKS_PASSED',count)
