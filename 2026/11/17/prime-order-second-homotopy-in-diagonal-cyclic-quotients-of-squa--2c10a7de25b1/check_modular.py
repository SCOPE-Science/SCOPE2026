from itertools import combinations, permutations, product
from math import factorial,comb
from collections import defaultdict

def allfaces(n=5):
 out=[]
 for k in range(1,n+1):
  for r in combinations(range(n),k):
   for c in combinations(range(n),k):
    for pc in permutations(c):
     out.append(sum(1<<(n*i+j) for i,j in zip(r,pc)))
 return out

p=5
faces=allfaces(p)
rotbit=[1<<(p*((i+1)%p)+(j+1)%p) for i in range(p) for j in range(p)]
rotmask={0:0}
def rot(m):
 if m not in rotmask:
  v=m;out=0
  while v:
   b=v&-v; out|=rotbit[b.bit_length()-1];v-=b
  rotmask[m]=out
 return rotmask[m]
canon_cache={}
def canon(chain):
 if chain in canon_cache:return canon_cache[chain]
 cur=chain; best=chain
 for _ in range(4):
  cur=tuple(rot(x) for x in cur)
  if cur<best:best=cur
 canon_cache[chain]=best
 return best

def flags(face, length):
 v=[];m=face
 while m:
  b=m&-m;v.append(b);m-=b
 s=len(v)
 if s<length:return
 for blocks in product(range(length),repeat=s):
  if len(set(blocks))!=length:continue
  bins=[0]*length
  for i,bb in enumerate(blocks):bins[bb] |=v[i]
  f=[]; acc=0
  for b in bins:
   acc|=b;f.append(acc)
  yield tuple(f)

orbits=[{} for _ in range(4)]
for face in faces:
 s=face.bit_count()
 for d in range(min(s,4)):
  dst=orbits[d]
  for ch in flags(face,d+1):
   can=canon(ch)
   if can not in dst:dst[can]=len(dst)
assert [len(x) for x in orbits] == [313,3200,8640,8640]
print('quotient barycentric chain counts', [len(x) for x in orbits],flush=True)

# d0 augmented not needed. Simplicial flag boundary with canonicalized faces.
def boundaries(d):
 rows=orbits[d-1]; cols=orbits[d]
 result=[]
 for ch in cols:
  v=defaultdict(int)
  for k in range(d+1):
   key=canon(ch[:k]+ch[k+1:])
   v[rows[key]] += (-1)**k
  result.append({k:x for k,x in v.items() if x})
 return result

bds=[None]
for d in range(1,4):
 bds.append(boundaries(d))
 print('boundary',d,'columns',len(bds[d]),flush=True)

# Verify the integer chain condition, without reducing coefficients modulo p.
for dim in (2,3):
 for col in bds[dim]:
  accum=defaultdict(int)
  for mid,coef in col.items():
   for low,val in bds[dim-1][mid].items():accum[low]+=coef*val
  assert all(v==0 for v in accum.values())
print('integral chain compositions vanish',flush=True)

def rank_sparse(columns,p):
 basis={}; z=0
 for col in columns:
  w={r:v%p for r,v in col.items() if v%p}
  while w:
   m=max(w)
   if m not in basis:
    inv=pow(w[m],-1,p)
    basis[m]={r:(c*inv)%p for r,c in w.items()}
    break
   f=w[m];pivot=basis[m]
   for r,c in pivot.items():
    v=(w.get(r,0)-f*c)%p
    if v:w[r]=v
    elif r in w:del w[r]
  else:z+=1
 print('rank',p,len(basis),'zero',z,flush=True)
 return len(basis)
for k in (2,3,5):
 ranks=[0]+[rank_sparse(bds[d],k) for d in range(1,4)]
 h1=len(orbits[1])-ranks[1]-ranks[2]
 h2=len(orbits[2])-ranks[2]-ranks[3]
 assert h1==0 and h2=={2:0,3:1,5:4}[k]
 print('field',k,'ranks',ranks, 'h1',h1,'h2',h2, flush=True)
print('MODULAR_QUOTIENT_H2_PASS',flush=True)
