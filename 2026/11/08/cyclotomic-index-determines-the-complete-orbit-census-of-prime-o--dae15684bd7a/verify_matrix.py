"""Exact independent rank checks of adjacency-Jordan and fixed counts over prime fields."""
from math import gcd

def rank(mat,p):
 a=[row[:] for row in mat]; nr=len(a); nc=len(a[0]); piv=0
 for col in range(nc):
  pivot=next((i for i in range(piv,nr) if a[i][col]%p),None)
  if pivot is None: continue
  a[piv],a[pivot]=a[pivot],a[piv]
  inv=pow(a[piv][col],-1,p)
  for j in range(col,nc):a[piv][j]=a[piv][j]*inv%p
  for i in range(piv+1,nr):
   mul=a[i][col]
   if mul:
    for j in range(col,nc):a[i][j]=(a[i][j]-mul*a[piv][j])%p
  piv+=1
  if piv==nr:break
 return piv

def mult(a,b,p):
 n=len(a)
 return [[sum(a[i][t]*b[t][j] for t in range(n))%p for j in range(n)] for i in range(n)]

def run(p):
 for k in range(3,p):
  if (p-1)%k:continue
  d=(p-1)//k
  if d%2:continue
  residues={pow(a,k,p) for a in range(1,p)}
  assert len(residues)==d and {(-a)%p for a in residues}==residues
  a=[[int(((j-i)%p) in residues) for j in range(p)] for i in range(p)]
  nil=[[ (a[i][j]-(d if i==j else 0))%p for j in range(p)] for i in range(p)]
  m=[[int(i==j) for j in range(p)] for i in range(p)]
  got=[]
  for t in range(1,k+2):
   m=mult(m,nil,p)
   r=rank(m,p)
   want=max(k+1-t,0)+(d-1)*max(k-t,0)
   assert r==want,(p,k,d,t,r,want)
   got.append(r)
  ell=next(i for i in range(1,p) if pow(d,i,p)==1)
  apow=[[int(i==j) for j in range(p)] for i in range(p)]
  def matpow(a,e):
   r=[[int(i==j) for j in range(p)] for i in range(p)]
   while e:
    if e%2:r=mult(r,a,p)
    a=mult(a,a,p);e//=2
   return r
  for t in {1,ell,2*ell,p*ell}:
   at=matpow(a,t)
   at=[[ (at[i][j]-(i==j))%p for j in range(p)] for i in range(p)]
   ker=p-rank(at,p)
   want=(p if t%(p*ell)==0 else (d if t%ell==0 else 0))
   assert ker==want,(p,k,t,ker,want)
  print('PASS',p,k,d,ell,got)
for p in [7,13,19,31,37,43]:run(p)
