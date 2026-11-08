"""Independent numerical and algebraic checks of the noisy two-point Anderson tail theorem.
Requires scipy, mpmath; run: python verify.py.
"""
from fractions import Fraction as F
from math import log
from scipy.integrate import quad
import numpy as np

def aa(x0,x1,theta,r,delta,e0,e1):
    k=1-r
    f0=-k*(x0-theta)+e0
    f1=-k*(x1-theta)+e1
    return (x0*f1-x1*f0)/(f1-f0)

# Verify the exact identity in rational arithmetic across a grid.
checks=0
for k in (F(1,4),F(1,2),F(3,4)):
 for theta in (F(-3,4),F(0),F(2,3)):
  for x0,x1 in [(F(0),F(1)),(F(-2),F(3)),(F(1,5),F(2,5))]:
   a,b=x0-theta,x1-theta
   for e0 in (F(-1,3),F(1,7),F(4,9)):
    for e1 in (F(-2,5),F(1,8),F(3,4)):
     d=-k*(x1-x0)+e1-e0
     if d==0:continue
     lhs=aa(x0,x1,theta,1-k,F(1,2),e0,e1)-theta
     rhs=(a*e1-b*e0)/d
     assert lhs==rhs,(lhs,rhs)
     checks+=1

# Two-point independent uniform noise, special case x0=theta=0, x1=1.
# Given e0=z, event |x+|>t iff e1 is in (z+k-|z|/t, z+k+|z|/t).
def tail(t,k,delta):
 def integral(z):
  lo=z+k-abs(z)/t
  hi=z+k+abs(z)/t
  return max(0.,min(delta,hi)-max(-delta,lo))
 # split at numerical kink positions; adaptive quadrature adequate to precision 1e-8
 return quad(integral,-delta,delta,epsabs=1e-11,limit=1000,points=[0., min(delta,delta-k), max(-delta,delta-k)])[0]/(4*delta**2)

k=.5
for t in (2.,5.,10.,100.):
 v=tail(t,k,.25)
 exact=1/(8*t*(t+1))
 assert abs(v-exact)<1e-9,(t,v,exact)
 checks+=1
# Supercritical constant C=0.25 for delta=0.5.
for t in (100.,1000.):
 v=tail(t,k,.5)
 assert abs(t*v-.25)<.003,(t,v,t*v)
 checks+=1

# Below critical: exact one-dimensional reduction for second moment.
def second_moment(delta,k=.5):
 assert 2*delta<k
 gap=k-2*delta
 # noise corner u=e0+delta; v=delta-e1, D=-(gap+u+v)
 return quad(lambda u: (delta-u)**2*(1/(gap+u)-1/(gap+u+2*delta)),0,2*delta,
             epsabs=1e-11,limit=1000)[0]/(4*delta**2)
for s in (1e-3,1e-5,1e-8):
 d=(k-s)/2
 val=second_moment(d,k)
 assert val>0 and val/log(k/s)>.09 and val/log(k/s)<.26,(s,val)
 checks+=1

# Critical symmetric geometry: abs(x-theta) <= abs(a) for a=-b.
for e0 in np.linspace(-.25,.25,101):
 for e1 in np.linspace(-.25,.25,101):
  if abs(e1-e0-.5)<1e-12: continue
  x=aa(-.5,.5,0.,.5,.25,e0,e1)
  assert abs(x)<=.50000000001,x
  checks+=1

print('PASS',checks,'checks')
for t in (2,5,10,100):
 print('critical tail:',t,tail(t,.5,.25),'formula:',1/(8*t*(t+1)))
for t in (10,100,1000):
 print('supercritical t*tail:',t,t*tail(t,.5,.5))
for s in (1e-3,1e-5,1e-8):
 d=(k-s)/2
 print('subcritical moment/log ratio',s,second_moment(d,k)/log(k/s))
