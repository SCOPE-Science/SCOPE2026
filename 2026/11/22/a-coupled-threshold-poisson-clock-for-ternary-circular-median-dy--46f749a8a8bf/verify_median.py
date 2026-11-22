#!/usr/bin/env python3
"""Reproducibility checks for three-level circular running median dynamics."""
from itertools import product
from collections import Counter
from random import Random
from math import exp

def median_step(x):
 n=len(x)
 return tuple(sorted((x[(i-1)%n],x[i],x[(i+1)%n]))[1] for i in range(n))

def binary_step(x):
 n=len(x)
 return tuple(1 if x[(i-1)%n]+x[i]+x[(i+1)%n]>=2 else 0 for i in range(n))

def binary_active(x):
 n=len(x)
 return tuple(x[(i-1)%n] ==x[(i+1)%n] != x[i] for i in range(n))

def binary_time(x):
 n=len(x);a=binary_active(x)
 if all(a):return 0 # checkerboard is already period two
 if not any(a):return 0
 longest=0;length=0
 for v in a+a:
  length=(length+1) if v else 0
  longest=max(longest,length)
 return (min(longest,n-1)+1)//2

def predicted_time(x):
 return max(binary_time(tuple(v>=1 for v in x)),binary_time(tuple(v==2 for v in x)))

def brute_time(x):
 x=tuple(x)
 for i in range(len(x)+2):
  if median_step(x)==x or median_step(median_step(x))==x:
   return i, median_step(x)!=x
  x=median_step(x)
 raise AssertionError('long transient')

def equilibrium_checkerboard_layer(x):
 n=len(x)
 for threshold in (1,2):
  b=[v>=threshold for v in x]
  if n%2==0 and all(b[i]!=b[(i+1)%n] for i in range(n)):
   return True
 return False

def transfer(q,L):
 # Exact forbidden-start automaton; states are length-L ternary histories.
 # A window length L+1 is forbidden precisely when a maximal alternating
 # binary-threshold run of length at least L begins at its second site.
 s=list(product(range(q),repeat=L));idx={x:i for i,x in enumerate(s)}
 edge=[]
 for u in s:
  ee=[]
  for c in range(q):
   block=u+(c,)
   reject=False
   for b in (1,2):
    bits=[int(z>=b) for z in block]
    if bits[0]!=bits[2] and all(bits[j]!=bits[j+1] for j in range(1,L)):
     reject=True;break
   if not reject:ee.append(idx[block[1:]])
  edge.append(ee)
 return edge

def cyclic_count_no_alternating(q,L,n):
 edge=transfer(q,L)
 total=0
 for i in range(len(edge)):
  v={i:1}
  for t in range(n):
   w={}
   for j,c in v.items():
    for z in edge[j]:w[z]=w.get(z,0)+c
   v=w
  total+=v.get(i,0)
 return total

def check():
 for n in range(3,12):
  counts=Counter()
  for x in product(range(3),repeat=n):
   b1=tuple(int(v>=1) for v in x); b2=tuple(int(v>=2) for v in x)
   y=median_step(x)
   assert tuple(int(v>=1) for v in y)==binary_step(b1)
   assert tuple(int(v>=2) for v in y)==binary_step(b2)
   t,osc=brute_time(x)
   assert t==predicted_time(x),(n,x,t,predicted_time(x))
   assert osc==equilibrium_checkerboard_layer(x)
   counts[(t,osc)]+=1
  osc=sum(v for (t,o),v in counts.items() if o)
  assert osc == (4*2**(n//2)-2 if n%2==0 else 0)
  assert max(t for t,o in counts)==(n-1)//2
  if n<=7:
   for t in range(min(1,(n-1)//2)+1):
    cnt=sum(v for (a,o),v in counts.items() if a<=t)
    # trace counts exclude checkerboard threshold words; add exact oscillator basin.
    expected=cyclic_count_no_alternating(3,2*t+3,n)
    assert cnt==expected,(n,t,cnt,expected)
  print('N',n,'TIME_OSC_COUNTS',sorted([(k, v) for k,v in counts.items()]),flush=True)
 rng=Random(25641)
 for n,t,trials in [(410,3,10000),(1845,4,5000)]:
  hits=0
  for _ in range(trials):
   x=[rng.randrange(3) for _ in range(n)]
   hits+=predicted_time(x)<=t
  mu=(10/9)*n*(2/9)**(t+1)
  rate=hits/trials
  print('POISSON_CHECK',n,t,'fraction',round(rate,5),'limit_formula',round(exp(-mu),5),flush=True)
  assert abs(rate-exp(-mu))<0.05
 print('VERIFY_MEDIAN_OK')
if __name__=='__main__':check()
