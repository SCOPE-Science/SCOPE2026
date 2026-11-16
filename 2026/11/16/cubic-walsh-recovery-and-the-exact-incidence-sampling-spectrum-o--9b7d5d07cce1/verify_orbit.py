"""Independent orbit enumeration and modular rank certificate."""
from itertools import permutations, product, combinations
from math import comb
import numpy as np

q=[(x,y) for x in range(3) for y in range(3)]
idx={v:i for i,v in enumerate(q)}
seed=set()
for a,b in q:
 for dx,dy in ((1,0),(0,1),(1,1),(1,2)):
  seed.add(tuple(sorted(idx[((a+k*dx)%3,(b+k*dy)%3)] for k in range(3))))
assert len(seed)==12
trips=list(combinations(range(9),3))
pos={a:i for i,a in enumerate(trips)}
set_of_sets=set()
for perm in permutations(range(9)):
 bits=0
 for a,b,c in seed:
  bits|=1<<pos[tuple(sorted((perm[a],perm[b],perm[c])))]
 set_of_sets.add(bits)
assert len(set_of_sets)==840
v=list(sorted(set_of_sets))
print('relabeling orbit count',len(v))
p=10007

def rank_mod(matrix):
 A=matrix.astype(np.int64)%p
 n=A.shape[0]; rank=0
 for j in range(n):
  nz=np.flatnonzero(A[rank:,j])
  if nz.size==0:continue
  k=rank+int(nz[0]);A[[rank,k]]=A[[k,rank]]
  inv=pow(int(A[rank,j]),-1,p)
  A[rank,j:]=(A[rank,j:]*inv)%p
  rows=np.flatnonzero(A[rank+1:,j])+rank+1
  if len(rows):
   vals=A[rows,j].copy()
   A[rows,j:]=(A[rows,j:]-vals[:,None]*A[rank,j:])%p
  rank+=1
  if rank==n:break
 return rank

# Recompute complete row Gram by popcount without a design exact-cover enumeration.
inter=np.empty((840,840),dtype=np.int16)
for i,a in enumerate(v):
 for j in range(i,840):
  inter[i,j]=inter[j,i]=(a&v[j]).bit_count()
for d,want in ((0,1),(1,49),(2,469),(3,840)):
 G=np.zeros_like(inter,dtype=np.int64)
 for k in range(d+1):
  G+=np.array([[comb(int(h),k) for h in row] for row in inter],dtype=np.int64)
 got=rank_mod(G)
 assert got==want,(d,got,want)
 print('degree',d,'rank over 10007',got,'PASS')
print('INDEPENDENT CHECK PASSED')
