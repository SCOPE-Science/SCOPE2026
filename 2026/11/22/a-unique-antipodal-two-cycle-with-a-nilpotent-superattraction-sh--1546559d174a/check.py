"""Numerical sanity tests; the infinite statements rely on the written proof."""
from math import sin, cos, pi, isfinite
import numpy as np

def state_map(x, p, q, r):
    a, b, c = x
    return np.array((b, sin(c), p*a + q*b - r*sin(c)), dtype=float)

def root(B):
    if abs(B-pi/2)<1.e-12: return 1.0
    lo, hi = 1.e-7, 1.
    assert sin(B*lo) > lo and sin(B*hi) <= hi
    for _ in range(85):
        m = (lo+hi)/2
        if sin(B*m)-m>0: lo=m
        else: hi=m
    return (lo+hi)/2

def jac(p, q, r, t):
    return np.array([[0.,1.,0.],[0.,0.,t],[p,q,-r*t]])

count=0
for p in (-2.,-0.5,0.2,1.,3.):
  for A in (-1.,-0.5,0.,0.6,1.):
    for B in (1.04,1.2,1.5,pi/2,1.7,2.,2.7,3.12):
      q=(A+B)/2; r=p+(B-A)/2
      v=root(B)
      P=np.array((v,-v,B*v)); Q=np.array((-v,v,-B*v))
      assert np.max(abs(state_map(P,p,q,r)-Q)) <1.e-12
      assert np.max(abs(state_map(Q,p,q,r)-P)) <1.e-12
      t=cos(B*v)
      J=jac(p,q,r,t)
      for lam in np.linalg.eigvals(J):
          assert abs(lam**3+r*t*lam**2-q*t*lam-p*t)<1.e-9
      if B==pi/2:
          assert np.max(abs(J@J@J))<1.e-14
      count+=1
for p in (-2.,-0.3,0.5,1.6):
  A=0.2
  for e in (1.e-3,1.e-5,1.e-7):
    for direction in (-1,1):
      B=pi/2+direction*e
      q=(A+B)/2; r=p+(B-A)/2
      v=root(B)
      J=jac(p,q,r,cos(B*v))
      rho=max(abs(np.linalg.eigvals(J)))**2
      ratio=rho/(abs(p*e)**(2/3))
      assert isfinite(ratio) and abs(ratio-1) < 1.6*(e**(1/3))
      count+=1
print('PASS:',count,'finite parameter/spectral sanity cases (not infinite proof)')
