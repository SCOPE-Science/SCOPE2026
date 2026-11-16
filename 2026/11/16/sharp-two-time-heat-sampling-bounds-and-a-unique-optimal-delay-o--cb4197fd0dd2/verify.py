"""Exact Fourier-fiber and optimizing-polynomial checks for two-rail heat sampling."""
import sympy as s
import numpy as np
r,z,ell=s.symbols('r z ell', real=True)
U=s.Matrix([[1,0],[r**2*(1+r)/2,r**2*(1-r)/2]])
V=s.Matrix([[1,0],[(1+r)/2,(1-r)/2]])
Glo=U.T*U; Ghi=V.T*V
Tlo=1+r**4*(1+r**2)/2
Thi=(3+r**2)/2
assert s.simplify(s.trace(Glo)-Tlo)==0
assert s.simplify(Glo.det()-r**4*(1-r)**2/4)==0
assert s.simplify(s.trace(Ghi)-Thi)==0
assert s.simplify(Ghi.det()-(1-r)**2/4)==0
F=s.factor(ell**2-s.trace(Glo)*ell+Glo.det())
Fr=s.factor(s.diff(F,r))
assert s.simplify(Fr+r**3*((4+6*r**2)*ell-(1-r)*(2-3*r))/2)==0
P=3*r**6-3*r**5+5*r**4-5*r**3+5*r**2+4*r-4
res=s.factor(s.resultant(4*F,Fr,ell))
assert s.factor(res/(-r**6*(r-1)*(r+1)**2))==P
assert s.factor(P.subs(r,s.Rational(2,3)))==s.Rational(64,243)
assert P.subs(r,0)==-4
assert P.subs(r,1)==5
assert (P.subs(r,s.Rational(637,1000)))<0
assert (P.subs(r,s.Rational(638,1000)))>0
root=float(s.nroots(P, maxsteps=200)[1]); assert .637<root<.638
T=float(Tlo.subs(r,root));D=float((r**4*(1-r)**2/4).subs(r,root))
A=(T-(T*T-4*D)**0.5)/2
assert abs(A-0.00488270447809)<1e-12
# Approximate the actual ladder heat-sampling frame by diagonalizing on finite cycles.
for N in [5,8,17,32]:
 for t in [.13,.674754444831455,1.7]:
  # Only endpoint frequency +/-pi is attained for even N. Other cycles approach it.
  qmin=np.exp(-5*t/3); qmax=np.exp(-t/3)
  C=np.cosh(t/3);S=np.sinh(t/3)
  def ev(q):
   M=np.array([[1.,0.],[q*C,q*S]])
   return np.linalg.eigvalsh(M.T@M)
  exactA=ev(qmin)[0]; exactB=ev(qmax)[1]
  eigs=[]
  for j in range(N):
   th=2*np.pi*j/N
   q=np.exp(-t*(1-2*np.cos(th)/3))
   eigs.extend(ev(q))
  assert min(eigs)>=exactA-1e-13 and max(eigs)<=exactB+1e-13
  assert abs(max(eigs)-exactB)<1e-12
  if N%2==0: assert abs(min(eigs)-exactA)<1e-12
print('CHECK_OK exact_gram=4 sextic_resultant=1 rational_brackets=2 finite_cycle_fibers=12')
