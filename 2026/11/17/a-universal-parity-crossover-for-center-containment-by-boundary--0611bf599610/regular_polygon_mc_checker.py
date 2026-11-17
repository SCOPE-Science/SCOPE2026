"""Geometric Monte Carlo of center inclusion, independent of angular-density quadrature."""
import math
import numpy as np
from scipy.integrate import quad

def H(m,x):
 a=math.pi/m; C=1/(2*m*math.tan(a));T=math.tan(a)
 return .5+C*((math.tan(x+a)-math.tan(x)-T) if x<0 else (math.tan(x-a)-math.tan(x)+T))

def predicted(m,n):
 if m%2==0: return n*2.**(1-n)
 a=math.pi/m;C=1/(2*m*math.tan(a))
 return m*n*sum(quad(lambda x:C/(math.cos(x)**2)*H(m,x)**(n-1),lo,hi,epsabs=1e-12)[0] for lo,hi in [(-a,0),(0,a)])

def simulate(m,n,N=300000):
 rng=np.random.default_rng(451+100*m+n)
 # each segment chosen with equal probability, then uniform arc-position
 side=rng.integers(0,m,size=(N,n)); s=rng.random((N,n))
 t0=2*np.pi*side/m;t1=2*np.pi*((side+1)%m)/m
 xs=(1-s)*np.cos(t0)+s*np.cos(t1)
 ys=(1-s)*np.sin(t0)+s*np.sin(t1)
 angles=np.sort(np.mod(np.arctan2(ys,xs),2*np.pi),axis=1)
 maxgap=np.diff(np.concatenate((angles,angles[:,0:1]+2*np.pi),axis=1),axis=1).max(axis=1)
 return np.mean(maxgap>np.pi)

def main():
 for m,n in [(3,3),(3,4),(3,6),(4,3),(5,3),(5,5),(6,7),(7,4)]:
  p=predicted(m,n);obs=simulate(m,n)
  N=300000;se=math.sqrt(p*(1-p)/N)
  print(m,n,'exact',round(p,9),'mc',round(obs,9),'z',round((obs-p)/se,3))
  assert abs(obs-p)<5*se
 print('POLYGON_CONTAINMENT_INDEPENDENT_MC_OK')
if __name__=='__main__':main()
