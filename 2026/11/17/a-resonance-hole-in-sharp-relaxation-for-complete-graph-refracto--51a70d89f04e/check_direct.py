"""Independent direct labelled simulation of a synchronous refractory birth automaton."""
from itertools import product
from collections import Counter
from math import factorial

def step(x,r,q):
    firing=x.count(1)
    return tuple((1 if firing==r else 0) if s==0 else (s+1 if s<q-1 else 0) for s in x)

def predict(x,r,q):
    a=[x.count(s) for s in range(q)]
    order=[1,0]+list(range(q-1,1,-1))
    for j,i in enumerate(order):
        if a[i]!=r:
            if j>0:return (j+q-1 if a[i] else j+q-2,1)
            if a[1]:return q-1,1
            s=next((s for s in range(2,q) if a[s]),q)
            return q-s,1
    return (0,q)

cases=0;states=0
for q in range(3,7):
 for n in range(1,8):
  if q**n>280000:continue
  for r in range(1,5):
   hist=Counter()
   for x in product(range(q),repeat=n):
    tau,p=predict(x,r,q)
    y=x;seen={}
    for t in range(2*q+3):
     if y in seen:
      obs_tau=seen[y];obs_p=t-obs_tau;break
     seen[y]=t
     y=step(y,r,q)
    else:raise AssertionError('no return')
    assert (tau,p)==(obs_tau,obs_p),(q,n,r,x,(tau,p),(obs_tau,obs_p))
    hist[(tau,p)]+=1
    states+=1
   assert sum(hist.values())==q**n
   if n==q*r:
    assert hist[(0,q)]==factorial(n)//(factorial(r)**q)
   else:assert hist[(0,q)]==0
   cases+=1
print('DIRECT_OK',cases,'systems',states,'labelled_states')
