"""Standalone symbolic and numerical checks for a binomial-feedback game."""
from fractions import Fraction
from math import comb, tanh, pi, sqrt
from scipy.integrate import solve_ivp
import sympy as sp

x,r=sp.symbols('x r', real=True)
for p,q in [(1,1),(2,3),(3,2),(2,2),(1,5),(4,6)]:
    n=p+q
    T=sp.Rational(p,n)
    gamma=sp.binomial(n,p)*x**p*(1-x)**q
    A=x*(1-x)
    rho=sp.Rational(1,4)
    c=gamma.subs(x,T)*rho
    F=A*(gamma*r-c)
    h=-(x-T) + sp.Rational(1,3)*(x-T)**3
    G=r*(1-r)*h
    a=sp.diff(F,r).subs({x:T,r:rho})
    deriv={
        'F_xx':sp.diff(F,x,2).subs({x:T,r:rho}),
        'F_xxx':sp.diff(F,x,3).subs({x:T,r:rho}),
        'F_xr':sp.diff(F,x,r).subs({x:T,r:rho}),
        'G_xxr':sp.diff(G,x,2,r).subs({x:T,r:rho}),
        'G_xx':sp.diff(G,x,2).subs({x:T,r:rho})
    }
    assert deriv['G_xxr']==0 and deriv['G_xx']==0
    cubic=sp.factor(deriv['F_xxx']-deriv['F_xr']*deriv['F_xx']/a)
    assert cubic==0,(p,q,cubic)
    assert sp.diff(gamma,x).subs(x,T)==0
    assert sp.diff(gamma,x,2).subs(x,T)==-n*gamma.subs(x,T)/A.subs(x,T)
    assert sp.diff(gamma,x,3).subs(x,T)==2*n*gamma.subs(x,T)*sp.diff(A,x).subs(x,T)/(A.subs(x,T)**2)
    if p==q:
        assert sp.factor(F.subs(x,1-x)-F)==0
        assert sp.factor(G.subs(x,1-x)+G)==0

# In the balanced case the analytic vector field is reversible;
# numerical crossings only diagnose integration accuracy, not periodicity proof.
p=q=2
N=p+q+1; M=p+1; beta=3.0; eps=0.1
Gmax=comb(N-1,M-1)*(0.25)**p
c=0.1; b=1.0; rho=c/(b*Gmax)
omega=sqrt((b*Gmax/(4*eps))*rho*(1-rho)*beta/2)
assert 0<rho<1

def rhs(t,z):
    xx,rr=z
    gam=comb(N-1,M-1)*xx**p*(1-xx)**q
    return [xx*(1-xx)/eps*(b*gam*rr-c),-rr*(1-rr)*tanh(beta*(xx-0.5)/2)]

def cross(t,z):return z[0]-0.5
cross.direction=-1
cross.terminal=True

for delta in [0.02,0.06,0.1]:
    z0=[0.5,rho+delta]
    sol=solve_ivp(rhs,(0,120),z0,rtol=1e-12,atol=1e-13,events=cross,max_step=0.05)
    assert len(sol.t_events[0])==1
    tau=sol.t_events[0][0]
    zz=sol.y_events[0][0]
    assert zz[1]<rho
    back=solve_ivp(rhs,(0,tau),zz,rtol=1e-12,atol=1e-13,max_step=0.05)
    assert abs(back.y[0,-1]-0.5)<1e-9
    assert abs(back.y[1,-1]-(rho+delta))<1e-9

print('VERIFY_OK', 'cases=6', 'rho=',rho, 'omega=',omega)
