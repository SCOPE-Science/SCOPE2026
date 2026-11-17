"""Standalone finite checks for a weighted Laguerre coefficient norm.
Run: python CHECK.py
"""
import math
import numpy as np
import sympy as sp
from scipy.special import roots_laguerre, eval_laguerre, eval_genlaguerre

x=sp.symbols('x',positive=True)
checks=0
for n in range(1,13):
    poly=sp.expand(x*sp.assoc_laguerre(n-1,1,x)/n)
    L=sp.laguerre(n,x)
    # F=e^{-x}poly; exact primitive identity.
    assert sp.simplify(sp.diff(poly,x)-poly-L)==0
    checks+=1
    # F''+F'+(n/x)F=0 is equivalent to the polynomial identity below.
    assert sp.simplify(x*(sp.diff(poly,x,2)-sp.diff(poly,x))+n*poly)==0
    checks+=1
    # Sonin derivative by expanding the common exponential factor.
    fp=sp.expand(sp.diff(poly,x)-poly)
    fpp=sp.expand(sp.diff(fp,x)-fp)
    rhs=sp.expand(2*poly*fp+(fp*fp+2*x*fp*fpp)/n-(1-2*x)*fp*fp/n)
    assert sp.simplify(rhs)==0
    checks+=1

# Test all critical points, and the exact one-or-two-candidate reduction.
for n in range(1,101):
    roots=roots_laguerre(n)[0]
    F=lambda z: (z/n)*np.exp(-z)*eval_genlaguerre(n-1,1,z)
    vals=np.abs(F(roots))
    closest=[]
    left=roots[roots<=0.5]
    right=roots[roots>=0.5]
    if len(left): closest.append(float(left[-1]))
    if len(right): closest.append(float(right[0]))
    assert np.isclose(np.max(vals),np.max(np.abs(F(np.array(closest)))),atol=1e-12,rtol=1e-10)
    checks+=1
    # The global norm is bounded by the exact Sonin value at its maximum x=.5.
    fn0=float(F(0.5))
    fpn0=float(np.exp(-0.5)*eval_laguerre(n,0.5))
    S0=fn0**2 + 0.5/n * fpn0**2
    assert (np.max(vals))**2 <= S0 + 2e-13
    checks+=1

c=math.exp(-0.25)/(2**0.25*math.sqrt(math.pi))
for n in (100,200,400,800):
    fn0 = (0.5/n)*math.exp(-0.5)*eval_genlaguerre(n-1,1,0.5)
    fpn0=math.exp(-0.5)*eval_laguerre(n,0.5)
    norm=(n**1.5*(fn0**2 + 0.5/n*fpn0**2))**0.5
    assert abs(norm-c)<0.01, (n,norm,c)
    checks+=1
print(f'LAGUERRE_VARIATION_ENVELOPE_CHECKS_PASSED {checks}')
print('limit_constant', format(c,'.15f'))
