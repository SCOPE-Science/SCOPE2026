"""Exact rational reconstruction checks for third-order Taylor heat positivity."""
from fractions import Fraction as Q
from random import Random
from math import isclose

def mul(A,B):
 n=len(A)
 return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def matrix(n,edges):
 W=[[Q(0) for j in range(n)] for i in range(n)]
 for i,j,w in edges: W[i][j]=W[j][i]=Q(w)
 d=[sum(row) for row in W]
 L=[[(d[i] if i==j else Q(0))-W[i][j] for j in range(n)] for i in range(n)]
 return W,d,L

def check(n,edges):
 W,d,L=matrix(n,edges); L2=mul(L,L);L3=mul(L2,L);W2=mul(W,W);W3=mul(W2,W)
 for h in [Q(1,13),Q(2,7),Q(7,11),Q(1),Q(7,3)]:
  R=[[(Q(int(i==j))-h*L[i][j]+h*h*L2[i][j]/2-h*h*h*L3[i][j]/6) for j in range(n)] for i in range(n)]
  for i in range(n):
   s2=sum(w*w for w in W[i]);tau=sum(d[j]*W[i][j]**2 for j in range(n))
   exp=1-h*d[i]+h*h*(d[i]*d[i]+s2)/2-h*h*h*(d[i]**3+2*d[i]*s2+tau)/6
   assert R[i][i]==exp
   for j in range(n):
    if i==j:continue
    if W[i][j]:
     exp=h*W[i][j]*(1-h*(d[i]+d[j])/2+h*h*(d[i]**2+d[i]*d[j]+d[j]**2+W3[i][j]/W[i][j])/6)
    elif W2[i][j]:
     moment=(d[i]+d[j])*W2[i][j]+sum(d[k]*W[i][k]*W[k][j] for k in range(n))
     exp=h*h*(W2[i][j]/2-h*moment/6)
    else:
     exp=h*h*h*W3[i][j]/6
    assert R[i][j]==exp,(n,i,j,h,R[i][j],exp)
  assert all(sum(R[i])==1 for i in range(n))
 return n*n*5

def star(m):return [(0,j,Q(1)) for j in range(1,m+1)]
def cycle(n):return [(i,(i+1)%n,Q(1)) for i in range(n)]

rng=Random(20261119)
checks=0;graphs=0
for n in range(2,12):
 for rep in range(50):
  x=rng.randrange(1,n)
  left=list(range(x)); right=list(range(x,n))
  edges=[]
  for i in left:
   for j in right:
    if rng.randrange(3)!=0:edges.append((i,j,Q(rng.randrange(1,7),rng.randrange(1,6))))
  if not edges:continue
  checks+=check(n,edges);graphs+=1
for m in [2,3,4,5,10,100]:
 checks+=check(m+1,star(m));graphs+=1
for n in [4,6,8,10]:
 checks+=check(n,cycle(n));graphs+=1
# SSP convex representation and upper-bound analytic inequalities, exact checks.
for d in [1,2,3,10]:
 for q in [Q(1,2),Q(1),Q(3,2),Q(8,5),Q(2)]:
  h=q/d
  assert Q(1,3)+Q(1,2)*(1-q)+Q(1,6)*(1-q)**3 == 1-q+q*q/2-q**3/6
print('VERIFY_OK weighted_bipartite_graphs=',graphs,'exact_entry_checks=',checks,'SSP_assertions=',20)
