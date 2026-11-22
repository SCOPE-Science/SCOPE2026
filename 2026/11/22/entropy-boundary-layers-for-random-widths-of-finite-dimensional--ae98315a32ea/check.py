"""Deterministic diagnostics for directional widths of Euclidean l_p unit balls.

Run: python check.py
Only finite tests. The proof is analytic and independent of these diagnostics.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.special import gamma

def S(d): return 2*math.pi**(d/2)/gamma(d/2)
def kappa(s): return math.pi**(s/2)/gamma(s/2+1)
def vq(s,q): return (2*gamma(1+1/q))**s/gamma(1+s/q)
def width(u,q): return 2*np.linalg.norm(np.asarray(u),ord=q)
def value(u,q): return np.linalg.norm(np.asarray(u),ord=q)
def ent(u):
 t=np.asarray(u)**2
 return float(-np.sum(np.where(t>0,t*np.log(np.maximum(t,1e-300)),0)))

def pred_constants(d,q):
 s=d-1; a=S(d); f0=d**(1/q-1/2)
 Caxisq=2*d*vq(s,q)*(q/2)**(s/q)/a
 Caxise=2*d*kappa(s)/a
 Cdiag=2**d*kappa(s)/(a*(abs(q-2)*f0)**(s/2))
 if q<2: return {'min':(1.,Caxisq,s/q),'max':(f0,Cdiag,s/2)}
 return {'min':(f0,Cdiag,s/2),'max':(1.,Caxise,s/2)}

checks=0
for d in [2,3,5,9]:
 s=d-1
 for q in [1.12,1.5,1.9,2.1,3,7]:
  mn,mx = pred_constants(d,q)['min'],pred_constants(d,q)['max']
  assert mn[0]<=mx[0]; checks+=1
  f0=d**(1/q-1/2)
  axis=np.zeros(d); axis[0]=1
  dia=np.ones(d)/math.sqrt(d)
  assert abs(value(axis,q)-1)<1e-12 and abs(value(dia,q)-f0)<1e-12; checks+=1
  # Local path at axis, r is tangent displacement.
  z=np.arange(1,d,dtype=float); z/=np.linalg.norm(z)
  for r in [1e-2,1e-3,1e-4]:
   u=np.r_[math.sqrt(1-r*r),r*z]
   diff=width(u,q)-2
   if q<2:
    approx=(2/q)*np.sum(abs(r*z)**q)-r*r
    assert abs(diff/approx-1)<.06, ('axis lower',d,q,r,diff/approx)
   else:
    approx=r*r-(2/q)*np.sum(abs(r*z)**q)
    assert abs((-diff)/approx-1)<.06,('axis upper',d,q,r,(-diff)/approx)
   checks+=1
  # Tangential path near equal-coordinate diagonal.
  tang=np.arange(d,dtype=float)-(d-1)/2
  tang/=np.linalg.norm(tang)
  for r in [1e-3, 5e-4, 1e-4]:
   u=math.sqrt(1-r*r)*dia+r*tang
   ratio=abs(width(u,q)-2*f0)/(abs(q-2)*f0*r*r)
   assert abs(ratio-1)<.03,('diag',d,q,r,ratio)
   checks+=1

# In dimension two, invert the exact directional-width map; compare sharp cdf tails.
for q in [1.25,1.5,3,5]:
 pred=pred_constants(2,q)
 f0=2**(1/q-.5)
 def w(theta): return width([math.cos(theta),math.sin(theta)],q)
 for eps in [1e-4, 1e-5, 1e-6]:
  if q<2:
   theta=brentq(lambda t:w(t)-(2+eps),0,math.pi/4,xtol=1e-15)
   prob=4*theta/math.pi
   cm,em=pred['min'][1:]
   assert abs(prob/(cm*eps**em)-1)<.32,(q,eps,'min',prob/(cm*eps**em))
   theta=brentq(lambda t:w(t)-(2*f0-eps),0,math.pi/4,xtol=1e-15)
   prob=4*(math.pi/4-theta)/math.pi
   cx,ex=pred['max'][1:]
   assert abs(prob/(cx*eps**ex)-1)<.05,(q,eps,'max',prob/(cx*eps**ex))
  else:
   theta=brentq(lambda t:w(t)-(2*f0+eps),0,math.pi/4,xtol=1e-15)
   prob=4*(math.pi/4-theta)/math.pi
   cm,em=pred['min'][1:]
   assert abs(prob/(cm*eps**em)-1)<.05,(q,eps,'min',prob/(cm*eps**em))
   theta=brentq(lambda t:w(t)-(2-eps),0,math.pi/4,xtol=1e-15)
   prob=4*theta/math.pi
   cx,ex=pred['max'][1:]
   assert abs(prob/(cx*eps**ex)-1)<.05,(q,eps,'max',prob/(cx*eps**ex))
  checks+=2

# Entropy limit, using deterministic Gaussian-sphere points.
rng=np.random.default_rng(146258)
for d in [2,3,5,10]:
 u=rng.standard_normal((400,d)); u/=np.linalg.norm(u,axis=1)[:,None]
 H=np.array([ent(v) for v in u])/2
 for delta in [-.03,-.01,.01,.03]:
  q=2-delta
  vals=np.array([(width(v,q)-2)/delta for v in u])
  assert np.max(abs(vals-H))<.04,('entropy',d,delta,np.max(abs(vals-H)))
  checks+=1
 # Sharp entropy lower-edge local normal form and upper-edge local normal form.
 a=np.zeros(d);a[0]=1
 diag=np.ones(d)/math.sqrt(d)
 z=np.arange(1,d,dtype=float);z/=np.linalg.norm(z)
 tang=np.arange(d,dtype=float)-(d-1)/2; tang/=np.linalg.norm(tang)
 for r in [1e-3,1e-4,1e-5]:
  u=np.r_[math.sqrt(1-r*r),r*z]
  h=ent(u)
  assert abs(h/(r*r*(math.log(1/r**2)+1+ent(z)))-1)<.015
  v=math.sqrt(1-r*r)*diag+r*tang
  coeff=(math.log(d)-ent(v))/(2*r*r)
  assert abs(coeff-1)<.02,('H diag',d,r,coeff)
  checks+=2

print('PASSED', checks, 'deterministic checks')
print('Example d=3, q=1.5:',pred_constants(3,1.5))
print('Example d=3, q=3:',pred_constants(3,3))
