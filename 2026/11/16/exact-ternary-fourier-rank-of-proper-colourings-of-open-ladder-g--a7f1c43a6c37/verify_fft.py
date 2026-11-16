import numpy as np
from collections import Counter
import sys,time

def transform_array(n):
 d=2*n-1; L=3**d
 T=np.zeros((L,2),dtype=np.int64)
 power=[3**(d-1-j) for j in range(d)]
 def dfs(i,a,b,ind):
  if i==n:
   T[ind,0]=1
   return
  for aa in range(3):
   if aa==a: continue
   for bb in range(3):
    if bb==b or bb==aa: continue
    dfs(i+1,aa,bb,ind+aa*power[2*i-1]+bb*power[2*i])
 for b in (1,2):dfs(1,0,b,b*power[0])
 num=int(T[:,0].sum())
 # reshape (3)*d,2. Axis shifts from innermost to outermost
 for ax in range(d):
  sh=[3]*d+[2]
  V=T.reshape(sh)
  t0=np.take(V,0,axis=ax);t1=np.take(V,1,axis=ax);t2=np.take(V,2,axis=ax)
  # after take arrays are new copies; output compute
  s0=t0+t1+t2
  # omega t1 = (-b,a-b), omega2 t2=(b-a,-a)
  s1=np.empty_like(t0);s2=np.empty_like(t0)
  s1[...,0]=t0[...,0]-t1[...,1]+t2[...,1]-t2[...,0]
  s1[...,1]=t0[...,1]+t1[...,0]-t1[...,1]-t2[...,0]
  s2[...,0]=t0[...,0]+t1[...,1]-t1[...,0]-t2[...,1]
  s2[...,1]=t0[...,1]-t1[...,0]+t2[...,0]-t2[...,1]
  idx=[slice(None)]*(d+1)
  for j,s in enumerate((s0,s1,s2)):
   idx[ax]=j; V[tuple(idx)]=s
 N=int(np.count_nonzero(np.any(T!=0,axis=-1)))
 zz=L-N
 nrm=(T[:,0]**2-T[:,0]*T[:,1]+T[:,1]**2)
 mags=Counter(nrm.tolist())
 assert N == (3*9**n - 24*n + 45)//16, (n,N)
 print('n=',n,'colourings=',num*3,'balanced frequency=',L,'rank=',N,'zeros=',zz,'min norm2=',min(k for k in mags if k),'max norm2=',max(mags),'num vals=',len(mags))
 print('small levels',sorted(mags.items())[:15]);print('largest',sorted(mags.items())[-6:])
 return T
if __name__=='__main__':
 for n in range(1,int(sys.argv[1])+1):
  tic=time.time();transform_array(n);print('elapsed',time.time()-tic,flush=True)
