"""Arithmetic checks of a renewable-reward foraging theorem.
For scientific reproducibility only; exact formulae/proofs in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def equilibrium(p, d, k, A):
    p=np.asarray(p,dtype=float); d=np.asarray(d,dtype=float); k=np.asarray(k,dtype=float)
    rr=p/d
    H=lambda ell: sum(np.maximum(p/ell-d,0)/k)
    ell=brentq(lambda z:H(z)-A, min(rr)*1.e-6, max(rr),xtol=1e-14)
    x=np.maximum(p/ell-d,0)/(A*k)
    f=p/(d+A*k*x)
    return ell,x,f

def rhs(t,y,p,d,k,A,g):
    n=len(p);f=y[:n];x=y[n:]
    df=p-(d+A*k*x)*f
    dx=g*x*(f-np.dot(x,f))
    return np.r_[df,dx]

# Correct scaled Lyapunov: (1/A)*sum (entropy / k) + (1/g)*D_KL
# Then resource cross = -sum_i (x_i-x_i*) (f_i-f_i*).
def Vdot(f,x,p,d,k,A,g):
    ell,xs,fs=equilibrium(p,d,k,A)
    df=p-(d+A*k*x)*f
    dx=g*x*(f-np.dot(x,f))
    direct=np.dot(((1-fs/f)/(A*k)),df)-np.dot(xs/x,dx)/g
    theoretical=-np.sum((d+A*k*xs)/(A*k)*(f-fs)**2/f)+np.dot((x-xs),(fs-ell))
    return direct,theoretical

rng=np.random.default_rng(20261120)
for rep in range(1500):
    n=int(rng.integers(2,10)); p=np.exp(rng.uniform(-1,2,n)); d=np.exp(rng.uniform(-1,1,n));k=np.exp(rng.uniform(-1,1,n));A=np.exp(rng.uniform(-2,3));g=np.exp(rng.uniform(-2,2))
    ell,xs,fs=equilibrium(p,d,k,A)
    assert abs(xs.sum()-1)<1e-10
    assert np.max(np.abs(p-(d+A*k*xs)*fs))<1e-10
    assert np.all(fs<=ell+1e-10)
    x=rng.dirichlet(np.ones(n)); f=np.exp(rng.uniform(-2,2,n))
    vd,th=Vdot(f,x,p,d,k,A,g)
    assert abs(vd-th)<3e-9*(1+abs(th)), (vd,th)
    assert th<=1e-10
print('PASS: 1500 random parameter tuples, water-filling identity and exact Lyapunov derivative')

p=np.array([6.,4.,2.]);d=np.ones(3);k=np.ones(3)
for A,expected_active in [(.25,1),(.5,1),(2,2),(3,2),(5,3)]:
    ell,xs,fs=equilibrium(p,d,k,A)
    assert (xs>1e-10).sum()==expected_active
    print('A=',A,'ell=',ell,'x=',xs,'F=',fs)

# Full nonlinear trajectories, positive starting preferences.
for A in [.25,2.,5.]:
    ell,xs,fs=equilibrium(p,d,k,A)
    for g in [.1,1.,15.]:
        y0=np.r_[np.array([1.,7.,.4]),[.2,.3,.5]]
        sol=solve_ivp(rhs,(0,5000),y0,args=(p,d,k,A,g),rtol=3e-9,atol=1e-11,method='LSODA')
        assert sol.success
        assert np.linalg.norm(sol.y[:3,-1]-fs)<5e-5
        assert np.linalg.norm(sol.y[3:,-1]-xs)<5e-5
print('PASS: 9 nonlinear relaxation tests')

# At two-plant activation A*=1/2, K=10/3 and u(t)*t -> 3/10.
p=np.array([6.,4.]);d=np.ones(2);k=np.ones(2);A=.5;g=1.
sol=solve_ivp(rhs,(0,10000),np.array([2.,7.,.7,.3]),args=(p,d,k,A,g),rtol=2e-11,atol=1e-13,method='LSODA',t_eval=[1000,5000,10000])
assert sol.success
for t,u in zip(sol.t,sol.y[-1]):print('critical t=',t,'t*x_2(t)=',t*u)
assert abs(10000*sol.y[-1,-1]-0.3)<.003
print('PASS: critical inverse-time coefficient approaches 3/10')
