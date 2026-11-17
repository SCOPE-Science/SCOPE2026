from itertools import product
from fractions import Fraction as F
from functools import lru_cache
import random

def bitsets(sizes):
 n=sum(sizes); starts=[]; j=0
 for size in sizes: starts.append(range(j,j+size));j+=size
 for bits in product((0,1),repeat=n):
  parity=tuple(sum(bits[i] for i in b)%2 for b in starts)
  yield bits,parity

def nearest(x,parity,sizes):
 n=sum(sizes); T={i for i,p in enumerate(parity) if p}
 if len(T)==0 or len(T)==len(sizes): return tuple(map(F,x)),F(0)
 wT=sum((F(1,sizes[i]) for i in T),F(0))
 wC=sum((F(1,sizes[i]) for i in range(len(sizes)) if i not in T),F(0))
 lam=wC/(wT+wC)
 offset=[]
 for i,s in enumerate(sizes):
  d=(lam if i in T else (1-lam))/s
  offset.extend([d]*s)
 y=tuple(F(a)+(F(1)-2*F(a))*d for a,d in zip(x,offset))
 d2=sum(((F(a)-b)**2 for a,b in zip(x,y)),F(0))
 assert d2==wT*wC/(wT+wC)
 return y,d2

def test(sizes):
 allv=list(bitsets(sizes)); code=[x for x,p in allv if len(set(p))==1]
 far2=F(0);fars=[]
 for x,p in allv:
  y,d2=nearest(x,p,sizes)
  e=[F(a)-b for a,b in zip(x,y)]
  for c in code:
   assert sum((ee*(F(ci)-yi) for ee,ci,yi in zip(e,c,y)),F(0))<=0,(sizes,x,c,y)
  if d2>far2: far2=d2;fars=[x]
  elif d2==far2: fars.append(x)
 ws=[F(1,s) for s in sizes];S=sum(ws)
 theoretical=max((sum((ws[i] for i in range(len(ws)) if mask>>i & 1),F(0))*sum((ws[i] for i in range(len(ws)) if not(mask>>i & 1)),F(0))/S for mask in range(1,(1<<len(ws))-1)))
 assert far2==theoretical
 print('pass',sizes,'n',sum(sizes),'code',len(code),'farthest',len(fars),'d2',far2)

for sizes in [(1,1,1),(2,2,2),(1,2,3),(2,2,3),(1,1,2,2),(1,2,2,2),(2,2,2,2),(1,1,1,1),(2,3,3),(3,3,3)]: test(sizes)
print('PARITY_BLOCK_HAUSDORFF_KKT_PASS')
