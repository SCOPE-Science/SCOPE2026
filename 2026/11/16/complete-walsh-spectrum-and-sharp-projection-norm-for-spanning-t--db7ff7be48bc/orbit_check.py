#!/usr/bin/env python3
"""Independent exact signed-Laplacian and symmetry-orbit certificate for K_{4,4}."""
from collections import Counter
from itertools import permutations
import csv,math
from pathlib import Path
N=1<<16

def map_mask(s, p):
 t=0
 while s:
  v=s & -s;s-=v;i=v.bit_length()-1;t |= 1 << p[i]
 return t

def perm_rows(a,b):
 p=list(range(16))
 for j in range(4):p[4*a+j],p[4*b+j]=p[4*b+j],p[4*a+j]
 return p

def perm_cols(a,b):
 p=list(range(16))
 for i in range(4):p[4*i+a],p[4*i+b]=p[4*i+b],p[4*i+a]
 return p
ps=[perm_rows(i,i+1) for i in range(3)]+[perm_cols(i,i+1) for i in range(3)]+[[4*(i%4)+(i//4) for i in range(16)]]

def det_bareiss(A):
 a=[row[:] for row in A];n=len(a);sgn=1;den=1
 for k in range(n-1):
  if a[k][k]==0:
   j=next((i for i in range(k+1,n) if a[i][k]!=0),None)
   if j is None: return 0
   a[k],a[j]=a[j],a[k];sgn=-sgn
  v=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    numerator=a[i][j]*v-a[i][k]*a[k][j]
    assert numerator%den==0
    a[i][j]=numerator//den
   a[i][k]=0
  den=v
 return sgn*a[n-1][n-1]

def signed_tree_sum(s):
 L=[[0]*8 for _ in range(8)]
 for i in range(4):
  for j in range(4):
   w=1-2*((s>>(4*i+j))&1);x,y=i,4+j
   L[x][x]+=w;L[y][y]+=w;L[x][y]-=w;L[y][x]-=w
 return det_bareiss([r[:-1] for r in L[:-1]])

seen=bytearray(N); records=[]; values=[None]*N
for s in range(N):
 if seen[s]:continue
 members=[s];seen[s]=1
 for x in members:
  for p in ps:
   y=map_mask(x,p)
   if not seen[y]:seen[y]=1;members.append(y)
 w=signed_tree_sum(s)
 for x in members:values[x]=w
 records.append((s,len(members),w))
assert sum(x[1] for x in records)==N
assert all(x is not None for x in values)
assert signed_tree_sum(0)==4096
assert all(values[x ^ (N-1)]==-values[x] for x in range(N))
h=Counter()
for s,size,w in records:h[w]+=size
assert sum(h.values())==N
assert len(records)==192
expected={0:42894,32:7008,-32:7008,64:448,-64:448,128:3504,-128:3504,224:16,-224:16,256:96,-256:96,288:144,-288:144,512:72,-512:72,640:32,-640:32,4096:1,-4096:1}
assert h==Counter(expected)
print('orbit_count',len(records),'orbit_hist',dict(Counter(size for _,size,_ in records)))
print('spectral_count',dict(sorted(h.items())))
print('rank',N-h[0],'minabs',min(abs(x) for x in h if x),'gcd',math.gcd(*h))

p=[int(x!=0) for x in values]
for b in range(16):
 t=1<<b
 for i in range(0,N,2*t):
  for j in range(i,i+t):
   u,v=p[j],p[j+t];p[j]=u+v;p[j+t]=u-v
l1_num=sum(abs(x) for x in p);g=math.gcd(l1_num,N)
print('proj_l1',l1_num//g,N//g,'nonzero_projkernel',sum(x!=0 for x in p))
with (Path(__file__).with_name('orbits.csv')).open(newline='') as f:
 rows=list(csv.reader(f))
assert rows[0]==['representative_integer_mask','orbit_size','signed_Walsh_multiplier']
assert [[int(c) for c in row] for row in rows[1:]]==[list(row) for row in records]
print('CERTIFIED_SYMMETRY_ORBIT_DETERMINANTS_PASS')
