"""Standalone checks of explicit orbit values and analytic bounds (not a proof)."""
import math
import numpy as np

def f(x): return np.logaddexp(x,-x)-math.log(2)

def vec(n,kind):
 if kind=='outlier':
  a=np.full(n,-1/math.sqrt(n*(n-1)));a[0]=math.sqrt((n-1)/n);return a
 a=np.zeros(n);a[0]=1/math.sqrt(2);a[1]=-1/math.sqrt(2);return a

checks=0
for n in range(4,13):
 a=vec(n,'outlier');e=vec(n,'pair')
 assert abs(sum(a))<1e-13 and abs(sum(e))<1e-13
 for r in (0.03,0.1):
  assert sum(f(r*a))<sum(f(r*e))
  checks+=1
 for r in (100,300):
  assert sum(f(r*e))<sum(f(r*a))
  checks+=1
 for r in (0.1,1,10,100):
  rng=np.random.default_rng(n*100+int(r*10))
  for i in range(150):
   u=rng.normal(size=n);u-=u.mean();u/=np.linalg.norm(u)
   val=sum(f(r*u));eta=n*math.log(2)/r
   if val <= sum(f(r*e)):
    assert np.sum(abs(u))>=math.sqrt(2)-1e-12
    assert np.sum(abs(u))<=math.sqrt(2)+eta+1e-12
   checks+=1
print('Checks passed',checks)
