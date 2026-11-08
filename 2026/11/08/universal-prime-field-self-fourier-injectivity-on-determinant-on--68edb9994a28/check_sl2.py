import numpy as np
from sympy import primitive_root, nextprime
for p in [2,3,5,7]:
 ell=p+1
 while not (int(ell)%p == 1 and __import__('sympy').isprime(ell)): ell+=1
 root=pow(primitive_root(ell),(ell-1)//p,ell)
 g=[(a,b,c,d) for a in range(p) for b in range(p) for c in range(p) for d in range(p) if (a*d-b*c)%p==1]
 X=np.array(g,dtype=np.int64)
 powers=np.array([pow(root,i,ell) for i in range(p)],dtype=np.int64)
 M=powers[X@X.T%p].copy()
 rank=0
 for j in range(len(g)):
  inds=np.flatnonzero(M[rank:,j])
  if len(inds)==0: continue
  i=rank+inds[0]
  M[[rank,i]]=M[[i,rank]]
  inv=pow(int(M[rank,j]),-1,ell)
  if rank+1<len(g):
   factors=(M[rank+1:,j]*inv)%ell
   M[rank+1:,j:]=(M[rank+1:,j:]-factors[:,None]*M[rank,j:][None,:])%ell
  rank+=1
  if rank==len(g):break
 print('exact_modular',p,'ell',ell,'root',root,'N',len(g),'rank',rank,'full',rank==len(g),flush=True)
