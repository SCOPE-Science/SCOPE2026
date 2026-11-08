"""Independent direct dynamical verification over GF(4) for small complete multipartite graphs."""
from itertools import product
from collections import Counter

def inv(parts):
 r=len(parts);o=sum(a%2 for a in parts);e=r-o;n=sum(parts)
 rho=r-(r%2); ss=o-(o%2); delta=int(o%2 and e>0)
 a3=delta;a2=rho-ss-2*delta;b2=int(o>0 and o%2==0);b1=ss-2*b2
 return (n-(2*a2+3*a3+b1+2*b2),a2,a3,b1,b2)

def predict_fixed(k,parts,q):
 a,b,c,d,e=inv(parts)
 t=k&-k
 return q**(a*min(t,2)+b*min(t,4)+c*min(t,6)+(2*d+2*e*min(t,2) if k%3==0 else 0))

def step(state,part_of):
 n=len(part_of);u=state[:n];v=state[n:]
 new=tuple(u[i] ^ __import__('functools').reduce(int.__xor__,(v[j] for j in range(n) if part_of[j]!=part_of[i]),0) for i in range(n))
 return v+new

count=0
for r in range(2,5):
 for parts in product((1,2,3),repeat=r):
  n=sum(parts)
  if n>4:continue
  pts=[i for i,a in enumerate(parts) for j in range(a)]
  ctr=Counter()
  for state in product(range(4),repeat=2*n):
   cur=step(state,pts);k=1
   while cur!=state:
    cur=step(cur,pts);k+=1
    assert k<=24
   ctr[k]+=1
  for k in (1,2,3,4,6,8,12,24):
   assert sum(v for d,v in ctr.items() if k%d==0)==predict_fixed(k,parts,4),(parts,k,ctr)
  count+=1
print('GF4_DIRECT_ORBITS_OK',count)
