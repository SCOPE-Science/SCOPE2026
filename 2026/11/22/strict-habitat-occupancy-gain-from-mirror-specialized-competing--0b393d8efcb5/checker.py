"""Reproduce equilibrium, determinant, and strict occupancy checks in a symmetric two-habitat colonization model."""
import math
import random
import sympy as sp
import numpy as np
from scipy.optimize import root

x,y,a,b,w,d,D=sp.symbols('x y a b w d D', positive=True)
F=a*x+b*y
G=b*x+a*y
J_s=sp.Matrix([[a*w-d-F,b*w-F],[b*w-G,a*w-D-G]])
J_a=sp.Matrix([[a*w-d-F,b*w+F],[b*w+G,a*w-D-G]])
eq={d:w*F/x,D:w*G/y}
assert sp.factor(J_a.det().subs(eq)-a*b*w*(x-y)**2*(x+y)/(x*y)) == 0
assert sp.factor(J_s.det().subs(eq)-b*w*(x+y)*(a*x*x+a*y*y+2*b*x*y)/(x*y)) == 0
assert sp.factor(J_s.trace()-J_a.trace()) == 0
h,l=sp.symbols('h l',positive=True)
w0=1-(h+l)/2
E=sp.symbols('E',positive=True)
# The equilibrium substitutions are d*h/(1-h)=a*h+b*l, D*l/(1-l)=b*h+a*l.
diff=(h-l)/(2*w0)*(a*(h*h-l*l))
R=d*h*h/(1-h)+D*l*l/(1-l)-(d*h*h+D*l*l)/w0
assert sp.factor(R-diff).subs({d:(1-h)*(a*h+b*l)/h,D:(1-l)*(b*h+a*l)/l}).simplify()==0

rho=sp.Rational(8,3)
xx=sp.Rational(15,32); yy=sp.Rational(5,32)
assert sp.Rational(3,8)*(2*xx+2*yy)==xx
assert sp.Rational(3,8)*(2*xx+2*yy)==3*yy
mono_sum=sp.sqrt(5)/2
assert sp.simplify(mono_sum-(sp.sqrt(5)/(1+sp.sqrt(5))+sp.sqrt(5)/(3+sp.sqrt(5))))==0
assert sp.simplify(sp.Rational(5,4)-mono_sum)>0

rng=random.Random(20261116)
checks=0
for _ in range(200):
  aa=10**rng.uniform(-.7,.7)
  bb=10**rng.uniform(-.8,.8)
  dd=10**rng.uniform(-.8,.4)
  DD=dd*10**rng.uniform(.03,.9)
  C=np.array([[aa,bb],[bb,aa]])
  Ds=np.diag([dd,DD])
  Rr=np.linalg.eigvals(np.linalg.solve(Ds,C)).real.max()
  if Rr<=1.03:continue
  ww=1/Rr
  eigvals,eigvecs=np.linalg.eig(np.linalg.solve(Ds,C))
  vec=np.abs(eigvecs[:,np.argmax(eigvals.real)].real)
  X,Y=(1-ww)*vec/vec.sum()
  def mono(v):return -np.array([dd,DD])*v+(1-v)*(C@v)
  z=root(mono,[.8,.8],tol=1e-11)
  if not z.success and max(abs(mono(z.x)))>1e-10:raise AssertionError(z.message)
  H,L=z.x
  assert 0<H<1 and 0<L<1 and H>L and X>Y>0
  assert 2*(X+Y)>H+L+1e-10,(aa,bb,dd,DD)
  jS=np.array([[aa*ww-dd-(aa*X+bb*Y),bb*ww-(aa*X+bb*Y)], [bb*ww-(bb*X+aa*Y),aa*ww-DD-(bb*X+aa*Y)]])
  jA=np.array([[aa*ww-dd-(aa*X+bb*Y),bb*ww+(aa*X+bb*Y)], [bb*ww+(bb*X+aa*Y),aa*ww-DD-(bb*X+aa*Y)]])
  assert max(np.linalg.eigvals(jS).real)<0
  assert max(np.linalg.eigvals(jA).real)<0
  checks+=1
assert checks>100,checks
print('PASS symbolic determinant identities, Rayleigh gap, exact example; numerical admissible cases:',checks)
