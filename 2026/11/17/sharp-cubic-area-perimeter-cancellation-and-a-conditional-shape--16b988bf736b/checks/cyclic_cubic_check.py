"""Standalone reproducibility checks for a fixed-side cyclic-polygon near-optimal law.
Scientific calculations only; no external dependencies beyond NumPy/SymPy.
"""
import math
import numpy as np
import sympy as sp
from numpy.random import default_rng

x,a=sp.symbols('x a',real=True)
Pminus=2*sp.sin(a)-2*sp.sin(a+x/2)+sp.cos(a)*x
Aminus=sp.sin(2*a)/2-sp.sin(2*a+x)/2+sp.cos(2*a)*x/2
p3=sp.simplify(sp.diff(Pminus,x,3).subs(x,0)/6)
a3=sp.simplify(sp.diff(Aminus,x,3).subs(x,0)/6)
res3=sp.trigsimp(a3-2*sp.cos(a)*p3)
assert sp.simplify(res3+sp.sin(a)**2/12)==0
print('CUBIC_COEFFICIENT:',res3)

rng=default_rng(20261113)
for m in [3,4,5,6,9]:
    d=m-1
    s=math.sin(math.pi/m); c=math.cos(math.pi/m)
    proj=np.eye(m)-np.ones((m,m))/m
    g=rng.normal(size=(180000,m))
    g=g@proj.T
    g/=np.linalg.norm(g,axis=1)[:,None]
    g*=rng.random(len(g))[:,None]**(1/d)
    cubic=(g**3).sum(axis=1)
    v_exact=6*(m-1)*(m-2)/(m*(m+1)*(m+3)*(m+5))
    v_emp=np.mean(cubic**2)
    assert abs(v_emp-v_exact)/v_exact < .055,(m,v_emp,v_exact)
    limit_var=(4/9)*s*v_exact
    print('MOMENT:',m,'empirical',v_emp,'exact',v_exact,'scaled_var',limit_var)
    if m<=6:
      for e in [1.e-3,1.e-4]:
        z=np.r_[math.sqrt((m-1)/m),np.full(m-1,-1/math.sqrt(m*(m-1)))]
        delta=math.sqrt(4*e/s)*z
        gaps=2*math.pi/m+delta
        P=2*np.sin(gaps/2).sum();A=np.sin(gaps).sum()/2
        DP=2*m*s-P; DA=m*s*c-A
        residual=DA-2*c*DP
        expected=-(2/3)*math.sqrt(s)*np.sum(z**3)
        val=residual/(e**1.5)
        assert abs(val-expected)<.2, (m,e,val,expected)
        print('ASYMPTOTIC:',m,e,val,expected,'difference',val-expected)

print('CYCLIC_POLYGON_CUBIC_CHECKS_OK')
