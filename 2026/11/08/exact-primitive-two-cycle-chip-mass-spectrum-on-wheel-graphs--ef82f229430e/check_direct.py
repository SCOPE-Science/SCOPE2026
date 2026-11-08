#!/usr/bin/env python3
"""Independent exhaustive dynamics and phase-boundary check for parallel chip-firing on wheels."""
from itertools import product
from collections import Counter,defaultdict

def multiply(P,Q):
 R=defaultdict(int)
 for a,x in P.items():
  for b,y in Q.items():R[a+b]+=x*y
 return R

def predicted(m):
 H=defaultdict(int)
 for word in product((0,1),repeat=m):
  k=word.count(0)
  if k==0:continue
  P={m+h:1 for h in range(k)}
  for i,phase in enumerate(word):
   n1=word[(i-1)%m]+word[(i+1)%m]
   if phase:
    Q={3+h:1 for h in range(2-n1)}
   else:
    Q={2-n1+h:1 for h in range(1+n1)}
   P=multiply(P,Q)
  for mass,v in P.items():H[mass]+=2*v
 return H

def direct(m):
 degrees=[m]+[3]*m
 edges=[list(range(1,m+1))]
 for i in range(m):edges.append([0,1+(i-1)%m,1+(i+1)%m])
 def F(c):
  f=[int(c[i]>=degrees[i]) for i in range(m+1)]
  return tuple(c[i]+sum(f[j] for j in edges[i])-degrees[i]*f[i] for i in range(m+1))
 D=Counter();searched=0
 for x in product(*(range(2*d) for d in degrees)):
  searched+=1
  y=F(x)
  if y!=x and F(y)==x:D[sum(x)]+=1
 return D,searched

if __name__=='__main__':
 total=0
 for m in range(3,7):
  d,n=direct(m);p=predicted(m)
  total+=n
  assert dict(d)==dict(p),(m,d,p)
  print(f'm={m}: direct states tested={n}, period-two states={sum(d.values())}, support=[{min(d)}, {max(d)}], endpoint={d[min(d)]}; PASS')
 print(f'ALL CHECKS PASSED, total tested={total}')
