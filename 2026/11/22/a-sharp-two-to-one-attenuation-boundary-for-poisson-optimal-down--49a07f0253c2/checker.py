"""Reproducibility checks for two-attenuation Poisson sensor placement.
The algebraic theorem is proved in RESULT.md; tests check symbolic identities and numerical instances.
"""
from fractions import Fraction
import math
import random
import sympy as s

r,p,t,A,n0,n1 = s.symbols('r p t A n0 n1', positive=True)
f,df = s.symbols('f df', positive=True)
I=s.Matrix([[(n0+n1*f)/A,n1*df],[n1*df,A*n1*df**2/f]])
assert s.simplify(I.det()-n0*n1*df**2/f)==0
F=t**r*(1-t)**2/(p+(1-p)*t)
P=s.expand(r*(1-t)*(p+(1-p)*t)-2*t*(p+(1-p)*t)-(1-p)*t*(1-t))
assert s.simplify(P-(r*p+(r*(1-2*p)-1-p)*t-(r+1)*(1-p)*t*t))==0
assert s.simplify(s.diff(s.log(F),t)-P/(t*(1-t)*(p+(1-p)*t)))==0
assert s.simplify(P.subs(t,1)+2)==0
# Calculus monotonicity in p for the derivative of log objective.
assert s.simplify(s.diff(s.diff(s.log(F),t),p)-1/(p+(1-p)*t)**2)==0
# Small-p asymptotic coefficients.

rng=random.Random(4420261118)
cases=0
for j in range(4000):
    slow=10**rng.uniform(-1.5,0.5)
    fast=slow*(1+10**rng.uniform(-1.2,1.2))
    pp=10**rng.uniform(-6,-.002)
    rr=slow/(fast-slow)
    bb=rr*(1-2*pp)-1-pp
    cc=(rr+1)*(1-pp)
    tt=2*rr*pp/(math.sqrt(bb*bb+4*cc*rr*pp)-bb) if bb<0 else (bb+math.sqrt(bb*bb+4*cc*rr*pp))/(2*cc)
    # use stable exact quadratic root via polynomial solve robustly
    tt=(bb+math.sqrt(bb*bb+4*cc*rr*pp))/(2*cc) if bb>=0 else 2*rr*pp/(math.sqrt(bb*bb+4*cc*rr*pp)-bb)
    assert 0<tt<1,(j,rr,pp,tt)
    def val(x):
        u=math.exp(-slow*x);v=math.exp(-fast*x)
        return (u-v)**2/(pp*u+(1-pp)*v)
    xx=-math.log(tt)/(fast-slow)
    vv=val(xx)
    assert vv>val(xx*.97) and vv>val(xx*1.03), (j,slow,fast,pp,xx)
    # independent derivative zero condition
    assert abs(float(P.subs({r:rr,p:pp,t:tt})))<1e-9
    cases+=1
# Explicit asymptotic cases: alpha<1, alpha=1, alpha>1.
for rr in [.5,1.,2.]:
    for pp in [1e-6,1e-9,1e-12]:
        bb=rr*(1-2*pp)-1-pp; cc=(rr+1)*(1-pp)
        tt=(bb+math.sqrt(bb*bb+4*cc*rr*pp))/(2*cc) if bb>=0 else 2*rr*pp/(math.sqrt(bb*bb+4*cc*rr*pp)-bb)
        if rr<1: asym=rr*pp/(1-rr)
        elif rr==1:asym=math.sqrt(pp/2)
        else:asym=(rr-1)/(rr+1)
        assert abs(tt/asym-1)<.01,(rr,pp,tt/asym)
print('PASS: symbolic Fisher determinant and derivative; 4000 numerical local-optimum comparisons; rare-mixture asymptotics')
