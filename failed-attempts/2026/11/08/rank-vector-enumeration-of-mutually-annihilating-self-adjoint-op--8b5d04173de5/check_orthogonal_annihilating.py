"""Independent finite-field enumeration of self-adjoint square-zero annihilating pairs.
Only public mathematical objects are described. No external packages except numpy.
"""
import itertools
from collections import Counter
import numpy as np

def rank_mod(M,q):
 A=(np.array(M,dtype=np.int64)%q).copy(); rows,cols=A.shape; k=0
 for j in range(cols):
  t=next((i for i in range(k,rows) if A[i,j]%q),None)
  if t is None:continue
  A[[k,t]]=A[[t,k]]; A[k]=A[k]*pow(int(A[k,j]),-1,q)%q
  for i in range(rows):
   if i!=k: A[i]=(A[i]-A[i,j]*A[k])%q
  k+=1
  if k==rows:break
 return k

def enumerate_ops(q,G):
 n=G.shape[0]; tri=[(i,j) for i in range(n) for j in range(i,n)]
 assert np.array_equal(G@G%q,np.eye(n,dtype=np.int64))
 found=[]
 for terms in itertools.product(range(q),repeat=len(tri)):
  S=np.zeros((n,n),dtype=np.int64)
  for (i,j),a in zip(tri,terms):S[i,j]=S[j,i]=a
  A=G@S%q
  if not np.any(A@A%q):found.append((A,rank_mod(A,q)))
 return found

def check():
 for q in (3,):
  for typ in ('split','nonsplit'):
   H=np.array([[0,1],[1,0]],dtype=np.int64)
   D=H if typ=='split' else np.eye(2,dtype=np.int64)
   G=np.block([[H,np.zeros((2,2),dtype=np.int64)],[np.zeros((2,2),dtype=np.int64),D]])
   ops=enumerate_ops(q,G)
   print('field',q,'type',typ,'squarezero',len(ops),'ranks',dict(Counter(r for _,r in ops)),flush=True)
   counts=Counter()
   for A,r in ops:
    for B,s in ops:
     if np.any(A@B%q):continue
     d=rank_mod(np.concatenate([A,B],axis=1),q)
     counts[(d,r,s)]+=1
   by_d=Counter()
   for (d,r,s),v in counts.items():by_d[d]+=v
   print('  mutual-zero pairs, by image span', dict(sorted(by_d.items())))
   print('  by (span,rankA,rankB):',dict(sorted(counts.items())))
   exp={0:1,1: (q+1)**2*(q*q-1) if typ=='split' else (q*q+1)*(q*q-1)}
   if typ=='split':exp[2]=2*(q+1)*(q**6-(q+1)*q*q+q)
   assert dict(by_d)==exp, (dict(by_d),exp)
 for q in (3,5):
  H=np.array([[0,1],[1,0]],dtype=np.int64)
  G=np.block([[H,np.zeros((2,1),dtype=np.int64)],[np.zeros((1,2),dtype=np.int64),np.eye(1,dtype=np.int64)]])
  ops=enumerate_ops(q,G)
  counts=Counter()
  for A,r in ops:
   for B,s in ops:
    if np.any(A@B%q):continue
    d=rank_mod(np.concatenate([A,B],axis=1),q)
    counts[d]+=1
  exp={0:1,1:(q+1)*(q*q-1)}
  print('field',q,'odd dimension 3','squarezero',len(ops),'pair image-span',dict(counts), flush=True)
  assert dict(counts)==exp
 print('ALL_ORTHOGONAL_ANNIHILATING_CHECKS_PASS')
if __name__=='__main__':check()
