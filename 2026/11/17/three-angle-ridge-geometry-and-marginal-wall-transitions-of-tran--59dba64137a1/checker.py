#!/usr/bin/env python3
"""Finite LP spot check of facet-pair ridge criteria and intrinsic normal Gram values."""
import itertools
import numpy as np
from scipy.optimize import linprog
from fractions import Fraction

def predicted(a,b,p,q):
 m,n=len(a),len(b); (i,j),(k,l)=p,q; T=sum(a)
 if a[i]+b[j]>=T-1e-9 or a[k]+b[l]>=T-1e-9: return False
 if i==k:return a[i]+b[j]+b[l]<T-1e-9
 if j==l:return a[i]+a[k]+b[j]<T-1e-9
 return True

def strict_ridge(a,b,p,q):
 m,n=len(a),len(b); T=sum(a)
 constraints=[]; rhs=[]
 for i in range(m):
  r=np.zeros(m*n); r[i*n:(i+1)*n]=1;constraints.append(r);rhs.append(a[i])
 for j in range(n):
  r=np.zeros(m*n);r[j::n]=1;constraints.append(r);rhs.append(b[j])
 epscol=m*n
 eq=np.array(constraints+[np.eye(m*n)[p[0]*n+p[1]],np.eye(m*n)[q[0]*n+q[1]]]);bb=np.array(rhs+[0,0]);
 A=[]
 for i in range(m):
  for j in range(n):
   if (i,j) in (p,q): continue
   r=np.zeros(m*n+1);r[i*n+j]=-1;r[-1]=1;A.append(r)
 eq=np.column_stack([eq,np.zeros(eq.shape[0])]);c=np.zeros(m*n+1);c[-1]=-1
 res=linprog(c,A_ub=np.array(A),b_ub=np.zeros(len(A)),A_eq=eq,b_eq=bb,bounds=[(0,None)]*(m*n)+[(0,None)],method='highs')
 return bool(res.success and res.x[-1]>1e-7)

def check_angles(m,n):
 for i,j,k,l in [(0,0,0,1),(0,0,1,0),(0,0,1,1)]:
  rows=np.eye(m)-np.ones((m,m))/m;cols=np.eye(n)-np.ones((n,n))/n
  dots=rows[i]@rows[k] * (cols[j]@cols[l]); denom=(1-1/m)*(1-1/n)
  ex=[-1/(n-1),-1/(m-1),1/((m-1)*(n-1))][[(0,0,0,1),(0,0,1,0),(0,0,1,1)].index((i,j,k,l))]
  assert abs(dots/denom-ex)<1e-10

rng=np.random.default_rng(20261114)
count=0
for m,n in itertools.product(range(3,6),repeat=2):
 for rep in range(6):
  a=np.ones(m)/m if rep==0 else rng.dirichlet(np.ones(m))
  b=np.ones(n)/n if rep==0 else rng.dirichlet(np.ones(n))
  # normalize sums exactly in numpy
  a=a/sum(a);b=b/sum(b)
  cells=list(itertools.product(range(m),range(n)))
  for p,q in itertools.combinations(cells,2):
   ans=predicted(a,b,p,q)
   obs=strict_ridge(a,b,p,q)
   if obs != ans:
    print('FAIL',m,n,rep,p,q,a,b,ans,obs);raise SystemExit(1)
   count+=1
  check_angles(m,n)
print('TRANSPORT_RIDGE_LP_PASS pair_cases='+str(count)+' dimensions=3..5 margin_cases=54 normals=exact_projection')

# Exact intrinsic-Gram test by rational projector for dimensions 3..8.
for m,n in itertools.product(range(3,9),repeat=2):
  R=[[Fraction(int(i==k),1)-Fraction(1,m) for k in range(m)] for i in range(m)]
  C=[[Fraction(int(j==l),1)-Fraction(1,n) for l in range(n)] for j in range(n)]
  a=R[0][0]*C[0][0]
  for p,q,expected in [((0,0),(0,1),-Fraction(1,n-1)),((0,0),(1,0),-Fraction(1,m-1)),((0,0),(1,1),Fraction(1,(m-1)*(n-1)))]:
    i,j=p;k,l=q
    assert R[i][k]*C[j][l]/a==expected
print('TRANSPORT_RIDGE_GRAM_EXACT_PASS dimensions=3..8')
