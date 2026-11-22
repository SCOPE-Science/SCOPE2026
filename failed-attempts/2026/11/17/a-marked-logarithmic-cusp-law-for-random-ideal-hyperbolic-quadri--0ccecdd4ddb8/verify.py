"""Standalone numerical checks for the marked cusp law of four cyclic points.

All analytical proofs and limit interchanges are in RESULT.md; numerical checks
corroborate identities and finite-threshold behavior only.
"""
import math
import numpy as np
from scipy.integrate import quad

PI=math.pi

def cross_ratio(g):
    x,y,z=g[...,0],g[...,1],g[...,2]
    return np.sin(x/2)*np.sin(z/2)/(np.sin((x+y)/2)*np.sin((y+z)/2))

def known_density(q):
    return 3/(PI*PI)*(-np.log1p(-q)/q-np.log(q)/(1-q))

# Source identity (Martin, Thm 4.1 restricted to circular cyclic order)
mass=quad(known_density,0,1,epsabs=1e-10)[0]
assert abs(mass-1)<1e-9, mass

# Check change-of-variables Jacobian numerically in its interior for multiple scales.
for e in [1e-3,1e-5,1e-8]:
    u,y,v=.43,1.72,.62
    x=e**u
    # Solve the defining equation for z in (0,2pi-x-y).
    from scipy.optimize import brentq
    fun=lambda z: float(cross_ratio(np.array([x,y,z])))-e*v
    z=brentq(fun,1e-15,2*PI-x-y-1e-14,xtol=1e-14)
    B=math.sin(x/2)/math.sin((x+y)/2)
    dzdq=2*math.sin((y+z)/2)**2/(B*math.sin(y/2))
    jac=x*abs(math.log(e))*e*dzdq
    approx=4*e*abs(math.log(e))*math.sin(y/2)**2
    assert abs(jac/approx-1)<.08, (e,jac,approx)

# A seeded independent Monte Carlo sample in angular-gap coordinates.
rng=np.random.default_rng(21092026)
n=2_000_000
exp=rng.exponential(size=(n,4))
g=2*PI*exp/exp.sum(axis=1)[:,None]
q=cross_ratio(g)
assert np.all((q>0)&(q<1))
for eps in [.02,.008,.003]:
    event=q<eps
    empirical=event.mean()
    exact=quad(known_density,0,eps,epsabs=1e-10)[0]
    se=math.sqrt(exact*(1-exact)/n)
    assert abs(empirical-exact)<5*se, (eps,empirical,exact,se)

# Moderate-threshold direction checks (not claimed as limiting proofs).
eps=.003
hit=q<eps
u=np.log(g[hit,0])/math.log(eps)
v=q[hit]/eps
y=g[hit,1]
print('sample_size=',n,'events=',int(hit.sum()),'condition_q=',eps)
print('exact_probability=',quad(known_density,0,eps)[0], 'observed=',hit.mean())
print('conditional_means_U_V_cosY=',float(u.mean()),float(v.mean()),float(np.cos(y).mean()))
print('limit_means_U_V_cosY=',.5,.5,-.5)
print('scalar_pdf_integral=',mass)
print('MARKED_IDEAL_QUADRILATERAL_CHECKS_OK')
