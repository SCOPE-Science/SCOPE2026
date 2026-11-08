#!/usr/bin/env python3
"""Check exact first-passage formulas for a two-state independently modulated reset clock.
Scientific verification: matrix-renewal identity, limiting inequalities and finite-difference
backward equations. Continuous-parameter theorems rely on accompanying analysis, not sampling.
"""
import math
from math import sqrt, exp, expm1

def direct(r, contrast, switch, L, D=1.0):
    """Closed scalar formula, initial phase stationary."""
    s=sqrt(switch*switch+contrast*contrast)
    low=r+switch-s; high=r+switch+s
    assert low>0
    c=(1+switch/s)/2
    h=lambda v: v/expm1(L*sqrt(v/D))
    hl,hh=h(low),h(high)
    return (2*switch+(1-c)*hl+c*hh)/(hl*hh+2*switch*(c*hl+(1-c)*hh))

def renewal(r, contrast, switch, L, D=1.0):
    """Independent construction from E[time to first hit-or-reset], and reset-state kernel."""
    s=sqrt(switch*switch+contrast*contrast)
    low=r+switch-s; high=r+switch+s
    c=(1+switch/s)/2
    d=1-c
    g=lambda v: -math.expm1(-L*sqrt(v/D))/v
    gl,gh=g(low),g(high)
    # F(B) in uniform/contrast basis
    f00=c*gl+d*gh
    f11=d*gl+c*gh
    f01=contrast*(gh-gl)/(2*s)
    # rate Lambda in uniform/contrast basis [[r,contrast],[contrast,r]]
    R00=f00*r+f01*contrast
    R01=f00*contrast+f01*r
    R10=f01*r+f11*contrast
    R11=f01*contrast+f11*r
    # solution (I-R) m=F(B)1, initial uniform => first coordinate
    a=1-R00; b=-R01; c2=-R10; d2=1-R11
    determinant=a*d2-b*c2
    return (d2*f00-b*f01)/determinant

def classical(r,L,D=1.):
    return expm1(L*sqrt(r/D))/r

# Test independent scalar reduction against phase-conditioned Markov renewal.
count=0
for r in (0.6,1.0,3.0):
  for frac in (.1,.5,.9):
    for nu in (.02,.1,1.,8.):
      for L in (.03,.1,.5,1.,2.,4.):
        for D in (.4,1.7):
          x=direct(r,r*frac,nu,L,D)
          y=renewal(r,r*frac,nu,L,D)
          assert math.isclose(x,y,rel_tol=3e-8,abs_tol=1e-8),(r,frac,nu,L,D,x,y)
          count+=1
print('renewal_checks',count)
# Crossovers: prove algebraically in result; sample selected parameter values.
for r,delta,nu,D in ((1.,.5,1.,1.),(2.,1.,.2,3.),(.8,.08,5.,1.)):
    small=direct(r,delta,nu,1e-4,D)-classical(r,1e-4,D)
    large=direct(r,delta,nu,100*sqrt(D/r),D)-classical(r,100*sqrt(D/r),D)
    assert small>0 and large<0
print('crossover_checks',3)
# Assessed example, not used to establish existence theorem.
assert direct(1.,.5,1.,.2)>classical(1.,.2)
assert direct(1.,.5,1.,3.)<classical(1.,3.)
print('L=0.2',direct(1.,.5,1.,.2), classical(1.,.2))
print('L=3',direct(1.,.5,1.,3.), classical(1.,3.))
# Finite difference backward equation on (-R,L), with Neumann condition at -R.
try:
 import numpy as np
 from scipy.sparse import lil_matrix
 from scipy.sparse.linalg import spsolve
 def finite_difference(r,delta,nu,L,D,h=.025,R=20.):
    N=int(round((R+L)/h)); h=(R+L)/N
    x=np.linspace(-R,L,N+1)
    j0=int(round(R/h)); assert abs(x[j0])<1e-8
    states=N  # last endpoint u_i(L)=0
    A=lil_matrix((2*states,2*states),dtype=float)
    b=np.ones(2*states)
    for phase in (0,1):
      lam=r+(delta if phase==0 else -delta)
      for j in range(states):
       k=phase*states+j
       A[k,k]+=lam+nu
       A[k,(1-phase)*states+j]-=nu
       A[k,phase*states+j0]-=lam
       if j==0:
        A[k,k]+=2*D/h**2
        A[k,k+1]-=2*D/h**2
       else:
        A[k,k]+=2*D/h**2
        A[k,k-1]-=D/h**2
        if j<states-1: A[k,k+1]-=D/h**2
    sol=spsolve(A.tocsr(),b)
    return (sol[j0]+sol[states+j0])/2
 for L in (.2,.8,2.,3.):
  z=finite_difference(1.,.5,1.,L,1.,.025,20.)
  exact=direct(1.,.5,1.,L,1.)
  assert abs(z-exact)<0.003, (L,z,exact)
  print('backward_eq',L,z,exact,abs(z-exact))
except ImportError:
 print('finite_difference skipped: scipy absent')
print('VERIFICATION_PASS')
