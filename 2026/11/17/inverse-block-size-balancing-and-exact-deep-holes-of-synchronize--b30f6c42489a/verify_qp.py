from itertools import product
import numpy as np
from scipy.optimize import minimize
from fractions import Fraction as F

def evaluate(sizes):
 n=sum(sizes); blocks=[];a=0
 for t in sizes:blocks.append(range(a,a+t));a+=t
 vertices=list(product((0,1),repeat=n))
 code=np.array([v for v in vertices if len({sum(v[i] for i in b)%2 for b in blocks})==1],dtype=float)
 for bits in vertices:
  T={j for j,b in enumerate(blocks) if sum(bits[i] for i in b)%2}
  if not T or len(T)==len(blocks):continue
  a=sum(F(1,sizes[j]) for j in T);b=sum(F(1,sizes[j]) for j in range(len(sizes)) if j not in T);lam=b/(a+b)
  offsets=np.concatenate([[float((lam if j in T else 1-lam)/sizes[j])]*sizes[j] for j in range(len(sizes))])
  x=np.array(bits,dtype=float)
  closest=x+(1-2*x)*offsets
  z=code@closest # no-op used only to prevent accidental reuse
  # independent QP on convex-hull barycentric coordinates
  def fn(q):
   diff=code.T@q-x
   return float(diff@diff)
  def jac(q):return 2*code@(code.T@q-x)
  ans=minimize(fn,np.full(len(code),1/len(code)),jac=jac,bounds=[(0,None)]*len(code),constraints=[{'type':'eq','fun':lambda t:sum(t)-1,'jac':lambda t:np.ones(len(t))}],method='SLSQP',options={'ftol':1e-12,'maxiter':250})
  assert ans.success, (sizes,bits,ans.message)
  assert abs(ans.fun-np.sum((closest-x)**2))<1e-8,(sizes,bits,ans.fun,np.sum((closest-x)**2))
  yield ans.fun

for sizes in ((2,2,2),(1,2,3),(2,2,3),(1,1,2,2)):
 results=list(evaluate(sizes))
 print('numeric convex_hull_QP',sizes,'violating_vertices',len(results),'max_numerical',max(results))
print('PARITY_BLOCK_INDEPENDENT_QP_PASS')
