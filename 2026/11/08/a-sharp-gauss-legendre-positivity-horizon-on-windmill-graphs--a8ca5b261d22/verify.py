"""Exact rational replay of the windmill [2/2] Pade sign theorem.
No third-party dependencies. Finite checks supplement the analytic proof.
"""
from fractions import Fraction as F
from itertools import product

def matmul(A,B):
 n=len(A);return [[sum((A[i][k]*B[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]

def inverse(A):
 n=len(A);M=[[F(x) for x in A[i]]+[F(int(i==j)) for j in range(n)] for i in range(n)]
 for i in range(n):
  k=next(k for k in range(i,n) if M[k][i]);M[i],M[k]=M[k],M[i]
  d=M[i][i];M[i]=[x/d for x in M[i]]
  for j in range(n):
   if j!=i:
    d=M[j][i]
    if d:M[j]=[a-d*b for a,b in zip(M[j],M[i])]
 return [row[n:] for row in M]

def D(z):return z*z+6*z+12

def g(z):return 12*z/D(z)

def graph(m,r):
 k=r-1;n=1+m*k;L=[[F(0) for j in range(n)] for i in range(n)]
 def edge(i,j):
  L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
 for b in range(m):
  leaves=[1+b*k+s for s in range(k)]
  for i in leaves:edge(0,i)
  for i in range(k):
   for j in range(i+1,k):edge(leaves[i],leaves[j])
 return L

def direct(m,r,h):
 L=graph(m,r);n=len(L);L2=matmul(L,L)
 B=[[h*h*L2[i][j]+6*h*L[i][j]+12*int(i==j) for j in range(n)] for i in range(n)]
 A=[[h*h*L2[i][j]-6*h*L[i][j]+12*int(i==j) for j in range(n)] for i in range(n)]
 return matmul(A,inverse(B))

def quartic_coeff(m,r):
 k=r-1;u=m*k
 A=u*u-u*(k-1)-2*k-1
 B=u*u+3*u+2*r+3
 return [-r*A,6*r*(r+1),12*B,72*(u+2),144]

def q(m,r,h):
 a,b,c,d,e=quartic_coeff(m,r)
 return m*(r-1)*(a*h**4+b*h**3+c*h**2+d*h+e)

def e_direct(m,r,h):
 n=1+m*(r-1)
 return m*r*D(h)*D(n*h)-(m-1)*D(r*h)*D(n*h)-D(r*h)*D(h)

def expected_offdiag(m,r,h,i,j):
 n=1+m*(r-1);k=r-1
 if i==0 or j==0:return g(n*h)/n
 if (i-1)//k!=(j-1)//k:return (n*g(h)-g(n*h))/(m*k*n)
 return (m*n*g(r*h)-(m-1)*n*g(h)-g(n*h))/(m*k*n)

def test():
 cases=0;offdiags=0
 for m,r in product(range(2,5),range(3,6)):
  k=r-1;A=k*m*(k*m-(k-1))-2*k-1
  assert A>=2*k*k-1>0
  for h in [F(1,5),F(1,2),F(1),F(2),F(4),F(10)]:
   assert q(m,r,h)==e_direct(m,r,h)
   T=direct(m,r,h);n=len(T)
   assert all(T[i][i]>0 for i in range(n))
   assert all(sum(row)==1 for row in T)
   for i in range(n):
    for j in range(n):
     if i==j:continue
     x=expected_offdiag(m,r,h,i,j)
     assert T[i][j]==x,(m,r,h,i,j)
     if i==0 or j==0 or (i-1)//k!=(j-1)//k:assert x>0
     else:assert (x>0)-(x<0)==(q(m,r,h)>0)-(q(m,r,h)<0)
     offdiags+=1
   cases+=1
 # One root: Q(0)>0, strictly decreasing Q(h)/h**4 for h>0, limit -A*r<0.
 print('VERIFY_OK',cases,'full rational matrix cases,',offdiags,'offdiagonal identities; quartic signs checked')

if __name__=='__main__':test()
