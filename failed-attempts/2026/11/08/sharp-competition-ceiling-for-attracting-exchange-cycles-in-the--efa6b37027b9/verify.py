#!/usr/bin/env python3
"""Independent numerical and symbolic checks of exchange-cycle formulas."""
import sympy as s
import mpmath as mp
u,v,a=s.symbols('u v a', positive=True)
P=s.Matrix([[0,1],[1,0]])
A=s.Matrix([[(v/u)*(1-u),-a*v],[-a*u,(u/v)*(1-v)]])
K=P*A
S=u+v
assert s.simplify(s.trace(K)+a*S)==0
assert s.simplify(K.det()-(S-1-(1-a*a)*u*v))==0
assert s.simplify((1+s.trace(K)+K.det())-(1-a)*(S-(1+a)*u*v))==0
assert s.simplify((1-s.trace(K)+K.det())-(1+a)*(S-(1-a)*u*v))==0
mp.mp.dps=60
crit=mp.findroot(lambda t:mp.sinh(t)**3-t*mp.cosh(t),(mp.mpf('.9'),mp.mpf('1.1')))
h=lambda t:2*t/mp.sinh(2*t)
astar=(1-h(crit))/(1+h(crit))
assert mp.mpf('.27783904026408')<astar<mp.mpf('.27783904026410')
assert mp.mpf('.97698898630967')<crit<mp.mpf('.97698898630969')
checks=0
for astr in ['0.025','0.05','0.2','0.2778390402640871511673254521332','0.3','0.5','0.8']:
 aa=mp.mpf(astr)
 t1=mp.findroot(lambda t:h(t)-(1-aa)/(1+aa),(.1,3))
 J=lambda t:(1+aa)*(t/mp.sinh(t))**2-t*mp.coth(t)+(1-aa)/2
 t2=mp.findroot(J,(.5,2))
 if abs(aa-astar)>mp.mpf('1e-22'):
  assert (t1<t2)==(aa<astar)
 for t in [min(t1,t2)*mp.mpf('.96'),(t1+t2)/2,max(t1,t2)*mp.mpf('1.04')]:
  summ=4*t*mp.coth(t)/(1-aa)
  U=summ*(1+mp.tanh(t))/2;V=summ*(1-mp.tanh(t))/2
  rr=mp.exp((1+aa)*summ/2)
  f=lambda x,y:(rr*x*mp.exp(-x-aa*y),rr*y*mp.exp(-aa*x-y))
  U2,V2=f(U,V)
  assert abs(U2-V)<mp.mpf('1e-43')
  assert abs(V2-U)<mp.mpf('1e-43')
  A0=mp.matrix([[V/U*(1-U),-aa*V],[-aa*U,U/V*(1-V)]])
  A1=mp.matrix([[U/V*(1-V),-aa*U],[-aa*V,V/U*(1-U)]])
  K0=mp.matrix([[-aa*U,U/V*(1-V)], [V/U*(1-U),-aa*V]])
  M=A1*A0;W=K0*K0
  assert max(abs(M[i,j]-W[i,j]) for i in range(2) for j in range(2))<mp.mpf('1e-43')
  tr=K0[0,0]+K0[1,1];det=mp.det(K0)
  schur=(1+tr+det>0 and 1-tr+det>0 and 1-det>0)
  pred=(t1<t<t2)
  if abs(t-t1)>mp.mpf('1e-30') and abs(t-t2)>mp.mpf('1e-30'):
   assert schur==pred
  checks+=1
print('VERIFY_OK symbolic_factorizations=4 root=1 exact_orbit_and_floquet_checks='+str(checks))
