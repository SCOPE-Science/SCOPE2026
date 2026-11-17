import numpy as np
from scipy.integrate import quad
from scipy.spatial import ConvexHull
from scipy.special import kv

def rate(lam,alpha):
  if lam==0: return 1.
  # v>max(0,lam/a-a), u>max(0,lam/b-b), ab>lam
  def inner(a):
    return np.exp(-a-alpha*max(0,lam/a-a))*quad(lambda b:np.exp(-b-alpha*max(0,lam/b-b)),lam/a,np.inf,epsabs=1e-10)[0]
  return quad(inner,0,np.sqrt(lam),epsabs=1e-8)[0]+quad(inner,np.sqrt(lam),np.inf,epsabs=1e-8)[0]

def count_exact(n,m,lam,rng,check=False):
 r=1-(2*np.pi/n)**2*lam/2
 angles0=np.sort(rng.uniform(0,2*np.pi,n))
 angles1=np.sort(rng.uniform(0,2*np.pi,m))
 # ext angle signed (-2pi,2pi); nearest for outer + inner
 aidx=np.searchsorted(angles0, angles1)
 left0=angles0[(aidx-1)%n]; right0=angles0[aidx%n]
 pl=np.mod(angles1-left0,2*np.pi); pr=np.mod(right0-angles1,2*np.pi)
 # nearest same radius using shifts; distances
 inner_left=np.mod(angles1-np.roll(angles1,1),2*np.pi)
 inner_right=np.mod(np.roll(angles1,-1)-angles1,2*np.pi)
 L0=(np.cos(pl)-r)/np.sin(pl) # from outer at -pl => (r-cos(pl))/(-sin pl)
 R0=(r-np.cos(pr))/np.sin(pr)
 L1=-np.tan(inner_left/2)
 R1=np.tan(inner_right/2)
 predicted=(np.maximum(L0,L1)<np.minimum(R0,R1))
 if check:
  xy=np.concatenate([np.stack([np.cos(angles0),np.sin(angles0)],axis=-1), r*np.stack([np.cos(angles1),np.sin(angles1)],axis=-1)])
  hv=ConvexHull(xy).vertices
  actual=np.isin(np.arange(n,n+m),hv)
  if not np.array_equal(predicted,actual):
   print('MISMATCH',n,m,lam,np.count_nonzero(predicted!=actual)); return False, predicted.mean(),actual.mean()
 return True,predicted.mean(),None

if __name__=='__main__':
 rng=np.random.default_rng(20261112)
 for lam in [0, .1, 1, 4]:
  p=rate(lam,1)
  print('lambda',lam,'p_theory',p,'p_no_inner_limit',2*np.sqrt(lam)*kv(1,2*np.sqrt(lam)) if lam else 1)
  for n in [100,300,800]:
   arr=[]
   for i in range(250 if n<=300 else 100):
    ok,a,_=count_exact(n,n,lam,rng,check=(i<10))
    assert ok
    arr.append(a)
   print('n',n,'mean',np.mean(arr),'std',np.std(arr))
 print('ALL_CHECKS_OK')
