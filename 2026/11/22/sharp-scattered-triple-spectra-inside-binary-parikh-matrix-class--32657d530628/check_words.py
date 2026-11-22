"""Direct positional subsequence enumeration; independent of partition formula."""
from itertools import combinations
from collections import defaultdict
from math import comb

def counts(word):
    pos_0=[i for i,x in enumerate(word) if x=='0']
    pos_1=[i for i,x in enumerate(word) if x=='1']
    n01=sum(i<j for i in pos_0 for j in pos_1)
    n010=sum(i<j<k for i in pos_0 for j in pos_1 for k in pos_0)
    return n01,n010

def bounds(a,b,t):
    q,r=divmod(t,b)
    _,s=divmod(t,a)
    return s*(a-s),a*t-((b-r)*q*q+r*(q+1)*(q+1))

nwords=0; nfibers=0
for a in range(1,8):
 for b in range(1,8):
  bins=defaultdict(list)
  for indices in combinations(range(a+b),a):
   ss=set(indices)
   w=''.join('0' if j in ss else '1' for j in range(a+b))
   t,c=counts(w)
   bins[t].append((c,w))
   nwords+=1
  assert set(bins)==set(range(a*b+1)), (a,b)
  for t, pairs in bins.items():
   lo,hi=bounds(a,b,t)
   assert (min(c for c,_ in pairs),max(c for c,_ in pairs))==(lo,hi),(a,b,t,lo,hi,pairs)
   assert sum(c==lo for c,_ in pairs)==1,('min unique',a,b,t)
   assert sum(c==hi for c,_ in pairs)==1,('max unique',a,b,t)
   assert all(c%2==((a-1)*t)%2 for c,_ in pairs),('parity',a,b,t)
   nfibers+=1
print('PASS direct positional triple counting:',nwords,'words,',nfibers,'fibers, a,b<=7; exact bounds, unique extremizers, parity')
