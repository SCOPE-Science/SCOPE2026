#!/usr/bin/env python3
"""Exact symbolic and finite numerical checks for a three-step implicit angular map."""
import sympy as s
import math
x,y,z, t, u=s.symbols('x y z t u', positive=True)
phi=lambda a,b: a*b*(b-a)/(a+b)
expr=s.factor(phi(x,y)+phi(y,z)+phi(z,x))
assert s.simplify(expr + (x-y)*(x-z)*(y-z)*(x*y+x*z+y*z)/((x+y)*(x+z)*(y+z)))==0
rad=3-2*s.sqrt(2)
z_plus=1+s.sqrt(2)
z_minus=s.sqrt(2)-1
assert s.simplify(z_plus*(z_plus-1)/(z_plus+1)-1)==0
assert s.simplify(z_minus*(z_minus-1)/(z_minus+1)+rad)==0

def Phi(w,v):return s.simplify(w*v*(v-w)/(v+w))
assert s.simplify(Phi(1,z_plus)-1)==0
assert s.simplify(Phi(z_plus,1)+1)==0
# The larger quadratic roots agree with both endpoint speeds.
def plusroot(w,drive):
 tau=drive/(w*w)
 return s.simplify(w*(1+tau+s.sqrt(1+6*tau+tau*tau))/2)
assert s.simplify(plusroot(s.Integer(1),s.Integer(1))-z_plus)==0
assert s.simplify(plusroot(z_plus,s.Integer(-1))-1)==0
assert s.simplify(Phi(z_plus,1)+1)==0
assert s.simplify(Phi(z_plus,1)+1)==0
# The larger quadratic roots agree with both endpoint speeds.
def plusroot(w,drive):
 tau=drive/(w*w)
 return s.simplify(w*(1+tau+s.sqrt(1+6*tau+tau*tau))/2)
assert s.simplify(plusroot(s.Integer(1),s.Integer(1))-z_plus)==0
assert s.simplify(plusroot(z_plus,s.Integer(-1))-1)==0
# Check the identity and its zero-set on 729 positive rational triples
cases=0
for a in range(1,10):
 for b in range(1,10):
  for c in range(1,10):
   A,B,C=map(s.Rational,(a,b,c))
   lhs=Phi(A,B)+Phi(B,C)+Phi(C,A)
   assert (lhs==0)==(a==b or a==c or b==c)
   cases+=1

def root(w, t):
 tau=t/(w*w)
 rad=1+6*tau+tau*tau
 if rad<0:return None
 return w*(1+tau+math.sqrt(rad))/2
# Identify singular endpoints and strict-interior branches for a=1
for sign in (+1,-1):
 threshold=1 if sign==1 else (3+2*math.sqrt(2))
 for scale in (1.00001,1.1,2,5,100):
  w=math.sqrt(threshold*scale)
  v=root(w,sign)
  assert v is not None
  final=root(v,-sign)
  assert final is not None
  assert abs(final-w)<1e-9*max(1,w)
# Compute off-grid drift for 3-step map for two unrelated phases, all sufficiently large speeds
for phase in (.2,.6,1.25):
 for w in (5,7,12,20):
  v=w
  for k in range(3):
   v=root(v,math.sin(phase+2*k*math.pi/3))
   assert v is not None
  assert abs(v-w)>1e-12
print('VERIFY_OK exact_phi_identity=1 rational_triples='+str(cases)+' exact_threshold_cases=2 high_speed_branch_tests=10 offgrid_tests=12')
