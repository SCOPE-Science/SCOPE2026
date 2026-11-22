#!/usr/bin/env python3
"""Exact, dependency-free verifier for the double Kummer pencil graph claim.

All calculations use Python's arbitrary-precision integer arithmetic.
No external data, network, or previous computation is required.
"""
from itertools import product
from math import prod

PERMS={"I":(0,1,2,3),"T":(0,2,1,3),"C":(0,2,3,1)}
EXPECTED={
 ("I","I"):(2,2,2,2,8,8,8,8,32),
 ("I","T"):(2,2,8,8,8,32),
 ("I","C"):(8,8,32),
 ("T","I"):(2,2,8,8,8,32),
 ("T","T"):(2,2,8,8,32),
 ("T","C"):(8,32),
 ("C","I"):(8,8,32),
 ("C","T"):(8,32),
 ("C","C"):(2,2,32),
}
VERTS=[('H',i) for i in range(4)]+[('V',j) for j in range(4)]+[('E',i,j) for i,j in product(range(4),repeat=2)]
INDEX={v:i for i,v in enumerate(VERTS)}
ROOT=('E',0,0)
OTHERS=[v for v in VERTS if v!=ROOT]
EDGES=[(INDEX['H',i],INDEX['E',i,j]) for i,j in product(range(4),repeat=2)] + [(INDEX['V',j],INDEX['E',i,j]) for i,j in product(range(4),repeat=2)]
L=[[0]*24 for _ in range(24)]
for u,v in EDGES:
 L[u][u]+=1; L[v][v]+=1; L[u][v]-=1; L[v][u]-=1
R=[[L[INDEX[u]][INDEX[v]] for v in OTHERS] for u in OTHERS]
assert len(VERTS)==24 and len(EDGES)==32
assert sum(L[i][i] for i in range(24))==64

def f(v,a,b):
 p,q=PERMS[a],PERMS[b]
 if v[0]=='H':return ('H',p[v[1]])
 if v[0]=='V':return ('V',q[v[1]])
 return ('E',p[v[1]],q[v[2]])

def orbit_matrix(a,b):
 seen=set(); orbits=[]
 for v in OTHERS:
  if v in seen:continue
  orbit=[];w=v
  while w not in seen:
   seen.add(w);orbit.append(w);w=f(w,a,b)
  assert w==v
  orbits.append(orbit)
 pos={v:i for i,o in enumerate(orbits) for v in o}
 M=[[0]*len(orbits) for _ in orbits]
 for j,orb in enumerate(orbits):
  v=orb[0];col=OTHERS.index(v)
  for row,u in enumerate(OTHERS):M[pos[u]][j]+=R[row][col]
 # Verify orbit-summed columns agree over every member of each orbit.
 for j,orb in enumerate(orbits):
  for v in orb:
   col=OTHERS.index(v)
   for k,oo in enumerate(orbits):
    assert M[k][j]==sum(R[OTHERS.index(u)][col] for u in oo)
 return M,len(orbits)

def relation_matrix(a,b):
 """Independent unreduced-by-orbits presentation [R | P-I]."""
 N=len(OTHERS)
 M=[row[:] + [0]*N for row in R]
 for j,v in enumerate(OTHERS):
  i=OTHERS.index(f(v,a,b))
  M[i][N+j]+=1
  M[j][N+j]-=1
 return M

def det_bareiss(A):
 """Exact fraction-free elimination (no symbolic algebra)."""
 n=len(A); B=[r[:] for r in A];sgn=1;last=1
 for k in range(n-1):
  if B[k][k]==0:
   i=next((i for i in range(k+1,n) if B[i][k]),None)
   if i is None:return 0
   B[k],B[i]=B[i],B[k];sgn=-sgn
  pivot=B[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    val=B[i][j]*pivot-B[i][k]*B[k][j]
    assert val%last==0
    B[i][j]=val//last
   B[i][k]=0
  last=pivot
 return sgn*B[-1][-1]

def v2(x,B):
 if not x:return B
 return (x & -x).bit_length()-1

def local_2_smith(A,bits=32):
 """Unimodular row/column operations over Z/2^bits (rectangular OK)."""
 rows=len(A);cols=len(A[0]);q=1<<bits
 X=[[v%q for v in row] for row in A];ans=[]
 for k in range(min(rows,cols)):
  options=[(v2(X[i][j],bits),i,j) for i in range(k,rows) for j in range(k,cols) if X[i][j]]
  if not options:
   ans.extend([bits]*(rows-k));break
  e,i,j=min(options)
  assert e<bits
  X[k],X[i]=X[i],X[k]
  for row in X:row[k],row[j]=row[j],row[k]
  d=1<<e;u=X[k][k]//d;mod=q//d
  assert u%2
  inv=pow(u,-1,mod)
  for r in range(k+1,rows):
   x=X[r][k]
   if x:
    assert x%d==0
    t=(x//d)*inv%mod
    X[r]=[(v-t*w)%q for v,w in zip(X[r],X[k])]
  for j in range(k+1,cols):
   x=X[k][j]
   if x:
    assert x%d==0
    t=(x//d)*inv%mod
    for r in range(rows):X[r][j]=(X[r][j]-t*X[r][k])%q
  assert all(X[r][k]==0 for r in range(k+1,rows))
  assert all(X[k][j]==0 for j in range(k+1,cols))
  ans.append(e)
 return tuple(sorted(ans))

def nonunit_powers(exponents):return tuple(1<<v for v in exponents if v>0)

def full_group_relation_matrix():
    """Coinvariants under independent GL_2(F2)=S3 on the two factors."""
    N=len(OTHERS)
    B=[row[:] for row in R]
    for a,b in [("T","I"),("C","I"),("I","T"),("I","C")]:
        M=relation_matrix(a,b)
        for i in range(N):B[i].extend(M[i][N:])
    return B

def run():
 print('24 vertices, 32 transverse nodes, genus 9')
 for a,b in product(PERMS, repeat=2):
  M,r=orbit_matrix(a,b)
  determinant=abs(det_bareiss(M))
  ev=local_2_smith(M)
  group=nonunit_powers(ev)
  ev_ind=local_2_smith(relation_matrix(a,b))
  group_ind=nonunit_powers(ev_ind)
  assert group==EXPECTED[a,b],(a,b,group)
  assert group_ind==group,(a,b,group_ind,group)
  assert determinant==prod(group)
  assert determinant&(determinant-1)==0
  print(a+b,'orbits_nonroot=',r,'order=',determinant,'group=',group,'independent_presentation=OK')
 assert abs(det_bareiss(R))==2**21==2**9*4**6
 # An invariant divisor supported on the three rational components.
 # For the standard basis e_H0 in Div^0, the unique solution R x=e_H0
 # has 32x integral and its H0-coordinate is 23/32.
 x=[0]*len(OTHERS)
 for i,v in enumerate(OTHERS):
  if v[0]=='H':x[i]=23 if v[1]==0 else 15
  elif v[0]=='V':x[i]=9 if v[1]==0 else 17
  elif v[0]=='E' and v[1]==0:x[i]=20
  elif v[0]=='E' and v[2]==0:x[i]=12
  else:x[i]=16
 h=OTHERS.index(('H',0))
 assert all(sum(R[i][j]*x[j] for j in range(23))==(32 if i==h else 0) for i in range(23))
 assert x[h]==23
 # It is fixed by each S3 x S3 action since H0 and E00 are fixed.
 assert all(f(('H',0),a,b)==('H',0) and f(ROOT,a,b)==ROOT for a,b in product(PERMS,repeat=2))
 # Hence [H0-E00] has exact order 32 in every fixed subgroup.
 assert nonunit_powers(local_2_smith(full_group_relation_matrix()))==(32,)
 print('FULL_S3xS3_FIXED_GROUP_C32_OK')
 print('UNIVERSAL_FIXED_C32_OK')
 print('DOUBLE_KUMMER_PENCIL_FROBENIUS_NINE_GROUPS_OK')

if __name__=='__main__':run()
