#!/usr/bin/env python3
"""Finite-field check of the full p-toral derivation classification of NF_n.

Uses standard Python only; verifies original Leibniz derivation identities and
D^p=D, including exhaustive arbitrary-endomorphism sweeps in small cases.
"""
from itertools import product

class FField:
 def __init__(self,q):
  assert q in (2,3,4,5)
  self.q=q;self.p=2 if q==4 else q
 def add(self,x,y):return (x^y) if self.q==4 else (x+y)%self.q
 def sub(self,x,y):return self.add(x,self.neg(y))
 def neg(self,x):return x if self.q==4 else (-x)%self.q
 def mul(self,x,y):
  if self.q!=4:return x*y%self.q
  z=0
  for j in range(2):
   if y>>j&1:z^=x<<j
  if z&4:z^=7 # t^2+t+1
  return z
 def pow(self,x,r):
  y=1
  while r:
   if r&1:y=self.mul(y,x)
   x=self.mul(x,x);r//=2
  return y
 def summation(self,terms):
  out=0
  for t in terms:out=self.add(out,t)
  return out

def ident(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def zero(n):return [[0 for _ in range(n)] for _ in range(n)]
def matmul(A,B,F):
 n=len(A);return [[F.summation(F.mul(A[i][k],B[k][j]) for k in range(n)) for j in range(n)] for i in range(n)]
def matpow(A,k,F):
 o=ident(len(A))
 while k:
  if k&1:o=matmul(o,A,F)
  A=matmul(A,A,F);k//=2
 return o
def matsub(A,B,F):return [[F.sub(x,y) for x,y in zip(rowa,rowb)] for rowa,rowb in zip(A,B)]
def diagH(n,F):return [[(i+1)%F.p if i==j else 0 for j in range(n)] for i in range(n)]
def D_from_a(a,F):
 n=len(a);return [[F.mul(a[0],(i+1)%F.p) if i==j else (a[i-j] if i>j else 0) for j in range(n)] for i in range(n)]
def is_derivation(M,F):
 n=len(M)
 for i in range(n):
  for j in range(n):
   lhs=[M[k][i+1] if j==0 and i<n-1 else 0 for k in range(n)]
   rhs=[0]*n
   if j==0:
    for k in range(1,n):rhs[k]=M[k-1][i]
   if i<n-1:rhs[i+1]=F.add(rhs[i+1],M[0][j])
   if lhs!=rhs:return False
 return True
def rank(A,F):
 M=[list(row) for row in A];n=len(M);r=0
 for j in range(n):
  sel=next((k for k in range(r,n) if M[k][j]),None)
  if sel is None:continue
  M[r],M[sel]=M[sel],M[r];inv=F.pow(M[r][j],F.q-2)
  M[r]=[F.mul(inv,x) for x in M[r]]
  for k in range(n):
   if k==r or not M[k][j]:continue
   a=M[k][j]; M[k]=[F.sub(x,F.mul(a,y)) for x,y in zip(M[k],M[r])]
  r+=1
 return r

def aut_from_generator(v,F):
 n=len(v);c=v[0];M=zero(n);col=list(v)
 for j in range(n):
  for i in range(n):M[i][j]=col[i]
  col=[0]+[F.mul(c,x) for x in col[:-1]]
 return M

def projected_generator(D,c,F):
 # D^p=D: spectral projector onto eigenvalue c in F_p is I-(D-cI)^(p-1).
 n=len(D); B=matsub(D,[[c if i==j else 0 for j in range(n)] for i in range(n)],F)
 P=matsub(ident(n),matpow(B,F.p-1,F),F)
 return [P[i][0] for i in range(n)]

def enumerate_params(q,n):
 F=FField(q);accepted=[]
 for a in product(range(q),repeat=n):
  D=D_from_a(a,F)
  assert is_derivation(D,F)
  if matpow(D,F.p,F)!=D:continue
  if a[0]==0:
   assert a==(0,)*n
   accepted.append((a[0],0));continue
  assert 1<=a[0]<F.p
  v=projected_generator(D,a[0],F)
  assert v[0]==1
  g=aut_from_generator(v,F)
  cH=[[F.mul(a[0],x) for x in row] for row in diagH(n,F)]
  assert matmul(D,g,F)==matmul(g,cH,F),('conjugacy',q,n,a)
  assert rank(D,F)==n-n//F.p
  accepted.append((a[0],rank(D,F)))
 m=1+(n-1)//F.p
 expected=1+(F.p-1)*q**(n-m)
 assert len(accepted)==expected,(q,n,len(accepted),expected)
 assert sorted(set(accepted))==[(0,0)]+[(c,n-n//F.p) for c in range(1,F.p)]
 return len(accepted), {c:sum(t[0]==c for t in accepted) for c in range(F.p)}

def unrestricted(q,n):
 F=FField(q);d=0;good=0
 for entries in product(range(q),repeat=n*n):
  D=[list(entries[i*n:(i+1)*n]) for i in range(n)]
  if not is_derivation(D,F):continue
  d+=1
  assert D==D_from_a([D[i][0] for i in range(n)],F)
  if matpow(D,F.p,F)==D:good+=1
 m=1+(n-1)//F.p
 expected=1+(F.p-1)*q**(n-m)
 assert d==q**n and good==expected,(q,n,d,good,expected)
 return d,good

if __name__=='__main__':
 for q,n in [(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,2),(3,3),(3,4),(3,5),(4,2),(4,3),(4,4),(4,5),(5,2),(5,3),(5,4)]:
  total,by_c=enumerate_params(q,n)
  print('PARAMETER_ENUM',f'q={q}',f'n={n}',f'p={FField(q).p}',f'total={total}',f'by_quotient_eigenvalue={by_c}')
 for q,n in [(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)]:
  d,good=unrestricted(q,n)
  print('UNRESTRICTED_ENDOMORPHISMS',f'q={q}',f'n={n}',f'derivations={d}',f'p_toral={good}')
 print('NULL_FILIFORM_P_TORAL_DERIVATIONS_PASS')
