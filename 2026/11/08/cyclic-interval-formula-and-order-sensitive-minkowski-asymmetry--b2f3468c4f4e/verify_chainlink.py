"""Reproduce exact cyclic-barrier values and independently solve the support LP.
Only finite numerical checks; infinite theorem follows from difference-constraint cycle proof."""
from fractions import Fraction
from itertools import product
from scipy.optimize import linprog
import numpy as np

def barrier(a,ell):
 n=len(a); total=sum(a)
 v=[(Fraction(total,total-n*ell),('ring',))]
 for i in range(n):
  partial=0
  for m in range(1,n):
   partial+=a[(i+m-1)%n]
   b=partial+a[(i+m)%n]
   v.append((Fraction(b,b-m*ell),('interval',i,m)))
 return max(v,key=lambda p:p[0])

def verify_instance(a,ell):
 n=len(a)
 A=[];B=[]
 for i in range(n):
  e=np.eye(n)[i]; d=e-np.eye(n)[(i+1)%n]
  A.extend([e,-e,d]);B.extend([a[i],0,a[i]-ell])
 A=np.array(A);B=np.array(B,dtype=float)
 norms=[];h=[];mini=[]
 for row in A:
  rp=linprog(-row,A_ub=A,b_ub=B,bounds=[(None,None)]*n,method='highs')
  rm=linprog(row,A_ub=A,b_ub=B,bounds=[(None,None)]*n,method='highs')
  assert rp.success and rm.success
  norms.append(row);h.append(-rp.fun);mini.append(rm.fun)
 # (lambda+1)c = y, and for each original valid halfspace n*y -lambda*h_K(n) <= min_K(n)
 lhs=np.array([list(row)+[-mx] for row,mx in zip(norms,h)],float)
 sol=linprog([0]*n+[1],A_ub=lhs,b_ub=mini,bounds=[(None,None)]*n+[(1,None)],method='highs')
 assert sol.success
 expected,witness=barrier(a,ell)
 assert abs(sol.x[-1]-float(expected))<1e-8,(a,ell,sol.x[-1],expected)
 return expected,witness

if __name__=='__main__':
 for n in range(3,5):
  for a in product((4,10),repeat=n):
   for ell in (1,2):
    verify_instance(a,ell)
 for a in ((4,4,20,20),(4,20,4,20),(4,4,4,4),(5,5,5),(6,8,7,11)):
  print(a,verify_instance(a,2))
 print('CHAINLINK_MINKOWSKI_SUPPORT_LP_CHECKS_PASSED')
