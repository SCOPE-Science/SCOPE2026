#!/usr/bin/env python3
"""Independent labelled-state dynamics, not reusing symbolic transitions."""
from itertools import product
from collections import Counter
from math import comb, factorial

def step(z,m):
 left,right=z[:m],z[m:]
 stim_left=sum(x==1 for x in right)>=2
 stim_right=sum(x==1 for x in left)>=2
 def upd(x,stim):
  if x==1:return 2
  if x==2:return 0
  return int(stim)
 return tuple(upd(x,stim_left) for x in left)+tuple(upd(x,stim_right) for x in right)

def trace(x,m):
 seen={};v=x
 while v not in seen:
  seen[v]=len(seen)
  v=step(v,m)
 t=seen[v];return t,len(seen)-t

def sat(x,m):
 return tuple(min(2,x[:m].count(i)) for i in range(3))+tuple(min(2,x[m:].count(i)) for i in range(3))

def satstep(v):
 a,b=v[:3],v[3:]
 def local(g,other):
  if other[1]==2:return g[2],g[0],g[1]
  return min(2,g[0]+g[2]),0,g[1]
 return local(a,b)+local(b,a)

def prediction(v):
 for t in range(6):
  if v[1]==v[2]==v[4]==v[5]==0:return t,1
  if v==(2,2,2,2,2,2):return t,3
  if v in {(2,0,2,2,2,0),(2,2,0,2,0,2)}:return t,4
  v=satstep(v)
 raise AssertionError(v)

def E(s):
 out=0
 for i in range(2,s-3):
  for j in range(2,s-i-1):
   k=s-i-j
   if k>=2:out+=factorial(s)//(factorial(i)*factorial(j)*factorial(k))
 return out

def R(s):return sum(comb(s,i) for i in range(2,s-1))

total=0
for m,n in [(a,b) for a in range(1,6) for b in range(1,6)]+[(6,6)]:
 counts=Counter()
 for x in product(range(3),repeat=m+n):
  observed=trace(x,m)
  expected=prediction(sat(x,m))
  assert observed==expected,(m,n,x,observed,expected)
  counts[observed]+=1
 # Multinomial profile sum: the coefficient extraction from products of
 # f0=1, f1=x, f2=e^x-1-x gives each count-profile weight.
 symbolic=Counter()
 fact=factorial
 for a0 in range(m+1):
  for a1 in range(m-a0+1):
   a=(a0,a1,m-a0-a1)
   wa=fact(m)//(fact(a[0])*fact(a[1])*fact(a[2]))
   for b0 in range(n+1):
    for b1 in range(n-b0+1):
     b=(b0,b1,n-b0-b1)
     wb=fact(n)//(fact(b[0])*fact(b[1])*fact(b[2]))
     symbolic[prediction(tuple(min(2,j) for j in a+b))]+=wa*wb
 assert symbolic==counts,(m,n,symbolic,counts)
 assert sum(v for (t,p),v in counts.items() if p==1 and t==0)==1
 assert sum(v for (t,p),v in counts.items() if p==3 and t==0)==E(m)*E(n)
 assert sum(v for (t,p),v in counts.items() if p==4 and t==0)==2*R(m)*R(n)
 assert all(p in (1,3,4) for t,p in counts)
 assert max(t for t,p in counts)<=5
 total+=3**(m+n)
 print(f'PAIR_OK m={m} n={n} states={3**(m+n)} recurrent3={counts[(0,3)]} recurrent4={counts[(0,4)]}')
print('DIRECT_OK labelled_states='+str(total))
