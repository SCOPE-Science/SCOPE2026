#!/usr/bin/env python3
"""Full canonical-point and dual-line enumeration for the rational BKS sextic over F125."""
from collections import Counter
p=5;Q=125;n=3
D=[tuple((a//(5**i))%5 for i in range(n)) for a in range(Q)]
def pack(v):return sum((t%5)*5**i for i,t in enumerate(v))
A=[[pack([D[a][i]+D[b][i] for i in range(n)]) for b in range(Q)] for a in range(Q)]
N=[pack([-t for t in d]) for d in D]
def mul(a,b):
 z=[0]*5
 for i,ai in enumerate(D[a]):
  for j,bj in enumerate(D[b]):z[i+j]+=ai*bj
 # t^3=-t-1
 for d in [4,3]:
  c=z[d];z[d]=0;z[d-2]-=c;z[d-3]-=c
 return pack(z[:3])
M=[[mul(a,b) for b in range(Q)] for a in range(Q)]
def add(a,b):return A[a][b]
def sub(a,b):return A[a][N[b]]
def powf(a,n):
 r=1
 while n:
  if n&1:r=M[r][a]
  a=M[a][a];n//=2
 return r
assert all(powf(a,124)==1 for a in range(1,Q))
P=[(1,a,b) for a in range(Q) for b in range(Q)]+[(0,1,b) for b in range(Q)]+[(0,0,1)]
def ev(v):
 x,y,z=v
 return add(sub(powf(y,6),add(M[powf(x,5)][z],M[x][powf(z,5)])),powf(sub(M[y][y],M[2][M[x][z]]),3))
def dot(l,v):return add(add(M[l[0]][v[0]],M[l[1]][v[1]]),M[l[2]][v[2]])==0
E=set(v for v in P if ev(v)==0)
assert len(E)==136
chars=Counter();sext=[]
for l in P:
 k=sum(dot(l,v) for v in E)
 chars[k]+=1
 if k==6:sext.append(l)
assert chars=={0:5940,1:3606,2:5460,3:610,4:15,6:120}
assert len(sext)==120
assert sum(n*v for n,v in chars.items())==len(E)*126
assert sum(n*(n-1)//2*v for n,v in chars.items())==len(E)*(len(E)-1)//2
c=Counter()
for l in sext:
 for v in P:
  if dot(l,v):c[v]+=1
assert Counter(c[v] for v in P)=={0:6571,1:3720,2:5340,6:120}
assert Counter(c[v] for v in P if v not in E)=={0:6555,1:3720,2:5340}
assert Counter(c[v] for v in E)=={0:16,6:120}
assert {v for v in E if c[v]==0}=={v for v in E if all(powf(x,5)==x for x in v)}
print('BKS125_FULL_CANONICAL_ENUMERATION_PASS',len(P),len(E),len(sext))
print('BKS125_LINE_CHARACTERS_PASS',sorted(chars.items()))
print('BKS125_POINT_SPECTRUM_PASS',[(n,v) for n,v in sorted(Counter(c[x] for x in P).items())])
