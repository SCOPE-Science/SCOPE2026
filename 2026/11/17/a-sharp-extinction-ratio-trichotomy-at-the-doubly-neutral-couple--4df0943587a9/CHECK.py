#!/usr/bin/env python3
"""Exact recurrence identities and finite illustrative tests of a coupled-logistic map."""
import math
import sympy as s
x,y,c,d,r=s.symbols('x y c d r', positive=True)
X=x*(1-x-c*y)
Y=y*(1-y+d*x)
assert s.simplify(X/Y-x/y-x*((1-c)*y-(1+d)*x)/(y*(1-y+d*x)))==0
rstar=(1-c)/(1+d)
assert s.simplify(X/Y-rstar-(x/y-rstar)*(1-x-y)/(1-y+d*x))==0
assert s.simplify(1/Y-1/y-(1-d*x/y)/(1-y+d*x))==0
assert s.simplify(((Y/X)-(y/x)-(1+d)*y/(1-x-y)).subs(c,1))==0

cases=[(0.6,0.7),(1.0,0.7),(1.7,0.7)]
for cc,dd in cases:
    xx=yy=0.01
    nend=1000000
    for n in range(1,nend+1):
        xx,yy=xx*(1-xx-cc*yy),yy*(1-yy+dd*xx)
        assert xx>0 and yy>0
    assert abs(nend*yy-(1+dd)/(1+cc*dd) if cc<1 else nend*yy-1)<0.1
    if cc<1:
        assert abs(nend*xx-(1-cc)/(1+cc*dd))<0.1
    elif cc==1:
        assert abs(nend*math.log(nend)*xx-1/(1+dd))<0.3
        assert abs(yy/xx-(1+dd)*math.log(nend)-dd*math.log(math.log(nend)))<100
    else:
        assert 0<nend**cc*xx<1e3
print('COUPLED_LOGISTIC_DUAL_NEUTRAL_CHECK_OK symbolic_identities=4 numerical_regimes=3')
