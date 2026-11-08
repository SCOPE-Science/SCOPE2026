#!/usr/bin/env python3
"""Independent finite-rational checks for the two-environment majority theorem.
These checks supplement the analytic proof; they do not certify all m.
"""
from fractions import Fraction as F
from math import comb
from itertools import product

count = 0

def majority(m,t):
    n=2*m+1
    return sum((F(comb(n,k))*t**k*(1-t)**(n-k) for k in range(m+1,n+1)),F(0))

def check(x):
    global count
    assert x
    count+=1

# Binomial increment via two additional independent votes.
for den in range(3,15):
    for num in range(1,den):
        t=F(num,den)
        for m in range(0,11):
            diff=majority(m+1,t)-majority(m,t)
            exact=comb(2*m+1,m)*t**(m+1)*(1-t)**(m+1)*(2*t-1)
            check(diff==exact)

# Explicit finite phase-shape comparisons for rational p,q,w grids.
for p in [F(3,5),F(2,3),F(3,4),F(4,5),F(9,10)]:
 for q in [F(1,10),F(1,5),F(1,4),F(1,3),F(2,5)]:
  for w in [F(1,5),F(1,3),F(2,5),F(1,2),F(3,5),F(2,3),F(4,5)]:
   sp=p*(1-p); sq=q*(1-q)
   R=w*(2*p-1)*sp/((1-w)*(1-2*q)*sq)
   z=sq/sp
   vals=[w*majority(m,p)+(1-w)*majority(m,q) for m in range(11)]
   for m in range(10):
    d=vals[m+1]-vals[m]
    check((d>0)-(d<0)==(R>z**m)-(R<z**m))
   # Structural one-switch condition: sign of increments cannot reverse more than once.
   signs=[(vals[i+1]>vals[i])-(vals[i+1]<vals[i]) for i in range(10)]
   nz=[s for s in signs if s]
   changes=sum(nz[j]!=nz[j-1] for j in range(1,len(nz)))
   check(changes<=1)
   if p+q>1:
    # Signs cannot change from negative to positive in peak regime.
    check(all(nz[j]<=nz[j-1] for j in range(1,len(nz))))
   elif p+q<1:
    check(all(nz[j]>=nz[j-1] for j in range(1,len(nz))))
   else:
    check(len(set(nz))<=1)

# Exact illustrative example.
p,q,w=F(9,10),F(2,5),F(1,2)
check(w*majority(0,p)+(1-w)*majority(0,q)==F(13,20))
check(w*majority(1,p)+(1-w)*majority(1,q)==F(331,500))
check(w*majority(2,p)+(1-w)*majority(2,q)==F(16361,25000))
check(F(331,500)>F(13,20))
check(F(331,500)>F(16361,25000))
# Dominance of infinitely many larger committee sizes is by analytic monotonicity.
print('PASS',count,'finite exact rational assertions')
