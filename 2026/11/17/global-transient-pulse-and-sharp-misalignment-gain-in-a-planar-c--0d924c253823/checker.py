"""Exact algebraic and ODE tests of the planar coupled saddle-flow identities."""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

b, g, lam, u = sp.symbols('b g lam u', positive=True, real=True)
H = sp.diag(-lam, lam)
v = sp.Matrix([1, u])/sp.sqrt(1+u*u)
M = sp.simplify(-b*(sp.eye(2)-2*v*v.T)*H)
M_goal = b*lam/(1+u*u)*sp.Matrix([[u*u-1, 2*u],[-2*u,u*u-1]])
assert sp.simplify(M-M_goal) == sp.zeros(2)
projected = sp.simplify(-g*(sp.eye(2)-v*v.T)*H*v)
v1dot = sp.simplify(projected[0]); v2dot=sp.simplify(projected[1]);
assert sp.simplify(sp.sqrt(1+u*u)**3*(v2dot-u*v1dot)+2*g*lam*u*(1+u*u)) == 0 or sp.simplify((v2dot-u*v1dot)*sp.sqrt(1+u*u)+2*g*lam*u)==0


def explicit(t, x0, beta, gamma, l, u0):
    w = u0*math.exp(-2*gamma*l*t)
    amp=math.exp(-beta*l*t)*((1+u0*u0)/(1+w*w))**(beta/(2*gamma))
    phi=-(beta/gamma)*(math.atan(u0)-math.atan(w))
    c,s=math.cos(phi),math.sin(phi)
    return amp*np.array([c*x0[0]-s*x0[1],s*x0[0]+c*x0[1]]),w

count=0
for beta in [0.25,0.8,2.0,3.4]:
  for gamma in [0.5,1.7,2.3]:
    for l in [0.6,1.8]:
      for u0 in [-15.0,-2.0,-0.7,0.0,0.65,1.0,3.0,20.0]:
        x0=np.array([0.73,-1.21])
        vec0=np.array([1.0,u0])/math.sqrt(1+u0*u0)
        def rhs(t,y):
            x=y[:2];v=y[2:]
            hh=np.array([-l*v[0], l*v[1]])
            vdot=-gamma*(hh-np.dot(v,hh)*v)
            grad=np.array([-l*x[0],l*x[1]])
            xdot=-beta*(grad-2*np.dot(v,grad)*v)
            return np.r_[xdot,vdot]
        end=4.5/l
        sol=solve_ivp(rhs,(0,end),np.r_[x0,vec0],rtol=3e-11,atol=2e-13,dense_output=True)
        assert sol.success
        for t in [0,end/5,end/2,end]:
            truth, w=explicit(t,x0,beta,gamma,l,u0)
            guess=sol.sol(t)
            assert np.linalg.norm(guess[:2]-truth) < 1e-6*max(1,np.linalg.norm(truth)),(beta,gamma,l,u0,t,guess[:2],truth)
            assert abs(guess[3]/guess[2]-w)<1e-8*max(1,abs(w))
        if abs(u0)>1:
            ts=math.log(abs(u0))/(2*gamma*l)
            if ts<=end:
                xt,_=explicit(ts,x0,beta,gamma,l,u0)
                gain=(0.5*(abs(u0)+1/abs(u0)))**(beta/(2*gamma))
                assert math.isclose(np.linalg.norm(xt)/np.linalg.norm(x0),gain,rel_tol=2e-12)
                xback,_=explicit(2*ts,x0,beta,gamma,l,u0)
                assert math.isclose(np.linalg.norm(xback),np.linalg.norm(x0),rel_tol=2e-12)
        count+=1
# Deterministic midpoint quadrature of uniform projective-line initialization.
angles=(np.arange(200000)+0.5)*math.pi/400000
for bb,gg in [(0.6,1.5),(2.0,1.0),(3.0,0.4)]:
    gains=np.where(angles <= math.pi/4, 1.0, np.sin(2*angles)**(-bb/(2*gg)))
    assert abs(np.mean(gains==1.0)-0.5)<1e-12
    for threshold in [1.1,1.5,2.3,4.0,8.0]:
        exact=math.asin(threshold**(-2*gg/bb))/math.pi
        observed=float(np.mean(gains>threshold))
        assert abs(observed-exact)<2e-5,(bb,gg,threshold,observed,exact)
print(f'PASS: exact matrix/projective identities; {count} ODE configurations at four times; sharp gain/return and Haar tail quadrature.')
