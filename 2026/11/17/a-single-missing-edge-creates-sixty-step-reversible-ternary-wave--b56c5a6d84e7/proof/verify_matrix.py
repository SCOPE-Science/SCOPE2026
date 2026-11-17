#!/usr/bin/env python3
"""Exact matrix-rank tests for reversible ternary waves on an edge-deleted complete graph."""

def ident(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def mul(A,B):
 n=len(A); k=len(B);m=len(B[0]);return [[sum(A[i][h]*B[h][j] for h in range(k))%3 for j in range(m)]for i in range(n)]
def rank(A):
 a=[[v%3 for v in row]for row in A];rows=len(a);cols=len(a[0]);r=0
 for j in range(cols):
  pivot=next((i for i in range(r,rows) if a[i][j]),None)
  if pivot is None:continue
  a[pivot],a[r]=a[r],a[pivot];inv=pow(a[r][j],-1,3);a[r]=[(v*inv)%3 for v in a[r]]
  for i in range(rows):
   if i!=r and a[i][j]:
    c=a[i][j];a[i]=[(x-c*y)%3 for x,y in zip(a[i],a[r])]
  r+=1
 return r

def wave(n):
 T=[[0]*(2*n)for _ in range(2*n)]
 for i in range(n):
  for j in range(n):
   if i!=j and not(i<2 and j<2):T[i][j]=1
  T[i][n+i]=2;T[n+i][i]=1
 return T

def three_power(t):
 z=1
 while t%3==0:t//=3;z*=3
 return z

def predicted_dim(n,t):
 if n%3==0:return (n-3)*(1+int(t%3==0))+2*int(t%4==0)+4*int(t%8==0)
 if n%3==1:return (n-3)*(1+int(t%3==0))+2*int(t%4==0)+4*int(t%10==0)
 z=three_power(t)
 return 4*int(t%4==0)+min(4,z)+(n-4)*min(2,z)

def predicted_order(n):return (8 if n==3 else 24) if n%3==0 else (60 if n%3==1 else 36)

def main():
 checked=0
 for n in range(3,19):
  T=wave(n);I=ident(2*n);P=I;L=predicted_order(n);first=None
  for t in range(1,L+1):
   P=mul(P,T)
   N=[[int((P[i][j]-I[i][j])%3)for j in range(2*n)]for i in range(2*n)]
   actual=2*n-rank(N);expected=predicted_dim(n,t)
   assert actual==expected,(n,t,actual,expected)
   checked+=1
   if P==I and first is None:first=t
  assert first==L,(n,first,L)
  assert predicted_dim(n,L)==2*n
  print('n=%2d order=%2d fixed_dim_t1=%2d fixed_dim_full=%2d'%(n,L,predicted_dim(n,1),predicted_dim(n,L)))
 print('PASS: exact matrix powers/nullities matched %d tests; all sharp orders verified'%checked)
if __name__=='__main__':main()
