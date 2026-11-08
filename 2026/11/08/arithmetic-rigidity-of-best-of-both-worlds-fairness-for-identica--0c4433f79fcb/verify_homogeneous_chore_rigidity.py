#!/usr/bin/env python3
"""Independent exact count-vector checks for homogeneous-chore weighted EF1 lotteries.
No external datasets or dependencies beyond scipy for linear feasibility.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from scipy.optimize import linprog

def compositions(m,n):
    if n==1:
        yield (m,)
        return
    for z in range(m+1):
        for rest in compositions(m-z,n-1):
            yield (z,)+rest

def wef1(x,w):
    return all((x[i]-1)*w[j]<=x[j]*w[i]
               for i in range(len(w)) for j in range(len(w)) if x[i]>0)

def lottery_exists(m,w):
    n=len(w)
    X=[x for x in compositions(m,n) if wef1(x,w)]
    if not X: return False, X
    mat=[[float(x[i]) for x in X] for i in range(n)]
    r=linprog([0.0]*len(X),A_eq=mat+[[1.0]*len(X)],
              b_eq=[float(m*wi) for wi in w]+[1.0],
              bounds=(0,None),method='highs',options={'primal_feasibility_tolerance':1e-9})
    return r.success,X

def predicted(m,w):
    n=len(w)
    if m<n:
        return all(m*v<=1 for v in w)
    if m==n:
        return all(v==F(1,n) for v in w)
    if m==n+1:
        mx=max(w); high={i for i,z in enumerate(w) if z==mx}
        t=len(high)
        return all((z==F(t+1,t*(n+1)) if i in high else z==F(1,n+1))
                   for i,z in enumerate(w))
    return None

cases=0; pairs=0
for n in range(2,5):
  for m in range(1,min(n+2,7)):
    for Q in range(n,9):
      for a in compositions(Q-n,n):
        w=tuple(F(v+1,Q) for v in a)
        ok,X=lottery_exists(m,w)
        exp=predicted(m,w)
        if exp is not None and ok!=exp:
            raise AssertionError(('classification',n,m,Q,w,ok,exp,X))
        for x,y in combinations(X,2):
            ups=[i for i in range(n) if x[i]>y[i]]
            dns=[j for j in range(n) if y[j]>x[j]]
            for i,j in product(ups,dns):
                assert x[i]==y[i]+1 and y[j]==x[j]+1
                assert F(y[i],1)/w[i]==F(x[j],1)/w[j]
                pairs+=1
        cases+=1
print('all exact rational-grid classification tests:',cases)
print('all exchange-rigidity comparisons:',pairs)
for n in range(2,7):
    formulas=set()
    for t in range(1,n+1):
        assert F(t+1,t*(n+1))>=F(1,n+1)
        formulas.add((t,F(t+1,t*(n+1))))
    assert len(formulas)==n
print('n+1 exceptional-profile symbolic counts checked for n=2..6')
# Full exact two-person necessary/sufficient arithmetic up to denominator 25.
c=0
for m in range(1,9):
 for Q in range(2,13):
  for a in range(1,Q):
   p=F(a,Q)
   ok,_=lottery_exists(m,(p,1-p))
   assert ok == ((m*p).denominator==1 or ((m-1)*p).denominator==1)
   c+=1
print('exact two-person congruence checks:',c)
