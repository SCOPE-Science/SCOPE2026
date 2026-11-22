#!/usr/bin/env python3
"""Exact combinatorial/integer verification of the Burkhardt node-plane graph."""
from collections import Counter, deque
from itertools import combinations, permutations

I=tuple(range(6))
pa=list(combinations(I,2))  # points [1:-1:0:0:0:0]
# [1:1:omega:omega:omega^2:omega^2], modulo overall multiplication by omega
cs=sorted({min(tuple((v+t)%3 for v in a) for t in range(3))
           for a in set(permutations((0,0,1,1,2,2)))})
planes=[(triple,s) for triple in combinations(I,3) for s in (1,2)]
assert (len(pa),len(cs),len(planes))==(15,30,40)
points=[('a',a) for a in pa]+[('b',c) for c in cs]

def incidence(P,T):
 typ,data=P
 (i,j,k),s=T
 if typ=='a':return int(not set((i,j,k)).intersection(data))
 c=data
 return int((c[j]-c[i])%3==s and (c[k]-c[i])%3==(2*s)%3)

B=[[incidence(P,T) for T in planes] for P in points]
assert all(sum(row)==8 for row in B)
assert all(sum(B[i][j] for i in range(45))==9 for j in range(40))

# Independent geometric construction, via the split Eisenstein algebra in F_7:
# omega maps to 2, omega^2 to 4; no accidental incidence identifications.
def norm(x):
 x=tuple(z%7 for z in x)
 v=next(t for t in x if t)
 return tuple(t*pow(v,-1,7)%7 for t in x)
coords=[norm(tuple(1 if k==a else -1 if k==b else 0 for k in I)) for a,b in pa]
coords += [norm(tuple(pow(2,c,7) for c in a)) for a in cs]
assert len(set(coords))==45
for i,P in enumerate(points):
 for j,(tr,s) in enumerate(planes):
  x=coords[i];a,b,c=tr; w=pow(2,s,7)
  alt=int((x[b]-w*x[a])%7==0 and (x[c]-w*w*x[a])%7==0)
  assert alt==B[i][j],(i,j)

# Gram identity and graph connectivity.
G=[[sum(B[i][k]*B[j][k] for k in range(40)) for j in range(45)] for i in range(45)]
assert all(sum(r)==72 for r in G)
for i in range(45):
 for j in range(45):
  assert sum(G[i][k]*G[k][j] for k in range(45))==12*G[i][j]+96
N=85;L=[[0]*N for _ in range(N)]
for i in range(45):
 for j in range(40):
  if B[i][j]:
   z=45+j
   L[i][i]+=1;L[z][z]+=1;L[i][z]-=1;L[z][i]-=1
assert sum(L[i][i] for i in range(N))==720
seen={0};q=deque([0])
while q:
 v=q.popleft()
 for j in range(N):
  if L[v][j]<0 and j not in seen:seen.add(j);q.append(j)
assert len(seen)==85

# Because G has eigenvalues 72^1,12^24,0^20, the Laplacian has
# eigenvalues 0^1,17^1,5^24,12^24,8^20,9^15. Matrix-tree:
# tau=17*5^24*12^24*8^20*9^15/85=2^108*3^54*5^23.
expected_total={2:108,3:54,5:23}

def smith_p(M,p,k):
 """Smith p-valuations by invertible row/column operations over Z/p^k."""
 n=len(M); mod=p**k
 A=[[int(x)%mod for x in row] for row in M]
 out=[]
 def v_p(x):
  if x==0:return k
  v=0
  while x%p==0:x//=p;v+=1
  return v
 for r in range(n):
  v=k;ii=jj=None
  for i in range(r,n):
   for j in range(r,n):
    w=v_p(A[i][j])
    if w<v:v=w;ii=i;jj=j
    if v==0:break
   if v==0:break
  assert ii is not None, ('modulus insufficient',p,k,r)
  A[r],A[ii]=A[ii],A[r]
  for row in A:row[r],row[jj]=row[jj],row[r]
  u=A[r][r]//(p**v)
  mred=mod//(p**v)
  inv=pow(u,-1,mred)
  for i in range(r+1,n):
   if A[i][r]:
    h=(A[i][r]//(p**v)*inv)%mred
    for j in range(r,n):A[i][j]=(A[i][j]-h*A[r][j])%mod
    assert A[i][r]==0
  for j in range(r+1,n):
   if A[r][j]:
    h=(A[r][j]//(p**v)*inv)%mred
    for i in range(r,n):A[i][j]=(A[i][j]-h*A[i][r])%mod
    assert A[r][j]==0
  out.append(v)
 return sorted(out)

expected={2:Counter({0:40,1:14,2:10,3:6,4:14}),
          3:Counter({0:55,1:14,2:5,3:10}),
          5:Counter({0:61,1:23})}
from math import prod
for sink in (0,84):
 A=[[L[i][j] for j in range(N) if j!=sink] for i in range(N) if i!=sink]
 val={p:smith_p(A,p,12) for p in (2,3,5)}
 for p,lv in val.items():
  assert Counter(lv)==expected[p],(p,sink,Counter(lv))
  assert sum(lv)==expected_total[p]
  assert max(lv)<12
 factors=[prod(p**val[p][i] for p in (2,3,5)) for i in range(84)]
 assert Counter(factors)==Counter({1:40,2:14,4:1,12:6,60:3,120:5,360:1,720:4,2160:10})
 assert all(b%a==0 for a,b in zip(factors,factors[1:]))
 print('sink',sink,'nonunit invariant factors',sorted((k,v) for k,v in Counter(factors).items() if k!=1))
print('spanning-tree prime factorization: 2^108 * 3^54 * 5^23')
print('BURKHARDT_85_CRITICAL_GROUP_VERIFIED_OK')
