"""Standalone algebraic and numerical checks for a three-site branching model.

Requires Python 3, SymPy, and SciPy. Checks support the accompanying analytic proof;
they do not replace it.
"""
from fractions import Fraction
from math import sqrt
import sympy as S
import numpy as np
from scipy.optimize import root

b,r1,r2,r3,z=S.symbols('b r1 r2 r3 z',positive=True)
t=r1/b
c=(r1-r2)*t
q=b*z*z-r3*z+c
migration=c/(z-t)
f1=S.factor(r1*t-b*t*t+migration*(t-t))
f2=S.factor(r2*t-b*t*t+migration*(t+z-2*t))
f3=S.factor(r3*z-b*z*z+migration*(t-z))
assert f1==0 and f2==0
assert S.simplify(f3+q)==0
assert S.factor(q.subs(z,t)) == t*(2*r1-r2-r3)

B=S.Rational(10);R1=S.Rational(6);R2=S.Rational(8);R3=S.Rational(1)
T=R1/B;Z=S.Rational(2,5);M=S.Rational(6)
assert (T,Z,M)==(S.Rational(3,5),S.Rational(2,5),S.Rational(6))
assert S.simplify(q.subs({b:B,r1:R1,r2:R2,r3:R3,z:Z}))==0
assert S.simplify(q.subs({b:B,r1:R1,r2:R2,r3:R3}) - (10*z+3)*(z-S.Rational(2,5)))==0
assert S.simplify(migration.subs({b:B,r1:R1,r2:R2,r3:R3,z:Z}))==M

def residual(p,m,rr=(6.,8.,1.),birth=10.):
    x,y,z_=p
    return np.array([rr[0]*x-birth*x*x+m*(y-x),
                     rr[1]*y-birth*y*y+m*(x+z_-2*y),
                     rr[2]*z_-birth*z_*z_+m*(y-z_)])

def solve(m,rr=(6.,8.,1.),birth=10.):
    x=root(lambda w: residual(w,m,rr,birth),np.array(rr)/birth,
           method='hybr',tol=1e-12)
    assert np.max(np.abs(residual(x.x,m,rr,birth)))<2e-9
    assert min(x.x)>0 and max(x.x)<1
    return x.x

for k in range(1,121):
    m=6*k/40
    p=solve(m)
    if abs(m-6)<1e-10:
        assert np.max(np.abs(p-np.array([.6,.6,.4])))<1e-11
    else:
        assert (p[1]>p[0]) == (m<6)
    assert p[0]>p[2] and p[1]>p[2]

# Diverse rational environmental qualities meeting the theorem's open cone.
# Numerical checks evaluate both sides of its exact algebraic threshold.
for a in range(2,12):
    for h in range(1,7):
        low=S.Rational(a,3)
        high=low+S.Rational(h,4)
        other=low-S.Rational(h+1,10)
        if other<=0 or 2*low <= high+other: continue
        birth=float(high+3)
        aa,hh,oo=map(float,(low,high,other))
        zz=(oo+sqrt(oo*oo+4*aa*(hh-aa)))/(2*birth)
        mt=(hh-aa)*(aa/birth)/(aa/birth-zz)
        for scale in (0.5,1.,2.):
            p=solve(mt*scale,(aa,hh,oo),birth)
            if scale==1.:
                assert abs(p[0]-p[1])<1e-9
            else:
                assert (p[1]>p[0])==(scale<1.)
            assert p[0]>p[2]
print('PASS: exact polynomial/root identities, 120 rate-grid comparisons, and parameter-cone tests')
