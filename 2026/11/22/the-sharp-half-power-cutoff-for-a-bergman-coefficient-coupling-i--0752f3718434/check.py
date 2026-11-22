"""Finite diagnostics for a sharp Bergman coefficient-form inequality.
These are checks only; the infinite-dimensional result is proved analytically.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.linalg import eigh_tridiagonal

def j(s,k):
 a=s/2.0
 return a*(k+1)*math.sqrt((k+2)*(k+3))/((k+1+a)*(k+2+a))

def eigmax(s,n):
 e=np.array([j(s,k) for k in range(n-1)])
 return float(eigh_tridiagonal(np.zeros(n),e,select='i',select_range=(n-1,n-1),check_finite=False)[0][0])

def run():
 checks=0
 for s in [0.5,0.6,1,2,10,100]:
  for k in [0,1,2,5,11,30,100,1000,10000]:
   assert j(s,k)<=s/2*(1+2e-12),(s,k,j(s,k));checks+=1
 for s in [.1,.2,.3,.4]:
  assert eigmax(s,350)>s,(s,eigmax(s,350));checks+=1
 for s in [.5,1,2]:
  assert eigmax(s,350)<s,(s,eigmax(s,350));checks+=1
 for s in [.2,.4,.5,1,2]:
  a=s/2
  for k in [1,2,3,10,40,200,600,2000]:
   w=math.sqrt((k+1)/(k+2))
   dk=(k+1)/(k+1+a)
   dk1=(k+2)/(k+2+a)
   hk=1/((k+1)*(k+2))
   hk1=1/((k+2)*(k+3))
   v=w*(a/((k+1+a)*(k+2+a)))/math.sqrt(hk*hk1)
   assert math.isclose(v,j(s,k),rel_tol=5e-10,abs_tol=1e-12),(s,k,v,j(s,k))
   checks+=1
 print('finite checks passed',checks)
 for s in [.2,.4,.5,1,2]:print('s',s,'largest finite eig at 350',eigmax(s,350),'essential edge',s)
if __name__=='__main__':run()
