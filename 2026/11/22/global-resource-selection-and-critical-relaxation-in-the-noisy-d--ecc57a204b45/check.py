#!/usr/bin/env python3
"""Exact algebraic identities and numerical cross-checks for the donation feedback ODE."""
import sympy as sp
from scipy.integrate import solve_ivp

x,n,s,r,k,t,e=sp.symbols('x n s r k t e', positive=True)
X,N=sp.symbols('X N', real=True)
xs=1/(1+t)
F=r*(1-2*n)+4*s*k*k*r*r*(sp.Rational(1,2)-x)
Fx=s*x*(1-x)*F
Fn=e*n*(1-n)*((1+t)*x-1)
ns=sp.Rational(1,2)+s*r*k*k*(t-1)/(1+t)
assert sp.simplify(F.subs({x:xs,n:ns}))==0
# Both boundary x roots and threshold
xtop=sp.Rational(1,2)-1/(4*s*r*k*k)
xbot=sp.Rational(1,2)+1/(4*s*r*k*k)
assert sp.simplify(F.subs({x:xtop,n:1})) == 0
assert sp.simplify(F.subs({x:xbot,n:0})) == 0
kt2=(1+t)/(2*s*r*(t-1))
kb2=(1+t)/(2*s*r*(1-t))
assert sp.simplify((sp.Rational(1,2)-1/(4*s*r*kt2))-xs)==0
assert sp.simplify((sp.Rational(1,2)+1/(4*s*r*kb2))-xs)==0
assert sp.simplify(1/(2*s*r*kt2)-(t-1)/(t+1))==0
assert sp.simplify(1/(2*s*r*kb2)-(1-t)/(t+1))==0
assert sp.simplify(e*(1+t)*(t-1)/(t+1)-e*(t-1))==0
# Derive entropy identity using equilibrium identity F(X,N)=0.
vdot=sp.expand((x-X)*Fx/(x*(1-x)) + 2*s*r/(e*(1+t))*(n-N)*Fn/(n*(1-n)))
assert sp.simplify(vdot -(-4*s*s*r*r*k*k*(x-X)**2 + 2*s*r*(n-N)*(X-xs)) - s*(x-X)*F.subs({x:X,n:N}))==0
# Formula for s(x-X)F(X,N) vanishes at selected target.


def target(theta,ss,rr,kk):
    xx=1/(1+theta)
    nn=.5+ss*rr*kk**2*(theta-1)/(1+theta)
    if nn<0: return .5+1/(4*ss*rr*kk**2),0.
    if nn>1: return .5-1/(4*ss*rr*kk**2),1.
    return xx,nn

def dyn(theta,ss,rr,kk,ee):
    def rhs(_,z):
        xx,nn=z
        return [ss*xx*(1-xx)*(rr*(1-2*nn)+4*ss*rr*rr*kk*kk*(.5-xx)), ee*nn*(1-nn)*((1+theta)*xx-1)]
    return rhs

# Numeric tests for below/above threshold and both sides of theta.
examples=[(.5,.5,4,0.3,2.),(.5,.5,4,1.2,2.),(2.,.5,4,0.3,2.),(2.,.5,4,1.2,2.),(1.,.5,4,0.3,2.),(.5,.5,4,0.0,2.)]
for theta,ss,rr,kk,ee in examples:
    rhs=dyn(theta,ss,rr,kk,ee)
    for init in [(0.11,0.12),(0.8,0.3),(0.6,0.9)]:
        T=250 if kk else 15
        sol=solve_ivp(rhs,[0,T],init,rtol=2e-10,atol=2e-12)
        assert sol.success
        assert all(-1e-9<v<1+1e-9 for v in sol.y[:,-1])
        if kk:
            dest=target(theta,ss,rr,kk)
            assert max(abs(sol.y[:,-1][j]-dest[j]) for j in range(2))<1e-5, (theta,kk,init,sol.y[:,-1],dest)

# Check dimensionless exact arithmetic cases (r=4, s=1/2, theta=2, eps=2)
assert target(2.,.5,4.,.5)==(1/3,.5+.5*4*.25/3)
assert target(2.,.5,4.,1.)==(.375,1.)
# At k=0 orbit first integral is exactly constant on trajectories.
print('PASS: symbolic flow, selected equilibria, entropy identity, exact critical thresholds, 18 trajectories')
