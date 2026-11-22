#!/usr/bin/env python3
"""Exact algebraic certificates and independent geometric slice tests.

Requires Python 3 standard library. All integral tests use edge interpolation,
not the closed forms under test.
"""
from fractions import Fraction as F
from math import sqrt, sin, cos, atan, pi, comb, isclose

def q(z):
    return 36*z**5-23*z**4+112*z**3-48*z**2+80*z-44

def lo(z):
    return 3*sqrt(3)/128 * z*z*(19-15*z+32*z*z-32*z**3)/((1+z)**3*(3+4*z*z))

def hi(z):
    return 3*sqrt(3)/128 * z*z*(33-29*z+18*z*z-18*z**3)/((1+z)**3*(4+3*z*z))

# Degree-12 Bernstein positivity certificate for a cross-branch comparison.
coefs = (498,1494,-7589,10185,-14424,17080)
bernstein = [sum(F(coefs[k]*comb(j,k),comb(12,k)) for k in range(min(j,5)+1)) for j in range(13)]
assert min(bernstein) == F(359,44) and all(x>0 for x in bernstein)
for j in range(21):
    z=F(j,20)
    a=sum(coefs[k]*z**k for k in range(6))
    b=sum(bernstein[i]*comb(12,i)*z**i*(1-z)**(12-i) for i in range(13))
    assert a==b

# Unique interior critical point: q'(z)>=244*z**2-96*z+80>0
assert q(F(0))==-44 and q(F(1))==113
left,right=F(519537,1000000),F(519539,1000000)
assert q(left)<0<q(right)
for _ in range(60):
    mid=(left+right)/2
    if q(mid)>0:right=mid
    else:left=mid
root=float((left+right)/2)
assert 0.51953789<root<0.51953790
assert hi(root)>hi(.5)>max(lo(j/1000) for j in range(1001))

# Independent exact geometric setup: interpolate each polygon edge at a line
# parallel to the normal of the chosen symmetrization axis. Two-point Gauss
# quadrature integrates each cubic chord-center integrand exactly.
def chord(poly, axis, coordinate):
    ex,ey=cos(axis),sin(axis)
    nx,ny=-ey,ex
    vals=[]
    for i,(x,y) in enumerate(poly):
        xx,yy=poly[(i+1)%len(poly)]
        a=x*ex+y*ey; b=xx*ex+yy*ey
        if (a<coordinate<b) or (b<coordinate<a):
            t=(coordinate-a)/(b-a)
            vals.append((x+(xx-x)*t)*nx+(y+(yy-y)*t)*ny)
    assert len(vals)==2,(poly,axis,coordinate,vals)
    return min(vals),max(vals)

def geometric_drop(poly,axis):
    u=sorted(set(x*cos(axis)+y*sin(axis) for x,y in poly))
    ans=0.
    for l,r in zip(u,u[1:]):
        if r-l<1e-13: continue
        midpoint=(l+r)/2; radius=(r-l)/(2*sqrt(3))
        for coordinate in (midpoint-radius,midpoint+radius):
            bottom,top=chord(poly,axis,coordinate)
            length=top-bottom;center=(top+bottom)/2
            ans+=(r-l)/2*length*center*center
    return ans

rt3=sqrt(3)
tri=[(1.,0.),(-.5,rt3/2),(-.5,-rt3/2)]
original=3*rt3/16
first=3*rt3/128
assert isclose(geometric_drop(tri,pi/2),first,rel_tol=1e-13,abs_tol=1e-13)
assert isclose(first/original,1/8,rel_tol=1e-14)

a,b=rt3/2,3/4
rhombus=[(a,0),(0,b),(-a,0),(0,-b)]
assert isclose(geometric_drop(rhombus,0),0,abs_tol=1e-13)
assert isclose(geometric_drop(rhombus,pi/2),0,abs_tol=1e-13)
checks=0
for j in range(1,200):
    z=j/200
    theta1=atan((a/b)*z)
    theta2=pi/2-atan((b/a)*z)
    assert isclose(geometric_drop(rhombus,theta1),lo(z),rel_tol=3e-12,abs_tol=1e-13)
    assert isclose(geometric_drop(rhombus,theta2),hi(z),rel_tol=3e-12,abs_tol=1e-13)
    checks+=2

second=hi(root)
fraction=(first+second)/original
assert .165522117<fraction<.165522120
print('PASS: 13 positive rational Bernstein coefficients, 21 polynomial identities,',checks,
      'independent polygon-slice comparisons;')
print(f'alpha={root:.12f}, second_drop={second:.12f}, two_step_fraction={fraction:.12f}')
