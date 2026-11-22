"""Independent symbolic and finite-grid checks for a single exceptional spline interval."""
import sympy as s
from fractions import Fraction
from math import sqrt

r=s.symbols('r', positive=True)
z=s.sqrt(3); q=2-z; T=2/z
F=lambda u,v:s.cancel((u*u+v*v)/(u+v))
# Signed inverse kernel B^{-1}, row zero.
D=(r+z)*(3*r+z)
a=(2*r+z)/D; b=r/D
assert s.simplify((2*(r+1)-q)*a-r*b-1)==0
assert s.simplify((2*(r+1)-q)*b-r*a)==0
L0=s.cancel(3*(T*(a+b)+r*F(a,b)))
d0=-r*(r-1)*(r+1)/(3*(r+z/3)**2*(r+z))
assert s.simplify(s.radsimp(L0-2-d0))==0
print('EXACT_SHORT_INTERVAL_WITNESS_OK')
# Signed inverse kernel row two; two uniform tails and intervening defect.
t=r/(2*r+z)
H=2*(r+1)-r*t
u1=1/((2+z)*H-1)
u0=t*u1
u2=H*u1
assert s.simplify((2*r+z)*u0-r*u1)==0
assert s.simplify(2*(r+1)*u1-r*u0-u2)==0
assert s.simplify((4-q)*u2-u1-1)==0
L2=s.cancel(3*(T*(u0+u2)+r*F(u0,u1)+F(u1,u2)))
d2=((4-2*z)/3 * (r-1)*(r+1)*(r+z/2) *
    (r*r+(5*z/3-1)*r+1) /
    ((r+z/3)**2*(r+z)*(r*r+(2+2*z/3)*r+z)))
assert s.simplify(s.radsimp(L2-2-d2))==0
assert s.simplify(s.limit(L2,r,s.oo)-(10-2*z)/3)==0
print('EXACT_LONG_INTERVAL_WITNESS_OK')
# Uniform grid knot value from geometric Green kernel.
c=1/(2*z)
assert s.simplify(6*c*T)==2
print('UNIFORM_REFERENCE_EXACT_OK')
# Finite cyclic matrices: test inverse Green and integrated absolute kernels.
import numpy as np
for rr in (0.2,0.5,1,2,3,8):
 for n in (12,24,60,120):
  hs=np.ones(n);hs[0]=rr
  mat=np.diag(2*(hs+np.roll(hs,1)))
  off=np.diag(hs[:-1],1)+np.diag(hs[:-1],-1)
  mat=mat+off
  mat[0,-1]=mat[-1,0]=hs[-1]
  inv=np.linalg.inv(mat)
  # integral of absolute of linear kernel on each knot interval
  G=6*inv
  for k in (0,2):
   u=G[k,:];v=np.roll(u,-1)
   cross=u*v<0
   integ=np.where(cross,(u*u+v*v)/(2*(abs(u)+abs(v))), (abs(u)+abs(v))/2)
   L=float(np.dot(hs,integ))
   target=float((L0 if k==0 else L2).subs(r,rr))
   if n==120:
    assert abs(L-target)<1e-9,(rr,k,n,L,target)
   assert L>=1.0-1e-9
 print('FINITE_CYCLIC_R',rr,'OK')
print('ALL_SINGLE_DEFECT_SPLINE_CHECKS_PASSED')
