"""Reproducible supplementary checks for sliding three-point pairwise p-dispersion.
Requires Python 3 and numpy only. Finite checks do not replace the proof.
"""
import numpy as np

def D(v,p):
    a=np.asarray(v,dtype=float)
    return (abs(a[0]-a[1])**p+abs(a[0]-a[2])**p+abs(a[1]-a[2])**p)**(1/p)

def T(x,p):
    return np.array([D(x[i:i+3],p) for i in range(len(x)-2)])

def V(x): return float(sum(abs(np.diff(x))))

def K(n,p): return [0,0,0,0,1.5,2.5][n] * (2**(1/p)) if n<=5 else 3*2**(1/p)

def grad(z,p):
    a,b,c=map(float,z)
    dif=[a-b,a-c,b-c]
    norm=sum(abs(t)**p for t in dif)**((p-1)/p)
    if norm==0: raise ValueError('nondifferentiable')
    q=[np.sign(t)*abs(t)**(p-1) for t in dif]
    return np.array([q[0]+q[1],-q[0]+q[2],-q[1]-q[2]])/norm

rng=np.random.default_rng(20261117)
count=0
for p in [1.05,1.2,1.5,2.,3.,5.,10.]:
 for n in [3,4,5,6,7,11]:
  for _ in range(500):
   x=rng.normal(size=n)
   y=x+rng.normal(scale=rng.choice([0.01,0.3,3.]),size=n)
   assert V(T(x,p)-T(y,p)) <= K(n,p)*V(x-y)+1e-9
   count+=1
 print('LIPSCHITZ_PAIR_CHECKS_PASS',p,flush=True)
sharp=0
for p in [1.05,1.2,1.5,2.,3.,5.,10.]:
 for n in [4,5,6,7]:
  for eps in [1e-3, min(1e-4, 10**(-min(80.,4/(p-1))))]:
   # left crossing triple (a,b,c)=(1,0,eps), right (b,c,d)=(0,eps,eps)
   x=np.full(n,eps)
   k=2 if n in (4,5) else 3
   x[k-2]=1.;x[k-1]=0.;x[k]=eps;x[k+1]=eps
   if k==3: x[0]=1.
   h=np.zeros(n);h[k:]=1.
   gs=[]
   for i in range(n-2):
    z=x[i:i+3]
    if max(z)==min(z):gs.append(0.)
    else: gs.append(float(grad(z,p)@h[i:i+3]))
   ratio=V(gs)
   assert ratio <= K(n,p)+1e-8,(p,n,ratio,K(n,p))
   if eps!=1e-3: assert ratio >= K(n,p)*0.965,(p,n,ratio,K(n,p))
   sharp+=1
print('CHECKS_COMPLETE',count,'LIPSCHITZ_PAIRS',sharp,'SHARPNESS_DERIVATIVES')
