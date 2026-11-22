"""Independent numerical quadrature for boundary mean-distance of a stadium.
No finite numerical result is used to prove the asymptotic theorem.
"""
import numpy as np
from scipy.special import roots_legendre
from math import pi,asinh,sqrt,log

def I(a,L=1.):
 if a==0:return L**3/3
 return L**3/3+2*(L*(0.5*(L*sqrt(L*L+a*a)+a*a*asinh(L/a))-L*L/2)-((L*L+a*a)**1.5-a**3-L**3)/3)

def primitive(z,b):
 return .5*(z*np.hypot(z,b)+b*b*np.arcsinh(z/np.maximum(b,1e-18)))

def check(r,n=180):
 L=1.; z,w=roots_legendre(n)
 angles=[(z+1)*pi/2+pi/2,(z+1)*pi/2-pi/2]
 wt=w*pi/2
 cap=[(r*np.cos(angles[0]),r*np.sin(angles[0])),(L+r*np.cos(angles[1]),r*np.sin(angles[1]))]
 num=2*I(0,L)+2*I(2*r,L)
 for cx,cy in cap:
  for sy in [-r,r]:
   a=np.abs(cy-sy)
   ints=primitive(L-cx,a)-primitive(-cx,a)
   num+=2*r*np.dot(wt,ints)
 for j,(cx,cy) in enumerate(cap):
  for k,(dx,dy) in enumerate(cap):
   sep=np.hypot(cx[:,None]-dx[None,:],cy[:,None]-dy[None,:])
   num+=r*r*np.sum(wt[:,None]*wt[None,:]*sep)
 P=2*(L+pi*r)
 ratio=num/P**3
 return ratio,(ratio-1/6)/(r*r*log(1/r))

if __name__=='__main__':
 for r in [.04,.02,.01,.005]:
  x,y=check(r)
  print(f'r={r:.4f} ratio={x:.12f} log-normalized-deficit={y:.9f}')
