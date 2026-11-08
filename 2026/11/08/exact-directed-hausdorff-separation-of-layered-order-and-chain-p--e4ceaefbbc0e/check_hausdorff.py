from itertools import product
from fractions import Fraction as F
import numpy as np
from scipy.optimize import minimize

def expected(ms):
 k=len(ms); N=sum(ms)
 if k==1:return 0.,0.,[1.]
 lam=0.
 for c in range(2,k+1):
  s=sorted(ms,reverse=True)[:c]
  lamb=(c-1)/sum(1/m for m in s)
  if c==k or lamb>=sorted(ms,reverse=True)[c]:
   lam=lamb;break
 t=[max(0,1-lam/m) for m in ms]
 d2=sum(m*(1-x)**2 for m,x in zip(ms,t))
 rev=max(ms[i]*sum(ms[i+1:])/(ms[i]+sum(ms[i+1:])) if i+1<k else 0 for i in range(k))
 return d2,rev,t

def experiment(ms):
 k=len(ms);N=sum(ms)
 d2,r2,t=expected(ms)
 # constrain C: sum of max in each layer <=1, exact all choices of one from each level
 offsets=np.cumsum([0]+list(ms));
 rows=[]
 for inds in product(*(range(offsets[i],offsets[i+1]) for i in range(k))):
  a=np.zeros(N)
  for ix in inds:a[ix]=1
  rows.append(a)
 A=np.array(rows)
 # O: all adjacent-layer inequalities, plus [0,1]
 B=[]
 for i in range(k-1):
  for a in range(offsets[i],offsets[i+1]):
   for b in range(offsets[i+1],offsets[i+2]):
    c=np.zeros(N);c[b]=1;c[a]=-1;B.append(c)
 B=np.array(B)
 def pr(z,poly):
  cons=[{'type':'ineq','fun':lambda y:y},{'type':'ineq','fun':lambda y:1-y}]
  if poly=='C':cons.append({'type':'ineq','fun':lambda y:1-A@y})
  else:cons.append({'type':'ineq','fun':lambda y:B@y})
  r=minimize(lambda y:np.sum((y-z)**2),z/2,jac=lambda y:2*(y-z),constraints=cons,method='SLSQP',options={'ftol':1e-10})
  assert r.success or np.max(np.maximum(-B@r.x if poly=='O' else A@r.x-1,0))<1e-6
  return np.sum((r.x-z)**2)
 out=[]
 # all ideals filters: choose one partial layer + fully upper
 O={tuple([1]*N),tuple([0]*N)}
 for i in range(k):
  for bits in product([0,1],repeat=ms[i]):
   O.add(tuple([0]*offsets[i]+list(bits)+[1]*(N-offsets[i+1])))
 C={tuple([0]*N)}
 for i in range(k):
  for bits in product([0,1],repeat=ms[i]):
   C.add(tuple([0]*offsets[i]+list(bits)+[0]*(N-offsets[i+1])))
 E=max(pr(np.array(z,float),'C') for z in O)
 R=max(pr(np.array(z,float),'O') for z in C)
 assert abs(E-d2)<1e-6 and abs(R-r2)<1e-6,(ms,E,d2,R,r2)
 return N,len(O),len(C)
if __name__=='__main__':
 import itertools
 c=0
 for k in (2,3,4):
  for ms in itertools.product((1,2),repeat=k):
   experiment(ms)
   c+=1
 for ms in [(3,1,2),(1,2,3),(3,2,1),(4,1,1),(3,3,3)]:
  experiment(ms); c+=1
 print('LAYERED_ORDER_CHAIN_HAUSDORFF_CHECKS_PASSED profiles=',c)
