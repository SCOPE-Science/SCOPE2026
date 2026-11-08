#!/usr/bin/env python3
"""Independent finite signed chain checks for subdivided multitheta complexes."""
from itertools import permutations
from collections import defaultdict

def graph(p):
 n=2+2*p
 e=set()
 for i in range(p):
  x=2+2*i;y=x+1
  for a,b in ((0,x),(x,y),(y,1)):
   e.add((min(a,b),max(a,b)))
 return n,e

def faces(p):
 n, edges=graph(p)
 by_degree=defaultdict(list)
 for mask in range(1,1<<n):
  if any(mask&(1<<i) and mask&(1<<j) for i,j in edges): continue
  face=tuple(i for i in range(n) if mask>>i&1)
  by_degree[len(face)-1].append(face)
 return by_degree

def sign_of_perm(a):
 cnt=0
 for i in range(len(a)):
  for j in range(i+1,len(a)):
   if a[i]>a[j]:cnt+=1
 return -1 if cnt&1 else 1

def action(p,arm_perm=None,pole=False):
 if arm_perm is None: arm_perm=list(range(p))
 perm=[1,0] if pole else [0,1]
 for j in range(p):
  k=arm_perm[j]
  perm.extend([2+2*k+(1 if pole else 0),2+2*k+(0 if pole else 1)])
 return perm

def lefschetz(p,faces,perm):
 val=0
 for d,fs in faces.items():
  sg=(-1)**d
  for face in fs:
   tr=[perm[i] for i in face]
   if sorted(tr)==list(face):val+=sg*sign_of_perm(tr)
 return val

def expected(p,ap,flip):
 s=sign_of_perm(ap)
 top=s*((-1)**p if flip else 1)
 low=(-1 if flip else 1)
 return 1-low+((-1)**(p-1))*top

def rank_mod2(columns):
 pivots={}
 for c in columns:
  while c:
   h=c.bit_length()-1
   if h in pivots:c^=pivots[h]
   else:
    pivots[h]=c;break
 return len(pivots)

def homology_mod2(d):
 ranks={}
 for k in range(1,max(d)+1):
  dlow=d[k-1]; row={f:i for i,f in enumerate(dlow)}
  cols=[]
  for face in d[k]:
   v=0
   for j in range(len(face)):
    v^=1<<row[face[:j]+face[j+1:]]
   cols.append(v)
  ranks[k]=rank_mod2(cols)
 return [len(d[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in range(max(d)+1)]

def test(p):
 f=faces(p)
 ident=list(range(p)); trans=ident.copy();trans[0],trans[1]=trans[1],trans[0]
 cyc=ident[1:]+ident[:1]
 rev=list(reversed(ident))
 permset=(list(permutations(ident)) if p<=6 else [ident,trans,cyc,rev])
 for perm in permset:
  for flip in (False,True):
   observed=lefschetz(p,f,action(p,perm,flip))
   want=expected(p,perm,flip)
   assert observed==want,(p,perm,flip,observed,want)
 betti=None
 if p<=5:
  betti=homology_mod2(f)
  expect=[0]*len(betti);expect[0]=1;expect[1]=1;expect[p-1]=1
  assert betti==expect,(p,betti,expect)
 print('p=%d vertices=%d faces=%d fvector=%s mod2_ordinary=%s signed_actions=%d PASS' %(p,2*p+2,sum(len(v) for v in f.values()),[len(f[i]) for i in range(max(f)+1)],betti,2*len(permset)))

if __name__=='__main__':
 for p in range(3,8):test(p)
 print('ALL_VERIFY_OK')
