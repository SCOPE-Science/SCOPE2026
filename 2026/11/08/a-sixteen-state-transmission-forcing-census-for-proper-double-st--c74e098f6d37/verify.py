from fractions import Fraction as Q
from itertools import product
from math import comb

def direct(a,b,alpha,beta,mask):
 n=2+a+b
 N=[{1,*range(2,2+a)},{0,*range(2+a,n)}]+[{0}]*a+[{1}]*b
 w=[Q((mask>>i)&1) for i in range(n)]
 filled={i for i in range(n) if (mask>>i)&1}
 used=set()
 for t in range(4):
  if len(filled)==n:return True,t
  D=[Q(0)]*n
  for v in filled:
   un=N[v]-filled
   if len(un)==1:
    u=next(iter(un))
    if (v,u) not in used:
     used.add((v,u));D[u]+=alpha*w[v]
  new=set()
  for u in range(n):
   if u not in filled:
    w[u]+=D[u]
    if w[u]>=beta:new.add(u)
  if not new:return False,t
  filled|=new
 raise RuntimeError((a,b,alpha,beta,mask,filled,w))

def reduced(a,b,alpha,beta,p,q,h,g):
 # vertices 0,1 hubs; 2 iff p, 3 iff q are omitted leaves
 W=[Q(h),Q(g),Q(0),Q(0)]
 full={i for i in (0,1) if W[i]>=beta}
 if not p:full.add(2)
 if not q:full.add(3)
 N=[{1}|({2} if p else set()),{0}|({3} if q else set()),({0} if p else set()),({1} if q else set())]
 used=set()
 for t in range(4):
  if len(full)==4:return True,t
  delta=[Q(0)]*4
  if t==0:
   if not h:delta[0]+=(a-p)*alpha
   if not g:delta[1]+=(b-q)*alpha
  for v in full:
   un=N[v]-full
   if len(un)==1:
    u=next(iter(un))
    if (v,u) not in used:
     used.add((v,u));delta[u]+=alpha*W[v]
  new=set()
  for v in range(4):
   if v not in full:
    W[v]+=delta[v]
    if W[v]>=beta:new.add(v)
  if not new:return False,t
  full|=new
 raise RuntimeError((a,b,p,q,h,g,W,full))

def formula(a,b,alpha,beta):
 n=a+b+2
 res=[0]*(n+1)
 for p,q,h,g in product((0,1),repeat=4):
  yes,_=reduced(a,b,alpha,beta,p,q,h,g)
  if yes:res[a+b-p-q+h+g]+=comb(a,p)*comb(b,q)
 return res

def brute(a,b,alpha,beta):
 n=a+b+2
 out=[0]*(n+1)
 for mask in range(1<<n):
  yes,t=direct(a,b,alpha,beta,mask)
  if yes:out[mask.bit_count()]+=1
  if yes and t>3:raise AssertionError((a,b,alpha,beta,mask,t))
 return out
def verify():
 vals=[Q(1,5),Q(2,5),Q(1,2),Q(3,5),Q(4,5),Q(1)]
 for a in range(2,6):
  for b in range(2,6):
   for alpha,beta in product(vals,repeat=2):
    x=formula(a,b,alpha,beta)
    y=brute(a,b,alpha,beta)
    assert x==y,(a,b,alpha,beta,x,y)
  print('EXACT_ALL_SUBSET_MATCH_OK a=',a)
 # A sharp nonmonotonicity witness: one successful set and its strict superset.
 a=b=2;alpha=Q(4,5);beta=Q(1)
 seed=(1<<2)|(1<<3)|(1<<5)
 assert direct(a,b,alpha,beta,seed)[0]
 assert not direct(a,b,alpha,beta,seed|(1<<1))[0]
 print('DOUBLE_STAR_UPWARD_CLOSURE_FAILURE_OK')
 print('VERIFY_OK',576)
if __name__=='__main__':verify()
