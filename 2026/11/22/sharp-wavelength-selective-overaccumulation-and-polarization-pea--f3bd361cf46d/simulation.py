import math, numpy as np
from numba import njit
@njit
def sample(tau,eps,alpha=1.0,v=1.0,dt=0.005,N=100000000,seed=29):
 np.random.seed(seed)
 x=0.;s=v; orientation=1.;cs=0.; pol_re=0.; pol_im=0.;acc=0.
 for j in range(N):
  if np.random.random()<alpha*dt:orientation=-orientation
  # midpoint integration of deterministic ODE
  cs0=math.cos(x)
  s_mid=s+0.5*dt*(v+eps*cs0-s)/tau
  x_mid=x+0.5*dt*orientation*s
  s+=dt*(v+eps*math.cos(x_mid)-s_mid)/tau
  x=(x+dt*orientation*s_mid)%(2*math.pi)
  if j>500000 and j%25==0:
   cs+=math.cos(x)
   pol_im+=orientation*math.sin(x)
   acc+=1
 return cs/acc,pol_im/acc
for tau in [0.15,0.5,1.0,2.0]:
 eps=0.08
 c,p=sample(tau,eps,seed=int(tau*1000)+123)
 F=(1+4*tau)/(1+2*tau+tau*tau)
 G=tau/(1+2*tau+tau*tau)
 # density c= -eps F / (2v); polarization sin = -eps G/2
 print(f'tau={tau} cos={c:.6f}, expected={-eps*F/2:.6f}; orientation_sin={p:.6f}, expected={-eps*G/2:.6f}',flush=True)
