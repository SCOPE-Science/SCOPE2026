"""Finite, reproducible checks for a nonoscillatory threshold-tipping example.

The general quantifiers follow from the written perturbation/Filippov proof;
finite computations here do not certify them.
"""
from math import sqrt, exp, log, pi
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

u,v,A,w,t=sp.symbols('u v A w t',real=True)
N=1+u
P=5+v
rho=10+A*sp.sin(w*t)
f1=sp.expand(rho*N*(1-N/2)-N*P)
f2=sp.expand(P*(N-1))
J=sp.Matrix([f1,f2]).jacobian([u,v]).subs({u:0,v:0,A:0})
assert J==sp.Matrix([[-5,-1],[5,0]])
assert J.charpoly().as_expr()==sp.Symbol('lambda')**2+5*sp.Symbol('lambda')+5
assert sp.simplify(f1+5*u+v-(A/2)*sp.sin(w*t)+5*u**2+u*v+(A/2)*u**2*sp.sin(w*t))==0
assert sp.simplify(f2-5*u-u*v)==0
D=sp.sqrt(5)
mu1=(5-D)/2
mu2=(5+D)/2
k=(mu2*sp.exp(-mu2*t)-mu1*sp.exp(-mu1*t))/D
I=(sp.exp(-mu1*t)-sp.exp(-mu2*t))/D
assert sp.simplify(sp.diff(I,t)-k)==0
assert sp.simplify(sp.diff(k,t,2)+5*sp.diff(k,t)+5*k)==0
assert sp.simplify(k.subs(t,0)-1)==0
node_u1=(sp.sin(D*t)-sp.exp(-mu1*t)+sp.exp(-mu2*t))/10
assert sp.simplify(sp.diff(node_u1,t,2)+5*sp.diff(node_u1,t)+5*node_u1-D*sp.cos(D*t)/2)==0
assert sp.simplify(node_u1.subs(t,0))==0
assert sp.simplify(sp.diff(node_u1,t).subs(t,0))==0
u2=float(node_u1.subs(t,2).evalf(35))
assert -.105<u2<-.096, u2
mus=[float(mu1),float(mu2)]
tstar=log(mus[1]/mus[0])/sqrt(5)
frozen_half=(exp(-mus[0]*tstar)-exp(-mus[1]*tstar))/(2*sqrt(5))
assert .076<frozen_half<.077
assert (1+2*sqrt(5))/(2*100)<.028
assert .01/2*(1/sqrt(5)+1/(np.e*mus[0]*sqrt(5)))<.004
# Finite illustrative integrations from the SAME initial condition.
def trajectory(A,omega=None,theta=0,T=32):
    def f(tt,y):
        n,p=y
        r=10+A*np.sin(omega*tt) if omega is not None else 10+theta*A
        return [r*n*(1-n/2)-n*p,p*(n-1)]
    out=solve_ivp(f,[0,T],[1,5],rtol=2e-11,atol=1e-12,max_step=.025)
    assert out.success
    return float(np.min(out.y[0])),float(np.min(out.y[1]))
for amp in (.002,.01):
    barrier=1-.09*amp
    for theta in (-1,0,1):
        minimum,pmin=trajectory(amp,None,theta)
        assert minimum>barrier and pmin>1,(amp,theta,minimum)
    for omega in (.01,100):
        minimum,pmin=trajectory(amp,omega,T=6)
        assert minimum>barrier and pmin>1,(amp,omega,minimum)
    minimum,pmin=trajectory(amp,sqrt(5),T=6)
    assert minimum<barrier and pmin>1,(amp,minimum,barrier)
print('VERIFY_OK exact_jacobian=1 exact_kernel=2 exact_node_response=1 frozen_bound=1 low_high_bounds=2 frozen_scenarios=6 forcing_scenarios=6')
