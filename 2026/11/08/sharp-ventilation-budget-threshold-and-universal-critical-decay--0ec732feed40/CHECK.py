"""Reproducible arithmetic checks for heterogeneous aerosol-SIS optimization.
Scientific checks only; this script is not a proof of the infinite-dimensional claims.
"""
import math
import random
from fractions import Fraction
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

r = sp.sqrt(2)
a1,a2=sp.Rational(2,5),sp.Rational(4,5)
d1=(1+r)/2
d2=1+1/r
budget=sp.simplify(d1+d2-2)
assert sp.simplify(budget-(r-sp.Rational(1,2)))==0
assert sp.simplify(a1/d1+a2/d2-sp.Rational(4,5))==0
lam=sp.simplify(a1/d1**2)
assert sp.simplify(lam-a2/d2**2)==0
C=sp.simplify(1+a1/d1**2+a2/d2**2)
L=sp.simplify(1+2*a1/d1**2+4*a2/d2**2)
assert sp.simplify(C-(1+2*lam))==0
assert sp.simplify(L-(1+6*lam))==0
prefactor=sp.simplify(C/L)
print('Exact critical budget:',budget)
print('Recovery rates:',d1,d2)
print('Critical infected coefficient:',prefactor,'~',float(prefactor))

rng=random.Random(1117)
for trial in range(80):
    m=rng.randrange(2,7)
    a=[rng.uniform(.05,2.0) for _ in range(m)]
    c=[rng.uniform(.15,4.0) for _ in range(m)]
    d=[rng.uniform(.4,2.0) for _ in range(m)]
    B=rng.uniform(.05,6.0)
    def cost_of(lam):
        return sum(c[i]*(max(d[i],math.sqrt(a[i]/(lam*c[i])))-d[i]) for i in range(m))
    lo,hi=1e-15,1e8
    for _ in range(150):
        mid=(lo+hi)/2
        if cost_of(mid)>B:lo=mid
        else:hi=mid
    rate=[max(d[i],math.sqrt(a[i]/(hi*c[i]))) for i in range(m)]
    val=sum(a[i]/rate[i] for i in range(m))
    bounds=[(d[i],None) for i in range(m)]
    obj=lambda z:sum(a[i]/z[i] for i in range(m))
    res=minimize(obj,rate,method='SLSQP',bounds=bounds,
      constraints=[{'type':'ineq','fun':lambda z: B-sum(c[i]*(z[i]-d[i]) for i in range(m))}],
      options={'ftol':1e-12,'maxiter':200})
    assert res.success, res.message
    assert abs(val-res.fun)<1e-7,(trial,val,res.fun)
print('80 random KKT/SLSQP checks: pass')

# For the rational-arctan parameters, critical convergence with slow t^-1 approach.
f1=2/3; f2=2/3
v1=float(d1);v2=float(d2)
def vector(t,z):
    x,y1,y2=z
    return [(.2*x+.2*y1+.2*y2)*(1-x)-x,
            f1*math.atan(3*x)*(1-y1)-v1*y1,
            f2*math.atan(6*x)*(1-y2)-v2*y2]
sol=solve_ivp(vector,(0,50000),[.4,.3,.1],rtol=1e-10,atol=1e-12,dense_output=True)
assert sol.success
for t in (1000,5000,10000,50000):
    x,y1,y2=sol.sol(t)
    print('critical t=',t,'tx=',t*x,'theoretical=',float(prefactor))
assert abs(50000*sol.sol(50000)[0]-float(prefactor))<.02
# Critical R0 linearization check
M=sp.Matrix([[sp.Rational(-4,5),sp.Rational(1,5),sp.Rational(1,5)],
             [2,-d1,0],[4,0,-d2]])
assert sp.simplify(M.det())==0
other=[complex(v) for v in M.eigenvals().keys() if abs(complex(v))>1e-7]
assert all(v.real<0 for v in other)
print('Critical Jacobian and coefficient checks: pass')
