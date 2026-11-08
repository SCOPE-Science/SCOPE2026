"""Standalone numerical checks for the asymmetric run-and-tumble ring result.
Units: p=1; the generator acts on (site,direction) probabilities.
"""
import math
import cmath
import numpy as np
from scipy.optimize import minimize_scalar,brentq

def t_root(delta):
 return brentq(lambda t: t**3+t**2-t-delta**-2,1,1/delta)

def predicted(n,p,delta):
 theta=2*math.pi/n
 s=math.sin(theta)
 a=1-math.cos(theta)
 if delta==0: return p*s,p*(a+s),1,1
 t=t_root(delta)
 alpha=math.sqrt((1-delta**2*t*t)/(t*t-1))
 z=t*alpha
 return p*s*z,p*(a+s*(z-alpha)),z,z-alpha

def analytic_gap(n,p,delta,u):
 vals=[2*u]
 for k in range(1,n):
  angle=2*math.pi*k/n
  s=math.sin(angle)
  z=cmath.sqrt(complex(u*u-p*p*s*s,2*delta*u*p*s))
  vals.append(p*(1-math.cos(angle))+u-z.real)
 return min(vals)

def generator(n,p,delta,u):
 # + -> - rate u(1-delta), - -> + rate u(1+delta)
 q=u*(1+delta)
 r=u*(1-delta)
 Q=np.zeros((2*n,2*n))
 for j in range(n):
  Q[2*((j+1)%n),2*j]+=p
  Q[2*j+1,2*j]+=r
  Q[2*j,2*j]-=p+r
  Q[2*((j-1)%n)+1,2*j+1]+=p
  Q[2*j,2*j+1]+=q
  Q[2*j+1,2*j+1]-=p+q
 return Q

count=0
for n in range(4,28):
 for delta in [0,.00001,.01,.1,.4,.75,.99]:
  p=1.3
  ustar,gstar,z,C=predicted(n,p,delta)
  for ratio in [0.05,.1,.3,.7,1,1.7,3,10]:
   u=ratio*ustar
   direct=np.linalg.eigvals(generator(n,p,delta,u))
   decay=sorted([-x.real for x in direct if abs(x)>1e-7])
   got=decay[0]
   formula=analytic_gap(n,p,delta,u)
   assert abs(got-formula)<1e-7,(n,delta,ratio,got,formula)
   assert got<=gstar+1e-7,(n,delta,ratio,got,gstar)
   if ratio!=1:assert got<gstar+1e-7
   count+=1
  if delta>0:
   numeric=minimize_scalar(lambda u:-analytic_gap(n,p,delta,u),bounds=(ustar*.8,ustar*1.2),method='bounded',options={'xatol':1e-11})
   assert abs(numeric.x-ustar)<1e-5,(n,delta,ustar,numeric.x)
print('all finite-matrix eigenvalue and global-optimum checks passed:',count)
for delta in [.0001,.001,.01]:
 u,g,z,C=predicted(1000,1,delta)
 epsilon=delta**(2/3)
 print('bias',delta,'z',z,'z_approx',1-.5*epsilon,'C',C,'C_approx',1-1.5*epsilon)
