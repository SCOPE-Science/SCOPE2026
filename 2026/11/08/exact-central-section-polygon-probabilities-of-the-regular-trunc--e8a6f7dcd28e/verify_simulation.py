"""Independent floating-point diagnostic for central sections of a truncated cube."""
import numpy as np
from itertools import product,combinations
from math import sqrt,acos,pi
rng=np.random.default_rng(20261103)
t=sqrt(2)-1
vertices=[]
for k in range(3):
 for signs in product((-1,1),repeat=3):
  vertices.append([signs[i]*(t if i==k else 1) for i in range(3)])
v=np.array(vertices)
E=[]
for i,j in combinations(range(len(v)),2):
 if abs(np.sum((v[i]-v[j])**2)-4*t*t)<1e-9:E.append((i,j))
assert len(E)==36
T=500000
observed=np.zeros(4,dtype=np.int64)
for start in range(0,T,50000):
 u=rng.normal(size=(50000,3));u/=np.linalg.norm(u,axis=1)[:,None]
 sg=(u@v.T)>0
 n=np.zeros(50000,dtype=np.int8)
 for i,j in E:n+=(sg[:,i]!=sg[:,j]).astype(np.int8)
 assert np.all(np.isin(n,[4,6,8,10]))
 for idx,k in enumerate([4,6,8,10]): observed[idx]+=np.count_nonzero(n==k)
a,b,c=[acos(q) for q in ((7-4*sqrt(2))/17,(5+2*sqrt(2))/17,(3+8*sqrt(2))/17)]
expected=np.array([3-6*a/pi,4+(6*a-12*b-12*c)/pi,-12+(6*a+24*b+6*c)/pi,6+(-6*a-12*b+6*c)/pi]);emp=observed/T
assert max(abs(emp-expected))<0.005
assert abs(np.dot(emp,[4,6,8,10])-36*c/pi)<.02
print('MONTE_CARLO_OK sample=',T,'empirical=',emp,'exact=',expected,'max_deviation=',max(abs(emp-expected)),'expected_vertices=',36*c/pi)
