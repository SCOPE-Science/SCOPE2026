from itertools import permutations
import numpy as np
from scipy.optimize import minimize
from verify_derangement_projection import candidate
from fractions import Fraction

def solve(p):
 n=len(p);m=n*n
 P=np.array([[int(j==p[i]) for j in range(n)] for i in range(n)])
 U=(np.ones((n,n))-np.eye(n))/(n-1)
 A=[]; b=[]
 for i in range(n):
  row=np.zeros((n,n));row[i,:]=1;A.append(row.ravel());b.append(1)
 for j in range(n-1):
  row=np.zeros((n,n));row[:,j]=1;A.append(row.ravel());b.append(1)
 A=np.array(A);b=np.array(b)
 bounds=[(0,0) if i==j else (0,None) for i in range(n) for j in range(n)]
 res=minimize(lambda x: np.sum((x.reshape(n,n)-P)**2),U.ravel(),jac=lambda x:2*(x-P.ravel()),constraints=[{'type':'eq','fun':lambda x:A@x-b,'jac':lambda x:A}],bounds=bounds,method='SLSQP',options={'maxiter':500,'ftol':1e-12})
 assert res.success,(n,p,res.message)
 exact=np.array(candidate(p),float).ravel()
 err=np.max(np.abs(res.x-exact))
 assert err<3e-6,(n,p,err)
 return err

def main():
 tests=0; e=0
 for n in range(3,7):
  patterns={}
  for p in permutations(range(n)):
   k=sum(i==p[i] for i in range(n))
   if k not in patterns:patterns[k]=p
  for k,p in patterns.items():
   e=max(e,solve(p));tests+=1
 print('INDEPENDENT_SLSQP_PASS','cases',tests,'max_entry_error',format(e,'.3g'))
if __name__=='__main__':main()

def spectral_checks():
 import numpy as np
 from itertools import permutations
 cases=0
 for n in range(3,7):
  U=(np.ones((n,n))-np.eye(n))/(n-1)
  c=n/(n-1)
  for p in permutations(range(n)):
   P=np.eye(n)[list(p)]
   sing=np.linalg.svd(P-U,compute_uv=False)
   assert abs(sing[-1])<1e-12
   assert max(sing)<=c+1e-12
   if any(i!=p[i] for i in range(n)):
    assert sum(abs(s-c) for s in sing[:-1])>1e-7
   cases+=1
  for eps in [0,0.3,0.7,1]:
   X=eps*U+(1-eps)*U.T
   assert np.linalg.norm((np.eye(n)-X)-(np.eye(n)-X).T)<1e-12
   assert abs(sum(np.linalg.svd(np.eye(n)-X,compute_uv=False))-n)<1e-10
 print('SPECTRAL_CHECKS_PASS','permutations',cases,'singular_bounds=PASS','nuclear_locus=PASS')

if __name__=='__main__':spectral_checks()
