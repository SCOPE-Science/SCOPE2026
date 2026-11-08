"""Independent verification of synchronous majority two-cycle counts on complete tripartite graphs."""
from itertools import combinations_with_replacement,product
from math import comb

def formula(a,b,c):
 ns=(a,b,c)
 ans=int(sum(x==max(ns) for x in ns)==1)
 for i in range(3):
  for j in range(i+1,3):
   if ns[i]==ns[j]:
    other=3-i-j
    d=ns[other]
    ans+=sum(comb(d,h) for h in range(d+1) if abs(2*h-d)<ns[i])
 return ans

def step(x,n):
 total=sum(x);N=sum(n)
 return tuple(m if 2*(total-s)>N-m else 0 if 2*(total-s)<N-m else s for s,m in zip(x,n))

def by_occupancy(n):
 ans=0
 for x in product(*[range(m+1) for m in n]):
  y=step(x,n)
  if y!=x and step(y,n)==x:
   weight=1
   for sz,s in zip(n,x):weight*=comb(sz,s)
   ans+=weight
 assert ans%2==0
 return ans//2

tests=0
for n in product(range(1,10),repeat=3):
 exact=by_occupancy(n)
 pred=formula(*n)
 if exact!=pred:raise AssertionError((n,exact,pred))
 tests+=1
print(f'PASS occupancy 2-cycle orbits: {tests} ordered triples with shore sizes 1..9; checked all occupancies.')
print('examples:',[(n,formula(*n)) for n in [(1,1,1),(2,2,2),(3,3,3),(4,4,1),(4,4,3),(4,3,2),(4,2,2),(1,1,10)]])
