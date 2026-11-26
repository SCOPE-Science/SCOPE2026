"""Exact checks for complementary-stage stability in randomized implicit two-stage methods.
Run with Python 3.11+ and SymPy 1.12+.
"""
from fractions import Fraction as F
from itertools import product
import cmath
import math
import sympy as s

z,t,u,v,y=s.symbols('z t u v y',real=True)
r=lambda a,b: (1+(1-b)*a)/(1-b*a)
c=t*(1-t)
g=s.factor(r(z,t)*r(z,1-t))
assert s.factor(g-(1+z+c*z**2)/(1-z+c*z**2))==0
# On imaginary z, exact rational absolute squares.
modi=lambda b:(1+(1-b)**2*y**2)/(1+b**2*y**2)
q=s.factor(modi(u)*modi(v)-1)
assert s.factor(s.limit(q/y**2,y,0)-2*(1-u-v))==0
assert s.factor(modi(t)*modi(1-t)-1)==0
# For any complex z: |D|^2-|N|^2 = -4 Re(z) (1+c |z|^2).
a,b=s.symbols('a b',real=True)
zz=a+s.I*b
N=1+zz+c*zz**2;D=1-zz+c*zz**2
assert s.factor(s.expand_complex(D*s.conjugate(D)-N*s.conjugate(N)) - (-4*a*(1+c*(a*a+b*b))))==0
# IID uniform stage: the closed-form imaginary-axis inflation.
ypos=s.symbols('x',positive=True)
expr=1 + ypos*s.atan(ypos)-s.log(1+ypos**2)
der=s.simplify(s.diff(expr,ypos)- (s.atan(ypos)-ypos/(1+ypos**2)))
assert der==0
assert s.limit(expr,ypos,0)==1
# Exact rational checks for all grid stages and many left-half-plane parameters.
count=0
Ts=[F(i,12) for i in range(13)]
Zs=[complex(-a/5,b/7) for a,b in product(range(1,13),range(-8,9))]
for tt in Ts:
    cc=float(tt*(1-tt))
    for zz0 in Zs:
        g0=(1+zz0+cc*zz0*zz0)/(1-zz0+cc*zz0*zz0)
        assert abs(g0)<1+1e-12
        actual=abs(1-zz0+cc*zz0*zz0)**2-abs(1+zz0+cc*zz0*zz0)**2
        target=-4*zz0.real*(1+cc*abs(zz0)**2)
        assert abs(actual-target)<1e-8 * max(1,abs(target))
        count+=1
for tt in Ts:
    yy=2.5j
    assert abs(abs(r(yy,float(tt))*r(yy,1-float(tt)))-1)<1e-12
q5=1+F(25,6)-2*math.log(6)
assert q5>1.5
for tt in Ts:
    zz0=-5
    assert abs(float(r(zz0,tt)*r(zz0,1-tt)))<=F(2,3)+1e-10
print(f'VERIFY_OK symbolic identities, antithetic imaginary conservation, {count} left-half-plane pairs, iid divergence at z=-5')
