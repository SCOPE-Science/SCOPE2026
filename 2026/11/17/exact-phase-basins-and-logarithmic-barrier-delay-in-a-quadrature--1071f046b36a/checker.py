"""Reproducible finite checks for the quadrature adaptive-oscillator theorem.

The infinite-dimensional claims follow from the written proof, not sampling.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp, quad

phi,K12,K21,a,eps=sp.symbols('phi K12 K21 a eps',real=True)
S=(K12+K21)/2; D=(K12-K21)/2
p=D*sp.cos(phi)
k12d=eps*(1-a*sp.sin(phi)-K12)
k21d=eps*(1+a*sp.sin(phi)-K21)
assert sp.simplify((k12d+k21d)/2-eps*(1-S))==0
assert sp.simplify((k12d-k21d)/2+eps*(D+a*sp.sin(phi)))==0
q,v=sp.symbols('q v',real=True)
E=v*v/2+eps*a*sp.log(sp.cosh(q))
qdot=v;vdot=-eps*(v+a*sp.tanh(q))
assert sp.simplify(sp.diff(E,q)*qdot+sp.diff(E,v)*vdot+eps*v*v)==0
lam=sp.symbols('lam')
assert sp.expand((lam**2+eps*lam+eps*a).subs(eps,4*a))== sp.expand((lam+2*a)**2)

# Direct integration of full original equations and reduced equations.
for strength,rate in [(0.6,0.9),(1.7,0.18),(0.8,3.2),(0.9,3.6)]:
    for initial_phi in [-2.7,-0.3,1.1,2.8]:
        initial=(initial_phi,1.5,-0.35)
        def original(t,z):
            ph,k1,k2=z
            return [0.5*(k1-k2)*math.cos(ph),rate*(1-strength*math.sin(ph)-k1),rate*(1+strength*math.sin(ph)-k2)]
        out=solve_ivp(original,(0,150),initial,rtol=2e-10,atol=2e-12,dense_output=True,max_step=.2)
        assert out.success
        target=0 if math.cos(initial_phi)>0 else math.pi
        assert abs(math.remainder(out.y[0,-1]-target,2*math.pi))<1e-3
        assert abs(out.y[1,-1]-1)<1e-3 and abs(out.y[2,-1]-1)<1e-3
        q0=math.atanh(math.sin(initial_phi));v0=(initial[1]-initial[2])/2
        def reduced(t,z):return [z[1],-rate*(z[1]+strength*math.tanh(z[0]))]
        red=solve_ivp(reduced,(0,150),(q0,v0),rtol=2e-10,atol=2e-12,dense_output=True,max_step=.2)
        tgrid=np.linspace(0,150,1000)
        yy=out.sol(tgrid)
        vv=(yy[1]-yy[2])/2
        rr=red.sol(tgrid)
        assert max(abs(rr[1]-vv))<1e-7
        # Numerical quadrature of exact energy dissipation using the continuous dense solution.
        E0=.5*v0*v0-rate*strength*math.log(abs(math.cos(initial_phi)))
        diss=quad(lambda t: red.sol(t)[1]**2,0,150,epsabs=1e-9,epsrel=1e-9)[0]
        # use sufficiently loose quadrature check independent of analytic identity.
        assert abs(E0/rate-diss)<.0002,(strength,rate,initial_phi,E0/rate,diss)

# First hitting times of a fixed q-level near the invariant phase barrier.
def T(q0,init_v,a=.8,eps=1.3,R=1.0):
    def f(t,z):return [z[1],-eps*(z[1]+a*math.tanh(z[0]))]
    def ev(t,z):return z[0]-R
    ev.terminal=True;ev.direction=-1
    z=solve_ivp(f,(0,100),(q0,init_v),events=ev,rtol=3e-11,atol=1e-12,max_step=.1)
    assert z.success and len(z.t_events[0])==1
    return z.t_events[0][0]
series=[(q0,T(q0,0.4)) for q0 in [6,8,10,12,14]]
shifts=[t-q0/.8 for q0,t in series]
assert max(shifts)-min(shifts)<.003,series
print('PASS symbolic reduction/energy/characteristic polynomial')
print('PASS 16 direct global trajectories and energy budgets')
print('PASS logarithmic exit-time coefficient: ',series)
print('PASS bounded delay correction: ',shifts)

# Qualitative linearization sanity checks, without inferring infinite claims from samples.
def trace_for(a,eps,q0=.3,v0=.0,end=30):
    def f(t,z):return [z[1],-eps*(z[1]+a*math.tanh(z[0]))]
    r=solve_ivp(f,(0,end),(q0,v0),rtol=3e-12,atol=1e-14,dense_output=True,max_step=.05)
    assert r.success
    return r
under=trace_for(1,1,end=30)
over=trace_for(1,5,end=30)
tt=np.linspace(0,30,601)
cross=lambda q: int(np.sum(q[1:]*q[:-1]<0))
assert cross(under.sol(tt)[0])>=5
assert cross(over.sol(tt)[0])<=1
critical=trace_for(1,4,end=9)
cc=[(t,math.exp(2*t)*critical.sol(t)[0]-math.exp(2*(t-1))*critical.sol(t-1)[0]) for t in [5.,6.,7.,8.,9.]]
assert max(z for _,z in cc)-min(z for _,z in cc)<.002,cc
print('PASS finite damped-focus/overdamped diagnostics and critical Jordan factor',cc)
