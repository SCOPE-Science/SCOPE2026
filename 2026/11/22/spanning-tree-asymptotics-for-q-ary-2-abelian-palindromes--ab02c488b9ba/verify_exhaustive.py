from itertools import product
from collections import Counter,defaultdict
from math import comb,pi,sqrt

def direct(w):
 c=Counter(zip(w,w[1:]));return all(c[a,b]==c[b,a] for a in set(w) for b in set(w))

def cycle(w,q):
 if w[0]!=w[-1]:return False
 counts=Counter()
 for x,y in zip(w,w[1:]):
  if x==0 or y==0 or x==y:continue
  a,b=sorted((x,y));counts[a,b]+=1 if x<y else -1
 return all(v==0 for v in counts.values())

for q,N in ((2,9),(3,10),(4,9),(5,7)):
 for n in range(1,N+1):
  direct_count=0; alt_count=0
  for w in product(range(q),repeat=n):
   a=direct(w);b=cycle(w,q)
   assert a==b,(q,n,w,a,b)
   direct_count+=a;alt_count+=b
  if q==3:
   tri=sum(comb(n-1,2*j)*comb(2*j,j) for j in range((n+1)//2))
   assert direct_count==3*tri,(n,direct_count,tri)
  print('q,n,count,prob',q,n,direct_count,round(direct_count/q**n,7))
 print()
