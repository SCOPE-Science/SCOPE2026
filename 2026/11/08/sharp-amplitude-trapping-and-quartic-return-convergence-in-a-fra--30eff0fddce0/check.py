"""Reproduce exact derivatives and sample dynamics for a fractional kinetic step."""
import math
import sympy as sp
r,a,eta=sp.symbols('r a eta',real=True,positive=True)
g=r/(1+r*r)**a
expected=-2*a*r*(3+(1-2*a)*r*r)/(1+r*r)**(a+2)
assert sp.simplify(sp.diff(g,r,2)-expected)==0
expected_e=(1+(1-2*a)*r*r)/(1+r*r)
assert sp.simplify(r*sp.diff(g,r)/g-expected_e)==0

def f(x,A,t):return x-t*x/(1+x*x)**A

def radius(x,A,t):return abs(f(x,A,t))

def R(A,t):return math.sqrt((t/2)**(1/A)-1)

# Evaluate the sharp invariant [0,R] envelope on a dense grid in contrasting regimes.
configs=[(0.2,2.1,True),(0.2,10.0,True),(0.32,2.7,True),(0.32,3.5,False),(0.4,2.5,True),(0.4,4.0,False)]
for A,t,expected_invariant in configs:
 if t<=2: continue
 rr=R(A,t)
 maximal=max(radius(rr*j/2000,A,t) for j in range(2001))
 assert (maximal <= rr+1e-10)==expected_invariant,(A,t,rr,maximal)
 assert abs(f(rr,A,t)+rr)<1e-10
 e=(1+(1-2*A)*rr*rr)/(1+rr*rr)
 assert abs((1-t*float(sp.diff(g,r).subs({r:rr,a:A}))) - (1-2*e))<1e-8

# At the finite critical tune: a>1/4 gives an attracting super-cycle.
for A in (0.3,0.4,0.49):
 crit=2*(4*A/(4*A-1))**A
 rr=R(A,crit)
 assert abs(1-crit*float(sp.diff(g,r).subs({r:rr,a:A})))<1e-9
 B=2*A*rr*(3+(1-2*A)*rr*rr)/(1+rr*rr)**2
 for d in (1e-3,1e-4,1e-5):
  nxt=radius(rr-d,A,crit)
  assert abs((rr-nxt)/(d*d)/B-1)<0.03
 for start in (rr/20,rr/2,rr*1.5,rr*100):
  r0=start
  for j in range(200):
   r0=radius(r0,A,crit)
  assert abs(rr-r0)<1e-9,(A,start,r0,rr)

# At the flip threshold eta=2, generic distance follows universal n^-1/2.
for A in (0.2,0.3,0.49):
 rn=0.1
 for k in range(1,100001):rn=radius(rn,A,2)
 assert abs(4*A*k*rn*rn-1)<0.02,(A,rn,k,4*A*k*rn*rn)
print('VERIFY_OK algebraic_second_derivative=1 elasticity=1 trapping_regimes=6 critical_supercycles=3 global_initializations=12 critical_relaxation=3')

import mpmath as mp
mp.mp.dps=85
for aa in (mp.mpf('0.3'),mp.mpf('0.4'),mp.mpf('0.49')):
 tc=2*(4*aa/(4*aa-1))**aa
 Rc=mp.sqrt((tc/2)**(1/aa)-1)
 Bc=(5*aa-1)*mp.sqrt(4*aa-1)/(4*aa)
 def ff(x):return x-tc*x/(1+x*x)**aa
 for delt in (mp.mpf('1e-3'),mp.mpf('-1e-3'),mp.mpf('1e-4')):
  xx=Rc+delt
  e2=Rc-ff(ff(xx))
  assert abs(e2/(Bc**3*delt**4)-1)<mp.mpf('0.03'), (aa,delt,e2/(Bc**3*delt**4))
print('VERIFY_OK quartic_two_step_limit=9')
