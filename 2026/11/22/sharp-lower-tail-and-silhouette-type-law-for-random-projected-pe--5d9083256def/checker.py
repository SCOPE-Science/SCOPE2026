#!/usr/bin/env python3
"""Numerical diagnostics for exact perimeter formulas and tangent-area asymptotics.
These checks support, but do not replace, the analytic proof in RESULT.md.
Requires NumPy and SciPy.
"""
import math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.integrate import quad
from scipy.optimize import brentq

V=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=float)
Pmin=2*(math.sqrt(2)+math.sqrt(6))
Pmax=6*math.sqrt(2)
count=0

def close(a,b,tol=1e-10):
 global count
 assert abs(a-b) <=tol*max(1,abs(a),abs(b)),(a,b,tol)
 count+=1

def formula(u):
 x,y,z=sorted(abs(float(t)) for t in u)[::-1]
 norm=math.sqrt(x*x+y*y+z*z)
 x,y,z=x/norm,y/norm,z/norm
 f=lambda t: math.sqrt(max(0,2-t*t))
 if x <= y+z:
  return 2*(f(x-y)+f(y-z)+f(x-z)),3
 return 2*(f(x+y)+f(x-y)+f(x+z)+f(x-z)),4

def actual(u):
 u=np.array(u,dtype=float);u/=np.linalg.norm(u)
 aa=np.cross(u,[0,0,1]);
 if np.linalg.norm(aa)<0.1:aa=np.cross(u,[1,0,0])
 aa/=np.linalg.norm(aa)
 bb=np.cross(u,aa)
 pts=np.stack((V@aa,V@bb),axis=1)
 hull=ConvexHull(pts)
 path=pts[hull.vertices]
 return float(np.linalg.norm(path-np.roll(path,1,axis=0),axis=1).sum()),len(path)

for u in [[1,0,0],[1,1,0],[1,1,1],[1,1,.1],[2,1,0],[.8,.5,.4]]:
 close(formula(u)[0],actual(u)[0])
close(formula([1,1,0])[0],Pmin)
close(formula([1,1,1])[0],Pmax)

rng=np.random.default_rng(20261117)
for i in range(2000):
 u=rng.normal(size=3)
 p,k=formula(u)
 p2,k2=actual(u)
 close(p,p2,2e-11)
 count+=1
 assert Pmin-1e-11<=p<=Pmax+1e-11
 count+=1
 assert k==k2

phi_star=math.atan(math.sqrt(2))
def f_tangent(phi):
 if phi<=phi_star:
  return 2*(math.sqrt(2)-math.sqrt(2/3)*math.cos(phi))
 return (4/math.sqrt(3))*math.sin(phi)

area_q=quad(lambda z:1/(2*f_tangent(z)**2),0,phi_star,epsabs=1e-13)[0]
area_t=quad(lambda z:1/(2*f_tangent(z)**2),phi_star,math.pi/2,epsabs=1e-13)[0]
close(area_t,3/(32*math.sqrt(2)))
C=12/math.pi*(area_q+area_t)
close(C,1.1953469179961405,3e-13)

u0=np.array([1/math.sqrt(2),1/math.sqrt(2),0])
ep=np.array([1/math.sqrt(2),-1/math.sqrt(2),0])
eq=np.array([0.,0.,1.])
def localp(r,phi):
 return formula(u0+r*(ep*math.cos(phi)+eq*math.sin(phi)))[0]

for phi in np.linspace(0,math.pi/2,61):
 for r in [1e-3,1e-4,1e-5]:
  close((localp(r,phi)-Pmin)/r, f_tangent(phi),max(5e-3,12*r))

def exact_prob(eps):
 def alpha(phi):
  # monotone in this small neighborhood
  maxr=2*eps
  assert localp(maxr,phi)>Pmin+eps
  rr=brentq(lambda r:localp(r,phi)-Pmin-eps,0,maxr,xtol=2e-15)
  return 1-1/math.sqrt(1+rr*rr)
 a=quad(alpha,0,phi_star,epsabs=1e-13)[0]
 b=quad(alpha,phi_star,math.pi/2,epsabs=1e-13)[0]
 return 12/math.pi*(a+b), (12/math.pi*b)/(12/math.pi*(a+b))
for eps,tol in [(1e-2,.04),(3e-3,.015),(1e-3,.006)]:
 prob,frac=exact_prob(eps)
 close(prob/eps**2,C,tol)
 close(frac,area_t/(area_q+area_t),tol)
print('checks_passed',count)
print('p_min',format(Pmin,'.15f'),'p_max',format(Pmax,'.15f'))
print('tangent_quad_area',format(area_q,'.15f'),'tangent_triangle_area',format(area_t,'.15f'))
print('tail_constant',format(C,'.15f'))
print('conditional_triangular_fraction',format(area_t/(area_q+area_t),'.15f'))
for e in [1e-2,3e-3,1e-3]:
 prob,ft=exact_prob(e)
 print('eps',e,'scaled_probability',prob/e**2,'triangular_fraction',ft)
