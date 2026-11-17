from itertools import product
from collections import Counter
import random

def field(q):
    if q==4:
        add=lambda a,b:a^b
        def mul(a,b):
            r=0
            for i in range(2):
                if (b>>i)&1: r ^= a<<i
            if r&8: r ^= 0b1100 # x3 = x^2+x in mod x2+x+1
            if r&4: r ^= 0b111
            return r
    else:
        add=lambda a,b:(a+b)%q
        mul=lambda a,b:(a*b)%q
    return add,mul

def matmul(a,b,q,add,mul):
 return tuple(add(add(mul(a[3*i],b[j]),mul(a[3*i+1],b[3+j])),mul(a[3*i+2],b[6+j])) for i in range(3) for j in range(3))

def rank(a,q,add,mul):
 s=[list(a[i*3:i*3+3]) for i in range(3)]
 r=0
 for j in range(3):
  k=next((i for i in range(r,3) if s[i][j]),None)
  if k is None:continue
  s[r],s[k]=s[k],s[r]
  inv=next(z for z in range(1,q) if mul(z,s[r][j])==1)
  s[r]=[mul(inv,z) for z in s[r]]
  for i in range(r+1,3):
   c=s[i][j]
   if c:
    s[i]=[add(s[i][h], -mul(c,s[r][h])%q) if q!=4 else s[i][h]^mul(c,s[r][h]) for h in range(3)]
  r+=1
  if r==3:break
 return r

def execute(q,all_targets=True):
 add,mul=field(q)
 z=(0,)*9
 def neg(a):return a if q==4 else (-a)%q
 def outer(u,v):return tuple(mul(u[i],v[j]) for i in range(3) for j in range(3))
 vec=list(product(range(q),repeat=3))
 sq={z}
 for u in vec[1:]:
  for v in vec[1:]:
   if add(add(mul(u[0],v[0]),mul(u[1],v[1])),mul(u[2],v[2]))==0: sq.add(outer(u,v))
 assert len(sq)==q**4+q**3-q,(q,len(sq))
 assert all(matmul(a,a,q,add,mul)==z for a in sq)
 sq=list(sq); counts=Counter()
 for a in sq:
  for b in sq:counts[tuple(add(a[j],b[j]) for j in range(9))]+=1
 assert sum(counts.values())==len(sq)**2
 def formula(C):
  t=add(add(C[0],C[4]),C[8])
  if t:return 0
  r=rank(C,q,add,mul)
  if r==0:return q**4+q**3-q
  if r==1:return 2*q*q-q
  if r==3:return 0
  C2=matmul(C,C,q,add,mul)
  if rank(C2,q,add,mul)==1:return 2*q
  if q in (2,4):
   if any(tuple(mul(l,x) for x in C)==C2 for l in range(q)):
    return 0
   return q
  trC2=(C2[0]+C2[4]+C2[8])%q
  lam=(trC2*pow(2,-1,q))%q
  if lam in {x*x%q for x in range(1,q)}:return q-1
  return q+1
 if all_targets:
  targets=product(range(q),repeat=9)
 else:
  random.seed(521+q)
  targets=list(counts.keys())+[tuple(random.randrange(q) for _ in range(9)) for _ in range(1200)]
 actual_types=Counter()
 total=0
 for C in targets:
  predicted=formula(C); actual=counts.get(C,0)
  if predicted!=actual:raise AssertionError((q,C,predicted,actual))
  actual_types[(rank(C,q,add,mul),predicted)] += 1
  total+=1
 print('FIELD',q,'SQUARE_ZERO',len(sq),'ORDERED_PAIRS',len(sq)**2,'TARGETS_CHECKED',total,'SUPPORTED_TARGETS',len(counts),'PROFILE',sorted(actual_types.items()))

for q in [2,3,4,5]:execute(q,q!=5)
print('SQUARE_ZERO_SUM_FIBERS_ALL_CHECKS_PASS')
