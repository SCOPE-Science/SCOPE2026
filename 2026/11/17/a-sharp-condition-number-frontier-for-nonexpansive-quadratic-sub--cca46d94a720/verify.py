"""Independent algebraic and finite-dimensional checks for a quadratic subgradient projector."""
import math
import random
import sympy as s

k, t, h = s.symbols('k t h', positive=True)
x, y = s.symbols('x y', real=True)
A = s.diag(1, k)
v = s.Matrix([x, y])
q = (v.T*A*v)[0]
r = (v.T*A*A*v)[0]
G = v - q/(2*r)*A*v
J = G.jacobian([x,y])
# For u=A v/||A v||, t=(v^T A v)/(v^T A^2 v).
# Verify reflected derivative identity at several rational instances.
for kval in [s.Rational(1), s.Rational(5,4), s.Rational(2), s.Rational(3), s.Rational(4), s.Rational(6)]:
 for xx, yy in [(1,0), (0,1), (2,3), (7,-2), (-1,5)]:
  vec=s.Matrix([xx,yy]);mat=s.diag(1,kval)
  av=mat*vec;d=(av.T*av)[0];uu=av*av.T/d
  tt=(vec.T*mat*vec)[0]/d
  R=s.eye(2)-2*uu
  P=s.eye(2)-uu
  Jac=J.subs({k:kval,x:xx,y:yy})
  assert (R*Jac-(P-tt*mat/2)).applyfunc(s.factor)==s.zeros(2)
print('EXACT_REFLECTION_JACOBIAN_IDENTITIES_PASS 30')
# The endpoint spectral mixture is the worst case for fixed t by convexity.
a=1/k
wb=(t-a)/(1-a)
wa=(1-t)/(1-a)
F=s.factor(1-2*(wb/(4-t)+wa/(4-k*t)))
assert s.factor(F - (3*k*t*t-4*(k+1)*t+8)/((4-t)*(4-k*t)))==0
assert s.factor(s.diff(h/(4*h-t),h,2)-8*t/(4*h-t)**3)==0
Q=3*k*t*t-4*(k+1)*t+8
vertex=s.Rational(2)*(k+1)/(3*k)
assert s.factor(Q.subs(t,vertex)-4*(4*k-k*k-1)/(3*k))==0
assert s.factor((k-(2+s.sqrt(3)))*(k-(2-s.sqrt(3)))-(k*k-4*k+1))==0
print('EXACT_SPECTRAL_CHORD_AND_THRESHOLD_IDENTITIES_PASS')
# Rational expansive example in dimension 2, with k=4 and t=5/6.
u=s.Matrix([s.sqrt(7)/3,s.sqrt(2)/3]); mat=s.diag(1,4); tt=(u.T*mat.inv()*u)[0]
assert tt==s.Rational(5,6)
B=4*s.eye(2)-tt*mat-2*u*u.T
assert s.factor(B.det()) < 0
print('EXACT_EXPANSION_WITNESS_K4_PASS det=',B.det())
# Boundary equality: spectral inequality loses strictness at 2+sqrt(3).
kcrit=2+s.sqrt(3)
tcrit=s.simplify(2*(kcrit+1)/(3*kcrit))
w_hi=s.simplify((1-tcrit)/(1-1/kcrit))
ucrit=s.Matrix([s.sqrt(1-w_hi),s.sqrt(w_hi)])
Acrit=s.diag(1,kcrit)
Bcrit=4*s.eye(2)-tcrit*Acrit-2*ucrit*ucrit.T
assert s.simplify(Bcrit.det())==0
print('EXACT_CRITICAL_DIRECTION_CERTIFICATE_PASS')
# Numerical finite-dimensional corroboration, not a replacement for proof.
rng=random.Random(7654321)
import numpy as np
for kval, expected in [(2,False),(3,False),(2+math.sqrt(3),False),(3.9,True),(4.5,True)]:
 A_np=np.diag([1.0,kval])
 best=0.0
 for i in range(2000):
  theta=(i+0.5)*math.pi/(2*2000)
  v_np=np.array([math.cos(theta),math.sin(theta)])
  av=A_np@v_np; un=av/np.linalg.norm(av)
  tn=(v_np@av)/(av@av)
  S=np.eye(2)-np.outer(un,un)-tn*A_np/2
  best=max(best,float(np.linalg.norm(S,2)))
 assert (best>1+1e-6)==expected,(kval,best)
 print('PLANAR_TRANSITION_SAMPLE',round(kval,8),round(best,10))
print('ALL_NEW_QUADRATIC_SUBGRADIENT_CHECKS_PASS')
