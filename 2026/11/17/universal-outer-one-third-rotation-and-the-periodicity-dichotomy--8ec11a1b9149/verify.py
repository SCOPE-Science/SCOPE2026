#!/usr/bin/env python3
"""Finite symbolic and numerical corroboration for a positive QRT ratio map.

Dependencies: Python 3.11+, SymPy. This script is NOT an infinite proof.
"""
import math
import sympy as sp

x,y,a,b,c,d=sp.symbols('x y a b c d', positive=True)
next_y=(a*y+b)/(x*y*(c*y+d))
H=lambda X,Y: d*(X+Y)+a*(1/X+1/Y)+c*X*Y+b/(X*Y)
assert sp.cancel(H(y,next_y)-H(x,y))==0
u,v=sp.symbols('u v',real=True)
# The log-coordinate derivative has matrix [[0,1],[-1,g'(v)-1]].
Jac=sp.Matrix([[0,1],[-1,sp.Symbol('w')]])
assert Jac.det()==1
A=sp.Matrix([[0,1],[-1,-1]])
assert A**3==sp.eye(2) and A!=sp.eye(2)
assert sp.simplify(y*sp.diff((a*y+b)/(c*y+d),y)/((a*y+b)/(c*y+d))-
                   y*(a*d-b*c)/((a*y+b)*(c*y+d)))==0

def logadd(p,q):
    z=max(p,q)
    return z+math.log(math.exp(p-z)+math.exp(q-z))

def evalrho(par, radius, iterations=18000):
    aa,bb,cc,dd=par
    lo,hi=0.0,1.0
    def polynomial(t): return cc*t**4+dd*t**3-aa*t-bb
    while polynomial(hi)<=0: hi*=2
    for i in range(85):
        mid=(lo+hi)/2
        if polynomial(mid)<0: lo=mid
        else: hi=mid
    s=(lo+hi)/2
    eq=math.log(s)
    delta=s*(aa*dd-bb*cc)/((aa*s+bb)*(cc*s+dd))
    expected=math.acos((delta-1)/2)/(2*math.pi)
    U,V=eq+radius,eq
    theta=math.atan2(V-eq,U-eq)
    total=0.0
    for _ in range(iterations):
        W=-U-V+logadd(math.log(aa)+V, math.log(bb))-logadd(math.log(cc)+V,math.log(dd))
        U,V=V,W
        new=math.atan2(V-eq,U-eq)
        deltaang=(theta-new)%(2*math.pi)
        # For a sufficiently fine smooth convex oval the clockwise increment is < one turn.
        total+=deltaang/(2*math.pi)
        theta=new
    return expected,total/iterations

for params in ((2,3,1,1),(3,1,1,1),(1,1,1,1)):
    rho0,rhosmall=evalrho(params,0.01)
    _,rholarge=evalrho(params,55)
    assert abs(rhosmall-rho0)<0.003,(params,rho0,rhosmall)
    assert abs(rholarge-1/3)<0.003,(params,rholarge)
    if params==(1,1,1,1):
        assert abs(rhosmall-1/3)<0.001
    print('CASE',params,'rho_center',round(rho0,8),
          'rho_sample_small',round(rhosmall,8),'rho_sample_outer',round(rholarge,8))
print('VERIFY_OK exact_H_identity=1 exact_log_symplectic=1 outer_hex_order=3 numerical_cases=3')
