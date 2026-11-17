#!/usr/bin/env python3
"""Independent numeric and symbolic checks for affine least squares on polygon perimeters.
Run: python verify_regular_polygon_affine.py ; requires mpmath and sympy.
"""
from math import ceil
import mpmath as mp
import sympy as sp

mp.mp.dps = 65

def main_formula(n):
    h = 2*mp.pi/n
    c = 6/(2+mp.cos(h))
    k = (n+2)//3
    a = 1+c*mp.cos(k*h)
    F = (c*(mp.sin((k-mp.mpf('0.5'))*h)/mp.sin(h/2)
             + mp.cos(k*h))-(n-2*k)
         +a*a/(c*(mp.cos((k-1)*h)-mp.cos(k*h))))
    return 1+2*F/n

def edge_abs(a,b):
    if a >= 0 and b >= 0: return (a+b)/2
    if a <= 0 and b <= 0: return -(a+b)/2
    return (a*a+b*b)/(2*abs(a-b))

def numeric_evaluation(n, position):
    h=2*mp.pi/n
    v=[(mp.cos(j*h),mp.sin(j*h)) for j in range(n)]
    x,y=position
    c=6/(2+mp.cos(h))
    kern=[1+c*(x*vx+y*vy) for vx,vy in v]
    return sum(edge_abs(kern[j],kern[(j+1)%n]) for j in range(n))/n

for n in range(3,111):
    h=2*mp.pi/n
    k=(n+2)//3
    c=6/(2+mp.cos(h))
    assert 1+c*mp.cos((k-1)*h)>0 and 1+c*mp.cos(k*h)<0
    exact=main_formula(n)
    direct=numeric_evaluation(n,(mp.mpf(1),mp.mpf(0)))
    assert abs(exact-direct)<mp.mpf('1e-51'),(n,exact,direct)
    for j in range(1,min(n,7)):
        v=(mp.cos(j*h),mp.sin(j*h))
        # exact rotational invariance
        assert abs(exact-numeric_evaluation(n,v))<mp.mpf('1e-51')
    for j in range(min(n,7)):
        v=(mp.cos(j*h),mp.sin(j*h))
        w=(mp.cos((j+1)*h),mp.sin((j+1)*h))
        for t in (mp.mpf('0.25'),mp.mpf('0.5'),mp.mpf('0.75')):
            x=((1-t)*v[0]+t*w[0],(1-t)*v[1]+t*w[1])
            assert numeric_evaluation(n,x)<exact-mp.mpf('1e-45')
    # independent exact edge second-moment calculation in 2-D
    cov=sum((v0*v0+v0*v1+v1*v1)/3 for v0,v1 in [
        (mp.cos(j*h),mp.cos((j+1)*h)) for j in range(n)])/n
    assert abs(cov-(2+mp.cos(h))/6)<mp.mpf('1e-51')
print('INDEPENDENT_FULL_PERIMETER_KERNEL_INTEGRATION_OK',108)
print('STRICT_VERTEX_ONLY_NORMING_AND_SIGN_CUTOFF_SAMPLES_OK',108)

# Explicit symbolic series, with the first negative vertex determined by n mod 3.
h=sp.symbols('h',positive=True)
c=6/(2+sp.cos(h))
a=2*sp.pi/3
for delta, expected_sign in ((sp.S.Zero,0),(sp.Rational(1,3),1),(sp.Rational(2,3),-1)):
    theta=a+delta*h
    z=1+c*sp.cos(theta)
    zm=1+c*sp.cos(theta-h)
    neg=c*(sp.sin(theta-h/2)/sp.sin(h/2)+sp.cos(theta))-(2*sp.pi/(3*h)-2*delta)+z*z/(zm-z)
    target=-2*sp.pi/(3*h)+2*sp.sqrt(3)/h+sp.sqrt(3)*h/6+expected_sign*h*h/sp.Integer(81)
    diff=sp.series(neg-target,h,0,3).removeO().expand()
    assert sp.simplify(diff)==0,(delta,diff)
print('EXACT_THREE_RESIDUE_TAYLOR_CERTIFICATES_OK')

limit=mp.mpf(1)/3+2*mp.sqrt(3)/mp.pi
C2=2*mp.pi*mp.sqrt(3)/3
C3=8*mp.pi**2/81
for n in (300,301,302,3000,3001,3002):
    eta={0:0,1:-1,2:1}[n%3]
    remainder=main_formula(n)-limit-C2/n**2-eta*C3/n**3
    assert abs(remainder)*n**4 < 25, (n,remainder*n**4)
print('INDEPENDENT_ASYMPTOTIC_REMAINDER_SAMPLES_OK')
print('ALL_REGULAR_POLYGON_AFFINE_PROJECTION_CHECKS_OK')
