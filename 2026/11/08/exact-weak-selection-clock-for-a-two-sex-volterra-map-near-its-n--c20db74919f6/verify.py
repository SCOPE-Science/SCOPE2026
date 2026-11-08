"""Reproduce exact near-balance slow-selection identities and finite-scale checks.

Run: python verify.py
Exact symbolic identities certify algebra; finite sample trajectories only corroborate
(the universal limit is established analytically in RESULT.md).
"""
import math
import sympy as sp
from scipy.optimize import brentq

x,y,a,b,c,d,t=sp.symbols('x y a b c d t',positive=True)
X=x-a*x*(1-y)+b*y*(1-x)
Y=y+d*x*(1-y)-c*y*(1-x)
eps=b*d-a*c
H=y+c*x/b
assert sp.factor((Y+c*X/b)-H-eps*x*(1-y)/b)==0
R=a+(b-a)*t
xg=b*t/R
yg=t
Hg=sp.factor(yg+c*xg/b)
assert sp.factor(sp.diff(Hg,t)-(1+a*c/R**2))==0
v=sp.factor(t*(1-t)*R/(R**2+a*c))
G=(a+c)*sp.log(t)-(b+a*c/b)*sp.log(1-t)-c*(b-a)*sp.log(R)/b
assert sp.simplify(sp.diff(G,t)-1/v)==0
# Invariant balanced curve and derivative contraction on every H chord.
assert sp.factor((X-x).subs({x:xg,y:t}))==0
assert sp.factor((Y-y).subs({x:xg,y:t,d:a*c/b}))==0
h=sp.symbols('h', real=True)
chord=sp.expand(X.subs(y,h-c*x/b))
p=(1-a)*(1-y)+(1-b)*y
q=(1-x)*c+x*d
assert sp.factor((sp.diff(chord,x)-(p-q)).subs({y:h-c*x/b,d:a*c/b}))==0

# Finite trajectories for both perturbation signs on the predicted slow clock.
a0,b0,c0=0.4,0.6,0.3
z0=(0.7,0.2)
H0=z0[1]+c0*z0[0]/b0

def y_on_h(H_value):
    return brentq(lambda yy: yy+c0*yy/(a0+(b0-a0)*yy)-H_value,0,1,xtol=1e-14)

def primitive(yy):
    rr=a0+(b0-a0)*yy
    return (a0+c0)*math.log(yy)-(b0+a0*c0/b0)*math.log(1-yy)-c0*(b0-a0)/b0*math.log(rr)

y_init=y_on_h(H0)
assert abs(y_init+c0*y_init/(a0+(b0-a0)*y_init)-H0)<1e-13
checked=0
for sign in (-1,1):
    for slow_T in (0.5,1.0):
        desired=primitive(y_init)+sign*slow_T
        target=brentq(lambda yy:primitive(yy)-desired,1e-12,1-1e-12,xtol=1e-14)
        expected_H=target+c0*target/(a0+(b0-a0)*target)
        last_error=None
        for s in (0.01,0.005,0.0025):
            d0=(a0*c0+sign*s)/b0
            xx,yy=z0
            n=round(slow_T/s)
            for _ in range(n):
                xx,yy=(xx-a0*xx*(1-yy)+b0*yy*(1-xx),
                       yy+d0*xx*(1-yy)-c0*yy*(1-xx))
            current_H=yy+c0*xx/b0
            err=abs(current_H-expected_H)
            assert err < 7*s  # empirical finite-parameter bound, not used in proof
            if last_error is not None: assert err<last_error
            last_error=err
        checked+=1
print('VERIFY_OK exact_slow_primitive=1 exact_balance_identity=1 exact_transverse_derivative=1 finite_slow_clocks=4 three_scale_convergence_checks=12')
