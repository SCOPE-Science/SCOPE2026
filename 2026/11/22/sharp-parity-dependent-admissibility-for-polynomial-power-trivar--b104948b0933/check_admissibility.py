"""Reproducible symbolic and numerical diagnostics for a trivariate copula admissibility theorem.
All infinite parameter claims require the analytic proof in RESULT.md.
"""
import math
import sympy as sp
from scipy.optimize import differential_evolution, brentq

x,y,z,l=sp.symbols('x y z l', real=True)
checks=0
for m in range(1,13):
    theta=sp.Integer(2)
    C=x*y*z*(1+l*(x-y)**m*z**theta*(1-z))
    d=sp.diff(C,x,y,z)
    A=2*(x-y) if m==1 else (m+1)*(x-y)**m-m*(m-1)*x*y*(x-y)**(m-2)
    B=z**theta*((theta+2)*z-(theta+1))
    assert sp.simplify(d-(1-l*B*A))==0
    checks+=1

def M(m):
    if m==2:return 2.,0.
    aa=m+1; bb=(m-1)**2; cc=(m-1)*(m-2)
    s=2*cc/(bb+math.sqrt(bb*bb+4*aa*cc))
    return s**(m-2)*(m*(m-1)*(1-s)-(m+1)*s*s),s

def values(m,theta):
    r=1 if theta==0 else (theta/(theta+2))**theta
    if m%2:return -(m+1),m+1
    mm,_=M(m)
    return -max((m+1)*r,mm),m+1

for m in (1,2,3,4,5,6,8,10):
    for theta in (0,0.1,1,4,20):
        lo,hi=values(m,theta)
        def prod(t):
            a,b,c=t
            A=2*(a-b) if m==1 else (m+1)*(a-b)**m-m*(m-1)*a*b*(a-b)**(m-2)
            B=(2*c-1) if theta==0 else c**theta*((theta+2)*c-theta-1)
            return A*B
        opt_min=differential_evolution(prod,[(0,1)]*3,seed=122+10*m+int(theta*10),tol=1e-9,polish=True,popsize=9,maxiter=350)
        opt_max=differential_evolution(lambda t:-prod(t),[(0,1)]*3,seed=222+10*m+int(theta*10),tol=1e-9,polish=True,popsize=9,maxiter=350)
        assert opt_min.fun >= lo-1e-7,(m,theta,opt_min.fun,lo)
        assert -opt_max.fun <= hi+1e-7,(m,theta,-opt_max.fun,hi)
        checks+=2

# Exact tractable witness inside the new region but outside the published sufficient bound.
# At m=2, theta=1, the admissible interval is [-1/2,1/3].
assert sp.factor(sp.diff(x*y*z*(1-sp.Rational(2,5)*(x-y)**2*z*(1-z)),x,y,z) - (1+sp.Rational(2,5)*z*(3*z-2)*(3*(x-y)**2-2*x*y)))==0
checks+=1
for m in (2,4,6,8,10,20,50,100):
    mm,s=M(m)
    assert 0<mm<m+1
    assert mm/(m+1)>math.exp(-2)
    assert 0<=s<1
    checks+=3
m2_theta_switch=brentq(lambda t:(t/(t+2))**t-2.0/3.0,1e-7,100)
assert abs(m2_theta_switch-0.15352844952779568)<1e-12
checks+=1
print(f'PASS {checks} supporting assertions; m=2 switch theta={m2_theta_switch:.16f}')
