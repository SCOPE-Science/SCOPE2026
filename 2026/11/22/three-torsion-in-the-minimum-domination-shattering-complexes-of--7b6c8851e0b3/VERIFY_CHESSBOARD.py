from itertools import combinations
import numpy as np

def faces(k,n=5):
  ans=[]
  for rows in combinations(range(n),k):
    for cols in combinations(range(n),k):
      from itertools import permutations
      for perm in permutations(cols):
        ans.append(tuple(sorted(r*n+c for r,c in zip(rows,perm))))
  return ans

def rank_mod(p,k):
  smaller=faces(k); larger=faces(k+1)
  lookup={s:i for i,s in enumerate(smaller)}
  A=np.zeros((len(smaller),len(larger)),dtype=np.int16)
  for j,seq in enumerate(larger):
    for i in range(k+1):
      sub=seq[:i]+seq[i+1:]
      A[lookup[sub],j]=(1 if i%2==0 else p-1)
  r=0
  for col in range(A.shape[1]):
    nz=np.nonzero(A[r:,col])[0]
    if not len(nz):continue
    pivot=r+nz[0]
    A[[r,pivot]]=A[[pivot,r]]
    scale=pow(int(A[r,col]),-1,p)
    A[r,col:]=(A[r,col:]*scale)%p
    nz_rows=np.flatnonzero(A[r+1:,col])
    if len(nz_rows):
      ri=nz_rows+r+1
      A[ri,col:]=(A[ri,col:]-A[ri,col,None]*A[r,col:])%p
    r+=1
    if r==min(A.shape):break
  return r

for p in (2,3,5):
    ranks=[rank_mod(p,k) for k in (1,2,3,4)]
    print('modulus',p,'ranks',ranks,'betti H1 H2 H3 H4', [200-ranks[0]-ranks[1],600-ranks[1]-ranks[2],600-ranks[2]-ranks[3],120-ranks[3]],flush=True)
