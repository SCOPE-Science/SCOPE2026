#!/usr/bin/env python3
"""Independent algebraic and numerical checks for three-epoch sinusoidal D-design."""
import math
from scipy.optimize import brentq, differential_evolution
import numpy as np
import sympy as sp

a,b,r,s=sp.symbols('a b r s',real=True)
X=sp.Matrix([[1,1,0],[1,sp.cos(a),sp.sin(a)],[1,sp.cos(a+b),sp.sin(a+b)]])
expected=4*sp.sin(a/2)*sp.sin(b/2)*sp.sin((a+b)/2)
assert sp.trigsimp(X.det()-expected)==0
Sigma=sp.Matrix([[1,r,r*s],[r,1,s],[r*s,s,1]])
assert sp.simplify(Sigma.det()-(1-r*r)*(1-s*s))==0

# Scalar phase function; return log geometric mean information up to a constant.
def logJ(x,y,c):
    if x<=0 or y<=0 or x+y>=2*math.pi: return -math.inf
    return (math.log(math.sin(x/2))+math.log(math.sin(y/2))
           +math.log(math.sin((x+y)/2))
           -.5*math.log(-math.expm1(-2*c*x))
           -.5*math.log(-math.expm1(-2*c*y)))

def root(c):
    # Numerically stable derivative: 2c/expm1(2c*x)
    def d(x):
        val=(1+2*math.cos(x))/math.sin(x)
        z=2*c*x
        return val-(0 if z>700 else 2*c/math.expm1(z))
    return brentq(d, .3, 2.1,xtol=5e-15)

r0=brentq(lambda x:(1+2*math.cos(x))/math.sin(x)-1/x,1.5,2*math.pi/3,xtol=5e-15)
assert 1.803<r0<1.804
cs=[0.0001,0.01,0.1,0.5,1,3,10,100]
rr=[root(c) for c in cs]
assert all(1.803 < u < 2*math.pi/3+1e-13 for u in rr)
assert all(x<=y+1e-13 for x,y in zip(rr,rr[1:])) and all(x<y for x,y in zip(rr[:6],rr[1:7]))
assert abs(rr[0]-r0)<0.0002
assert abs(rr[-1]-2*math.pi/3)<1e-12
checks=0
for c,theta in zip(cs,rr):
    target=logJ(theta,theta,c)
    # independently solve full two-variable optimization, not imposing equal gaps
    def neg(z):
        val=logJ(float(z[0]),float(z[1]),c)
        return -val if math.isfinite(val) else 1e10
    out=differential_evolution(neg,[(.005,3.13),(.005,3.13)],seed=42,tol=1e-11,polish=True)
    assert abs(out.fun+target)<2e-7,(c,out.fun,target)
    assert max(abs(out.x[0]-theta),abs(out.x[1]-theta))<0.004,(c,out.x,theta)
    checks+=1
    # asymmetric perturbations always decrease information.
    for eps in np.linspace(-min(theta,.1),min(theta,.1),101):
        if eps==0:continue
        assert logJ(theta+eps,theta-eps,c)<target+1e-12
        checks+=1
    # regular grid of all feasible unequal gaps
    for aa in np.linspace(.035,2*math.pi-.035,69):
        for bb in np.linspace(.035,2*math.pi-.035,69):
            if aa+bb>=2*math.pi:continue
            assert logJ(aa,bb,c)<=target+2e-9
            checks+=1
print('symbolic determinants checked')
print('unrestricted two-gap global optimizations checked:',len(cs))
print('numerical inequalities checked:',checks)
print('persistent-noise phase radians:',r0)
for c,u in zip(cs,rr):print(f'c={c:g} phase={u:.12f} gap fraction of period={u/(2*math.pi):.12f}')
