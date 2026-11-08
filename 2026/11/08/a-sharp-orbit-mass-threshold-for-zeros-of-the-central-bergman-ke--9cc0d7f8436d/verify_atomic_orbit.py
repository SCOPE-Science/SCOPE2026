#!/usr/bin/env python3
"""Standalone checks of the equal-orbit atomic Bergman-kernel formulas."""
import sympy as s
import numpy as np
q,r=s.symbols('q r', integer=True, positive=True)
L=q*(1+(q-1)*r**2)/(1-r**2)**2
bcrit=(1-r)**2/(1+(q-1)*r)
tcrit=(1-r**2)**2/(q*r*((q+1)+q*r+(q-1)*r**2))
assert s.factor(q*tcrit/(1+tcrit*L)-bcrit)==0
assert s.factor((1-r**2)**2-(q/L)*(1+(q-1)*r**2))==0
z=s.symbols('z')
for qq in (2,3,5,7):
 for n in range(0,5):
  # Exact coefficient identity from the rational generating function.
  assert s.series((1+(qq-1)*z)/(1-z)**2,z,0,n+1).removeO().expand().coeff(z,n)==qq*n+1
for qq in (2,3,5,9):
 for rho in (0.3,0.7):
  rr=rho**qq
  ll=qq*(1+(qq-1)*rr**2)/(1-rr**2)**2
  tc=float(tcrit.subs({q:qq,r:rr}))
  nodes=rho*np.exp(2j*np.pi*np.arange(qq)/qq)
  G=1/(1-nodes[:,None]*nodes[None,:].conj())**2
  for fac in (0.5,1.,2.,100.):
   t=fac*tc
   beta=qq*t/(1+t*ll)
   yminus=(2+(qq-1)*beta-np.sqrt(4*qq*beta+(qq-1)**2*beta**2))/2
   z0=yminus**(1/qq)/rho
   v=1/(1-z0*np.conj(nodes))**2
   kt0=1-t*v.dot(np.linalg.solve(np.eye(qq)+t*G,np.ones(qq)))
   assert abs(kt0)<5e-7,(qq,rho,fac,kt0)
   if fac<1: assert yminus>rr
   elif fac>1: assert yminus<rr
   else: assert abs(yminus-rr)<1e-8
print('ATOMIC_ORBIT_THRESHOLD_PASS exact_identities=2 coefficients=20 direct_gram_cases=32')
